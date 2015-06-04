# -*- coding: utf-8 -*-. 

from modelDummy import *

# Declaracion de constantes.
const_maxDescription = 140
const_minDescription = 1
const_maxName = 50
const_minName = 1
scale_type = [1,2]

class backLog(object):
    '''Clase que permite (completar)'''
    
    
    def findName(self,dname):
        '''Permite buscar una descripcion'''
        
        checkTypeName = (type(dname)) == str
        if checkTypeName:
            long_dName = const_minName <= len(dname) <= const_maxName
            if long_dName:
                dBackLog = clsBackLog.query.filter_by(BL_name = dname).all()
                return dBackLog
        return []
    
    def insertBackLog(self,name,description,scale):
        '''Permite insertar un producto'''
        
        checkTypeName = (type(name) == str)
        checkTypeDesc = (type(description) == str)
        checkTypeScale = (type(scale) == int)
        if (checkTypeName and checkTypeDesc and checkTypeScale):
           
            long_name = const_minName <= len(name) <= const_maxName
            long_description = (const_minDescription <= len(description) <= const_maxDescription)
            checkScale = scale in scale_type
            if  (long_name and long_description and checkScale):
                dDescAux = self.findName(name);
                if (dDescAux == []):
                    new_prod = clsBackLog(BL_name = name, BL_description = description, BL_scaleType = scale)
                    db.session.add(new_prod)
                    db.session.commit()
                    return True
        return False


    def modifyBackLog(self, name, new_name, new_description, new_scale):   
        '''Permite actualizar los valores de un producto'''            
        typeName          = (type(name) == str)
        typeNewName       = (type(new_name) == str)
        typeDescription   = (type(new_description) == str)
        typeScale         = (type(new_scale) == int) 

        if (typeName and typeNewName and typeDescription and typeScale):
            long_n   = const_minName <= len(name) <= const_maxName
            long_New = const_minName <= len(new_name) <= const_maxName
            long_d = const_minDescription <= len(new_description) <= const_maxDescription
            checkScale = new_scale in scale_type
            if long_d and long_n and long_New and checkScale:
                aName = self.findName(name)
                aNewName = self.findName(new_name)
                if (aName != [] and aNewName == []):
                    new_n = clsBackLog.query.filter_by(BL_name = name).first()
                    new_n.BL_name        = new_name 
                    new_n.BL_description = new_description
                    aUserHistory = clsUserHistory.query.all()
                    if (aUserHistory == []):
                        new_n.BL_scaleType   = new_scale 
                    db.session.commit()
                    return True
        return False

    def deleteProduct(self, name):
        '''Permite eliminar una a descripción de la tabla'''
        if (type(name) != str):
            return False
        else:
            long_name =  (const_minName > len(name) > const_maxName)
            if long_name:
                return False
            else:
                aName = self.findName(name)
                if (aName == []):
                    return False
                else:
                    tupla = clsBackLog.query.filter_by(BL_name = name).first()    
                    db.session.delete(tupla)
                    db.session.commit()
                    return True

    def scaleType(self,productId):
        checkTypeId = type(productId) == int    
        if checkTypeId: 
            found = clsBackLog.query.filter_by(id_backLog=productId).all()
            if found != []:
                oBackLog = clsBackLog.query.filter_by(id_backLog = productId).first()
                scale = oBackLog.BL_scaleType
                return scale
        return ([])

    def actorsAsociatedToProduct(self,productId):
        ''' Permite obtener una lista de los Actores asociados a una pila de Producto'''
        checkTypeId = type(productId) == int    
        if checkTypeId: 
            found = clsRole.query.filter_by(id_pila=productId).all()
            return found
        return([])              
                   
    def accionsAsociatedToProduct(self,accionId):
        ''' Permite obtener una lista de las acciones asociados a una pila de Producto'''
        checkTypeId = type(accionId) == int    
        if checkTypeId: 
            found = clsAccions.query.filter_by(id_backLog=accionId).all()
            return found
        return([])  

    def objectivesAsociatedToProduct(self,productId):
        ''' Permite obtener una lista de los Objetivos asociados a una pila de Producto'''
        checkTypeId = type(productId) == int    
        if checkTypeId: 
            found = clsObjective.query.filter_by(id_backlog=productId).all()
            return found
        return([])   
    
    def userHistoryAsociatedToProduct(self,productId):
        ''' Permite obtener una lista de los historias de usuario asociadas a una pila de Producto'''
        checkTypeId = type(productId) == int    
        if checkTypeId: 
            found = clsUserHistory.query.filter_by(id_backLog=productId).all()
            return found
        return([])                                