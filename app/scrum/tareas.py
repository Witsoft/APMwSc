# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.backLog               import *
from app.scrum.userHistory           import *
from app.scrum.task              import *
tareas = Blueprint('tareas', __name__)


@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params  = request.get_json()

    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VHistoria', 'msg':['No se pudo crear tarea.']}, ]
    res     = results[1]

    # Obtenemos el id de la historia actual
    idHistory = int(session['idHistoria'])
    print('idHistoria AcrearTarea',idHistory)

    # Extraemos los parametros
    TaskDesc = params['descripcion']
        
    oBackLog  = backlog()
    oHistory  = userHistory()
    oTask = task()
       
    userHistoriesList = oBackLog.userHistoryAsociatedToProduct(idHistory)  
    insert            = oTask.insertTask(TaskDesc,idHistory)
    
    if insert:        
        res = results[0]
    else:
        res = results[1]
        
    res['label'] = res['label'] + '/' + repr(idHistory)

    # Extraemos los parametros
    TaskDesc = params['descripcion']
        
    oBackLog  = backlog()
    oHistory  = userHistory()
    oTask = task()
       
    userHistoriesList = oBackLog.userHistoryAsociatedToProduct(idHistory)  
    insert            = oTask.insertTask(TaskDesc,idHistory)
    
    if insert:        
        res = results[0]
        
    print(res['label'] + '/' + str(idHistory))
    res['label'] = res['label'] + '/' + str(idHistory)


    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AElimTarea')
def AElimTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea borrada']}, {'label':'/VTarea', 'msg':['No se pudo eliminar esta tarea']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idHistoria  = int(session['idHistoria'])
    idTarea     = int(session['idTarea'])
    oTarea   = task()
    result   = clsTask.query.filter_by(HW_idTask = idTarea).first()
    delete   = oTarea.deleteTask(result.HW_description)
    
    if delete == True:
        res = results[0]
    else:
        res = results[1]
    
    res['label'] = res['label'] + '/' + str(idHistoria)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AModifTarea', methods=['POST'])
def AModifTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea modificada']}, {'label':'/VCrearTarea', 'msg':['No se pudo modificar esta tarea.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    idHistoria  = int(session['idHistoria'])
    
    new_description = params['descripcion']
    idTarea         = params['idTarea']
        
    oTarea   = task()
    result   = clsTask.query.filter_by(HW_idTask = idTarea).first()
    modify   = oTarea.updateTask(result.HW_description,new_description)
    
    if modify:
        res = results[0]
    else:
        res = results[1]
         
    res['label'] = res['label'] + '/' + repr(idHistoria)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@tareas.route('/tareas/VCrearTarea')
def VCrearTarea():
    #GET parameter
    
    # Obtenemos el id de la historia actual.
    idHistory = int(request.args.get('idHistoria'))
    print('idHistoria VCrearTarea',idHistory)  
    
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    # Buscamos la historia actual.
    oUserHistory = userHistory()
    hist         = oUserHistory.searchIdUserHistory(idHistory)
    
    res['usuario']        = session['usuario']
    res['codHistoria']    = hist[0].UH_codeUserHistory

    session['idHistoria'] = idHistory
    res['idHistoria'] = idHistory


    return json.dumps(res)



@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter
    
    # Obtenemos el id de la historia y de la tarea.
    idTarea    = int(request.args['idTarea'])
    idHistoria = int(session['idHistoria'])

    found = clsUserHistory.query.filter_by(UH_idUserHistory = idHistoria).first()
    codHistoria = found.UH_codeUserHistory
    
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idTarea = request.args.get('idTarea')
    result   = clsTask.query.filter_by(HW_idTask = idTarea).first()
    res['fTarea'] = {'idTarea': idTarea,'descripcion': result.HW_description}
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = codHistoria

    session['idTarea'] = idTarea
    res['idTarea'] = idTarea

    return json.dumps(res)


#Use case code starts here


#Use case code ends here

