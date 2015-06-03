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

@historias.route('/historias/ACambiarPrioridades', methods=['POST'])
def ACambiarPrioridades():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Prioridades reasignadas']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label']+'/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

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
    priority    = params['prioridad']
    print(idObjective[0])

    
    oUserHistory = userHistory()
    inserted     = oUserHistory.insertUserHistory(codeHistory,idSuperHist,idType,idAccion,1,priority)

    if inserted:
        oObjUserHist = objectivesUserHistory()
        oActUserHist = actorsUserHistory()
        result       = oUserHistory.searchUserHistory(codeHistory)
        idInserted   = result[0].id_userHistory
        for idobj in idObjective:
            insertedObj  = oObjUserHist.insertObjectiveAsociatedInUserHistory(idobj,idInserted)
        for idact in idActor:
            insertedAct  = oActUserHist.insertActorAsociatedInUserHistory(idact,idInserted)
        
        print(insertedObj)
        print(insertedAct)
        
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
    params  = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    
    # Extraemos los valores
    oUserHist    = userHistory()
    oObjUserHist = objectivesUserHistory()
    oActUserHist = actorsUserHistory()
    
    idHistory    = params['idHistoria']
    idSupHist    = params['super']
    idaccion     = params['accion']
    idBackLog    = params['idPila']
    idActors     = params['actores']
    codeHist     = params['codigo']
    idObjectives = params['objetivos']
    type         = params['tipo']
    priority     = params['prioridad']
    
    # Actualizamos los datos de la historia
    updated     = oUserHist.updateUserHistory(idHistory,codeHist,idSupHist,type,idaccion,priority)
    
    if updated:
        # Buscamos los actores asociados
        idActorsList = oActUserHist.idActorsAsociatedToUserHistory(idHistory)
        # Eliminamos los actores asociados
        for id in idActorsList:
            insertedAct = oActUserHist.deleteActorAsociatedInUserHistory(id,idHistory)
        # Insertamos los nuevos actores seleccionados
        for id in idActors:
            insertedAct = oActUserHist.insertActorAsociatedInUserHistory(id,idHistory)
            
        # Buscamos los objetivos asociados
        idObjectivesList = oObjUserHist.idObjectivesAsociatedToUserHistory(idHistory)
        # Eliminamos los objetivos asociados
        for id in idObjectivesList:
            insertedObj = oObjUserHist.deleteObjectiveAsociatedInUserHistory(id,idHistory)
        # Insertamos los nuevos objetivos seleccionados
        for id in idObjectives:
            insertedAct = oObjUserHist.insertObjectiveAsociatedInUserHistory(id,idHistory)
        
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



@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    scale = {1:'Alta',2:'Media',3:'Baja'}
    idProduct = request.args.get('idPila')  #Obtenemos el id de la historia
    idProduct = int(idProduct)
    
    # Objetenemos los datos asociados al producto
    oBacklog      = backLog() 
    oObjective    = objective()    
    actorList     = oBacklog.actorsAsociatedToProduct(idProduct)
    accionList    = oBacklog.accionsAsociatedToProduct(idProduct)
    objectiveList = oBacklog.objectivesAsociatedToProduct(idProduct)
    historyList   = oBacklog.userHistoryAsociatedToProduct(idProduct)

    # Obtenemos todos los objetivos que son no trasnversales.        
    for object in objectiveList:
        idObjective = object.idobjective
        transverse  = oObjective.verifyObjectiveTransverse(idObjective)
        if (int(transverse) == 1):
            objectiveList.remove(object)
    
    typeScale = oBacklog.scaleType(idProduct)
    # Obtenemos el tipo de escala asociado al producto (id,valor)
    if typeScale == 1:
        resultScale = [(i,scale[i]) for i in range(1,3+1)]
    elif typeScale == 2:
        resultScale = [(i,i) for i in range(1,20+1)]
    
    #Valores dependientes del proyecto
    res['fHistoria_opcionesActores']       = [{'key':act.idrole,'value':act.namerole}for act in actorList]
    res['fHistoria_opcionesAcciones']      = [{'key':acc.idaccion,'value':acc.acciondescription}for acc in accionList]
    res['fHistoria_opcionesObjetivos']     = [{'key':obj.idobjective,'value':obj.descObjective}for obj in objectiveList]
    res['fHistoria_opcionesHistorias']     = [{'key':hist.id_userHistory,'value':hist.cod_userHistory}for hist in historyList]
    res['fHistoria_opcionesTiposHistoria'] = [{'key':1,'value':'Opcional'},{'key':2,'value':'Obligatoria'}]
    res['fHistoria_opcionesPrioridad']     = [{'key':scale[0], 'value':scale[1]}for scale in resultScale]
    
    res['fHistoria'] = {'super':0, 'idPila':1}
    res['idPila'] = 1
 
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    # Obtenemos el id de la historia
    idHistoria = request.args.get('idHistoria')  
    idHistoria = int(idHistoria)

    scale = {1:'Alta',2:'Media',3:'Baja'}
    # Obtenemos la historia que queremos modificar.
    history    = clsUserHistory.query.filter_by(id_userHistory = idHistoria).first()
    
    # Obtenemos todas las acciones, actores y objetivos asociados al producto.
    oBacklog      = backLog() 
    oObjective    = objective()
    oUserHist     = userHistory()
    oActUserHist  = actorsUserHistory()
    oObjUserHist  = objectivesUserHistory()
    actorList     = oBacklog.actorsAsociatedToProduct(1)
    accionList    = oBacklog.accionsAsociatedToProduct(1)
    objectiveList = oBacklog.objectivesAsociatedToProduct(1)
    
    # Obtenemos todas las historias de usuarios excepto la actual
    historias =  oUserHist.getAllUserHistoryId(1)
    for hist in historias:
        if hist.id_userHistory == idHistoria:
            historias.remove(hist)
            break

    # Obtenemos todos los objetivos que son no trasnversales.        
    for object in objectiveList:
        idObjective = object.idobjective
        transverse  = oObjective.verifyObjectiveTransverse(idObjective)
        if (int(transverse) == 1):
            objectiveList.remove(object)

    # Obtenemos los actores asociados a una historia de usuario.
    actors = oActUserHist.idActorsAsociatedToUserHistory(idHistoria)

    # Obtenemos los objetivos asociados a una historia de usuario.
    objectives = oObjUserHist.idObjectivesAsociatedToUserHistory(idHistoria)            
    
    # Obtenemos la escala a mostrar
    
    typeScale = oUserHist.scaleType(idHistoria)
    # Obtenemos el tipo de escala asociado al producto (id,valor)
    if typeScale == 1:
        resultScale = [(i,scale[i]) for i in range(1,3+1)]
    elif typeScale == 2:
        resultScale = [(i,i) for i in range(1,20+1)]
    
    
    res['fHistoria_opcionesHistorias']     = [{'key':hist.id_userHistory,'value':hist.cod_userHistory}for hist in historias] 
    res['fHistoria_opcionesHistorias'].append({'key':0,'value':'Ninguno'})
    res['fHistoria_opcionesTiposHistoria'] = [{'key':1,'value':'Opcional'},{'key':2,'value':'Obligatoria'}]
    res['fHistoria_opcionesActores']       = [{'key':act.idrole,'value':act.namerole}for act in actorList]
    res['fHistoria_opcionesAcciones']      = [{'key':acc.idaccion,'value':acc.acciondescription}for acc in accionList]
    res['fHistoria_opcionesObjetivos']     = [{'key':obj.idobjective,'value':obj.descObjective}for obj in objectiveList]
    res['fHistoria_opcionesPrioridad']     = [{'key':scale[0], 'value':scale[1]}for scale in resultScale]
    
    #Escala dependiente del proyecto
