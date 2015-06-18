# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from userHistory import *

# Declaracion de constantes.
MIN_ID               = 1
MIN_WEIGHT           = 1
MIN_TASK_DESCRIPTION = 1
MAX_TASK_DESCRIPTION = 140

class task(object):
    '''Clase que permite manejar los tasks de manera persistente'''

    def getAllTask(self,HW_idUserHistory):
        typeId  = (type(HW_idUserHistory) == int)
        if (typeId  and HW_idUserHistory  >= MIN_ID):
            otask = clsTask.query.filter_by(HW_idUserHistory = HW_idUserHistory).all()
            return otask
        return ([])
    

    def insertTask(self, HW_description, C_idCategory, HW_weight, UH_idUserHistory):
        '''Permite insertar un Task'''
         
        typedescription = (type(HW_description) == str)
        typeidCategory  = (type(C_idCategory) == int)
        typeWeight      = (type(HW_weight) == int)
        typeid          = (type(UH_idUserHistory) == int)
 
        if (typedescription and typeidCategory and typeWeight and typeid):
            long_HW_description  = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
            min_C_idCategory     = C_idCategory >= MIN_ID
            min_HW_weight        = HW_weight >= MIN_WEIGHT
            min_UH_idUserHistory = UH_idUserHistory >= MIN_ID 
            if (long_HW_description and min_C_idCategory and min_HW_weight and min_UH_idUserHistory):
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = UH_idUserHistory).all()
                oCategory    = clsCategory.query.filter_by(C_idCategory = C_idCategory).all()
                oTask = clsTask.query.filter_by(HW_description = HW_description).all()
                if (oUserHistory != []) and (oCategory != []) and (oTask == []):
                    new_task = clsTask(HW_description,C_idCategory,HW_weight,UH_idUserHistory)
                    db.session.add(new_task)
                    db.session.commit()
                    return True
        return False
    
    
    def deleteTask(self, HW_description):
        '''Permite eliminar un Task según su descripción'''
        
        typedescription = (type(HW_description) == str)
        
        if typedescription:
            len_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
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
        typedescription = (type(HW_description) == str)
        
        if typedescription:
            oTask = clsTask.query.filter_by(HW_description = HW_description).all()
        else:
            oTask = False
        return oTask
    

    def updateTask(self, HW_description, newDescription, C_idCategory, HW_weight):
        '''Permite actualizar la descripcion de un Task'''
          
        typedescription    = (type(HW_description) == str)
        typeNewdescription = (type(newDescription) == str)
        typeidCategory     = (type(C_idCategory) == int)
        typeWeight         = (type(HW_weight) == int)        
         
        if (typedescription and typeNewdescription and typeidCategory and typeWeight):
            long_HW_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
            long_newDescription = MIN_TASK_DESCRIPTION <= len(newDescription) <= MAX_TASK_DESCRIPTION
            min_C_idCategory    = C_idCategory >= MIN_ID 
            min_HW_weight       = HW_weight >= MIN_WEIGHT
             
            if (long_HW_description and long_newDescription and min_C_idCategory and min_HW_weight):
                foundTask = self.searchTask(HW_description)
                foundNew  = self.searchTask(newDescription)
                if ((foundTask != []) and ((foundNew == [])or(HW_description == newDescription))):
                    oTask = clsTask.query.filter_by(HW_description = HW_description).first()
                    oTask.HW_description = newDescription
                    oTask.HW_idCategory   = C_idCategory
                    oTask.HW_weight      = HW_weight
                    db.session.commit()
                    print("update: ",HW_description, newDescription, C_idCategory, HW_weight)
                    return True
        return False
    
    
    def taskAsociatedToUserHistory(self,idUserHistory):
        ''' Permite obtener una lista de las tareas asociadas a una historia de usuario'''
        checkTypeId = type(idUserHistory) == int    
        if checkTypeId: 
            found = clsTask.query.filter_by(HW_idUserHistory  = idUserHistory).all()
            return found
        return([])                                

    def historyWeight(self,idUserHistory):
        checkTypeId = type(idUserHistory) == int    
        if checkTypeId: 
            oTask = task()
            taskList = oTask.taskAsociatedToUserHistory(idUserHistory)
            if taskList != []:
                for i in taskList:
                    peso = 0 + i.HW_weight
                return peso
        return (0)
                
                
#Fin clase Task
