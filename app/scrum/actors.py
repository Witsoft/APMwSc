# -*- coding: utf-8 -*-. 

from app.scrum.model import *

# Declaracion de constantes.
maxNameActor = 50
minNameActor = 1
minActorDescription = 1
maxActorDescription = 140

actors       = ['Product Owner', 'Scrum Master', 'Team Member']


class actor(object):
    '''Clase que permite manejar los Actores de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla actor esta vacia'''
        aactor = clsActor.query.all()
        return (aactor == [])

    def insertActor(self,nameactor,actordescription,id_pila):
        '''Permite insertar un actor'''
        
        typename = (type(nameactor) == str)
        typedescription = (type(actordescription) == str)
        typeid = (type(id_pila) == int)
        if (typename and typedescription and typeid):
            long_nameactor = minNameActor <= len(nameactor) <= maxNameActor
            long_actordescription = minActorDescription <= len(actordescription) <= maxActorDescription
            if (long_nameactor and long_actordescription and (nameactor in actors)):
                backLog = clsbackLog.query.filter_by(id_backLog = id_pila).all()
                aactor = clsActor.query.filter_by(nameactor = nameactor).all()
                if ((aactor == []) and (backLog != [])):
                    new_actor = clsActor(nameactor = nameactor, actordescription = actordescription,id_pila = id_pila)
                    db.session.add(new_actor)
                    db.session.commit()
                    return True
        return False

    def findNameActor(self, nameactor):
        """Permite buscar un elemento en la base de datos"""
        if type(nameactor) == str:
            if len(nameactor) >= minNameActor and len(nameactor) <= maxNameActor:
                found = clsActor.query.filter_by(nameactor=nameactor).all()
                return found
        return([])
                
    def updateActor(self, name, newNameActor):
        """Permite modificar un nombre de la clase actor"""
        validname    = (type(name) == str)
        validnewname = (type(newNameActor) == str)  
        if ((validname) and (validnewname)):
            if (((name == 'Product Owner') or (name == 'Scrum Master') or(name == 'Team Member')) and ((newNameActor == 'Product Owner') or (newNameActor == 'Scrum Master') or(newNameActor == 'Team Member'))):
                lengthname    = minNameActor <= len(name) <= maxNameActor
                lengthnewname = minNameActor <= len(newNameActor) <= maxNameActor
                if ((lengthname) and (lengthnewname)):
                    found1 = self.findNameActor(name)
                    found2 = self.findNameActor(newNameActor)
                    if (found1 != []) and (found2 == []):
                        update_actor = clsActor.query.filter_by(nameactor = name).first()
                        update_actor.nameactor = newNameActor
                        db.session.commit()
                        return True
        return False                   
                
    def searchActor(self,idactor): 
        '''Permite buscar un actor dado su id'''
        if (idactor == '') or (idactor == None) or idactor <=0 or type(idactor) != int:
            return []
        else:
            actor1 = clsActor.query.filter_by(idactor=idactor).all()
            return actor1
           
    def deleteActor(self,idactor):
        '''Permite eliminar un actor dado su id'''
        if (type(idactor) != int) or idactor <=0:
            return False
        else:
            aactor = clsActor.query.filter_by(idactor=idactor).all()
            if aactor == []:
                return False
            else:
                for i in aactor:    
                    db.session.delete(i)
                db.session.commit()
                return True

# Fin Clase Actor
