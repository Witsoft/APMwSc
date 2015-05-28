# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *


# Declaracion de constantes.
minId = 1
minAccionDescription = 1
maxAccionDescription   = 140

class accions(object):
    '''Clase que permite manejar las acciones de manera persistente'''

    def insertAccion(self,acciondescription, id_backLog):
        '''Permite insertar una Accion'''
                   
        typedescription = (type(acciondescription) == str)
        typeid = (type(id_backLog) == int)
        
        if (typedescription and typeid):
            long_acciondescription = minAccionDescription <= len(acciondescription) <= maxAccionDescription
            
            if long_acciondescription:
                obackLog = clsBackLog.query.filter_by(id_backLog = id_backLog).all()
                oaccion = clsAccions.query.filter_by(acciondescription = acciondescription).all()
                if (obackLog != []) and (oaccion == []):
                    new_accion = clsAccions(acciondescription = acciondescription,id_backLog = id_backLog)
                    db.session.add(new_accion)
                    db.session.commit()
                    return True
        return False
                
                
    def searchAccion(self, acciondescription):
        '''Permite buscar acciones por su descripcion'''
        oAccion = clsAccions.query.filter_by(acciondescription = acciondescription).all()
        return oAccion
    
    def searchIdAccion(self, idaccion):
        '''Permite buscar acciones por su id'''
        oAccion = clsAccions.query.filter_by(idaccion  = idaccion).all()
        return oAccion
            
    def updateAccion(self, acciondescription,newDescription):
        '''Permite actualizar la descripcion de una accion'''
           
        typedescription = (type(acciondescription) == str)
        typeNewdescription = (type(newDescription) == str)
        
        if (typedescription and typeNewdescription):
            long_acciondescription = minAccionDescription <= len(acciondescription) <= maxAccionDescription
            long_newDescription = minAccionDescription <= len(newDescription) <= maxAccionDescription
            
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
            Len_description = minAccionDescription <= len(acciondescription) <= maxAccionDescription
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