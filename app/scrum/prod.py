# -*- coding: utf-8 -*-
from flask             import request, session, Blueprint, json
from app.scrum.backLog import *


prod = Blueprint('prod', __name__)


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    
    prodDesc = params['descripcion']
    
    oBackLog = backLog()
    result   = oBackLog.insertBackLog(prodDesc)
    
    if result:
        res = results[0]
    else:
        res = results[1]
    
    
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

    newdescription = params['descripcion']

    idPila = params['idPila'] #Obtenemos el id del producto

    oBackLog = backLog()
    result   = clsBackLog.query.filter_by(id_backLog = idPila).first()  #Conseguimos el producto a modificar
    oBackLog.modifyDescription(result.BL_description, newdescription) #Modificamos el producto      

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
    accionList = oBackLog.accionsAsociatedToProduct(1)
    objectList = oBackLog.objectivesAsociatedToProduct(1)
    

    res['data3'] = [{'idActor':act.idrole,'descripcion':act.namerole + ' : ' + act.roledescription}for act in actorsList]
    res['data5'] = [{'idAccion':acc.idaccion, 'descripcion':acc.acciondescription}for acc in accionList]
    res['data7'] = [{'idObjetivo':obj.idobjective, 'descripcion':obj.descObjective} for obj in objectList]
    
    res['idPila'] = idPila    
    
    #result   = clsBackLog.query.filter_by(id_backLog = idPila).first()
    
    #res['fPila'] = {'idPila':idPila, 'descripcion':result.BL_description}

    result   = clsBackLog.query.filter_by(id_backLog = idPila).first()
    
    res['fPila'] = {'idPila':idPila,'descripcion':result.BL_description}



    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    # Obtenemos la lista de productos.
    productList = clsBackLog.query.all()  
    for prod in productList:
        print(prod.id_backLog,prod.BL_description)

    res['data0'] = [{'idPila':prod.id_backLog,'nombre':prod.BL_description}for prod in productList]

    return json.dumps(res)


#Use case code starts here


#Use case code ends here
