# -*- coding: utf-8 -*-. 

import unittest

from historyDummy import *
from accionsDummy import *

class TestHistory(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertUserHistory   #
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