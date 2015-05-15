# -*- coding: utf-8 -*-. 

from app.scrum.model import *

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
                #backLog = clsbackLog.query.filter_by(id_backLog = id_backLog).all()
                oaccion = clsAccions.query.filter_by(acciondescription = acciondescription).all()
                if (oaccion == []): #and (backLog != [])):
                    new_accion = clsAccions(acciondescription = acciondescription,id_backLog = id_backLog)
                    db.session.add(new_role)
                    db.session.commit()
                    return True
        return False
                
                
    def searchAccion(self, acciondescription):
        '''Permite buscar acciones por su descripcion'''
        oAccion = clsAccions.query.filter_by(acciondescription = acciondescription).all()
        return oAccion
            
    def updateAccion(self, acciondescription,newDescription):
        '''Permite actualizar la descripcion de una accion'''
           
        typedescription = (type(acciondescription) == str)
        typeNewdescription = (type(newDescription) == str)
        if (typedescription and typeid):
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
    
       
    def deleteAccion(self, idaccion):
        '''Permite eliminar una accion segun su id'''
        
        typeid = (type(idaccion) == int)
        if typeid and idaccion >= minId:
            foundid = clsAccions.query.filter_by(idaccion = idaccion).all()
            if foundid != []:
                oAccion = clsAccions.query.filter_by(idaccion = idaccion).first()
                for i in oAccion:    
                    db.session.delete(i)          
                db.session.commit()
                return True
        return False 

           
# Fin Clase Accion