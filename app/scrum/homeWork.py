# -*- coding: utf-8 -*-. 

from app.scrum.userHistory import *

# Declaracion de constantes.
minId = 1
minHomeWorkDescription = 1
maxHomeWorkDescription = 140

class homeWork(object):
    '''Clase que permite manejar los homeWorks de manera persistente'''

    def searchIdHomeWork(self, HW_idHomeWork ):
        '''Permite buscar HomeWorks por su id'''
        typeHW_idHomeWork  = (type(HW_idHomeWork ) == int)
        if (typeHW_idHomeWork  and HW_idHomeWork  >= minId):
            ohomeWork = clsHomeWork.query.filter_by(HW_idHomeWork = HW_idHomeWork ).all()
            return ohomeWork
        return ([])
    
    def insertHomeWork(self,HW_description, id_userHistory):
        '''Permite insertar un HomeWork'''
                   
        typedescription = (type(HW_description) == str)
        typeid = (type(id_userHistory) == int)
        
        if (typedescription and typeid):
            long_HW_description = minHomeWorkDescription <= len(HW_description) <= maxHomeWorkDescription
            
            if long_HW_description:
                oUserHistory = clsUserHistory.query.filter_by(id_userHistory = id_userHistory).all()
                oHomeWork = clsHomeWork.query.filter_by(HW_description = HW_description).all()
                if (oUserHistory != []) and (oHomeWork == []):
                    new_homeWork = clsHomeWork(HW_description = HW_description,id_userHistory = id_userHistory)
                    db.session.add(new_homeWork)
                    db.session.commit()
                    return True
        return False
    
    def deleteHomeWork(self, HW_description):
        '''Permite eliminar un HomeWork según su descripción'''
        
        typedescription = (type(HW_description) == str)
        
        if typedescription:
            len_description = minHomeWorkDescription <= len(HW_description) <= maxHomeWorkDescription
            if len_description:
                foundid = clsHomeWork.query.filter_by(HW_description = HW_description).all()
                if foundid != []:
                    oHomeWork = clsHomeWork.query.filter_by(HW_description = HW_description).all()
                    for i in oHomeWork:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False
    
    def searchHomeWork(self, HW_description):
        '''Permite buscar HomeWorks por su descripcion'''
        oHomeWork = clsHomeWork.query.filter_by(HW_description = HW_description).all()
        return oHomeWork
    
    def updateHomeWork(self, HW_description,newDescription):
        '''Permite actualizar la descripcion de un HomeWork'''
           
        typedescription = (type(HW_description) == str)
        typeNewdescription = (type(newDescription) == str)
        
        if (typedescription and typeNewdescription):
            long_HW_description = minHomeWorkDescription <= len(HW_description) <= maxHomeWorkDescription
            long_newDescription = minHomeWorkDescription <= len(newDescription) <= maxHomeWorkDescription
            
            if (long_HW_description and long_newDescription):
                foundHomeWork = self.searchHomeWork(HW_description)
                foundNew = self.searchHomeWork(newDescription)
                if ((foundHomeWork != []) and (foundNew == [])):
                    oHomeWork = clsHomeWork.query.filter_by(HW_description = HW_description).first()
                    oHomeWork.HW_description = newDescription
                    db.session.commit()
                    return True
        return False