# -*- coding: utf-8 -*-
from flask                 import request, session, Blueprint, json
from app.scrum.backLog     import *
from app.scrum.userHistory import *
from app.scrum.role        import *
from app.scrum.accions     import *
from app.scrum.objective   import *    

historias = Blueprint('historias', __name__)


@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    # Extraemos los parametros.
    idActor     = params['actores']
    idType      = params['tipo']
    idSuperHist = params['super']
    idAccion    = params['accion']
    codeHistory = params['codigo']
    idObjective = params['objetivos']

    oUserHistory = userHistory()
    varInsert    = oUserHistory.insertUserHistory(codeHistory,idType,1)
        
    if (varInsert):
        result = oUserHistory.searchUserHistory(codeHistory)
        # Buscamos el id de la historia de usuario recien insertada.
        idVarInsert = result[0].id_userHistory
        
        # Modificamos las tablas que referencian a la historia de usuario.
        oActor     = role()
        oAccion    = accions()
        oObjective = objective()

        resultUpdateAccion   = oAccion.updateAccionReferenceToHistory(idAccion,idVarInsert)
        #resultUpdateActor    = oActor.updateRoleReferenceToHistory(idActor,idVarInsert)
        #resultUpdateObjetivo = oObjective.updateObjectiveReferenceToHistory(idObjective,idVarInsert)
        
        if resultUpdateAccion:# and resultUpdateActor and resultUpdateObjective:
           res = results[0]
        else:
           res = results[1]       
    
    
    #Datos de prueba
    res['label'] = res['label'] + '/1'

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
    res['fHistoria_opcionesActores'] = [{'key':act.idrole,'value':act.roledescription}for act in actorList]
    res['fHistoria_opcionesAcciones'] = [{'key':acc.idaccion,'value':acc.acciondescription}for acc in accionList]
    res['fHistoria_opcionesObjetivos'] = [{'key':obj.idobjective,'value':obj.descObjective}for obj in objectiveList]
    res['fHistoria_opcionesHistorias'] = [{'key':hist.id_userHistory,'value':hist.cod_userHistory}for hist in historyList]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
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
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Datos de prueba
    res['idPila'] = 1
    res['data0'] = [
      {'idHistoria':1, 'enunciado':'En tanto que picho podría tomar agua para saciar mi sed'}]
    

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here