# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *


# Declaracion de constantes.
MIN_ID = 1
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
                oBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                oAccion  = clsAccions.query.filter_by(acciondescription = accionDescription).all()
                if oBacklog != [] and oAccion == []:
                    newAccion = clsAccions(accionDescription,idBacklog)
                    db.session.add(newAccion)
                    db.session.commit()
                    return True
        return False
                
                
    def searchAccion(self, acciondescription):
        '''Permite buscar acciones por su descripcion'''
        oAccion = clsAccions.query.filter_by(acciondescription = acciondescription).all()
        return oAccion
    
    def searchIdAccion(self, idaccion):
        '''Permite buscar acciones por su id'''
        typeIdAccion = (type(idaccion) == int)
        if (typeIdAccion and idaccion >= MIN_ID):
            oAccion = clsAccions.query.filter_by(idaccion  = idaccion).all()
            return oAccion
        return ([])

            
    def updateAccion(self, acciondescription,newDescription):
        '''Permite actualizar la descripcion de una accion'''
           
        typedescription = (type(acciondescription) == str)
        typeNewdescription = (type(newDescription) == str)
        
        if (typedescription and typeNewdescription):
            long_acciondescription = MIN_ACCION_DESCRIPTION <= len(acciondescription) <= MAX_ACCION_DESCRIPTION
            long_newDescription = MIN_ACCION_DESCRIPTION <= len(newDescription) <= MAX_ACCION_DESCRIPTION
            
            if (long_acciondescription and long_newDescription):
                foundAccion = self.searchAccion(acciondescription)
                foundNew = self.searchAccion(newDescription)
                if ((foundAccion != []) and (foundNew == [])):
                    oAccion = clsAccions.query.filter_by(acciondescription = acciondescription).first()
                    oAccion.acciondescription = newDescription
                    db.session.commit()
                    return True
        return False
    
    def updateAccionReferenceToHistory(self, idAccion, ref_idUserHistory):
        '''Permite actualizar la referencia a la historia de usuario a la cual pertenece la accion'''
        result = clsUserHistory.query.filter_by(id_userHistory = ref_idUserHistory).all()
        
        if (result != []):
            oAccion = clsAccions.query.filter_by(idaccion = idAccion).first()
            oAccion.id_userHistory = ref_idUserHistory
            db.session.commit()
            return True
        return False
       
    def deleteAccion(self, acciondescription):
        '''Permite eliminar una accion segun su id'''
        
        typedescription = (type(acciondescription) == str)
        
        
        if typedescription:
            Len_description = MIN_ACCION_DESCRIPTION <= len(acciondescription) <= MAX_ACCION_DESCRIPTION
            if Len_description:
                foundid = clsAccions.query.filter_by(acciondescription = acciondescription).all()
                if foundid != []:
                    oAccion = clsAccions.query.filter_by(acciondescription = acciondescription).all()
                    for i in oAccion:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 

           
# Fin Clase Accion