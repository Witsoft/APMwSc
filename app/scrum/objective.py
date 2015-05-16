# -*- coding: utf-8 -*-. 

from model   import *
from backLog import *

# Declaracion de constantes.
const_minIdBacklog = 1
const_minDescObj   = 1
const_maxDescObj   = 140


class objective(object):
    '''Clase que permite manejar los objetivos de manera persistente'''

    def insertObjective(self,descObjective, id_backLog):
        '''Permite insertar un Objetivo'''

        checkDesc    = type(descObjective) == str
        checkId_BL   = type(id_backLog) == int 
        checkIdMin   = id_backLog >= const_minIdBacklog 
        
        if checkDesc and checkId_BL and checkIdMin: 
            checkDescLen = const_minDescObj <= len(descObjective) <= const_maxDescObj
            
            if checkDescLen:
                aBackLog = clsBackLog.query.filter_by(id_backLog = id_backLog).all()
                aObj     = self.searchObjective(descObjective)

                if (aBackLog != []) and (aObj == []) :
                    new_objective = clsObjective(descObjective = descObjective,id_backLog = id_backLog)
                    db.session.add(new_objective)
                    db.session.commit()
                    return True
        return False
                
    def searchObjective(self, descObjective):
        '''Permite buscar objetivos por su descripcion'''
        aObj = clsObjective.query.filter_by(descObjective = descObjective).all()
        return aObj
            
    def updateObjective(self, descObjective,newDescObjective):
        '''Permite actualizar la descripcion de un objetivo'''
           
        checkDesc    = type(descObjective) == str 
        checkNewDesc = type(newDescObjective) == str
        
        if checkDesc and checkNewDesc: 
            checkDescLen    = const_minDescObj <= len(descObjective) <= const_maxDescObj
            checkNewDescLen = const_minDescObj <= len(newDescObjective) <= const_maxDescObj
        
        if checkDescLen and checkNewDescLen:
            aObj = self.searchObjective(descObjective)
            if aObj != []:
                result = self.searchObjective(newDescObjective)
                if result == []:                
                    aObj[0].descObjective = newDescObjective
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
