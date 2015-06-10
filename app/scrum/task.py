# -*- coding: utf-8 -*-. 

from app.scrum.userHistory import *

# Declaracion de constantes.
minId = 1
minTaskDescription = 1
maxTaskDescription = 140

class task(object):
    '''Clase que permite manejar los tasks de manera persistente'''

    def searchIdTask(self, HW_idTask ):
        '''Permite buscar Tasks por su id'''
        typeHW_idTask  = (type(HW_idTask ) == int)
        if (typeHW_idTask  and HW_idTask  >= minId):
            otask = clsTask.query.filter_by(HW_idTask = HW_idTask ).all()
            return otask
        return ([])
   
    def getAllTask(self,idUserHistory):
        '''Permite obtener todas las tareas asociadas a una historia de usuario'''
        typeId    = type(idUserHistory) == int
        otask = []

        if typeId:  
            checkId = idUserHistory  >= minId
        
            if checkId:      
                otask = clsTask.query.filter_by(HW_idUserHistory = idUserHistory).all()     
        return otask
    
    
    def insertTask(self,HW_description, id_userHistory):
        '''Permite insertar un Task'''
                   
        typedescription = (type(HW_description) == str)
        typeid = (type(id_userHistory) == int)
        
        if (typedescription and typeid):
            long_HW_description = minTaskDescription <= len(HW_description) <= maxTaskDescription
            
            if long_HW_description:
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = id_userHistory).all()
                oTask = clsTask.query.filter_by(HW_description = HW_description).all()
                if (oUserHistory != []) and (oTask == []):
                    new_task = clsTask(HW_description,id_userHistory)
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
