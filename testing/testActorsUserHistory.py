# -*- coding: utf-8 -*-. 

import unittest

from actorsUserHistoryDummy import *
from historyDummy import *
from accionsDummy import *

class TestActorsUserHistory(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertAccion   #
    #############################################
         
    # Caso Inicial
 
    # Prueba 1
    def testinsertActorAsociatedInUserHistory(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Insertamos el actor
        aAcc = accions()
        y = aAcc.insertAccion('Cualquier cosa2',1)
        print(y)
        search = aAcc.searchAccion('Cualquier cosa2')
        print(search)
        idFound = search[0].idaccion
        #Insertamos la historia
        aHist = userHistory()
        x = aHist.insertUserHistory('Hist300',0, 1,idFound, 1)
        print(x)
        searchHist = aHist.searchUserHistory('Hist300')
        print(searchHist)
        aHist.deleteUserHistory('Hist300')
        aAcc.deleteAccion('Cualquier Cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
         

    
         

    