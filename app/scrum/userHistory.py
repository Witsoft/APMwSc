# -*- coding: utf-8 -*-. 

import sys

# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes
CONST_MAX_COD    = 11
CONST_MIN_COD    = 1
CONST_MIN_ID     = 1
CONST_MIN_IDHIST = 0
CONST_MIN_SCALE  = 1
CONST_MAX_SCALE  = 20

arrayType = [1,2]
options   = {1:'podria ',2:'puede '}

class userHistory(object):
    '''Clase que permite manejar las historias de manera persistente'''
    
    def getAllUserHistoryId(self, idBacklog):
        '''Permite obtener todas las historias de usuario asocidas a un producto'''
        checkIdBacklog = type(idBacklog) == int
        
        if checkIdBacklog:
            checkLengIdBacklog = idBacklog >= CONST_MIN_ID
            
            if checkLengIdBacklog:
                existIdBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).first()
                
                if existIdBacklog != []:
                    found = clsUserHistory.query.filter_by(UH_idBacklog = idBacklog).all()
                    return found
        return ([])
        
        
    def isEpic(self, idUserHistory):
        '''Clase que permite reconocer las épicas'''
        checkId = type(idUserHistory) == int and CONST_MIN_ID <= idUserHistory
        
        if checkId:
            existId = clsUserHistory.query.filter_by(UH_idSuperHistory = idUserHistory).all()
            
            if existId != []:
                return True
        return False
    
    
    def succesors(self,id,succ = [],visit = []):
        '''Permite encontrar los sucesores de una historia de usuario'''
        if (id != 0):
            result = clsUserHistory.query.filter_by(UH_idSuperHistory = id).all()
            idHistories = []
            for elem in result:
                idHistories.append(elem.UH_idUserHistory)
    
            for id in idHistories:
                if not(id in visit):
                    succ.append(id)
                    visit.append(id)
                    succ = self.succesors(id,succ,visit)        
        return succ
                            
    
    def historySuccesors(self, idUserHistory):
        '''Permite saber las subhistorias que componen a una historia mas general'''
        succ = []
        checkIdHistory = type(idUserHistory) == int and CONST_MIN_ID <= idUserHistory
        
        if checkIdHistory:
            existId = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
            if existId != []:
                visited = []
                self.succesors(idUserHistory,succ,visited)
        return succ
                
                
    def insertUserHistory(self,codeUserHistory,idSuperHistory,accionType,idAccion,idBacklog, priority):
        '''Permite insertar una Historia de usuario'''
        checkCodUserHistory = type(codeUserHistory) == str
        checkPriority       = type(priority) == int and CONST_MIN_SCALE <= priority <= CONST_MAX_SCALE
        
        if checkCodUserHistory and checkPriority:
            checkLenCodUserHistory = CONST_MIN_COD <= len(codeUserHistory) <= CONST_MAX_COD
            checkIdSuperHistory    = type(idSuperHistory) == int and idSuperHistory >= CONST_MIN_IDHIST
            
            if checkCodUserHistory and checkLenCodUserHistory and checkIdSuperHistory:
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = idSuperHistory).all()
                
                if oUserHistory !=[] or idSuperHistory == 0:
                    checkTypeAccion = accionType in arrayType
                    checkIdAccion   = type(idAccion) == int and idAccion >= CONST_MIN_ID
                    checkIdBacklog  = type(idBacklog) == int and idBacklog >= CONST_MIN_ID
                    
                    if checkTypeAccion and checkIdAccion and checkIdBacklog:
                        oHistorys = clsAccion.query.filter_by(AC_idAccion = idAccion).all()
                        oBacklog  = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                
                        if oBacklog != [] and oHistorys != []:                         
                            newUserHistory = clsUserHistory(codeUserHistory,idSuperHistory,accionType,idAccion,idBacklog,priority)
                            db.session.add(newUserHistory)
                            db.session.commit()
                            return True
        return False
    
        
    def searchUserHistory(self,codeUserHistory):
        '''Permite encontrar una historia de usuario por codigo'''
        typecod = type(codeUserHistory) == str
        
        if typecod:
            checkLenCodeUserHistory = len(codeUserHistory) <= CONST_MAX_COD
            if checkLenCodeUserHistory:
                found = clsUserHistory.query.filter_by(UH_codeUserHistory = codeUserHistory).all()
                return found
        return ([])
    
    
    def searchIdUserHistory(self,idUserHistory):
        '''Permite encontrar una historia de usuario por su id'''
        checkTypeId           = type(idUserHistory) == int
        checkLenIdUserHistory = idUserHistory >= CONST_MIN_ID
        
        if checkTypeId and checkLenIdUserHistory:
            found = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
            return found
        return ([])
    
    
    def updateUserHistory(self,idUserHist,newCodeUserHistory,newIdSuperHistory,newAccionType,newIdAccion,newScale):
        '''Permite modificar una Historia de usuario'''
        checkCodUserHistory    = type(newCodeUserHistory) == str
        checkScale             = type(newScale) == int
        checkLenCodUserHistory = CONST_MIN_COD <= len(newCodeUserHistory) <= CONST_MAX_COD
        checkIdHistory         = type(newIdSuperHistory) == int and newIdSuperHistory >= CONST_MIN_IDHIST
        
        if checkCodUserHistory and checkLenCodUserHistory and checkIdHistory and checkScale:
            oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory  = newIdSuperHistory).all()
                      
            if oUserHistory !=[] or newIdSuperHistory == 0:
                checkTypeAccion = newAccionType in arrayType
                checkIdAccion   = type(newIdAccion) == int and newIdAccion >= CONST_MIN_ID
                
                if checkTypeAccion and checkIdAccion:
                    oAccions = clsAccion.query.filter_by(AC_idAccion  = newIdAccion).all()
                    
                    if oAccions != []:
                        result            = clsUserHistory.query.filter_by(UH_idUserHistory  = idUserHist).all()
                        checkSuperHistory = clsUserHistory.query.filter_by(UH_idSuperHistory = idUserHist).all()
                        
                        if result != []:
                            result[0].UH_codeUserHistory = newCodeUserHistory
                            result[0].UH_accionType      = newAccionType
                            result[0].UH_idAccion        = newIdAccion
                            result[0].UH_scale           = newScale
                            if checkSuperHistory == []:
                                result[0].UH_idSuperHistory = newIdSuperHistory

                            db.session.commit()
                        return True
        return False
    
    
    def updatePriority(self,idHistory,priority):
        '''Permite actualizar la prioridad de una historia de usuario'''
        checkIdHistory  = type(idHistory) == int and CONST_MIN_ID <= idHistory
        checkPriority   = type(priority) == int and 0 <= priority
        if checkIdHistory and checkPriority:
            found = clsUserHistory.query.filter_by(UH_idUserHistory = idHistory).first()
            if found != None:
                found.UH_scale = priority
                db.session.commit()
                return True
        return False

    
    def scaleType(self,historyId):
        '''Permite saber el tipo de escala seleccionada para un producto'''
        checkTypeId = type(historyId) == int    
        
        if checkTypeId: 
            found = clsUserHistory.query.filter_by(UH_idUserHistory = historyId).first()
            
            if found != None:
                productId = found.UH_idBacklog 
                oBacklog  = clsBacklog.query.filter_by(BL_idBacklog = productId).first()
                scale     = oBacklog.BL_scaleType
                return scale
        return (None)


    def accionsAsociatedToUserHistory(self,userHistoryId):
        ''' Permite obtener una lista de los Acciones asociados a una historia de usuario'''
        checkTypeId = type(userHistoryId) == int and userHistoryId >= CONST_MIN_ID
        
        if checkTypeId: 
            found = clsUserHistory.query.filter_by(UH_idUserHistory = userHistoryId).all()
            return found
        return([])
    
    def searchidUserHistoryIdAccion(self, idAccion):
        '''Permite obtener los ids de las historias de usuario que contiene el idAccion'''
        checkIdAccion = type(idAccion) == int and idAccion >= CONST_MIN_ID
 
        if checkIdAccion:
            result = clsUserHistory.query.filter_by(UH_idAccion  = idAccion).all()
            return result
    
    
    def deleteUserHistory(self,codeUserHistory):
        '''Permite eliminar una historia segun su codigo'''
        
        checkTypeCodeHistory = type(codeUserHistory) == str
        
        if checkTypeCodeHistory:
            checkLenCodeHistory = CONST_MIN_COD <= len(codeUserHistory) <= CONST_MAX_COD
            
            if checkLenCodeHistory:
                found = clsUserHistory.query.filter_by(UH_codeUserHistory = codeUserHistory).all()
                
                if found != []:
                    for i in found:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 


    def transformUserHistory(self,idUserHistory):
        ''''''
        
        historyDict   = {}
        # Buscamos la historia de usuario.
        foundHistory = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).first()
        
        # Guardamos el id de la historia.
        historyDict['idHistory'] = foundHistory.UH_idUserHistory 
        
        # Almacenamos en el diccionario el valor de la escala correspondiente.
        historyDict['priority'] = foundHistory.UH_scale
        
        # Obtenemos los id de los actores que componen la historia.
        result = clsActorsUserHistory.query.filter_by(AUH_idUserHistory = idUserHistory)
        idActorsList = []
        for act in result:
            idActorsList.append(act.AUH_idActor)
              
        missingActors = len(idActorsList)
        actorsString  = ''
        
        # Almacenamos los actores asociados a la historia en el diccionario de la historia.
        for act in idActorsList:
            result       = clsActor.query.filter_by(A_idActor = act).all()
            actorsString = actorsString + ' ' + str(result[0].A_nameActor) + ' '
            
            if missingActors != 1:
                actorsString = actorsString + ',' 
                 
            missingActors = missingActors - 1   
        historyDict['actors'] = actorsString.lower()
        
        # Almacenamos la accion asociada la historia en el diccionario de la historia.
        idAccions   = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
        foundAccion = clsAccion.query.filter_by(AC_idAccion  = idAccions[0].UH_idAccion).all()
    
        # Obtenemos el tipo de accion de la historia.
        option    = foundHistory.UH_accionType
        historyDict['accions'] = ' ' + options[option] + str(foundAccion[0].AC_accionDescription).lower() + ' ' 

        # Obtenemos los id de los objetivos que componen la historia.
        result  = clsObjectivesUserHistory.query.filter_by(OUH_idUserHistory = idUserHistory)
        idObjectivesList  = []
        
        for obj in result:
            idObjectivesList.append(obj.OUH_idObjective)
    
        missingObjectives = len(idObjectivesList)
        objectivesString  = ''
        
        # Almacenamos los objetivos asociados a la historia en el diccionario de la historia.
        for obj in idObjectivesList: 
            result           = clsObjective.query.filter_by(O_idObjective = obj).all()
            objectivesString = objectivesString + ' ' + str(result[0].O_descObjective)
            
            if missingObjectives != 1:
                objectivesString = ' ' + objectivesString + ',' 
                 
            if missingObjectives == 1: 
                objectivesString = objectivesString + '.'  
                
            missingObjectives = missingObjectives - 1
            
        historyDict['objectives'] = objectivesString.lower()
        
        return historyDict
            
# Fin Clase userHistory
