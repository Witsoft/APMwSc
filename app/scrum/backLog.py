# -*- coding: utf-8 -*-. 
'''
Fecha:    14/05/2015.
'''

from model import *

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
        
    def insertDescription(self, dName):
        '''Permite insertar una descripción'''
        
        if (type(dName) != str):
            return False
        else:
            new_dName = clsBackLog(BL_name = dName)
            long_dName = len(new_dName.BL_name)
            
            if  ((long_dName > const_maxDescription) or (long_dName < const_minDescription)):
                return False
            else:
                #dNameAux = clsBackLog.query.filter_by(BL_name = dName).all()
                dNAmeAux = self.findDescription(dName);
                if (dNameAux != []):
                    return False
                else:
                    db.session.add(new_dName)
                    db.session.commit()
                    return True

 
                    
                    
                    
                    
                    
                    
                    