# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes.
CONST_MIN_ID_BACKLOG = 1
CONST_MIN_ID_OBJ     = 1
CONST_MIN_DESC_OBJ   = 1
CONST_MAX_DESC_OBJ   = 140

arrayType = [True,False]


class objective(object):
    '''Clase que permite manejar los objetivos de manera persistente'''

    def insertObjective(self,descObjective, idBacklog, objType):
        '''Permite insertar un Objetivo'''

        checkObjType = objType in arrayType
        checkDesc    = type(descObjective) == str
        checkId_BL   = type(idBacklog) == int 
        checkIdMin   = idBacklog >= CONST_MIN_ID_BACKLOG 
        
        if checkDesc and checkId_BL and checkIdMin and checkObjType: 
            checkDescLen = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            
            if checkDescLen:
                oBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                oObj     = clsObjective.query.filter_by(O_descObjective  = descObjective).all()

                if oBacklog != [] and oObj == [] :
                    new_objective = clsObjective(descObjective, idBacklog, objType)
                    db.session.add(new_objective)
                    db.session.commit()
                    return True
        return False
    
                
    def searchObjective(self, descObjective):
        '''Permite buscar objetivos por su descripcion'''
        oObj = clsObjective.query.filter_by(O_descObjective = descObjective).all()
        return oObj
    
    
    def searchIdObjective(self, idObjective):
        '''Permite buscar objetivos por su id'''
        checkIdObjective = type(idObjective) == int and idObjective >= CONST_MIN_ID_OBJ 
        
        if checkIdObjective:
            oObj = clsObjective.query.filter_by(O_idObjective = idObjective).all()
            return oObj
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
                oObj = clsObjective.query.filter_by(O_descObjective = descObjective).all()
                
                if oObj != []:
                    oObj[0].O_descObjective = newDescObjective
                    oObj[0].O_objType       = newObjType
                    db.session.commit()
                    return True
        return False   
 

    def verifyObjectiveTransverse(self, idObjective):
        '''Permite verificar si un objetivo es de tipo trasnversal o no'''
        checkDesc = type(idObjective) == int
        
        if checkDesc:
            oObj = clsObjective.query.filter_by(O_idObjective = idObjective).all()
            return oObj[0].O_objType
        

    def deleteObjective(self, descObjective):
        '''Permite eliminar un objetivo de acuerdo a su descripcion'''
        checkDesc = type(descObjective) == str
        
        if checkDesc:
            checkDescLen = CONST_MIN_DESC_OBJ <= len(descObjective) <= CONST_MAX_DESC_OBJ
            
            if checkDescLen:
                oObj = clsObjective.query.filter_by(O_descObjective = descObjective).all()
                
                if oObj != []:  
                    for i in oObj:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 

# Fin Clase Objective