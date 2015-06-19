# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.category import *
from app.scrum.model    import *
from _operator import length_hint

cates = Blueprint('cates', __name__)


@cates.route('/cates/ACrearCategoria', methods=['POST'])
def ACrearCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría creada.']}, {'label':'/VCategorias', 'msg':['Error al intentar crear categoría.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    if params != {}:    
        # Extraemos los parametros.
        cateName    = params['nombre']
        cateWeight  = params['peso']
        
        cCategory = category()
        inserted = cCategory.insertCategory(cateName,cateWeight)
        
        if inserted:
            res = results[0]    
            
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AElimCategoria')
def AElimCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    print('idCategoria AElimCategoria',idCategoria)
    results = [{'label':'/VCategorias', 'msg':['Categoría eliminada.']}, {'label':'/VCategorias', 'msg':['Error al intentar eliminar categoría.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AModifCategoria', methods=['POST'])
def AModifCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría actualizada.']}, {'label':'/VCategorias', 'msg':['Error al intentar modificar categoría.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    # Obtenemos el id de la categoría
    idCategoria = request.args['idCategoria']

    # Obtenemos los paràmetros    
    newNameCategory = params['nombre']
    newWeidght      = params['peso']

    cCategory = category()    

    # Buscamos la categoriaía a modificar
    showCate = cCategory.seachIdCategory(idCategory)
    



    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/VCategoria')
def VCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['idCategoria'] = int(idCategoria)

    # Buscamos la tupla asociada al id capturado
    cCategory = category()
    showCate  = cCategory.searchIdCategory(idCategoria)
        
    res['fCategoria'] = {'idCategoria':showCate.C_idCategory, 'peso':showCate.C_nameCate, 
                         'nombre':showCate.C_weight}


    #Action code ends here
    return json.dumps(res)



@cates.route('/cates/VCategorias')
def VCategorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    # Obtenemos una lista con los datos asociados a las categorías.
    cateList  = clsCategory.query.all()        
    
    # Mostramos los datos en la vista.
    
    ListaCompleta = []
    for i in cateList:
        ListaCompleta.append((i.C_idCategory,i.C_nameCate,i.C_weight))
    
    decorated = [(tup[2], tup) for tup in ListaCompleta]
    decorated.sort()

    #ListaCompleta.sorted(key=lambda tup: tup[2]) 
    
    res['data0'] = [{'idCategoria':cat[1][0],'nombre':cat[1][1],'peso':cat[1][2]} for cat in decorated]

    #sorted(cateList, key=lambda category: category[2])



    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

