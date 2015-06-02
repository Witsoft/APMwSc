# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes.
const_minIdBacklog = 1
const_minIdObj     = 1
const_minDescObj   = 1
const_maxDescObj   = 140
arrayType          = [True,False]


class objective(object):
    '''Clase que permite manejar los objetivos de manera persistente'''

    def insertObjective(self,descObjective, id_backLog, objType):
        '''Permite insertar un Objetivo'''

        checkObjType = objType in arrayType
        checkDesc    = type(descObjective) == str
        checkId_BL   = type(id_backLog) == int 
        checkIdMin   = id_backLog >= const_minIdBacklog 
        
        if checkDesc and checkId_BL and checkIdMin and checkObjType: 
            checkDescLen = const_minDescObj <= len(descObjective) <= const_maxDescObj
            
            if checkDescLen:
                aBackLog = clsBackLog.query.filter_by(id_backLog = id_backLog).all()
                aObj     = self.searchObjective(descObjective)

                if (aBackLog != []) and (aObj == []) :
                    new_objective = clsObjective(descObjective, id_backLog)
                    db.session.add(new_objective)
                    db.session.commit()
                    return True
        return False
                
    def searchObjective(self, descObjective):
        '''Permite buscar objetivos por su descripcion'''
        aObj = clsObjective.query.filter_by(descObjective = descObjective).all()
        return aObj
    
    def searchIdObjective(self, IdObjective):
        '''Permite buscar objetivos por su id'''
        checkIdObjective = type(IdObjective) == int and IdObjective >= const_minIdObj 
        if (checkIdObjective):
            aObj = clsObjective.query.filter_by(idobjective = IdObjective).all()
            return aObj
        return ([])
            
    def updateObjective(self, descObjective, newDescObjective,newObjType):
        '''Permite actualizar la descripcion de un objetivo'''
        
        checkObjType = newObjType in arrayType   
        checkDesc    = type(descObjective) == str 
        checkNewDesc = type(newDescObjective) == str
        
        if checkDesc and checkNewDesc and checkObjType: 
            checkDescLen    = const_minDescObj <= len(descObjective) <= const_maxDescObj
            checkNewDescLen = const_minDescObj <= len(newDescObjective) <= const_maxDescObj
        
            if checkDescLen and checkNewDescLen:
                aObj = self.searchObjective(descObjective)
                
                if aObj != []:
                    result = self.searchObjective(newDescObjective)
                
                    if result == []:                
                        aObj[0].descObjective = newDescObjective
                        aObj[0].obj_type = newObjType
                        db.session.commit()
                        return True
        return False   
    
#     def updateObjectiveReferenceToHistory(self, idObjective, ref_idUserHistory):
#         '''Permite actualizar la referencia a la historia de usuario a la cual pertenece el objetivo'''
#         result = clsUserHistory.query.filter_by(id_userHistory = ref_idUserHistory).all()
#         
#         if (result != []):
#             oObjective = clsObjective.query.filter_by(idobjective = idObjective).first()
#             oObjective.id_userHistory = ref_idUserHistory
#             db.session.commit()
#             return True
#         return False   

    def verifyObjectiveTransverse(self, idObjetive):
        '''Permite verificar si un objetivo es de tipo trasnversal o no'''
        
        checkDesc = type(idObjective) == int
        if checkDesc:
            result = self.searchIdObjective(idObjective)
            return result[0].obj_type

    def deleteObjective(self, descObjective):
        '''Permite eliminar un objetivo de acuerdo a su descripcion'''
        
        checkDesc = type(descObjective) == str
        
        if checkDesc:
            checkDescLen = const_minDescObj <= len(descObjective) <= const_maxDescObj
            
            if checkDescLen:
                aObj = self.searchObjective(descObjective)
                
                if aObj != []:  
                    for i in aObj:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 

           

# Fin Clase Objective
