# -*- coding: utf-8 -*-
from flask          import request, session, Blueprint, json
from app.scrum.role import *

actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]

    idPila   = 1
    nameRole = params['nombre']
    descRole = params['descripcion'] 
    
    oRole  = role()
    result = oRole.insertRole(nameRole,descRole,idPila)
    if result:
        res = results[0]
        res['label'] = res['label'] + '/' + str(idPila)
    else:
        res = results[1]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AElimActor')
def AElimActor():
    #GET parameter
    idActor = request.args['idActor']
    results = [{'label':'/VProducto', 'msg':['Actor eliminado']}, {'label':'/VActor', 'msg':['No se pudo eliminar este actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    #idPila = 1
    #res['label'] = res['label'] + '/' + str(idPila)
    
    idPila   = 1
    
    # Action code goes here
    idActor     = params['idActor'] #Obtenemos el id del actor
    newNameRole = params['nombre']
    newDescRole = params['descripcion'] 
    
    actorNombre   = clsRole.query.filter_by(idrole = idActor).first() #Conseguimos el actor a modificar  
    oRole  = role()
    result = oRole.updateRole(actorNombre.namerole, newNameRole, newDescRole)    #Modfificamos el actor deseado
    
    if result:
        res = results[0]
        res['label'] = res['label'] + '/' + str(idPila)
    else:
        res = results[1]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/VActor')
def VActor():
    #GET parameter
    idActor = request.args['idActor']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['idPila'] = 1 
    res['idActor'] = 1
    
    idActor = request.args.get('idActor')

    result   = clsRole.query.filter_by(idrole = idActor).first()
    
    res['idPila'] = 1 
    res['fActor'] = {'idActor':idActor, 'nombre':result.namerole, 'descripcion':result.roledescription}    

    #Action code ends here
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    #Datos de prueba
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here