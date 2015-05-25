# -*- coding: utf-8 -*-. 

from app.scrum.model import *
from lxml.html._diffcommand import description

# Declaracion de constantes.
const_maxDescription = 140
const_minDescription = 1

class backLog(object):
    '''Clase que permite (completar)'''
    
    def findDescription(self,dDescription):
        '''Permite buscar una descripcion'''
        
        checkTypeDesc = (type(dDescription)) != str
        if checkTypeDesc:
            return []
        else:
            long_dDescription = len(dDescription)
            if ((long_dDescription >const_maxDescription) or (long_dDescription < const_minDescription)):
                return []
            else:
                dBackLog = clsBackLog.query.filter_by(BL_description = dDescription).all()
                return dBackLog
        
    def insertBackLog(self,description):
        '''Permite insertar una descripción'''
        
        checkTypeDesc = (type(description)) != str
        if checkTypeDesc:
            return False
        else:
            new_prod = clsBackLog(BL_description = description)
            long_description = len(new_prod.BL_description)
            
            if  ((long_description > const_maxDescription) or (long_description < const_minDescription)):
                return False
            else:
                dDescAux = self.findDescription(description);
                if (dDescAux != []):
                    return False
                else:
                    db.session.add(new_prod)
                    db.session.commit()
                    return True

    def modifyDescription(self, description, new_description):   
        '''Permite actualizar los valores de una Descripcion'''    
        
        typenew_d   = (type(new_description) == str) 
        type_d      = (type(description) == str)
        if (type_d and typenew_d):
            long_d = const_minDescription <= len(new_d.BL_description) <= const_maxDescription
            if long_d:
                aDescription = self.findDescription(description)
                if (aDescription != []):
                    new_d = clsBackLog.query.filter_by(BL_description = description).first()
                    new_d.BL_description = new_description
                    db.session.commit()
                    return True
        return False

    def deleteProduct(self, description):
        '''Permite eliminar una a descripción de la tabla'''
        if (type(description) != str):
            return False
        else:
            long_description =  (const_mindescription > len(description) > const_maxdescription)
            if long_description:
                return False
            else:
                adescription = self.finddescription(description)
                if (adescription == []):
                    return False
                else:
                    tupla = clsBackLog.query.filter_by(BL_description = description).first()    
                    db.session.delete(tupla)
                    db.session.commit()
                    return True

    def actorsAsociatedToProduct(self,productId):
        ''' Permite obtener una lista de los Actores asociados a una pila de Producto'''
        checkTypeId = type(productId) == int    
        if checkTypeId: 
            found = clsRole.query.filter_by(id_pila=productId).all()
            return found
        return([])              
                   
