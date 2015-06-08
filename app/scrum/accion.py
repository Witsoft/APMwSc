# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.accions import *
from app.scrum.backLog import *

accion = Blueprint('accion', __name__)


@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters.
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]
    res     = results[1]
    
    # Obtenemos el id del producto.
    idPila  = int(session['idPila'])
    print('idPila ACrearAccion',idPila) 
    
    if params != {}:           
        # Extraemos los parametros.
        newDescription = params['descripcion']
        
        if request.method == 'POST':
            oAccion  = accions()
            inserted = oAccion.insertAccion(newDescription,idPila)
            
            if inserted:
                res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

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
    results  = [{'label':'/VProducto', 'msg':['Accion eliminada']}, {'label':'/VAccion', 'msg':['No se pudo eliminar esta acción']}, ]
    res      = results[0]
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
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar acción']}, ]
    res     = results[1] 
    
    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])
    print('idPila AModifAccion',idPila) 
     
    # Extraemos los parametros.
    newDescription = params['descripcion']
    idAccion       = int(params['idAccion']) 

    oAccion = accions()
    found   = oAccion.searchIdAccion(idAccion)
    result  = oAccion.updateAccion(found[0].AC_accionDescription, newDescription)     
    
    if result:
        res = results[0]
        
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            
    return json.dumps(res)



@accion.route('/accion/VAccion')
def VAccion():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto y de la accion.
    idPila   = int(session['idPila'])
    idAccion = int(request.args.get('idAccion'))
    print('idPila VAccion',idPila)
    print('idAccion VAccion',idAccion)
    
    if "actor" in session:
        res['actor']=session['actor']
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Buscamos la accion actual.
    oAccion = accions()
    result  =  oAccion.searchIdAccion(idAccion)
    
    res['fAccion'] = {'idAccion':idAccion, 'descripcion':result[0].AC_accionDescription}
    res['idPila']  = idPila

    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto.
    idPila = request.args.get('idPila',1)
    print('idPila VCrearAccion',idPila)

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    res['idPila'] = idPila

    return json.dumps(res)



#Use case code starts here


#Use case code ends here