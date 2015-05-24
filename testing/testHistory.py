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
        
        
    ######################################################      
    #       Suite de Pruebas para deleteUserHistory      #
    ###################################################### 
      
    # Caso Inicial
      
    # Prueba 38
    def testdeleteUserHistoryExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        aAcc.insertUserHistory('luis','opcional',1)
        aAcc.deleteUserHistory('opcional')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Normales
  
    # Prueba 39
    def testdeleteUserHistory(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A'*11,'obligatorio',1)
        result = aAcc.deleteUserHistory('obligatorio')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')
 
    # Prueba 40      
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
      
    # Prueba 41
    def testdeleteUserHistory1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.insertUserHistory('A','A',1)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Maliciosos
  
    # Prueba 42
    def testdeleteUserHistoryInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.deleteUserHistory('')
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 43
    def testdeleteUserHistoryNotString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        aAcc.insertUserHistory('hola',12345,1)
        result = aAcc.deleteUserHistory(12345)
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 44    
    def test_44deleteUserHistoryNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = userHistory()
        result = aAcc.deleteUserHistory('llegaRapido')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
        
        
        
        
        
    