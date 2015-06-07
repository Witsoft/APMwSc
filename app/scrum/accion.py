# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.accions import *
from app.scrum.backLog import *

accion = Blueprint('accion', __name__)


@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]

    #Action code goes here, res should be a list with a label and a message

    if request.method == 'POST':
    
        oAccion = accions()
        newDescription = params['descripcion']
        result = oAccion.insertAccion(newDescription,1)
        if result:
            res = results[0]
        else:
            res = results[1]
    else:
            res = results[1]

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@accion.route('/accion/AElimAccion')
def AElimAccion():
    #GET parameter
    idAccion = request.args['idAccion']
    results = [{'label':'/VProducto', 'msg':['Accion eliminada']}, {'label':'/VAccion', 'msg':['No se pudo eliminar esta acción']}, ]
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



@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar acción']}, ]
    res = results[0]
    idPila = 1    
    
    #Action code goes here, res should be a list with a label and a message       
    newdescription = params['descripcion']
    idAccion       = params['idAccion']  #Obtenemos el id de la acción

    oAccion  = accions()
    result   = clsAccions.query.filter_by(idaccion = idAccion).first()  #Conseguimos la acción a modificar
    oAccion.updateAccion(result.acciondescription, newdescription) #Modificamos la acción      

    res['label'] = res['label'] + '/' + str(idPila)
    
    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@accion.route('/accion/VAccion')
def VAccion():
    #GET parameter
    idAccion = request.args['idAccion']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['idPila'] = 1 
    res['idAccion'] = 1

    idAccion = request.args.get('idAccion')
    result   = clsAccions.query.filter_by(idaccion = idAccion).first()
    res['idPila'] = 1 
    res['fAccion'] = {'idAccion':idAccion, 'descripcion':result.acciondescription}
    #Action code ends here
    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
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