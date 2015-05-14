# -*- coding: utf-8 -*-. 

import model

# Declaracion de constantes.
const_minIdBacklog = 1
const_minDescObj   = 1
const_maxDescObj   = 140


class objective(object):
    '''Clase que permite manejar los objetivos de manera persistente'''

    def insertObjective(self,descObjective, id_backlog):
        '''Permite insertar un Objetivo'''
        
        checkDesc    = type(descObjective) == str
        checkId_BL   = type(id_backlog) == int 
        checkIdMin   = id_backlog >= const_minIdBacklog   
        checkDescLen = const_minDescObj <= len(descObjective) <= const_maxDescObj
        
        if checkDesc and checkId_BL and checkIdMin and checkDescLen:
            aObj = clsRole.query.filter_by(id_backlog = id_backlog).all()
            if aObj != []:
                new_objetive = clsObjective(descObjective = descObjective,id_backlog = id_backlog)
                db.session.add(new_objective)
                db.session.commit()
                return True
        return False
                
    def searchObjective(self, descObjective):
        '''Permite buscar objetivos por su descripcion'''
        aObj = clsObjective.query.filter_by(descObjective = descObjective).all()
        return aObj
            
    def updateObjective(self, descObject,newDescObjective):
        '''Permite actualizar la descripcion de un objetivo'''
           
        checkDesc    = type(descObjective) == str  
        checkDescLen = const_minDescObj <= len(descObjective) <= const_maxDescObj
        
        checkNewDesc    = type(newDescObjective) == str  
        checkNewDescLen = const_minDescObj <= len(newDescObjective) <= const_maxDescObj
        
        if checkDesc and checkDescLen and checkNewDesc and checkNewDescLen:
            aObj = self.searchObjective(descObjective)
            if aObj != []:
                result = searchObjective(newDescObjective)
                if result == []:                
                    aObj.descObject = newDescObject
                    db.session.commit()
                    return True
        return False     
    
       
    def deleteObjective(self, descObjective):
        '''Permite eliminar un objetivo de acuerdo a su descripcion'''
        
        checkDesc    = type(descObjective) == str  
        checkDescLen = const_minDescObj <= len(descObjective) <= const_maxDescObj
        
        if checkDesc and checkDescLen:
            aObj = self.searchObjective(descObjective)
            if aObj != []:  
                for i in aObj:    
                    db.session.delete(i)          
                db.session.commit()
                return True
        return False 

           

# Fin Clase Objective
