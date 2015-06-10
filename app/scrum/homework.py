# -*- coding: utf-8 -*-. 

from app.scrum.userHistory import *

# Declaracion de constantes.
minId = 1
minHomeworkDescription = 1
maxHomeworkDescription = 140

class homework(object):
    '''Clase que permite manejar los homeworks de manera persistente'''

    def searchIdHomework(self, HW_idHomework ):
        '''Permite buscar Homeworks por su id'''
        typeHW_idHomework  = (type(HW_idHomework ) == int)
        if (typeHW_idHomework  and HW_idHomework  >= minId):
            ohomework = clsHomework.query.filter_by(HW_idHomework = HW_idHomework ).all()
            return ohomework
        return ([])
   
    def getAllHomework(self,idUserHistory):
        '''Permite obtener todas las tareas asociadas a una historia de usuario'''
        typeId    = type(idUserHistory) == int
        ohomework = []

        if typeId:  
            checkId = idUserHistory  >= minId
        
            if checkId:      
                ohomework = clsHomework.query.filter_by(HW_idUserHistory = idUserHistory).all()     
        return ohomework
    
    
    def insertHomework(self,HW_description, id_userHistory):
        '''Permite insertar un Homework'''
                   
        typedescription = (type(HW_description) == str)
        typeid = (type(id_userHistory) == int)
        
        if (typedescription and typeid):
            long_HW_description = minHomeworkDescription <= len(HW_description) <= maxHomeworkDescription
            
            if long_HW_description:
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = id_userHistory).all()
                oHomework = clsHomework.query.filter_by(HW_description = HW_description).all()
                if (oUserHistory != []) and (oHomework == []):
                    new_homework = clsHomework(HW_description,id_userHistory)
                    db.session.add(new_homework)
                    db.session.commit()
                    return True
        return False
    
    def deleteHomework(self, HW_description):
        '''Permite eliminar un Homework según su descripción'''
        
        typedescription = (type(HW_description) == str)
        
        if typedescription:
            len_description = minHomeworkDescription <= len(HW_description) <= maxHomeworkDescription
            if len_description:
                foundid = clsHomework.query.filter_by(HW_description = HW_description).all()
                if foundid != []:
                    oHomework = clsHomework.query.filter_by(HW_description = HW_description).all()
                    for i in oHomework:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False
    
    def searchHomework(self, HW_description):
        '''Permite buscar Homeworks por su descripcion'''
        oHomework = clsHomework.query.filter_by(HW_description = HW_description).all()
        return oHomework
    
    def updateHomework(self, HW_description,newDescription):
        '''Permite actualizar la descripcion de un Homework'''
           
        typedescription = (type(HW_description) == str)
        typeNewdescription = (type(newDescription) == str)
        
        if (typedescription and typeNewdescription):
            long_HW_description = minHomeworkDescription <= len(HW_description) <= maxHomeworkDescription
            long_newDescription = minHomeworkDescription <= len(newDescription) <= maxHomeworkDescription
            
            if (long_HW_description and long_newDescription):
                foundHomework = self.searchHomework(HW_description)
                foundNew = self.searchHomework(newDescription)
                if ((foundHomework != []) and ((foundNew == [])or(HW_description == newDescription))):
                    oHomework = clsHomework.query.filter_by(HW_description = HW_description).first()
                    oHomework.HW_description = newDescription
                    db.session.commit()
                    return True
        return False