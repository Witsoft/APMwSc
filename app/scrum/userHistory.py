# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes
CONST_MAX_COD    = 11
CONST_MIN_COD    = 1
CONST_MIN_ID     = 1
CONST_MIN_IDHIST = 0
CONST_MIN_SCALE  = 1
CONST_MAX_SCALE  = 20

arrayType = [1,2]

class userHistory(object):
    '''Clase que permite manejar las historias de manera persistente'''
    
    def getAllUserHistoryId(self, idBacklog):
        checkIdBacklog = (type(idBacklog) == int)
        if checkIdBacklog:
            checkLengIdBacklog = (idBacklog >= CONST_MIN_ID)
            if checkLengIdBacklog:
                existIdBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).first()
                if existIdBacklog != []:
                    found = clsUserHistory.query.filter_by(idBacklog = idBacklog).all()
                    return found
        return ([])
        
        
    def isEpic(self, id_userHistory):
        '''Clase que permite reconocer las épicas'''
        checkId = (type(id_userHistory) == int) and (CONST_MIN_ID <= id_userHistory)
        if checkId:
            existId = clsUserHistory.query.filter_by(id_History = id_userHistory).all()
            if existId != []:
                return True
        return False
    
    
    def succesors(self,id,succ = [],visit = []):
        '''Permite encontrar los sucesores de una historia de usuario'''
        if (id != 0):
            result = clsUserHistory.query.filter_by(id_History = id).all()
            idHistories = []
            for elem in result:
                idHistories.append(elem.id_userHistory)
    
            for id in idHistories:
                if not(id in visit):
                    succ.append(id)
                    visit.append(id)
                    succ = self.succesors(id,succ,visit)
                    
        return succ
                            
    
    def historySuccesors(self, id_userHistory):
        '''Permite saber las subhistorias que componen a una historia mas general'''
        succ = []
        checkIdHistory = (type(id_userHistory) == int) and (CONST_MIN_ID <= id_userHistory)
        if checkIdHistory:
            existId = clsUserHistory.query.filter_by(id_userHistory = id_userHistory).all()
            if existId != []:
                visited = []
                self.succesors(id_userHistory,succ,visited)
        return succ
                
                
    def insertUserHistory(self,cod_userHistory,id_History,type_accion,id_Accion,idBacklog, priority):
        '''Permite insertar una Historia de usuario'''
        checkCodUserHistory    = type(cod_userHistory) == str
        checkPriority =  (type(priority) == int) and (CONST_MIN_SCALE <= priority <= CONST_MAX_SCALE)
        
        if checkCodUserHistory and checkPriority:
            checkLenCodUserHistory = CONST_MIN_COD <= len(cod_userHistory) <= CONST_MAX_COD
            checkIdHistory         = type(id_History) == int and id_History >= CONST_MIN_IDHIST
            
            if checkCodUserHistory and checkLenCodUserHistory and checkIdHistory:
                oUserHistory = clsUserHistory.query.filter_by(id_userHistory = id_History).all()
                
                if oUserHistory !=[] or id_History == 0:
                    checkTypeAccion = type_accion in arrayType
                    checkIdAccion   = type(id_Accion) == int and id_Accion >= CONST_MIN_ID
                    checkIdBacklog  = type(idBacklog) == int and idBacklog >= CONST_MIN_ID
                    
                    if checkTypeAccion and checkIdAccion and checkIdBacklog:
                        oHistorys = clsAccions.query.filter_by(idaccion = id_Accion).all()
                        oBacklog  = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                
                        if oBacklog != [] and oHistorys != []:                         
                            
                            new_history = clsUserHistory(cod_userHistory,id_History,type_accion,id_Accion,idBacklog,priority)
                            db.session.add(new_history)
                            db.session.commit()
                            return True
        return False
    
        
    def searchUserHistory(self,cod_userHistory):
        typecod = (type(cod_userHistory) == str)
        if typecod:
            leng_cod_userHistory = (len(cod_userHistory) <= CONST_MAX_COD)
            if leng_cod_userHistory:
                found = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                return found
        return ([])
    
    def updateUserHistory(self,iduserHist,new_cod_userHistory,new_id_History,new_type_accion,new_id_Accion,new_Scale):
        '''Permite modificar una Historia de usuario'''
        checkCodUserHistory    = type(new_cod_userHistory) == str
        checkScale             = type(new_Scale) == int
        checkLenCodUserHistory = CONST_MIN_COD <= len(new_cod_userHistory) <= CONST_MAX_COD
        checkIdHistory         = type(new_id_History) == int and new_id_History >= CONST_MIN_IDHIST
        
        if checkCodUserHistory and checkLenCodUserHistory and checkIdHistory and checkScale:
            oUserHistory = clsUserHistory.query.filter_by(id_userHistory = new_id_History).all()
            
            if oUserHistory !=[] or new_id_History == 0:
                checkTypeAccion = new_type_accion in arrayType
                checkIdAccion   = type(new_id_Accion) == int and new_id_Accion >= CONST_MIN_ID
                
                if checkTypeAccion and checkIdAccion:
                    oAccions = clsAccions.query.filter_by(idaccion = new_id_Accion).all()
                    
                    if oAccions != []:
                        result = clsUserHistory.query.filter_by(id_userHistory = iduserHist).all()
                        checkSuperHistory = clsUserHistory.query.filter_by(id_History = iduserHist).all()
                        if result != []:
                            result[0].cod_userHistory = new_cod_userHistory
                            result[0].type_accion     = new_type_accion
                            result[0].id_Accion       = new_id_Accion
                            result[0].UH_scale        = new_Scale
                            if (checkSuperHistory == []):
                                result[0].id_History      = new_id_History
                            db.session.commit()
                        return True
        return False
    
    def updatePriority(self,idHistory,priority):
        checkIdHistory  = (type(idHistory) == int) and (CONST_MIN_ID <= idHistory)
        checkPriority   = (type(priority) == int) and (CONST_MIN_SCALE <= priority)
        if checkIdHistory and checkPriority:
            found = clsUserHistory.query.filter_by(id_userHistory = idHistory).first()
            if found != None:
                found.UH_scale = priority
                db.session.commit()
                return True
        return False
    
    def scaleType(self,historyId):
        checkTypeId = type(historyId) == int    
        if checkTypeId: 
            found = clsUserHistory.query.filter_by(id_userHistory = historyId).first()
            if found != None:
                productId = found.idBacklog
                oBacklog = clsBacklog.query.filter_by(BL_idBacklog = productId).first()
                scale = oBacklog.BL_scaleType
                return scale
        return (None)


    def accionsAsociatedToUserHistory(self,userHistoryId):
        ''' Permite obtener una lista de los Acciones asociados a una historia de usuario'''
        checkTypeId = type(userHistoryId) == int and userHistoryId >= CONST_MIN_ID
        if checkTypeId: 
            found = clsUserHistory.query.filter_by(id_userHistory = userHistoryId).all()
            return found
        return([])
    
    def deleteUserHistory(self, cod_userHistory):
        '''Permite eliminar una historia segun su codigo'''
        
        type_codeHistory = (type(cod_userHistory) == str)
        
        if type_codeHistory:
            Len_codHistory = CONST_MIN_COD <= len(cod_userHistory) <= CONST_MAX_COD
            if Len_codHistory:
                foundid = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                if foundid != []:
                    oHistory = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                    for i in oHistory:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 


# Fin Clase userHistory
