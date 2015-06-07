# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes.
CONST_MIN_ID_BACKLOG = 1
CONST_MIN_ID_OBJ     = 1
CONST_MIN_DESC_OBJ   = 1
CONST_MAX_DESC_OBJ   = 140

arrayType          = [True,False]


class objective(object):
    '''Clase que permite manejar los objetivos de manera persistente'''

    def insertObjective(self,descObjective, idBacklog, objType):
        '''Permite insertar un Objetivo'''

        checkObjType = objType in arrayType
        checkDesc    = type(descObjective) == str
        checkId_BL   = type(idBacklog) == int 
        checkIdMin   = idBacklog >= CONST_MIN_ID_BACKLOG 
        
        if checkDesc and checkId_BL and checkIdMin and checkObjType: 
            print("Entre")
            checkDescLen = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            
            if checkDescLen:
                aBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                aObj     = self.searchObjective(descObjective)

                if (aBacklog != []) and (aObj == []) :
                    new_objective = clsObjective(descObjective, idBacklog, objType)
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
        checkIdObjective = type(IdObjective) == int and IdObjective >= CONST_MIN_ID_OBJ 
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
            checkDescLen    = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            checkNewDescLen = CONST_MIN_DESC_OBJ <= len(newDescObjective) <= CONST_MAX_DESC_OBJ
        
            if checkDescLen and checkNewDescLen:
                aObj = self.searchObjective(descObjective)
                
                if aObj != []:
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

    def verifyObjectiveTransverse(self, idObjective):
        '''Permite verificar si un objetivo es de tipo trasnversal o no'''
        
        checkDesc = type(idObjective) == int
        if checkDesc:
            result = self.searchIdObjective(idObjective)
            return result[0].obj_type

    def deleteObjective(self, descObjective):
        '''Permite eliminar un objetivo de acuerdo a su descripcion'''
        
        checkDesc = type(descObjective) == str
        
        if checkDesc:
            checkDescLen = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            
            if checkDescLen:
                aObj = self.searchObjective(descObjective)
                
                if aObj != []:  
                    for i in aObj:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 

           

# Fin Clase Objective
