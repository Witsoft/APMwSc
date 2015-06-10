# -*- coding: utf-8 -*-. 

from app.scrum.userHistory import *

# Declaracion de constantes.
minId = 1
minTaskDescription = 1
maxTaskDescription = 140

class task(object):
    '''Clase que permite manejar los tasks de manera persistente'''

    def getAllTask(self,HW_refUserHistory):
        typeId  = (type(HW_refUserHistory) == int)
        if (typeId  and HW_refUserHistory  >= minId):
            otask = clsTask.query.filter_by(HW_refUserHistory = HW_refUserHistory).all()
            return otask
        return ([])
    
    def insertTask(self,HW_description, id_userHistory):
        '''Permite insertar un Task'''
                   
        typedescription = (type(HW_description) == str)
        typeid = (type(id_userHistory) == int)
        
        if (typedescription and typeid):
            long_HW_description = minTaskDescription <= len(HW_description) <= maxTaskDescription
            
            if long_HW_description:
                oUserHistory = clsUserHistory.query.filter_by(id_userHistory = id_userHistory).all()
                oTask = clsTask.query.filter_by(HW_description = HW_description).all()
                if (oUserHistory != []) and (oTask == []):
                    new_task = clsTask(HW_description = HW_description,HW_refUserHistory = id_userHistory)
                    db.session.add(new_task)
                    db.session.commit()
                    return True
        return False
    
    def deleteTask(self, HW_description):
        '''Permite eliminar un Task según su descripción'''
        
        typedescription = (type(HW_description) == str)
        
        if typedescription:
            len_description = minTaskDescription <= len(HW_description) <= maxTaskDescription
            if len_description:
                foundid = clsTask.query.filter_by(HW_description = HW_description).all()
                if foundid != []:
                    oTask = clsTask.query.filter_by(HW_description = HW_description).all()
                    for i in oTask:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False
    
    def searchTask(self, HW_description):
        '''Permite buscar Tasks por su descripcion'''
        oTask = clsTask.query.filter_by(HW_description = HW_description).all()
        return oTask
    
    def updateTask(self, HW_description,newDescription):
        '''Permite actualizar la descripcion de un Task'''
           
        typedescription = (type(HW_description) == str)
        typeNewdescription = (type(newDescription) == str)
        
        if (typedescription and typeNewdescription):
            long_HW_description = minTaskDescription <= len(HW_description) <= maxTaskDescription
            long_newDescription = minTaskDescription <= len(newDescription) <= maxTaskDescription
            
            if (long_HW_description and long_newDescription):
                foundTask = self.searchTask(HW_description)
                foundNew = self.searchTask(newDescription)
                if ((foundTask != []) and ((foundNew == [])or(HW_description == newDescription))):
                    oTask = clsTask.query.filter_by(HW_description = HW_description).first()
                    oTask.HW_description = newDescription
                    db.session.commit()
                    return True
        return False