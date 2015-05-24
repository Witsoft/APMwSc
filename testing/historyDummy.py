# -*- coding: utf-8 -*-. 

from modelDummy   import *
from backLogDummy import *

# Declaracion de constantes
arrayType = ['obligatorio', 'opcional']

class userHistory(object):
    '''Clase que permite manejar las historias de manera persistente'''

    def insertUserHistory(self,cod_userHistory, type_userHistory, id_backLog):
        '''Permite insertar una Historia'''
        
        leng_cod_userHistory = len(cod_userHistory) <= 10           
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