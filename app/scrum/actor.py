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



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    idPila   = 1
    
    # Action code goes here
    print(params)
    idActor     = params['idActor'] #Obetenemos el id del actor
    newNameRole = params['nombre']
    newDescRole = params['descripcion'] 
    
    actorNombre   = clsRole.query.filter_by(idrole = idActor).first() #Conseguimos el actor a modificar
    
    oRole  = role()
    print('nombre:%r nuevoNombre:%r nuevaDesc:%r',actorNombre.namerole, newNameRole, newDescRole)
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
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    idActor = request.args.get('idActor')

    result   = clsRole.query.filter_by(idrole = idActor).first()
    
    res['idPila'] = 1 
    res['fActor'] = {'idActor':idActor, 'nombre':result.namerole, 'descripcion':result.roledescription}    

    #Action code ends here
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Datos de prueba
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here