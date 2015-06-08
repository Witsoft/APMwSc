# -*- coding: utf-8 -*-. 

from modelDummy   import *
from backLogDummy import *

# Declaracion de constantes.
CONST_MAX_NAME_ACTOR        = 50
CONST_MIN_NAME_ACTOR        = 1
CONST_MIN_ACTOR_DESCRIPTION = 1
CONST_MAX_ACTOR_DESCRIPTION = 140
CONST_MIN_ID                = 1

class role(object):
    '''Clase que permite manejar los Actores de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla actor esta vacia'''
        aActor = clsActor.query.all()
        return (aActor == [])
    

    def insertActor(self,nameActor,actordescription,idBacklog):
        '''Permite insertar un actor'''
        checkTypeName        = type(nameActor) == str
        checkTypeDescription = type(actordescription) == str
        checkTypeId          = type(idBacklog) == int
        
        if checkTypeName  and checkTypeDescription and checkTypeId:
            checkLongName        = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR
            checkLongDescription = CONST_MIN_ACTOR_DESCRIPTION <= len(actordescription) <= CONST_MAX_ACTOR_DESCRIPTION
            
            if checkLongName and checkLongDescription:
                oBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                oActor   = clsActor.query.filter_by(A_nameActor = nameActor).all()
                
                if (oActor == []) and (oBacklog != []):
                    newActor = clsActor(nameActor, actordescription, idBacklog)
                    db.session.add(newActor)
                    db.session.commit()
                    return True
        return False


    def findNameActor(self, nameActor):
        '''Permte buscar un elemento en la tabla de actores'''
        checkTypeName = type(nameActor) == str
        if checkTypeName:
            checkLenName = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR
            
            if  checkLenName:
                found = clsActor.query.filter_by(A_nameActor = nameActor).all()
                return found
        return([])
    
    
    def findIdActor(self, idActor):
        '''Permite buscar un elemento en la tabla de actores por su id'''
        checkIdActor = type(idActor) == int and idActor >= CONST_MIN_ID
        if checkIdActor:
                found = clsActor.query.filter_by(A_idActor = idActor).all()
                return found
        return([])
              

    def updateActor(self, nameActor, newNameActor, newDescription):
        '''Permite modificar un nombre de la clase actor'''
    
        checkTypeName        = type(nameActor) == str
        checkTypeNewActor    = type(newNameActor) == str
        checkTypeDescription = type(newDescription) == str
    
        if checkTypeName and checkTypeNewActor and checkTypeDescription:
            checkLongnameActor      = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR
            checkLongNewnameActor   = CONST_MIN_NAME_ACTOR <= len(newNameActor) <= CONST_MAX_NAME_ACTOR
            checkLongNewDescription = CONST_MIN_ACTOR_DESCRIPTION <= len(newDescription) <= CONST_MAX_ACTOR_DESCRIPTION
            
            if checkLongnameActor and checkLongNewnameActor  and checkLongNewDescription:    
                foundnameActor = clsActor.query.filter_by(A_nameActor = nameActor).all()
                foundNewActor  = clsActor.query.filter_by(A_nameActor = newNameActor).all()
                
                if foundnameActor != []:
                    updateActor = clsActor.query.filter_by(A_nameActor = nameActor).first()
                    updateActor.A_nameActor        = newNameActor
                    updateActor.A_actorDescription = newDescription
                    db.session.commit()
                    return True
        return False   
    

    def deleteActor(self,nameActor):
        '''Permite eliminar un actor dado su nombre'''

        checkTypeName = type(nameActor) == str       
        if checkTypeName:
            checkLongNameActor = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR 
            if checkLongNameActor:
                oActor = clsActor.query.filter_by(A_nameActor = nameActor).all()
                if oActor != []:
                    tupla = clsActor.query.filter_by(A_nameActor = nameActor).first()    
                    db.session.delete(tupla)
                    db.session.commit()
                    return True
        return False
    
# Fin Clase Actor