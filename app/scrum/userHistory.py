# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes
const_max_cod    = 11
const_min_cod    = 1
const_min_id     = 1
const_min_idHist = 0

arrayType = [1,2]

class userHistory(object):
    '''Clase que permite manejar las historias de manera persistente'''

    def insertUserHistory(self,cod_userHistory,id_History,type_accion,id_Accion,id_backLog):
        '''Permite insertar una Historia de usuario'''
        checkCodUserHistory    = type(cod_userHistory) == str
        checkLenCodUserHistory = const_min_cod <= len(cod_userHistory) <= const_max_cod
        checkIdHistory         = type(id_History) == int and id_History >= const_min_idHist
        
        if checkCodUserHistory and checkLenCodUserHistory and checkIdHistory:
            oUserHistory = clsUserHistory.query.filter_by(id_userHistory = id_History).all()
            
            if oUserHistory !=[] or id_History == 0:
                checkTypeAccion = type_accion in arrayType
                checkIdAccion   = type(id_Accion) == int and id_Accion >= const_min_id
                checkIdBacklog  = type(id_backLog) == int and id_backLog >= const_min_id
                
                if checkTypeAccion and checkIdAccion and checkIdBacklog:
                    oAccions = clsAccions.query.filter_by(idaccion = id_Accion).all()
                    oBackLog = clsBackLog.query.filter_by(id_backLog = id_backLog).all()
            
                    if (oBackLog != [] and oAccions != []):
                        new_history = clsUserHistory(cod_userHistory = cod_userHistory,id_History = id_History,type_accion = type_accion,ref_idaccion = id_Accion,id_backLog = id_backLog)
                        db.session.add(new_history)
                        db.session.commit()
                        return True
        return False
        
    def searchUserHistory(self,cod_userHistory):
        typecod = (type(cod_userHistory) == str)
        if typecod:
            leng_cod_userHistory = (len(cod_userHistory) <= const_max_cod)
            if leng_cod_userHistory:
                found = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                return found
        return ([])
     
#     def deleteUserHistory(self, cod_userHistory):
#         '''Permite eliminar una historia segun su id'''
#         
#         typeUD = (type(cod_userHistory) == str)  
#         if typeUD:
#             Len_UD = const_min_cod <= len(cod_userHistory) <= const_max_cod
#             if Len_UD:
#                 foundid = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
#                 if foundid != []:
#                     oHistory = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
#                     for i in oHistory:    
#                         db.session.delete(i)          
#                     db.session.commit()
#                     return True
#         return False 
#     
#     def actorsAsociatedToUserHistory(self,userHistoryId):
#         ''' Permite obtener una lista de los Actores asociados a una historia de usuario'''
#         checkTypeId = type(userHistoryId) == int    
#         if checkTypeId: 
#             found = clsRole.query.filter_by(id_userHistory = userHistoryId).all()
#             return found
#         return([])
#     
#     def objectivesAsociatedToUserHistory(self,userHistoryId):
#         ''' Permite obtener una lista de los Actores asociados a una historia de usuario'''
#         checkTypeId = type(userHistoryId) == int    
#         if checkTypeId: 
#             found = clsObjective.query.filter_by(id_userHistory = userHistoryId).all()
#             return found
#         return([])    
#     
#     def accionsAsociatedToUserHistory(self,userHistoryId):
#         ''' Permite obtener una lista de los Actores asociados a una historia de usuario'''
#         checkTypeId = type(userHistoryId) == int    
#         if checkTypeId: 
#             found = clsAccions.query.filter_by(id_userHistory = userHistoryId).all()
#             return found
#         return([])
#           
# # Fin Clase userHistory