# -*- coding: utf-8 -*-

#Agregando proyect root

import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

#Dependencias flask
from flask import request, session, Blueprint, json
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import text

#Definicion de blueprint y bd
objetivo = Blueprint('objetivo', __name__)
from base import *


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message  
    idPila = str(session['idPila'])
    session.pop('idPila', None)
    objetivo = objective()
    objetivo.insertObjective(descObjective = params['descripcion'], id_backlog = idPila)
    res['label'] = res['label'] + '/' + str(idPila)
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
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message
    idPila = int(request.args.get('idPila', 1))
    objetivo = objective()
    objetivo.updateObjective(params['descripcion'])
    res['label'] = res['label'] + '/' + str(idPila)
    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    #Action code goes here, res should be a JSON structure
    params = request.get_json()    
    session['idPila'] = request.args['idPila']
    #Action code ends here
    
    return json.dumps(res)



@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    #Action code goes here, res should be a JSON structure     
    objetivo = objective()

    idPila = int(request.args.get('idPila', 1))
    #objs = objetivo.listarObjetivos()
    #res['fObjetivo'] = objs[idProducto-1]
    #idObjetivo=idPila

    #res['idPila'] = 1 

    #Action code ends here
    
    return json.dumps(res)





#Use case code starts here


#Use case code ends here