# -*- coding: utf-8 -*-. 

from modelDummy   import *
from backLogDummy import *

# Declaracion de constantes.
CONST_MIN_ID_BACKLOG = 1
CONST_MIN_ID_OBJ     = 1
CONST_MIN_DESC_OBJ   = 1
CONST_MAX_DESC_OBJ   = 140

typeObj   = {0:False,1:True}
arrayType = [True,False]


class objective(object):
    '''Clase que permite manejar los objetivos de manera persistente'''

    def insertObjective(self,descObjective, idBacklog, objType):
        '''Permite insertar un Objetivo'''
        checkObjType = objType in arrayType
        checkDesc    = type(descObjective) == str
        checkId_BL   = type(idBacklog) == int 
        
        if checkDesc and checkId_BL and checkObjType: 
            checkDescLen = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            checkIdMin   = CONST_MIN_ID_BACKLOG <= idBacklog  
            
            if checkDescLen and checkIdMin:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()

                if foundBacklog != []:
                    foundObjectives    = clsObjective.query.filter_by(O_idBacklog = idBacklog).all()
                    foundObjectiveDesc = []
                    for desc in foundObjectives:
                        if desc.O_descObjective.lower() == descObjective.lower():
                            foundObjectiveDesc.append(desc)
                            break
                        
                    if foundObjectiveDesc == []:
                        newObjective = clsObjective(descObjective, idBacklog, objType)
                        db.session.add(newObjective)
                        db.session.commit()
                        return True
        return False
    
                
    def searchObjective(self, descObjective, idBacklog):
        '''Permite buscar objetivos por su descripcion'''
        checkTypeId   = type(idBacklog) == int
        checkTypeDesc = type(descObjective) == str       
        
        foundObjective = []
        if checkTypeId and checkTypeDesc:
            checkLenDesc = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            checkId      = CONST_MIN_ID_OBJ <= idBacklog  
            
            if checkLenDesc and checkId:
                foundObjective = clsObjective.query.filter_by(O_descObjective = descObjective,O_idBacklog = idBacklog).all()
        return foundObjective 
    
    
    def searchIdObjective(self, idObjective):
        '''Permite buscar objetivos por su id'''
        checkIdObjective = type(idObjective) == int and idObjective >= CONST_MIN_ID_OBJ 
        
        foundObjective = []
        if checkIdObjective:
            checkId = idObjective >= CONST_MIN_ID_OBJ
            if checkId:
                foundObjective = clsObjective.query.filter_by(O_idObjective = idObjective).all()
            
        return foundObjective 
    
            
    def updateObjective(self, descObjective, newDescObjective,newObjType,idBacklog):
        '''Permite actualizar la descripcion de un objetivo'''
        checkObjType       = newObjType in arrayType   
        checkDesc          = type(descObjective) == str 
        checkNewDesc       = type(newDescObjective) == str
        checkTypeIdBacklog = type(idBacklog) == int
        
        if checkDesc and checkNewDesc and checkObjType and checkTypeIdBacklog: 
            checkDescLen    = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            checkNewDescLen = CONST_MIN_DESC_OBJ <= len(newDescObjective) <= CONST_MAX_DESC_OBJ
            checkIdBacklog  = CONST_MIN_ID_OBJ <= idBacklog
        
            if checkDescLen and checkNewDescLen and checkIdBacklog:
                foundObjective = clsObjective.query.filter_by(O_descObjective = descObjective,O_idBacklog = idBacklog).all()
                foundNewObj    = clsObjective.query.filter_by(O_descObjective = newDescObjective,O_idBacklog = idBacklog).all()
                
                if foundObjective != [] and (foundNewObj == [] or descObjective == newDescObjective):
                    foundObjective[0].O_descObjective = newDescObjective
                    typeObjective                     = int(foundObjective[0].O_objType)
                    
                    if typeObj[typeObjective] == arrayType[0]:
                        foundObjective[0].O_objType = newObjType
                        
                    elif typeObj[typeObjective] == arrayType[1]:
                        idObj       = foundObjective[0].O_idObjective
                        idHistories = clsUserHistory.query.filter_by(UH_idBacklog = idBacklog).all()
                        
                        if idHistories != []:
                            for hist in idHistories:
                                idsObjectives = clsObjectivesUserHistory.query.filter_by(OUH_idUserHistory = hist.UH_idUserHistory).all()

                                idsList = []
                                for obj in idsObjectives:
                                    idsList.append(obj.OUH_idObjective)

                                if idObj in idsList:
                                    checkLenIdsObjectives = len(idsObjectives)
                                     
                                    if checkLenIdsObjectives == 1:
                                        found = clsUserHistory.query.filter_by(UH_codeUserHistory = hist.UH_codeUserHistory).all()
                                        foundObjective[0].O_objType = newObjType
                                        if found != []:
                                            for i in found:    
                                                db.session.delete(i)          
                                            db.session.commit() 
                                    else:  
                                        oObjective = clsObjectivesUserHistory.query.filter_by(OUH_idObjectivesUserHist = idObj,OUH_idUserHistory = hist.UH_idUserHistory).all()
                                        foundObjective[0].O_objType = newObjType
                                        if oObjective != []:
                                            for i in oObjective:
                                                db.session.delete(i)
                                            db.session.commit()
                        else:
                            foundObjective[0].O_objType = newObjType
                    db.session.commit()
                    return True
        return False   
 

    def verifyObjectiveTransverse(self, idObjective):
        '''Permite verificar si un objetivo es de tipo trasnversal o no'''
        checkDesc = type(idObjective) == int
        
        if checkDesc:
            oObj = clsObjective.query.filter_by(O_idObjective = idObjective).all()
            return oObj[0].O_objType
        

    def deleteObjective(self, descObjective, idBacklog):
        '''Permite eliminar un objetivo de acuerdo a su descripcion'''
        checkTypeDescription = type(descObjective) == str
        checkTypeIdBacklog   = type(idBacklog) == int   
        
        if checkTypeDescription and checkTypeIdBacklog:
            checkLenDescription = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            checkLongIdBacklog  = CONST_MIN_ID_OBJ <= idBacklog 
            
            if checkLenDescription and checkLongIdBacklog :
                found = clsObjective.query.filter_by(O_descObjective = descObjective,O_idBacklog = idBacklog).all()
                
                if found != []:
                    for i in found:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 

# Fin Clase Objective