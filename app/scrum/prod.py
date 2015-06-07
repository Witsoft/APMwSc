# -*- coding: utf-8 -*-
from flask             import request, session, Blueprint, json
from app.scrum.backLog import *


prod = Blueprint('prod', __name__)


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    
    prodName  = params['nombre']
    prodDesc  = params['descripcion']
    prodScale = params['escala']
    
    oBacklog = backlog()
    result   = oBacklog.insertBacklog(prodName,prodDesc,prodScale)
    
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
    newname        = params['nombre']
    newdescription = params['descripcion']
    newscale       = params['escala']
     
    idPila = params['idPila'] #Obtenemos el id del producto

    oBacklog = backlog()
    result   = clsBacklog.query.filter_by(BL_idBacklog = idPila).first()  #Conseguimos el producto a modificar
    oBacklog.modifyBacklog(result.BL_name, newname, newdescription, newscale) #Modificamos el producto      

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
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]

    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProducto')
def VProducto():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    idPila = int(request.args.get('idPila', 1))
    
    #idPila    = request.args.get('idPila')
    idProduct = idPila
    #idProduct = 1
    #pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}]
    #res['fPila'] = pilas[idPila-1]    

    oBacklog   = backlog()
    actorsList = oBacklog.actorsAsociatedToProduct(idProduct)
    accionList = oBacklog.accionsAsociatedToProduct(idProduct)
    objectList = oBacklog.objectivesAsociatedToProduct(idProduct)
    

    res['data3'] = [{'idActor':act.A_idActor,'descripcion':act.A_nameActor + ' : ' + act.A_actorDescription}for act in actorsList]
    res['data5'] = [{'idAccion':acc.idaccion, 'descripcion':acc.acciondescription}for acc in accionList]
    res['data7'] = [{'idObjetivo':obj.idobjective, 'descripcion':obj.descObjective} for obj in objectList]
      

    result   = clsBacklog.query.filter_by(BL_idBacklog = idPila).first()
    
    res['idPila'] = idPila  
    res['fPila'] = {'idPila':idPila,'nombre': result.BL_name,'descripcion':result.BL_description,'escala':result.BL_scaleType}
    res['fPila_opcionesEscala'] = [{'key':1,'value':'Alta/Media/Baja'}, {'key':2,'value':'Entre 1 y 20'}]
    res['fPila_escala'] = {'prioridad':1}
    

    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Obtenemos la lista de productos.
    productList = clsBacklog.query.all()
    
    res['data0'] = [{'idPila':prod.BL_idBacklog,'nombre':prod.BL_name, 'descripcion': prod.BL_description, 'prioridad': prod.BL_scaleType}for prod in productList]

    return json.dumps(res)


#Use case code starts here


#Use case code ends here
