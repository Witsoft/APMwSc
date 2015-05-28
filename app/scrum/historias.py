# -*- coding: utf-8 -*-
from flask                           import request, session, Blueprint, json
from app.scrum.backLog               import *
from app.scrum.userHistory           import *
from app.scrum.role                  import *
from app.scrum.accions               import *
from app.scrum.objective             import *   
from app.scrum.objectivesUserHistory import *
from app.scrum.actorsUserHistory     import * 

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
    print(params)
 
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
        
        
        if insertedObj: #insertedAct and insertedObj:
            res = results[0]  
            res['label'] = res['label'] + '/1'
        else:
            res = results[1] 
            
#     if (inserted):
#         result = oUserHistory.searchUserHistory(codeHistory)
#         # Buscamos el id de la historia de usuario recien insertada.
#         idVarInsert = result[0].id_userHistory
#         
#         # Modificamos las tablas que referencian a la historia de usuario.
#         oActor     = role()
#         oAccion    = accions()
#         oObjective = objective()
# 
#         resultUpdateAccion   = oAccion.updateAccionReferenceToHistory(idAccion,idVarInsert)
# 
#         for id in idActor:
#             resultUpdateActor    = oActor.updateRoleReferenceToHistory(id,idVarInsert)
#         
#         for id in idObjective:
#             resultUpdateObjective = oObjective.updateObjectiveReferenceToHistory(id,idVarInsert)
#         
#         if resultUpdateAccion and resultUpdateActor and resultUpdateObjective:
#            res = results[0]
#         else:
#            res = results[1] 

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
    res['fHistoria_opcionesActores'] = [{'key':act.idrole,'value':act.namerole}for act in actorList]
    res['fHistoria_opcionesAcciones'] = [{'key':acc.idaccion,'value':acc.acciondescription}for acc in accionList]
    res['fHistoria_opcionesObjetivos'] = [{'key':obj.idobjective,'value':obj.descObjective}for obj in objectiveList]
    res['fHistoria_opcionesHistorias'] = [{'key':hist.id_userHistory,'value':hist.cod_userHistory}for hist in historyList]
    res['fHistoria_opcionesTiposHistoria'] = [{'key':1,'value':'Opcional'},{'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0}
    res['idPila'] = 1


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0, 
       'actor':1, 'accion':2, 'objetivo':3, 'tipo':1} 
    res['idPila'] = 1

    return json.dumps(res)



@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor'] = session['actor']
    
    
#     
#     
#     oBacklog          = backLog() 
#     oUserHistory      = userHistory()
#     userHistoriesList = oBacklog.userHistoryAsociatedToProduct(1)  
#     
#     #####################################################3
#     for hist in userHistoriesList:
#         result1 = oUserHistory.actorsAsociatedToUserHistory(hist.id_userHistory)
#         result2 = oUserHistory.objectivesAsociatedToUserHistory(hist.id_userHistory)
#         result3 = oUserHistory.accionsAsociatedToUserHistory(hist.id_userHistory)
#         print('Historia: ' + str(hist.cod_userHistory) + ' Actores: ' + str(result1) +' Accion: ' + str(result2) + ' Objetivos: ' + str(result3) + '\n')
#            
#     
#     #######################################################
#     
#     userHistories = []
#     options       = {1:'podria ',2:'puede '}
#     for hist in userHistoriesList:
#         historyDict   = {}
#         
#         historyDict['idHistory'] = hist.id_userHistory
#         
#         actorsList    = oUserHistory.actorsAsociatedToUserHistory(hist.id_userHistory)
#         missingActors = len(actorsList)
#         actorsString  = ''
#         for act in actorsList:
#             actorsString = actorsString + ' ' + str(act.namerole) + ' '
#             if missingActors != 1:
#                 actorsString = actorsString + ','    
#         historyDict['actors'] = actorsString.lower()
#         
#         accionsList = oUserHistory.accionsAsociatedToUserHistory(hist.id_userHistory)
#         historyDict['accions'] = ' ' + options[1] + str(accionsList[0].acciondescription).lower() + ' ' 
#         
#         objectivesList    = oUserHistory.objectivesAsociatedToUserHistory(hist.id_userHistory)
#         missingObjectives = len(objectivesList)
#         objectivesString  = ''
#         for obj in objectivesList:
#             objectivesString = objectivesString + ' ' + str(obj.descObjective)
#             if missingObjectives != 1:
#                 objectivesString = ' ' + objectivesString + ','  
#             elif missingObjectives == 1: 
#                 objectivesString = objectivesString + '.'  
#         historyDict['objectives'] = objectivesString.lower()
#             
#         userHistories.append(historyDict)
#        
#         print(userHistories)
#            
#     res['idPila']  = 1
#     res['data0']   = [{'idHistoria':hist['idHistory'], 'enunciado':'En tanto' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in userHistories] 
    res['idPila']  = 1
    res['data0']   = [{'idHistoria':1, 'enunciado':'En tanto'}]
    return json.dumps(res)





#Use case code starts here


#Use case code ends here