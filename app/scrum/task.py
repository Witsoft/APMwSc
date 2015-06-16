# -*- coding: utf-8 -*-. 

from app.scrum.userHistory import *

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
    
    
    def insertTask(self,HW_description, UH_idUserHistory):
        '''Permite insertar un Task'''
         
        typedescription = (type(HW_description) == str)
        typeid          = (type(UH_idUserHistory) == int)
         
        oHistory = userHistory()
 
        if (typedescription and typeid):
            long_HW_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
            if long_HW_description:
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = UH_idUserHistory).all()
                oTask = clsTask.query.filter_by(HW_description = HW_description).all()
                if (oUserHistory != []) and (oTask == []):
                    new_task = clsTask(HW_description,UH_idUserHistory)
                    db.session.add(new_task)
                    db.session.commit()
                    return True
        return False

#     def insertTask(self, HW_description, C_idCategory, HW_weight, UH_idUserHistory):
#         '''Permite insertar un Task'''
#         
#         typedescription = (type(HW_description) == str)
#         typeidCategory  = (type(C_idCategory) == int)
#         typeWeight      = (type(HW_weight) == int)
#         typeid          = (type(UH_idUserHistory) == int)
# 
#         if (typedescription and typeidCategory and typeWeight and typeid):
#             long_HW_description  = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
#             min_C_idCategory     = C_idCategory >= MIN_ID
#             min_HW_weight        = HW_weight >= MIN_WEIGHT
#             min_UH_idUserHistory = UH_idUserHistory >= MIN_ID 
#             if (long_HW_description and min_C_idCategory and min_HW_weight and min_UH_idUserHistory):
#                 oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = UH_idUserHistory).all()
#                 oTask = clsTask.query.filter_by(HW_description = HW_description).all()
#                 if (oUserHistory != []) and (oTask == []):
#                     new_task = clsTask(HW_description,C_idCategory,HW_weight,UH_idUserHistory)
#                     db.session.add(new_task)
#                     db.session.commit()
#                     return True
#         return False
    
    
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
    
    
    def updateTask(self, HW_description,newDescription):
        '''Permite actualizar la descripcion de un Task'''
            
        typedescription = (type(HW_description) == str)
        typeNewdescription = (type(newDescription) == str)
         
        if (typedescription and typeNewdescription):
            long_HW_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
            long_newDescription = MIN_TASK_DESCRIPTION <= len(newDescription) <= MAX_TASK_DESCRIPTION
             
            if (long_HW_description and long_newDescription):
                foundTask = self.searchTask(HW_description)
                foundNew = self.searchTask(newDescription)
                if ((foundTask != []) and ((foundNew == [])or(HW_description == newDescription))):
                    oTask = clsTask.query.filter_by(HW_description = HW_description).first()
                    oTask.HW_description = newDescription
                    db.session.commit()
                    return True
        return False

#     def updateTask(self, HW_description, newDescription, C_idCategory, HW_weight):
#         '''Permite actualizar la descripcion de un Task'''
#          
#         typedescription    = (type(HW_description) == str)
#         typeNewdescription = (type(newDescription) == str)
#         typeidCategory     = (type(C_idCategory) == int)
#         typeWeight         = (type(HW_weight) == int)        
#         
#         if (typedescription and typeNewdescription and typeidCategory and typeWeight):
#             long_HW_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
#             long_newDescription = MIN_TASK_DESCRIPTION <= len(newDescription) <= MAX_TASK_DESCRIPTION
#             min_C_idCategory    = C_idCategory >= MIN_ID 
#             min_HW_weight       = HW_weight >= MIN_WEIGHT
#             
#             if (long_HW_description and long_newDescription and min_C_idCategory and min_HW_weight):
#                 foundTask = self.searchTask(HW_description)
#                 foundNew  = self.searchTask(newDescription)
#                 if ((foundTask != []) and ((foundNew == [])or(HW_description == newDescription))):
#                     oTask = clsTask.query.filter_by(HW_description = HW_description).first()
#                     oTask.HW_description = newDescription
#                     oTask.C_idCategory   = C_idCategory
#                     oTask.HW_weight      = HW_weight
#                     db.session.commit()
#                     return True
#         return False
    
#Fin clase Task
