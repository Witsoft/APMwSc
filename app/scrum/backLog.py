# -*- coding: utf-8 -*-. 

from app.scrum.model import *
from distutils.command.check import check

# Declaracion de constantes.
CONST_MAX_DESCRIPTION = 140
CONST_MIN_DESCRIPTION = 1
CONST_MAX_NAME        = 50
CONST_MIN_NAME        = 1

scale_type = [1,2]

class backlog(object):
    '''Clase que permite (completar)'''
    
    def getAllProducts(self):
        '''Permite obtener todos los productos de la tabla'''
        result = clsBacklog.query.all()
        return result
    
    def findName(self,name):
        '''Permite buscar un nombre'''
        checkTypeName = type(name) == str
        
        if checkTypeName:
            checkLongName = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME
            if checkLongName:
                oBacklog = clsBacklog.query.filter_by(BL_name = name).all()
                return oBacklog
        return []
    
    def findIdProduct(self,idBacklog):
        '''Permite buscar un elemento por su id'''
        checkTypeId = type(idBacklog) == int
        found = None
        if checkTypeId:
            found = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).first()
        return found
    
    def insertBacklog(self,name,description,scale):
        '''Permite insertar un producto'''
        checkTypeName  = type(name) == str
        checkTypeDesc  = type(description) == str
        checkTypeScale = type(scale) == int
        
        if checkTypeName and checkTypeDesc and checkTypeScale:
            checkLongName        = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME
            checkLongDescription = CONST_MIN_DESCRIPTION <= len(description) <= CONST_MAX_DESCRIPTION
            checkScale = scale in scale_type
            
            if  checkLongName and checkLongDescription and checkScale:
                found = self.findName(name);
                
                if found == []:
                    newProd = clsBacklog(name,description,scale)
                    db.session.add(newProd)
                    db.session.commit()
                    return True
        return False


    def modifyBacklog(self, name, new_name, new_description, new_scale):   
        '''Permite actualizar los valores de un producto'''            
        checkTypeName          = type(name) == str
        checkTypeNewName       = type(new_name) == str
        checkTypeDescription   = type(new_description) == str
        checkTypeScale         = type(new_scale) == int 

        if checkTypeName  and checkTypeNewName  and checkTypeDescription and checkTypeScale:
            checkLongName    = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME
            checkLongNewName = CONST_MIN_NAME <= len(new_name) <= CONST_MAX_NAME
            checkLongNewDesc = CONST_MIN_DESCRIPTION <= len(new_description) <= CONST_MAX_DESCRIPTION
            checkNewScale    = new_scale in scale_type
            
            if checkLongName and checkLongNewName and checkLongNewDesc and checkNewScale:
                foundName    = self.findName(name)
                foundNewName = self.findName(new_name)
                
                if foundName != [] and (foundNewName == [] or new_name == name):
                    idBacklog        = foundName[0].BL_idBacklog
                    foundUserHistory = clsUserHistory.query.filter_by(UH_idBacklog  = idBacklog).all()
                    currentScale     = foundName[0].BL_scaleType
                    
                    if currentScale != new_scale and foundUserHistory != []:
                        return False
                    
                    newBacklog                = clsBacklog.query.filter_by(BL_name = name).first()
                    newBacklog.BL_name        = new_name 
                    newBacklog.BL_description = new_description                   
                    newBacklog.BL_scaleType   = new_scale 
                    db.session.commit()
                    return True

        return False
    

    def deleteProduct(self, name):
        '''Permite eliminar un producto de la tabla'''
        checkTypeName = type(name) == str
        checkLongName = CONST_MIN_NAME > len(name) > CONST_MAX_NAME
        
        if (not checkTypeName) and checkLongName:
            return False
        else:
            foundName = self.findName(name)
            if foundName == []:
                return False
            else:
                tupla = clsBacklog.query.filter_by(BL_name = name).first()    
                db.session.delete(tupla)
                db.session.commit()
                return True
            

    def scaleType(self,idBacklog):
        '''Permite obtener el tipo de escala seleccionado para un producto'''
        checkTypeId = type(idBacklog) == int
            
        if checkTypeId: 
            found = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
            if found != []:
                scale = found[0].BL_scaleType
                return scale
        return ([])
    

    def actorsAsociatedToProduct(self,idBacklog):
        ''' Permite obtener una lista de los Actores asociados a una pila de Producto'''
        checkTypeId = type(idBacklog) == int    
        if checkTypeId: 
            found = clsActor.query.filter_by(A_idBacklog = idBacklog).all()
            return found
        return([])              
                   

    def accionsAsociatedToProduct(self,idBacklog):
        ''' Permite obtener una lista de las acciones asociados a una pila de Producto'''
        checkTypeId = type(idBacklog) == int    
        if checkTypeId: 
            found = clsAccion.query.filter_by(AC_idBacklog  = idBacklog).all()
            return found
        return([]) 
     

    def objectivesAsociatedToProduct(self,idBacklog):
        ''' Permite obtener una lista de los Objetivos asociados a una pila de Producto'''
        checkTypeId = type(idBacklog) == int    
        if checkTypeId: 
            found = clsObjective.query.filter_by(O_idBacklog = idBacklog).all()
            return found
        return([]) 
      
    
    def userHistoryAsociatedToProduct(self,idBacklog):
        ''' Permite obtener una lista de los historias de usuario asociadas a una pila de Producto'''
        checkTypeId = type(idBacklog) == int    
        if checkTypeId: 
            found = clsUserHistory.query.filter_by(UH_idBacklog  = idBacklog).all()
            return found
        return([])                                

# Fin Clase Backlog