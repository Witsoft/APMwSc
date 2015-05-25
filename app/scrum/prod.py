# -*- coding: utf-8 -*-
from flask             import request, session, Blueprint, json
from app.scrum.backLog import *

prod = Blueprint('prod', __name__)


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res     = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, ]
    res     = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProducto')
def VProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']


    idPila = int(request.args.get('idPila', 1))
    #pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}]
    #res['fPila'] = pilas[idPila-1]    
    
    oBackLog   = backLog()
    actorsList = oBackLog.actorsAsociatedToProduct(1)
    objectList = oBackLog.objectivesAsociatedToProduct(1)

    res['data3'] = [{'idActor':act.idrole,'descripcion':act.roledescription}for act in actorsList]
    res['data5'] = [{'idAccion':1, 'descripcion':'Accion 1'}, {'idAccion':2, 'descripcion':'Accion 2'}, {'idAccion':3, 'descripcion':'Accion 3'}, {'idAccion':4, 'descripcion':'Accion 4'}, ]
    res['data7'] = [{'idObjetivo':obj.idobjective, 'descripcion':obj.desObjective} for obj in objectList]
    res['idPila'] = idPila    

    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    # Obtenemos la lista de productos.
    productList = clsBackLog.query.all()
    # Como hasta ahora hay un solo producto.
    productId   = productList[0].id_backLog
    productName = productList[0].BL_name      

    res['data0'] = [{'idPila':productId, 'nombre':productName}]

    return json.dumps(res)


#Use case code starts here


#Use case code ends here
