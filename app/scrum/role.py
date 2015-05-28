# -*- coding: utf-8 -*-. 

from app.scrum.backLog import *

# Declaracion de constantes.
maxNameRole = 50
minNameRole = 1
minRoleDescription = 1
maxRoleDescription = 140
minId = 1

class role(object):
    '''Clase que permite manejar los Roles de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla role esta vacia'''
        arole = clsRole.query.all()
        return (arole == [])

    def insertRole(self,namerole,roledescription, id_pila):
        '''Permite insertar un role'''
        typename        = (type(namerole) == str)
        typedescription = (type(roledescription) == str)
        typeid          = (type(id_pila) == int)
        if (typename and typedescription and typeid):
            long_namerole        = minNameRole <= len(namerole) <= maxNameRole
            long_roledescription = minRoleDescription <= len(roledescription) <= maxRoleDescription
            
            if long_namerole and long_roledescription: 
                print('Entree en segundo')              
                backLog = clsBackLog.query.filter_by(id_backLog = id_pila).all()     
                arole   = clsRole.query.filter_by(namerole = namerole).all()
                if ((arole == []) and (backLog != [])):
                    new_role = clsRole(namerole = namerole,roledescription = roledescription,id_pila = id_pila)
                    db.session.add(new_role)
                    db.session.commit()
                    return True
        return False


    def findNameRole(self, namerole):
        """Permite buscar un elemento en la base de datos"""
        if type(namerole) == str:
            if len(namerole) >= minNameRole and len(namerole) <= maxNameRole:
                found = clsRole.query.filter_by(namerole=namerole).all()
                return found
        return([])
    
    def findIdRole(self, idrole):
        """Permite buscar un elemento en la base de datos por su id"""
        checkIdRole = type(idrole) == int and idrole >= minId
        if checkIdRole:
                found = clsRole.query.filter_by(idrole=idrole).all()
                return found
        return([])
                

    def updateRole(self, namerole, newNameRole, newDescription):
        """Permite modificar un nombre de la clase role"""
    
        typename = (type(namerole) == str)
        typenewrole = (type(newNameRole) == str)
        typedescription = (type(newDescription) == str)
    
        if (typename and typedescription and typenewrole):
            long_namerole = minNameRole <= len(namerole) <= maxNameRole
            long_newNameRole = minNameRole <= len(newNameRole) <= maxNameRole
            long_roledescription = minRoleDescription <= len(newDescription) <= maxRoleDescription
            if (long_namerole and long_newNameRole and long_roledescription and (namerole in roles) and (newNameRole in roles)):    
                foundnamerole = self.findNameRole(namerole)
                foundnewrole  = self.findNameRole(newNameRole)
                if (foundnamerole != []) and (foundnewrole == []):
                    
                    update_role = clsRole.query.filter_by(namerole = namerole).first()
                    update_role.namerole = newNameRole
                    update_role.roledescription = newDescription
                    db.session.commit()
                    return True
        return False  
    
    def updateRoleReferenceToHistory(self,idRole, ref_idUserHistory):
        '''Permite actualizar la referencia a la historia de usuario a la cual pertenece el actor'''
        result = clsUserHistory.query.filter_by(id_userHistory = ref_idUserHistory).all()
        
        if (result != []):
            oRole = clsRole.query.filter_by(idrole = idRole).first()
            oRole.id_userHistory = ref_idUserHistory
            db.session.commit()
            return True
        return False   

           
    def deleteRole(self,idrole):
        '''Permite eliminar un role dado su id'''
        if ((type(idrole) == int) and idrole >= minId):
            arole = clsRole.query.filter_by(idrole=idrole).all()
            if (arole != []):
                tupla = clsRole.query.filter_by(idrole=idrole).first()    
                db.session.delete(tupla)
                db.session.commit()
                return True
        return False
    
# Fin Clase Role
