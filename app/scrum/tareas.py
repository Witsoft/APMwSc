# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.backLog               import *
from app.scrum.userHistory           import *
from app.scrum.homework              import *
tareas = Blueprint('tareas', __name__)


@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VCrearTarea', 'msg':['No se pudo crear tarea.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    idHistoria  = int(session['idHistoria'])
    #print('idHistoria AcrearTarea',idHistoria)
    #idHistoria    = 1
    oBackLog = backLog()
    oHistory = userHistory()
    userHistoriesList = oBackLog.userHistoryAsociatedToProduct(1)  
    oHomework = homework()
    
    descTarea = params['descripcion']
    
    insert = oHomework.insertHomework(descTarea,idHistoria)
    
    if insert == True:        
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



@tareas.route('/tareas/AElimTarea')
def AElimTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea borrada']}, {'label':'/VTarea', 'msg':['No se pudo eliminar esta tarea']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idHistoria  = int(session['idHistoria'])
    idTarea     = int(session['idTarea'])
    oTarea   = homework()
    result   = clsHomework.query.filter_by(HW_idHomework = idTarea).first()
    delete   = oTarea.deleteHomework(result.HW_description)
    
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
        
    oTarea   = homework()
    result   = clsHomework.query.filter_by(HW_idHomework = idTarea).first()
    modify   = oTarea.updateHomework(result.HW_description,new_description)
    
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
    idHistoria  = int(session['idHistoria'])
    print('idHistoria VCrearTarea',idHistoria)
    
    idHistoria = request.args['idHistoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = 'H01'
    
    res['idHistoria'] = idHistoria


    #Action code ends here
    return json.dumps(res)



@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter
    idTarea = request.args['idTarea']
    idHistoria = int(session['idHistoria'])
    found = clsUserHistory.query.filter_by(id_userHistory = idHistoria).first()
    codHistoria = found.cod_userHistory
    
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    idTarea = request.args.get('idTarea')
    result   = clsHomework.query.filter_by(HW_idHomework = idTarea).first()
    res['fTarea'] = {'idTarea': idTarea,'descripcion': result.HW_description}
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = codHistoria

    session['idTarea'] = idTarea
    res['idTarea'] = idTarea

    #Action code ends here
    return json.dumps(res)


#Use case code starts here


#Use case code ends here

