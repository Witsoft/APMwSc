# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.objective import *
from app.scrum.backLog import *
#import model 

objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters

    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    
    if request.method == 'POST':
    
        oObjective = objective()
        newDescription = params['descripcion']
        transverseObjective = params['transversal']
                
        result = oObjective.insertObjective(newDescription,1,transverseObjective)

        if result:
            res = results[0]
        else:
            res = results[1]
    else:
            res = results[1]

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)
    
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
    idPila  = 1

    idObjetivo     = params['idObjetivo']  #Obtenemos el id del objetivo
    newDescription = params['descripcion'] #Obtenemos la nueva descripción del objetivo
    newType        = params['transversal'] #Obtenemos el tipo de objetivo(transversal,no transversal)
    objetivoDesc = clsObjective.query.filter_by(idobjective = idObjetivo).first() #Conseguimos el objetivo a modificar
    print("Antes",objetivoDesc.obj_type)
    oObjetivo    = objective()
    result       = oObjetivo.updateObjective(objetivoDesc.descObjective, newDescription,newType) #Modificamos la descripción del objetivo

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


@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    boolean = {0:False,1:True}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure
    idObjetivo = request.args.get('idObjetivo')
    
    result   = clsObjective.query.filter_by(idobjective = idObjetivo).first()
    entero   = int(result.obj_type)
    istrans  = boolean[entero]

    res['idPila'] = 1 
    res['fObjetivo_opcionesTransversalidad'] = [
      {'key':True, 'value':'Si'},{'key':False, 'value':'No'}]
    res['fObjetivo'] = {'idObjetivo':idObjetivo, 'descripcion':result.descObjective, 'transversal':istrans}    
    
    #Action code ends here
    return json.dumps(res)



@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
   
    #Action code goes here, res should be a JSON structure
    #params = request.get_json() 
    
    #Datos de prueba
    res['idPila'] = 1
    res['fObjetivo_opcionesTransversalidad'] = [
      {'key':True, 'value':'Si'},{'key':False, 'value':'No'},
    ]   

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here