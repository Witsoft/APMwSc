# -*- coding: utf-8 -*-. 

import unittest

from historyDummy import *
from accionsDummy import *

class TestHistory(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertUserHistory   #
    #############################################
        
    # Caso Inicial
 
    # Prueba 0
    def testInserAccionExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc = accions()
        aAcc.insertAccion('Reservar un taxi.',1)
        aAcc.deleteAccion('Reservar un taxi.')
        aBackLog.deleteProduct('Reservar un taxi.')
                
        # Prueba 1
    def testInsertHistoryElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('hola','obligatorio',1)
        self.assertTrue(result)
       
        # Prueba 2
        # Insertando una historia en un idBacklog que no existe
    def testInsertHistoryElementNotExist(self):
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('chao','opcional',2)
        self.assertFalse(result)
        
    # Prueba 3
    def testInsertHistoryRepeatedElement(self):
        aAcc   = userHistory()
        result1 = aAcc.insertUserHistory('hola','obligatorio',1)
        self.assertFalse(result1)
        
    # Casos Fronteras
     
    # Prueba 4
    def test4InsertHistoryShortDesc0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('','',1)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')    
    # Prueba 5
    def testinsertUserHistoryLongDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A','A',1)
        self.assertFalse(result)
        aAcc.deleteUserHistory('A')
        aBackLog.deleteProduct('Taxi seguro.')    
        
    # Prueba 6
    def test6insertUserHistoryLongDesc11(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A'*11,'obligatorio',1)
        self.assertTrue(result)
        aAcc.deleteUserHistory('obligatorio')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 7
    def testInsertObjectiveLongDesc12(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('B'*12,'obligatorios',1)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
        
     # Prueba 8
    def testinsertUserHistoryIdBackLogInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('B'*4,'obligatorio',0)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
     
    # Casos Esquinas
      
    # Prueba 9
    def testinsertUserHistoryIdBackLogNoExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('luis','opcional',2)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
     
    # Prueba 10
    def testinsertUserHistoryLongDesc11AndIdBackLogNoExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A'*11,'obligatorio',3)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
     
    # Casos Maliciosos
     
    # Prueba 11
    def testInsertNotString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('luis',4350,1)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 12
    def testInsertNoneString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A',None,1)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
        
        
    #############################################      
    #   Suite de Pruebas para searchUserHistory #
    #############################################
    
    #Casos Frontera
    
    #Caso 13
    def testSearchHistoryExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo1','obligatorio',1)
        result = userH.searchUserHistory('codigo1')
        aBackLog.deleteProduct('Reservar un taxi.')        
    
    #Caso 14
    def testSearchHistoryTrue(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo2','obligatorio',1)
        result = userH.searchUserHistory('codigo2')
        self.assertNotEqual([],result)
        #userH.deleteUserHistory('codigo2')
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Caso 15
    def testSearchHistoryNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo3','obligatorio',1)
        result = userH.searchUserHistory('codigo4')
        self.assertEqual([],result)
        #userH.deleteUserHistory('codigo3')
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Caso 16
    def testSearchHistoryLong10(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo7890','obligatorio',1)
        result = userH.searchUserHistory('codigo7890')
        self.assertNotEqual([],result)
        #userH.deleteUserHistory('codigo7890')
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Caso 17    
    def testSearchHistoryLong11(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo78910','obligatorio',1)
        result = userH.searchUserHistory('codigo78910')
        self.assertNotEqual([],result)
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Casos Malicia
    
    #Caso 18
    def testSearchHistoryNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory(None,'obligatorio',1)
        result = userH.searchUserHistory(None)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Reservar un taxi.') 
        
        
    ######################################################      
    #       Suite de Pruebas para deleteUserHistory      #
    ###################################################### 
      
    # Caso Inicial
      
    # Prueba 19
    def testdeleteUserHistoryExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        aAcc.insertUserHistory('luis','opcional',1)
        aAcc.deleteUserHistory('luis')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Normales
  
    # Prueba 20
    def testdeleteUserHistory(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A'*11,'obligatorio',1)
        result = aAcc.deleteUserHistory('A'*11)
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')
 
    # Prueba 21      
    def testdeleteUserHistory_1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.deleteUserHistory('opcional')
        self.assertFalse(result)
        aAcc.deleteUserHistory('opcional')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Fronteras
      
    # Prueba 22
    def testdeleteUserHistory1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A','A',1)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Maliciosos
  
    # Prueba 23
    def testdeleteUserHistoryInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.deleteUserHistory('')
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 24
    def testdeleteUserHistoryNotString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        aAcc.insertUserHistory(12345,'opcional',1)
        result = aAcc.deleteUserHistory(12345)
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 25    
    def test_44deleteUserHistoryNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.deleteUserHistory('llegaRapido')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
        
        
        
        
        
    