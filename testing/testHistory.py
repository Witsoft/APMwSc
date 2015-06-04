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
    def testInserHistoryExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Cualquier cosa2',1)
        search = aAcc.searchAccion('Cualquier cosa2')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 2
    # Insertando una historia en un idBacklog que no existe
    def testInsertHistoryElementNotExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
        result = searchHist = aHist.searchUserHistory('H2')
        self.assertTrue(result)
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 3
    def testInsertHistoryRepeatedElement(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
        result1 = aHist.insertUserHistory('H2',0, 1,idFound, 2,1)
        self.assertFalse(result1)
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
               
         
    # Casos Fronteras
      
    # Prueba 4
    def test4InsertHistoryShortDesc0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 1,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      
    # Prueba 5
    def test4InsertHistoryShortDesc1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 1,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H')
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      
    # Prueba 6
    def test4InsertHistoryShortDesc11(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H'*11)
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 7
    def testInsertHistoryElementType2(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, 2,idFound, 1,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H3')
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H3')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 8
    def testInsertHistoryElementBakcLog2(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, 2,idFound, 2,1)
        self.assertFalse(result)
                
        # Eliminamos accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 9
    def testInsertHistoryElementCodBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 2,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 10
    def testInsertHistoryElementTypeBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 2*((2^31)-1),idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 11
    def testInsertHistoryElementBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 2,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
     
    # Casos Esquinas
       
    # Prueba 12
    def testinsertUserHistoryIdBackLogNoExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H1',0, 2,idFound, 3,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')

      
    # Prueba 13
    def testinsertUserHistoryLongDesc11AndIdBackLogNoExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2,idFound, 3,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 14
    def testinsertUserHistoryLongCod11AndIdBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 15
    def testinsertUserHistoryLongCod11AndTypeBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 16
    def testinsertUserHistory0Cod11AndTypeBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 17
    def testinsertUserHistoryLongCod11AndType0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 18
    def testinsertUserHistory0Cod11AndType0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 19
    def testinsertUserHistoryLongCod11AndType0AndBackLog0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 20
    def testinsertUserHistoryLongBackLog0AndType0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 21
    def testinsertUserHistoryLongCod0AndType0AndBackLog0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 0,idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 22
    def testinsertUserHistoryLongCodBigAndType0AndBackLog0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 0,idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 23
    def testinsertUserHistoryLongCodBigAndTypeBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
     
    # Prueba 24
    def testinsertUserHistoryLongCod1AndTypeBigAndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 25
    def testinsertUserHistoryLongCod1AndType1AndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 26
    def testinsertUserHistoryLongCod0AndType1AndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 1,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 27
    def testinsertUserHistoryLongCod1AndType1AndBackLog0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 28
    def testinsertUserHistoryLongCod1AndType0AndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 29
    def testinsertUserHistoryLongCod1AndType1AndBackLog1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 30
    def testinsertUserHistoryLongCod1AndType0AndBackLog1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
    
    # Prueba 31
    def testinsertUserHistoryLongCod11AndType0AndBackLog1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 
           
    # Prueba 32
    def testinsertUserHistoryLongCod11AndType0AndBackLog00(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 00,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')      
      
    # Prueba 33
    def testinsertUserHistoryLongCod11AndType1AndBackLog0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')    
      
    # Prueba 34
    def testinsertUserHistoryLongCod11AndType1AndBackLog1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
        self.assertTrue(result)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')     
     
    # Prueba 35
    def testinsertUserHistoryLongCod11AndTypeBigAndBackLog1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 36
    def testinsertUserHistoryLongCod11AndType1AndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 37
    def testinsertUserHistoryLongCod11AndType0AndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 38
    def testinsertUserHistoryLongCod11AndTypeBigAndBackLog0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
      
    # Prueba 39
    def testinsertUserHistoryLongCod11AndTypeBigAndBackLog11(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 11,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')    
      
    # Prueba 40
    def testinsertUserHistoryLongCod11AndTypeBigAndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')   
      
    # Prueba 41
    def testinsertUserHistoryLongCodBigAndTypeBigAndBackLogBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
      
      
      
    # Casos Maliciosos
      
    # Prueba 42
    def testinsertUserHistoryCodNotString(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(123,0, 1,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 43
    def testinsertUserHistoryCodNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(None,0, 1,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 44
    def testinsertUserHistoryTypeNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H2',0, None,idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')   
        
    # Prueba 45
    def testinsertUserHistoryBackLogNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, 1,idFound, None,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 46
    def testinsertUserHistoryTypeNoneBackLogNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, None,idFound, None,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
           
    # Prueba 47
    def testinsertUserHistoryCodeNoneTypeNoneBackLogNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(None,0, None,idFound, None,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')     
        
    # Prueba 48
    def testinsertUserHistoryTypeNoneBackLogString(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, None,idFound, '1',1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')    
        
    # Prueba 49
    def testinsertUserHistoryTypeStringBackLogNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, '1',idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 
           
    # Prueba 50
    def testinsertUserHistoryTypeArrayBackLogNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, [],idFound, 1,1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')        

         
         
    #############################################      
    #   Suite de Pruebas para searchUserHistory #
    #############################################
     
    #Casos Frontera
    
    # Prueba 51
    def testSearchHistoryExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H1')
        self.assertTrue(searchHist)
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 52
    def testSearchHistoryNotExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        aHist = userHistory()
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H1')
        self.assertEqual([],searchHist)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
         
    # Prueba 53
    def testSearchHistoryLong11(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11)
        self.assertNotEqual([],searchHist)
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
    # Prueba 54
    def testSearchHistoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound, 1,1)
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*((2^31)-1))
        self.assertEqual([],searchHist)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
      
     
    #Casos Malicia
     
    # Prueba 55
    def testSearchHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory(None,0, 1,idFound, 1,1)
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*((2^31)-1))
        self.assertEqual([],searchHist)
                
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  

         
         
    ######################################################      
    #       Suite de Pruebas para deleteUserHistory      #
    ###################################################### 
       
    # Caso Inicial
    
    # Prueba 56
    def testdeleteUserHistoryExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H1')
        self.assertTrue(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  

    # Prueba 57
    def testdeleteUserHistoryNotExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
               
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H1')
        self.assertFalse(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  

       
    # Casos Fronteras

    # Prueba 58
    def testdeleteUserHistoryLong11(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
        
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11)
        idFound1 = searchHist[0].id_userHistory
                
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H'*11)
        self.assertTrue(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  

    # Prueba 59
    def testdeleteUserHistoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound, 1,1)
                
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H'*((2^31)-1))
        self.assertFalse(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  

    # Casos Maliciosos
   
    # Prueba 60
    def testdeleteUserHistoryInvalid(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()

        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('')
        self.assertFalse(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 
        
    # Prueba 61
    def testdeleteUserHistoryNotString(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
                
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(12345)
        self.assertFalse(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 
        
    # Prueba 62  
    def test_44deleteUserHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
                
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(None)
        self.assertFalse(result)
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 