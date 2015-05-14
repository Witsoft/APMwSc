# -*- coding: utf-8 -*-. 

from model import *

# Declaracion de constantes.
maxNameRole = 50
minNameRole = 1

roles       = ['Product Owner', 'Scrum Master', 'Team Member']


class role(object):
    '''Clase que permite manejar los Roles de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla role esta vacia'''
        arole = clsRole.query.all()
        return (arole == [])

    def insertRole(self,namerole):
        '''Permite insertar un role'''
        arole = clsRole.query.filter_by(namerole = namerole).all()
        if (arole == []):
            new_role = clsRole(namerole = namerole)
            if  type(namerole) != str:
                return False
            else:
                long_namerole=len(new_role.namerole)
                if long_namerole < minNameRole or long_namerole > maxNameRole or new_role.namerole not in roles:
                    return False
                else:
                    db.session.add(new_role)
                    db.session.commit()
                    return True
        else:
            return False

    def findNameRole(self, namerole):
        """Permite buscar un elemento en la base de datos"""
        if type(namerole) == str:
            if len(namerole) >= minNameRole and len(namerole) <= maxNameRole:
                found = clsRole.query.filter_by(namerole=namerole).all()
                return found
        return([])
                
    def updateRole(self, name, newNameRole):
        """Permite modificar un nombre de la clase role"""
        validname    = (type(name) == str)
        validnewname = (type(newNameRole) == str)  
        if ((validname) and (validnewname)):
            if (((name == 'Product Owner') or (name == 'Scrum Master') or(name == 'Team Member')) and ((newNameRole == 'Product Owner') or (newNameRole == 'Scrum Master') or(newNameRole == 'Team Member'))):
                lengthname    = minNameRole <= len(name) <= maxNameRole
                lengthnewname = minNameRole <= len(newNameRole) <= maxNameRole
                if ((lengthname) and (lengthnewname)):
                    found1 = self.findNameRole(name)
                    found2 = self.findNameRole(newNameRole)
                    if (found1 != []) and (found2 == []):
                        update_role = clsRole.query.filter_by(namerole = name).first()
                        update_role.namerole = newNameRole
                        db.session.commit()
                        return True
        return False                   
                
    def searchRole(self,idrole): 
        '''Permite buscar un role dado su id'''
        if (idrole == '') or (idrole == None) or idrole <=0 or type(idrole) != int:
            return []
        else:
            role1 = clsRole.query.filter_by(idrole=idrole).all()
            return role1
           
    def deleteRole(self,idrole):
        '''Permite eliminar un role dado su id'''
        if (type(idrole) != int) or idrole <=0:
            return False
        else:
            arole = clsRole.query.filter_by(idrole=idrole).all()
            if arole == []:
                return False
            else:
                for i in arole:    
                    db.session.delete(i)
                db.session.commit()
                return True

# Fin Clase Role