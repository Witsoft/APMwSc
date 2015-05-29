# -*- coding: utf-8 -*-
from flask                           import request, session, Blueprint, json
from app.scrum.backLog               import *
from app.scrum.userHistory           import *
from app.scrum.role                  import *
from app.scrum.accions               import *
from app.scrum.objective             import *   
from app.scrum.objectivesUserHistory import *
from app.scrum.actorsUserHistory     import * 
from sqlalchemy.ext.baked import Result

historias = Blueprint('historias', __name__)


@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    
   
    # Extraemos los parametros.
    codeHistory = params['codigo']
    idSuperHist = params['super']
    idType      = params['tipo']
    idActor     = params['actores']
    idAccion    = params['accion']
    idObjective = params['objetivos']
 
    oUserHistory = userHistory()
    inserted     = oUserHistory.insertUserHistory(codeHistory,idSuperHist,idType,idAccion,1)

    if inserted:
        oObjUserHist = objectivesUserHistory()
        oActUserHist = actorsUserHistory()
        result       = oUserHistory.searchUserHistory(codeHistory)
        idInserted   = result[0].id_userHistory
        for idobj in idObjective:
            insertedObj  = oObjUserHist.insertObjectiveAsociatedInUserHistory(idobj,idInserted)
        for idact in idActor:
            insertedAct  = oActUserHist.insertActorAsociatedInUserHistory(idact,idInserted)
        
        if insertedAct and insertedObj:
            res = results[0]  
            res['label'] = res['label'] + '/1'
        else:
            res = results[1] 
            

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    #Datos de prueba
    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    oBacklog      = backLog() 
    actorList     = oBacklog.actorsAsociatedToProduct(1)
    accionList    = oBacklog.accionsAsociatedToProduct(1)
    objectiveList = oBacklog.objectivesAsociatedToProduct(1)
    historyList   = oBacklog.userHistoryAsociatedToProduct(1)

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores']       = [{'key':act.idrole,'value':act.namerole}for act in actorList]
    res['fHistoria_opcionesAcciones']      = [{'key':acc.idaccion,'value':acc.acciondescription}for acc in accionList]
    res['fHistoria_opcionesObjetivos']     = [{'key':obj.idobjective,'value':obj.descObjective}for obj in objectiveList]
    res['fHistoria_opcionesHistorias']     = [{'key':hist.id_userHistory,'value':hist.cod_userHistory}for hist in historyList]
    res['fHistoria_opcionesTiposHistoria'] = [{'key':1,'value':'Opcional'},{'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0}
    res['idPila']    = 1


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    idHistoria = request.args.get('idHistoria')  #Obtenemos el id de la historia
    idHistoria = int(idHistoria)
    print('id Historia: %r' % idHistoria)
    
    oUserHist   = userHistory()
    oRole       = role()
    oAccion     = accions()
    oObjective  = objective()
    oActUsrHist = actorsUserHistory()
    oObjUsrHist = objectivesUserHistory()
    
    # Obtenemos los actores
    idActorsList = oActUsrHist.idActorsAsociatedToUserHistory(idHistoria)
    actorList    = []
    for id in idActorsList:
        result = oRole.findIdRole(id)
        actorList.append(result[0])   
    
    # Obtenemos la accion
    acc       = oUserHist.accionsAsociatedToUserHistory(idHistoria)
    idAccion  = acc[0].ref_idaccion
    accion    = oAccion.searchIdAccion(idAccion)
    desAccion = accion[0].acciondescription
    
    # Obtenemos los objetivos
    idObjectivesList = oObjUsrHist.idObjectivesAsociatedToUserHistory(idHistoria)
    objectiveList    = []
    for id in idObjectivesList:
        result = oObjective.searchIdObjective(id)
        objectiveList.append(result[0])
        
    # Obtenemos todas las historias de usuarios excepto la actual
    historias =  oUserHist.getAllUserHistoryId(1)
    for hist in historias:
        if hist.id_userHistory == idHistoria:
            historias.remove(hist)
            break
    
    #Ejemplo de relleno de listas para selectores
    res['fHistoria_opcionesActores']   = [{'key':act.idrole,'value':act.namerole}for act in actorList]
    res['fHistoria_opcionesAcciones']  = [{'key':idAccion,'value':desAccion}]
    res['fHistoria_opcionesObjetivos'] = [{'key':obj.idobjective,'value':obj.descObjective}for obj in objectiveList]
    res['fHistoria_opcionesHistorias'] = [{'key':hist.id_userHistory, 'value':hist.cod_userHistory}for hist in historias]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    #res['fHistoria'] = {'super':0, 
    #   'actores':[1], 'accion':2, 'objetivos':[3], 'tipo':1} 
    res['idPila'] = 1
    
    
    #Obtenemos la historia seleccionada
    history   = clsUserHistory.query.filter_by(id_userHistory = idHistoria).first()
    
    res['fHistoria'] = {'idHistoria':idHistoria, 'idPila':history.id_backLog,
                        'actores':[1],'objetivos':[1], 'accion':history.ref_idaccion, 
                        'super':history.id_History, 'tipo':history.type_accion, 'codigo':history.cod_userHistory} 
    
    

    return json.dumps(res)



@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor'] = session['actor']
    
    oRole             = role()
    oAccion           = accions()
    oObjective        = objective()
    oBacklog          = backLog() 
    oUserHistory      = userHistory()
    oActUserHist      = actorsUserHistory()
    oObjUserHIst      = objectivesUserHistory()
    userHistoriesList = oBacklog.userHistoryAsociatedToProduct(1)  
         
    userHistories = []
    options       = {1:'podria ',2:'puede '}
    for hist in userHistoriesList:
        historyDict   = {}
         
        historyDict['idHistory'] = hist.id_userHistory
         
        idActorsList  = oActUserHist.idActorsAsociatedToUserHistory(hist.id_userHistory)
        missingActors = len(idActorsList)
        actorsString  = ''
        
        for act in idActorsList:
            result       = oRole.findIdRole(act)
            actorsString = actorsString + ' ' + str(result[0].namerole) + ' '
            if missingActors != 1:
                actorsString = actorsString + ','    
        historyDict['actors'] = actorsString.lower()

        idAccions = oUserHistory.accionsAsociatedToUserHistory(hist.id_userHistory)
        result    = oAccion.searchIdAccion(idAccions[0].ref_idaccion)
        historyDict['accions'] = ' ' + options[1] + str(result[0].acciondescription).lower() + ' ' 
         
        idObjectivesList  = oObjUserHIst.idObjectivesAsociatedToUserHistory(hist.id_userHistory)
        missingObjectives = len(idObjectivesList)
        objectivesString  = ''
        
        for obj in idObjectivesList: 
            result           = oObjective.searchIdObjective(obj)
            objectivesString = objectivesString + ' ' + str(result[0].descObjective)
            if missingObjectives != 1:
                objectivesString = ' ' + objectivesString + ','  
            elif missingObjectives == 1: 
                objectivesString = objectivesString + '.'  
        historyDict['objectives'] = objectivesString.lower()
             
        userHistories.append(historyDict)

    res['idPila']  = 1
    res['data0']   = [{'idHistoria':hist['idHistory'], 'enunciado':'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in userHistories]
    return json.dumps(res)