#    res['fHistoria_opcionesPrioridad'] = [
#      {'key':1, 'value':'Alta'},
#      {'key':2, 'value':'Media'},
#     {'key':3, 'value':'Baja'},
#    ]
    
    res['fHistoria'] = {'super':history.id_History, 'idHistoria':idHistoria, 'idPila':history.id_backLog, 'codigo':history.cod_userHistory,
       'actores':[1], 'accion':history.ref_idaccion, 'objetivos':[1], 'tipo':history.type_accion,
       'prioridad':history.UH_scale}
    
    res['idPila']  = 1   

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
    #priorities    = {1:'Alta',2:'Media',3:'Baja'}
    
    for hist in userHistoriesList:
        historyDict   = {}
         
        historyDict['idHistory'] = hist.id_userHistory
        historyDict['priority'] = hist.UH_scale
         
        idActorsList  = oActUserHist.idActorsAsociatedToUserHistory(hist.id_userHistory)
        missingActors = len(idActorsList)
        actorsString  = ''
        
        for act in idActorsList:
            result       = oRole.findIdRole(act)
            actorsString = actorsString + ' ' + str(result[0].namerole) + ' '
            if missingActors != 1:
                actorsString = actorsString + ','  
            missingActors = missingActors - 1   
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
            if missingObjectives == 1: 
                objectivesString = objectivesString + '.'  
            missingObjectives = missingObjectives - 1
        historyDict['objectives'] = objectivesString.lower()
             
        userHistories.append(historyDict)

    res['data0']   = [{'idHistoria':hist['idHistory'], 'prioridad':hist['priority'],'enunciado':'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in userHistories]
    
    res['idPila']  = 1
    
    return json.dumps(res)

@historias.route('/historias/VPrioridades')
def VPrioridades():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    oRole             = role()
    oAccion           = accions()
    oObjective        = objective()
    oBacklog          = backLog() 
    oUserHistory      = userHistory()
    oActUserHist      = actorsUserHistory()
    oObjUserHIst      = objectivesUserHistory()
    userHistoriesList = oBacklog.userHistoryAsociatedToProduct(1)  
         
    userHistories = []
    options       = {1:'podría ',2:'puede '}
    for hist in userHistoriesList:
        historyDict   = {}
         
        historyDict['idHistory'] = hist.id_userHistory
        historyDict['priority'] = hist.UH_scale
         
        idActorsList  = oActUserHist.idActorsAsociatedToUserHistory(hist.id_userHistory)
        missingActors = len(idActorsList)
        actorsString  = ''
        
        for act in idActorsList:
            result       = oRole.findIdRole(act)
            actorsString = actorsString + ' ' + str(result[0].namerole) + ' '
            if missingActors != 1:
                actorsString = actorsString + ',' 
            missingActors = missingActors - 1   
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
            missingObjectives = missingObjectives - 1 
        historyDict['objectives'] = objectivesString.lower()
             
        userHistories.append(historyDict)

    
    res['data0']   = [{'idHistoria':hist['idHistory'], 'prioridad':hist['priority'],'enunciado':'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in userHistories]

    #Escala dependiente del proyecto
    res['fPrioridades_opcionesPrioridad'] = [
      {'key':1, 'value':'Alta'},
      {'key':2, 'value':'Media'},
      {'key':3, 'value':'Baja'},
    ]
    res['idPila'] = 1
    res['fPrioridades'] = {'idPila':1,
      'lista':[{'idHistoria':hist['idHistory'],'prioridad':hist['priority'], 'enunciado':'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in userHistories]}


    #Action code ends here
    return json.dumps(res)
