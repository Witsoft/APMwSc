# -*- coding: utf-8 -*-. 

from app.scrum.model import *

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

    def modifyDescription(self, dName, new_dName):   
        '''Permite actualizar los valores de una Descripcion'''    
        if ((type(new_dName) != str) or (type(dName) != str)):
            return False
        else:
            aName = self.findName(dName)
            if (aName == []):
                return False
            else:
                new_dName = clsBackLog(BL_name = new_dName)
                long_dName = len(new_dName.BL_name)
                if ((long_dName > const_maxName) or (long_dName < const_minName)):
                    return False
                else:
                    aName.BL_name = new_dName
                    db.session.commit()
                    return True

    def modifyName(self, Name, new_description):   
        '''Permite actualizar los valores de una Descripcion'''    
        if ((type(new_description) != str) or (type(Name) != str)):
            return False
        else:
            aName = self.findName(Name)
            if (aName == []):
                return False
            else:
                new_mod = clsBackLog(BL_name = Name, BL_description = new_description)
                long_description = len(new_mod.BL_description)
                if ((long_description > const_maxDescription) or (long_description < const_minDescription)):
                    return False
                else:
                    aName.BL_description = new_description
                    db.session.commit()
                    return True

    
    def deleteProduct(self, Name):
        '''Permite eliminar una a descripción de la tabla'''
        if (type(Name) != str):
            return False
        else:
            long_Name = len(Name)
            if ((long_Name > const_maxName)or(long_Name < const_minName)):
                return False
            else:
                aName = self.findName(Name)
                if (aName == []):
                    return False
                else:
                    for i in aName:    
                        db.session.delete(i)
                        db.session.commit()
                    return True

    def actorsAsociatedToProduct(self,productId):
        ''' Permite obtener una lista de los Actores asociados a una pila de Producto'''
        checkTypeId = type(productId) == int    
        if checkTypeId: 
            found = clsRole.query.filter_by(id_pila=productId).all()
            return found
        return([])              
                   
