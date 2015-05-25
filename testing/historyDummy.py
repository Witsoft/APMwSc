# -*- coding: utf-8 -*-. 

from modelDummy   import *
from backLogDummy import *

# Declaracion de constantes
arrayType = ['obligatorio', 'opcional']
minuserHistory = 1
maxuserHistory = 140
const_max_cod = 11

class userHistory(object):
    '''Clase que permite manejar las historias de manera persistente'''

    def insertUserHistory(self,cod_userHistory, type_userHistory, id_backLog):
        '''Permite insertar una Historia'''
        
        if (type(cod_userHistory) == str):
            leng_cod_userHistory = len(cod_userHistory) <= const_max_cod           
            typeid = (type(id_backLog) == int)
            
            if (leng_cod_userHistory and typeid):
                tipo_userhistory = ((type_userHistory == arrayType[0]) or (type_userHistory == arrayType[1]) )
                
                if tipo_userhistory:
                    obackLog = clsBackLog.query.filter_by(id_backLog = id_backLog).all()
                    ohistory = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                    if (obackLog != []) and (ohistory == []):
                        new_history = clsUserHistory(cod_userHistory = cod_userHistory, type_userHistory = type_userHistory,id_backLog = id_backLog)
                        db.session.add(new_history)
                        db.session.commit()
                        return True
        return False
    
    def searchUserHistory(self,cod_userHistory):
        '''Permite buscar una historia segun su codigo'''
        typecod = (type(cod_userHistory) == str)
        if typecod:
            leng_cod_userHistory = (len(cod_userHistory) <= const_max_cod)
            if leng_cod_userHistory:
                found = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                return found
        return ([])
    
    
    def deleteUserHistory(self, cod_userHistory):
        '''Permite eliminar una historia segun su id'''
        
        typeUD = (type(cod_userHistory) == str)  
        if typeUD:
            Len_UD = minuserHistory <= len(cod_userHistory) <= maxuserHistory
            if Len_UD:
                foundid = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                if foundid != []:
                    oHistory = clsUserHistory.query.filter_by(cod_userHistory = cod_userHistory).all()
                    for i in oHistory:    
                        db.session.delete(i)          
                    db.session.commit()
                    return True
        return False 

           
# Fin Clase Accion