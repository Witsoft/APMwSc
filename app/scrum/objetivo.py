# -*- coding: utf-8 -*-

from flask               import request, session, Blueprint, json
from app.scrum.objective import *
from app.scrum.backLog   import *
from app.scrum.objectivesUserHistory   import *

objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res     = results[1]
    
    # Obtenemos el id del producto.
    idPila  = int(session['idPila'])
    print('idPila ACrearObjetivo',idPila) 
    
    if request.method == 'POST':
    
        # Extraemos los parametros.
        newDescription      = params['descripcion']
        transverseObjective = params['transversal']
        
        oObjective = objective()
        result     = oObjective.insertObjective(newDescription,idPila,transverseObjective)

        if result:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            
    return json.dumps(res)



@objetivo.route('/objetivo/AElimObjetivo')
def AElimObjetivo():
    #GET parameter
    #idObjetivo = request.args['idObjetivo']
    results = [{'label':'/VProducto', 'msg':['Objetivo eliminado']}, {'label':'/VProducto', 'msg':['No se pudo eliminar este objetivo']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    
    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])
    idObjective  = int(session['idObjective'])
    
    # Conseguimos el objetivo a eliminar  
    oObjetivo    = objective()
    found = oObjetivo.searchIdObjective(idObjective) 
    
    oObjUserHistory = objectivesUserHistory()
    result = oObjUserHistory.searchidUserHistoryIdObjective(idObjective)
    # Verificamos si el objetivo esta asociado a una historia
    print("result",result)
    if (result == []):
        deleted = oObjetivo.deleteObjective(found[0].O_descObjective) 

        if deleted:
            res = results[0]  

    res['label'] = res['label'] +  '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res     = results[1] 
    
    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])
    print('idPila AModifAccion',idPila) 
    
    # Extraemos los parametros.
    idObjetivo     = params['idObjetivo']  # Obtenemos el id del objetivo
    newDescription = params['descripcion'] # Obtenemos la nueva descripción del objetivo
    newType        = params['transversal'] # Obtenemos el tipo de objetivo(transversal,no transversal)
    
    oObjetivo    = objective()
    # Conseguimos el objetivo a modificar.
    objetivoDesc = oObjetivo.searchIdObjective(idObjetivo) 
    #Modificamos la descripción del objetivo.    
    result       = oObjetivo.updateObjective(objetivoDesc[0].O_descObjective , newDescription,newType) 

    if result:
        res = results[0]
        
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            
    return json.dumps(res)



@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto y del objetivo.
    idPila      = int(session['idPila'])
    idObjective = int(request.args.get('idObjetivo'))
    print('idPila VObjetivo',idPila)
    print('idObjetivo VObjetivo',idObjective)
    
    boolean = {0:False,1:True}
    
    if "actor" in session:
        res['actor']=session['actor']
        
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    res['usuario'] = session['usuario']
    
    oObjective = objective()
    result     = oObjective.searchIdObjective(idObjective)
    number     = int(result[0].O_objType)
    istransver = boolean[number]

    res['fObjetivo_opcionesTransversalidad'] = [{'key':True, 'value':'Si'},{'key':False, 'value':'No'}]
    res['fObjetivo'] = {'idObjetivo':idObjective, 'descripcion':result[0].O_descObjective , 'transversal':istransver}    
    res['idPila']    = idPila
    session['idObjective'] = idObjective

    return json.dumps(res)



@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto.
    idPila = request.args.get('idPila',1)
    print('idPila VCrearObjetivo',idPila)
    
    if "actor" in session:
        res['actor']=session['actor']
        
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
   
    res['fObjetivo_opcionesTransversalidad'] = [{'key':True, 'value':'Si'},
                                                {'key':False, 'value':'No'},
                                                {'key':0,'value':'Seleccione una opción'}]
    res['fObjetivo'] = {'transversal':0} 
    res['idPila']    = idPila   

    return json.dumps(res)




#Use case code starts here


#Use case code ends here