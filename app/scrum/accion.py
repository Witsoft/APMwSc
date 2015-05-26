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
            print("Se registró satisfactoriamente la acción")
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



@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar acción']}, ]
    res = results[0]
    idPila = 1
    #Action code goes here, res should be a list with a label and a message

#     if request.method == 'POST':
# 
# 
#         DescriptionList = clsAccions.query.filter_by(id_backLog = idPila).all() 
#         oldDescription = DescriptionList[0]
#         oAccion = accions()
#         newDescription = params['descripcion']
#         result = oAccion.updateAccion(oldDescription,newDescription)
#         if result:
#             print("Se actualizó satisfactoriamente la acción")
#             res = results[0]
#         else:
#             res = results[1]
#     else:
#             res = results[1]

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
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idPila'] = 1 

    #Action code ends here
    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here