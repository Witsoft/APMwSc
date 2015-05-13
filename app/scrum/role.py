# -*- coding: utf-8 -*-. 

from app.scrum.model import *

# Declaracion de constantes.
minIdrole   = 0
maxNameRole = 50
roles       = ['Product Owner', 'Scrum Master', 'Team Member']


class role(object):
    '''Clase que permite manejar los Roles de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla role esta vacia'''
        arole = clsRole.query.all()
        return (arole == [])

    def insertRole(self,idrole,namerole):
        '''Permite insertar un role'''
        arole = clsRole.query.filter_by(idrole=idrole).all()
        if (arole == []):
            new_role = clsRole(idrole = idrole, namerole = namerole)
            if  type(namerole) != str:
                return False
            else:
                long_namerole=len(new_role.namerole)
                if (type(idrole) == str or new_role.idrole == None or new_role.idrole <= minIdrole \
                        or new_role.namerole == '' or long_namerole > maxNameRole or new_role.namerole not in roles):
                    return False
                else:
                    db.session.add(new_role)
                    db.session.commit()
                    return True
        else:
            return False
    
    def updateRole(self,idrole,namerole):
        '''Permite actualizar un role'''
        if namerole == None:
            return False
        else:
            arole = clsRole(idrole = idrole, namerole = namerole)
            if (type(idrole) != int or idrole == None or len(namerole)<=minIdrole \
                or namerole == '' or len(namerole) > maxNameRole or arole.namerole not in roles):
                return False
            else:
                rolel = clsRole.query.filter_by(idrole=idrole).all()                
                if rolel == []:
                    return False
                else:
                    role1 = clsRole.query.filter_by(idrole=idrole).first()
                    role1.namerole = namerole
                    db.session.commit()
                    return True
                   
    def searchRole(self,idrole): 
        '''Permite buscar un role dado su id'''
        if (idrole == '') or (idrole == None) or idrole <=0 or type(idrole) != int:
            return []
        else:
            role1 = clsRole.query.filter_by(idrole=idrole).all()
            return role1
           
    def deleteRole(self,idrole):
        '''Permite eliminar un role dado su id'''
        if (idrole == '') or (idrole == None) or idrole <=0 or type(idrole) != int:
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
