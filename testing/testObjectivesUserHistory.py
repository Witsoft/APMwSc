# -*- coding: utf-8 -*-. 

import unittest

from objectivesUserHistoryDummy import *
from historyDummy import *
from accionsDummy import *
from objectiveDummy import *

class TestActorsUserHistory(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertAccion   #
    #############################################

    # Caso Inicial
 
    # Prueba 0
    def testinsertObjectiveAsociatedInUserHistory(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Cualquier cosa2',1)
        search = aAcc.searchAccion('Cualquier cosa2')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('Hist300',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('Hist300')
        idFound1 = searchHist[0].id_userHistory

      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Cualquier cosa2',1)
        search = aObj.searchObjective('Cualquier cosa2')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1) 
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('Hist300')
        aObj.deleteObjective('Cualquier Cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Casos Normales
    
    # Prueba 1
    
    def testinsertObjectiveAsociatedInUserHistory1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
        self.assertTrue(result)
              
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
     # Casos Fronteras
     
     # Prueba 2
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveNoExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(0, idFound1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
     # Prueba 3
    def testinsertObjectiveAsociatedInUserHistoryIdHistoryNoExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, 0) 
        self.assertFalse(result)
       
       # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 4
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective

         
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory((2**31)-1,idFound1) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 5
    def testinsertObjectiveAsociatedInUserHistoryIdUserHistoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, (2**31)-1) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')    

     # Caso Esquina
    
    # Prueba 6   
    
    def testinsertObjectiveAsociatedInUserHistoryNotExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(0, 0) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')    
        
    # Prueba 7
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveAndIdHIstoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
       # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory((2**31)-1, (2**31)-1) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 8
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveNotExistIdHIstoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
       # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(0, (2**31)-1) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 9
    def testinsertActorAsociatedInUserHistoryIdActorBigIdHIstoryNotExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory((2**31)-1, 0) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
            # Casos Malicia 
     
     # Prueba 10   
    def testinsertObjectiveAsociatedInUserHistoryNoExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(-1, -1) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 11   
    def testinsertObjectiveAsociatedInUserHistoryString(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory('1', '0') 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
     # Prueba 12   
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(None, idFound1) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
     # Prueba 13   
    def testinsertObjectiveAsociatedInUserHistoryIduserHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, None) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 14   
    def testinsertObjectiveAsociatedInUserHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(None, None) 
        self.assertFalse(result)
       
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    #########################################################      
    #   Suite de Pruebas para idActorsAsociatedToUserHistory   #
    #########################################################     
      
    # Caso Inicial 
     
    # Prueba 15
    
    def testidObjectivesAsociatedToUserHistory(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory 
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(idFound1)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Caso Frontera
    
    # Prueba 16    
    def testidObjectivesAsociatedToUserHistoryid_userHistory1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(idFound1)
        self.assertTrue(result) 
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 18   
    def testidObjectivosAsociatedToUserHistoryid_userHistory0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(0)
        self.assertEqual([],result)     
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 18   
    def testidObjectivesAsociatedToUserHistoryid_userHistoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
            
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory((2**31)-1)
        self.assertEqual([],result)     
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Casos Malicia

      # Prueba 19   
    def testidActorsAsociatedToUserHistoryid_userHistoryNoExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(-1)
        self.assertEqual([],result)     
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 20   
    def testidObjectivesAsociatedToUserHistoryid_userHistoryNoInt(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
            
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory('1')
        self.assertEqual([],result)     
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 21   
    def testidObjectiveAsociatedToUserHistoryid_userHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(None)
        self.assertEqual([],result)     
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 22   
    def testidActorsAsociatedToUserHistoryid_userHistoryStringInvalid(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Descripcion',1)
        search = aObj.searchObjective('Descripcion')
        idFound2 = search[0].idobjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(' ')
        self.assertEqual([],result)     
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aObj.deleteObjective('Descripcion')
        aBackLog.deleteProduct('Taxi seguro.')    

        









        
         

  

 
         
         