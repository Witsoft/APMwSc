# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

# Declaracion de constantes.
CONST_MAX_NAME_CATEGORY     = 50
CONST_MIN_NAME_CATEGORY     = 1
CONST_MIN_ID_CATEGORY       = 1
CONST_MIN_WEIGHT            = 0

class category(object):
    '''Clase que permite crear una variedad de Categorías para ser usadas en una o más tareas'''
    
    def insertCategory(self,nameCategory,weight):
        '''Permite insertar una categoría'''
        
        checkTypeNameCategory = type(nameCategory) == str
        checkTypeWeight       = type(weight) == int
        
        if checkTypeNameCategory and checkTypeWeight:
            checkLongNameCategory = CONST_MIN_NAME_CATEGORY <= len(nameCategory) <= CONST_MAX_NAME_CATEGORY
            checkLongWeight       = CONST_MIN_WEIGHT <= weight            
            
            if checkLongNameCategory and checkLongWeight:
                foundName = clsCategory.query.filter_by(C_nameCate = nameCategory).all()
                
                if foundName == []:
                    newCategory = clsCategory(nameCategory,weight)
                    db.session.add(newCategory)
                    db.session.commit()
                    return True                                           
        return False

    def updateCategory(self,nameCategory,newNameCategory,weight,newWeight):
        '''Permite modificar el nombre y el peso de una categoría'''
    
        checkTypeNameCategory    = type(nameCategory) == str
        checkTypeNewNameCategory = type(newNameCategory) == str
        checkTypeWeight          = type(Weight) == int
        checkTypeNewWeight       = type(newWeight) == int
    
        if checkTypeNameCategory and checkTypeNewNameCategory and checkTypeWeight and checkTypeNewWeight:
            checkLongNameCategory    = CONST_MIN_NAME_CATEGORY <= len(nameCategory) <= CONST_MAX_NAME_CATEGORY
            checkLongNewNameCategory = CONST_MIN_NAME_CATEGORY <= len(newNameCategory) <= CONST_MAX_NAME_CATEGORY
            checkWeight          = CONST_MIN_WEIGHT <= weight
            checkNewWeight       = CONST_MIN_WEIGHT <= newWeight 
            
            if checkLongNameCategory and checkLongNewNameCategory and checkWeight and checkNewWeight:    
                foundNameCategory = clsCategory.query.filter_by(C_nameCate = nameCategory).all()
                foundNewNameCategory  = clsActor.query.filter_by(C_nameCate = newNameCategory).all()
                
                if foundNameCategory != [] and foundNewNameCategory == []:
                    updateActor = clsCategory.query.filter_by(C_nameCate = nameCategory).first()
                    updateActor.C_nameCategoy = newNameCategory
                    updateActor.C_weight      = newWeight
                    db.session.commit()
                    return True
        return False   
    

    def deleteCategory(self,nameCategory):
        '''Permite eliminar una categoría dada su nombre'''

        checkTypeNameCategory = type(nameCategory) == str

        if checkTypeNameCategory:
            
            checkLongNameCategory = CONST_MIN_NAME_CATEGORY <= len(nameCategory) <= CONST_MAX_NAME_CATEGORY 
            if checkLongNameCategory:
                cCategory = clsCategory.query.filter_by(C_nameCate = nameCategory).all()
                if cCategory != []:
                    tupla = clsCategory.query.filter_by(C_nameCate = nameCategory).first()    
                    db.session.delete(tupla)
                    db.session.commit()
                    return True
        return False
    
    def searchCategory(self, C_nameCate):
        '''Permite buscar categorias por su nombre'''
        
        typeNameCategory = (type(C_nameCate) == str)
        
        cCategory = []
        if typeNameCategory:
            cCategory = clsCategory.query.filter_by(C_nameCate = C_nameCate).all()
        return cCategory

    def searchIdCategory(self, idCategory):
        '''Permite buscar categorias por su id'''
        
        typeIdCategory = (type(idCategory) == int)
        
        cCategory = []
        if typeIdCategory:
            cCategory = clsCategory.query.filter_by(C_idCategory = idCategory).all()
        return cCategory

    
# Fin Clase Category