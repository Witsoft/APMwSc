# -*- coding: utf-8 -*-

from flask                 import request, session, Blueprint, json
from app.scrum.backLog     import *
from app.scrum.userHistory import *
from app.scrum.task        import *

tareas = Blueprint('tareas', __name__)


@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VHistoria', 'msg':['No se pudo crear tarea.']}, ]
    res     = results[0]
    
    # Obtenemos el id de la historia actual
    idHistory = int(session['idHistoria'])

    # Extraemos los parámetros
    taskDesc    = params['descripcion']
    idCategoria = params['categoria']
    taskPeso    = params['peso']
    oBackLog    = backlog()
    oTask       = task()
    
    insert   = oTask.insertTask(taskDesc, idCategoria, taskPeso, idHistory)
    
    if insert:        
        res = results[0]
    else:
        res = results[1]
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
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea borrada']}, {'label':'/VHistoria', 'msg':['No se pudo eliminar la tarea']}, ]
    res     = results[1]

    # Obtenemos los parámetros
    idHistoria = int(session['idHistoria'])
    idTarea    = int(session['idTarea'])

    # Eliminamos la tarea 
    oTarea     = task()
    result     = clsTask.query.filter_by(HW_idTask = idTarea).first()
    delete     = oTarea.deleteTask(result.HW_description)

    if delete:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idHistoria)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AModifTarea', methods=['POST'])
def AModifTarea():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea modificada']}, {'label':'/VCrearTarea', 'msg':['No se pudo modificar esta tarea.']}, ]
    res     = results[1]

    # Obtenemos los parámetros
    idHistoria  = int(session['idHistoria'])
    new_description = params['descripcion']
    idTarea         = params['idTarea']
    new_idCategoria = params['categoria']
    new_taskPeso    = params['peso']
  
    # Buscamos la tarea a modificar
    oTarea   = task()
    result   = clsTask.query.filter_by(HW_idTask = idTarea).first()
 
    # Modificamos la tarea
    modify   = oTarea.updateTask(result.HW_description,new_description,new_idCategoria,new_taskPeso)
    
    if modify:
        res = results[0]
         
    res['label'] = res['label'] + '/' + str(idHistoria)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@tareas.route('/tareas/VCrearTarea')
def VCrearTarea():
    #GET parameter
    res = {}    
    # Obtenemos el id de la historia actual
    idHistory = int(request.args.get('idHistoria'))
    
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    # Buscamos la historia actual
    oUserHistory = userHistory()
    hist         = oUserHistory.searchIdUserHistory(idHistory)
    
    res['usuario']        = session['usuario']
    res['codHistoria']    = hist[0].UH_codeUserHistory
    
    # Obtenemos una lista con los datos asociados a las categorías
    cateList  = clsCategory.query.all()        
    
    # Mostramos los datos en la vista
    ListaCompleta = []
    for i in cateList:
        ListaCompleta.append((i.C_idCategory,i.C_nameCate,i.C_weight))
    
    decorated = [(tup[2], tup) for tup in ListaCompleta]
    decorated.sort()

    res['fTarea_opcionesCategoria'] = [
     {'key':cat[1][0] ,'value':cat[1][1]+" ("+str(cat[1][2])+")",'peso':cat[1][2]} for cat in decorated]                                 

    res['fTarea'] = {'idHistoria':idHistory}

    session['idHistoria'] = idHistory
    res['idHistoria']     = idHistory

    return json.dumps(res)


@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter
    
    # Obtenemos el id de la historia y de la tarea
    idTarea    = int(request.args['idTarea'])
    idHistoria = int(session['idHistoria'])

    found = clsUserHistory.query.filter_by(UH_idUserHistory = idHistoria).first()
    codHistoria = found.UH_codeUserHistory
    
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idTarea = request.args.get('idTarea')
    result   = clsTask.query.filter_by(HW_idTask = idTarea).first()
    categoryList     = clsCategory.query.all()
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario']      = session['usuario']
    res['codHistoria']  = codHistoria

    res['fTarea_opcionesCategoria'] = [
      {'key':cat.C_idCategory ,'value':cat.C_nameCate+" ("+str(cat.C_weight)+")",'peso':result.HW_weight}for cat in categoryList]

    res['fTarea'] = {'idHistoria':idHistoria,'idTarea': idTarea,'descripcion': result.HW_description, 'categoria': result.HW_idCategory, 'peso':result.HW_weight}


    session['idTarea'] = idTarea
    res['idTarea']     = idTarea
    res['idHistoria']  = idHistoria

    return json.dumps(res)


#Use case code starts here


#Use case code ends here

