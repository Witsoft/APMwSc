# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes.
MIN_ID                 = 1
MIN_ACCION_DESCRIPTION = 1
MAX_ACCION_DESCRIPTION = 140

class accions(object):
    '''Clase que permite manejar las acciones de manera persistente'''

    def insertAccion(self,accionDescription,idBacklog):
        '''Permite insertar una Accion'''   
        
        checkTypeDescription = type(accionDescription) == str
        checkTypeId          = type(idBacklog) == int
        
        if checkTypeDescription and checkTypeId:
            checkLongAccionDescription = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            
            if checkLongAccionDescription:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                foundAccion  = clsAccion.query.filter_by(AC_accionDescription = accionDescription).all()
                
                if foundBacklog != [] and foundAccion == []:
                    newAccion = clsAccion(accionDescription,idBacklog)
                    db.session.add(newAccion)
                    db.session.commit()
                    return True
        return False
                
                
    def searchAccion(self, accionDescription):
        '''Permite buscar acciones por su descripcion'''
        foundAccion = clsAccion.query.filter_by(AC_accionDescription = accionDescription).all()
        return foundAccion
    
    
    def searchIdAccion(self, idAccion):
        '''Permite buscar acciones por su id'''
        checkTypeIdAccion = type(idAccion) == int
        
        if checkTypeIdAccion and idAccion >= MIN_ID:
            foundAccion = clsAccion.query.filter_by(AC_idAccion  = idAccion).all()
            return foundAccion
        return ([])

            
    def updateAccion(self, accionDescription,newDescription):
        '''Permite actualizar la descripcion de una accion'''   
        checkTypeDescription    = type(accionDescription) == str
        checkTypeNewdescription = type(newDescription) == str
        
        if checkTypeDescription and checkTypeNewdescription:
            checkLongAccionDescription = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            checkLongNewDescription    = MIN_ACCION_DESCRIPTION <= len(newDescription) <= MAX_ACCION_DESCRIPTION
            
            if checkLongAccionDescription and checkLongNewDescription:
                foundAccion = clsAccion.query.filter_by(AC_accionDescription = accionDescription).all()
                foundNew    = clsAccion.query.filter_by(AC_accionDescription = newDescription).all()
                
                if foundAccion != [] and (foundNew == [] or accionDescription == newDescription):
                    foundAccion[0].AC_accionDescription = newDescription
                    db.session.commit()
                    return True
        return False
    
       
    def deleteAccion(self, accionDescription):
        '''Permite eliminar una accion segun su id'''
        checkTypeDescription = type(accionDescription) == str        
        
        if checkTypeDescription:
            checkLenDescription = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            
            if checkLenDescription:
                found = clsAccion.query.filter_by(AC_accionDescription = accionDescription).all()
               
                if found != []:
                    for i in found:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 
      
# Fin Clase Accion