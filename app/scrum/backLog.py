# -*- coding: utf-8 -*-. 

from app.scrum.model import *

# Declaracion de constantes.
const_maxDescription = 140
const_minDescription = 1


class backLog(object):
    '''Clase que permite (completar)'''
    
    def findDescription(self,dName):
        '''Permite buscar un nombre'''
        if (type(dName) != str):
            return []
        else:
            long_dName = len(dName)
            if ((long_dName >const_maxDescription) or (long_dName < const_minDescription)):
                return []
            else:
                dUser = clsUser.query.filter_by(BL_name = dName).all()
                return dUser
