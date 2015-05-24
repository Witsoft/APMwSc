# -*- coding: utf-8 -*-. 

import unittest

from historyDummy import *
from accionsDummy import *

class TestHistory(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertUserHistory #
    #############################################
        
    # Caso Inicial

    # Prueba 1
    def testInserAccionExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc = accions()
        aAcc.insertAccion('Reservar un taxi.',1)
        aAcc.deleteAccion('Reservar un taxi.')
        aBackLog.deleteProduct('Reservar un taxi.')
         
        # Prueba 2
    def testInsertHistoryElement(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
       aAcc   = userHistory()
       result = aAcc.insertUserHistory('hola','obligatorio',1)
       #self.assertTrue(result)
       
    #############################################      
    #   Suite de Pruebas para searchUserHistory #
    #############################################
    
    #Casos Frontera
    
    #Caso 1
    def testSearchHistoryExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo1','obligatorio',1)
        result = userH.searchUserHistory('codigo1')
        aBackLog.deleteProduct('Reservar un taxi.')        
    
    #Caso 2
    def testSearchHistoryTrue(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo2','obligatorio',1)
        result = userH.searchUserHistory('codigo2')
        self.assertNotEqual([],result)
        #userH.deleteUserHistory('codigo2')
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Caso 3
    def testSearchHistoryNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo3','obligatorio',1)
        result = userH.searchUserHistory('codigo4')
        self.assertEqual([],result)
        #userH.deleteUserHistory('codigo3')
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Caso 4
    def testSearchHistoryLong10(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo7890','obligatorio',1)
        result = userH.searchUserHistory('codigo7890')
        self.assertNotEqual([],result)
        #userH.deleteUserHistory('codigo7890')
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Caso 5    
    def testSearchHistoryLong11(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory('codigo78910','obligatorio',1)
        result = userH.searchUserHistory('codigo78910')
        self.assertEqual([],result)
        aBackLog.deleteProduct('Reservar un taxi.')
    
    #Casos Malicia
    
    #Caso 6
    def testSearchHistoryNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        userH = userHistory()
        userH.insertUserHistory(None,'obligatorio',1)
        result = userH.searchUserHistory(None)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Reservar un taxi.') 