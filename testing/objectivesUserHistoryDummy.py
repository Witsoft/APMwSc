# -*- coding: utf-8 -*-. 

from roleDummy import *

# Definicion de constantes
const_min_id = 1


class objectivesUserHistory(object):
    '''Clase que permite manejar los objetivos asociados a una historia de manera persistente'''
    
    def insertObjectiveAsociatedInUserHistory(self,id_Objective, id_userHistory):
        '''Permite insertar un objetivo a una historia de usuario'''
        
        checkIdObjective = type(id_Objective) == int and id_Objective >= const_min_id
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= const_min_id
        
        if checkIdObjective and checkUserHistory:
            oObjective     = clsObjective.query.filter_by(idobjective = id_Objective).all()
            oIdUserHistory = clsUserHistory.query.filter_by(id_userHistory = id_userHistory).all()
            
            if oObjective != [] and oIdUserHistory != []:
                newObj = clsObjectivesUserHistory(ref_idobjective = id_Objective, ref_idUserHistory = id_userHistory)
                db.session.add(newObj)
                db.session.commit()
                return True
        return False
        
    def idObjectivesAsociatedToUserHistory(self,id_userHistory):
        '''Permite obtener los ids de los objetivos asociados a una historia de usuario'''
        
        checkIdUserHistory = type(id_userHistory) == int and id_userHistory >= const_min_id
        if checkIdUserHistory:
            result  = clsObjectivesUserHistory.query.filter_by(ref_idUserHistory = id_userHistory).all()
            idsList = []
            for obj in result:
                idsList.append(obj.ref_idobjective)
            return idsList
        return ([])