# -*- coding: utf-8 -*-. 

from app.scrum.role import *

# Definicion de constantes
const_min_id = 1


class actorsUserHistory(object):
    '''Clase que permite manejar los objetivos asociados a una historia de manera persistente'''
    
    def insertActorAsociatedInUserHistory(self,id_Actor, id_userHistory):
        '''Permite insertar un actor a una historia de usuario'''
        
        checkIdActor     = type(id_Actor) == int and id_Actor >= const_min_id
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= const_min_id
        
        if checkIdActor and checkUserHistory:
            oActor         = clsRole.query.filter_by(idrole = id_Actor).all()
            oIdUserHistory = clsUserHistory.query.filter_by(id_userHistory = id_userHistory).all()
            
            if oActor != [] and oIdUserHistory != []:
                newAct = clsRolesUserHistory(ref_idrole = id_Actor, ref_idUserHistory = id_userHistory)
                db.session.add(newAct)
                db.session.commit()
                return True
        return False
        
    def idActorsAsociatedToUserHistory(self, id_userHistory):
        '''Permite obtener los ids de los actores asociados a una historia de usuario'''
        
        checkIdUserHistory = type(id_userHistory) == int and id_userHistory >= const_min_id
        if checkIdUserHistory:
            result = clsRolesUserHistory.query.filter_by(ref_idUserHistory = id_userHistory)
            idsList = []
            for act in result:
                idsList.append(act.ref_idrole)
            return idsList
        
    def deleteActorAsociatedInUserHistory(self,id_Actor, id_userHistory):
        '''Permite eliminar un actor de una historia de usuario'''
        
        checkIdActor     = type(id_Actor) == int and id_Actor >= const_min_id
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= const_min_id

        if checkIdActor and checkUserHistory:
            oActor = clsRolesUserHistory.query.filter_by(ref_idrole = id_Actor,ref_idUserHistory = id_userHistory).all()
            if oActor != []:
                for i in oActor:
                    db.session.delete(i)
                db.session.commit()
                return True
        return False