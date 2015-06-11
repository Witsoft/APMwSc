# # -*- coding: utf-8 -*-. 
 
import sys
import unittest
 
# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')
 
from accions     import *
from objective   import *
from userHistory import *
 
class TestHistory(unittest.TestCase):
      
    #############################################      
    #   Suite de Pruebas para insertUserHistory #
    #############################################
           
    # Caso Inicial
       
    # Prueba 1
    def testInserHistoryExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H1',0,1,idFound,idBacklog,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 2
    # Insertando una historia en un idBacklog que no existe
    def testInsertHistoryElementNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H2',0, 1,idFound, idBacklog,1)
        result = searchHist = aHist.searchUserHistory('H2')
        self.assertTrue(result)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 3
    def testInsertHistoryRepeatedElement(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H2',0,1,idFound,idBacklog,1)
        result1 = aHist.insertUserHistory('H2',0,1,idFound,2,1)
        self.assertFalse(result1)
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                        
    # Casos Fronteras
         
    # Prueba 4
    def test4InsertHistoryShortDesc0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 1,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 5
    def test4InsertHistoryShortDesc1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound,idBacklog,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H')
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H')
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 6
    def test4InsertHistoryShortDesc11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0,1,idFound,idBacklog,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H'*11)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 7
    def testInsertHistoryElementType2(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0,2,idFound,idBacklog,1)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H3')
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H3')
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 8
    def testInsertHistoryElementBakcLog2(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, 2,idFound, 2,1)
        self.assertFalse(result)
                   
        # Eliminamos accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 9
    def testInsertHistoryElementCodBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 2,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 10
    def testInsertHistoryElementTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 2*((2^31)-1),idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 11
    def testInsertHistoryElementBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 2,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Casos Esquinas
          
    # Prueba 12
    def testinsertUserHistoryIdBacklogNoExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H1',0, 2,idFound, 3,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 13
    def testinsertUserHistoryLongDesc11AndIdBacklogNoExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2,idFound, 3,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 14
    def testinsertUserHistoryLongCod11AndIdBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 15
    def testinsertUserHistoryLongCod11AndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 16
    def testinsertUserHistory0Cod11AndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 17
    def testinsertUserHistoryLongCod11AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 18
    def testinsertUserHistory0Cod11AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 19
    def testinsertUserHistoryLongCod11AndType0AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 20
    def testinsertUserHistoryLongBacklog0AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 21
    def testinsertUserHistoryLongCod0AndType0AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 0,idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 22
    def testinsertUserHistoryLongCodBigAndType0AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 0,idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 23
    def testinsertUserHistoryLongCodBigAndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 24
    def testinsertUserHistoryLongCod1AndTypeBigAndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 25
    def testinsertUserHistoryLongCod1AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 26
    def testinsertUserHistoryLongCod0AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 1,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 27
    def testinsertUserHistoryLongCod1AndType1AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
              
    # Prueba 28
    def testinsertUserHistoryLongCod1AndType0AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 29
    def testinsertUserHistoryLongCod1AndType1AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 30
    def testinsertUserHistoryLongCod1AndType0AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 31
    def testinsertUserHistoryLongCod11AndType0AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
              
    # Prueba 32
    def testinsertUserHistoryLongCod11AndType0AndBacklog00(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound,0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')      
         
    # Prueba 33
    def testinsertUserHistoryLongCod11AndType1AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Prueba 34
    def testinsertUserHistoryLongCod11AndType1AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
        
    # Prueba 35
    def testinsertUserHistoryLongCod11AndTypeBigAndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 36
    def testinsertUserHistoryLongCod11AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 37
    def testinsertUserHistoryLongCod11AndType0AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 38
    def testinsertUserHistoryLongCod11AndTypeBigAndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 0,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
         
    # Prueba 39
    def testinsertUserHistoryLongCod11AndTypeBigAndBacklog11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 11,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Prueba 40
    def testinsertUserHistoryLongCod11AndTypeBigAndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
         
    # Prueba 41
    def testinsertUserHistoryLongCodBigAndTypeBigAndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
                 
    # Casos Maliciosos
         
    # Prueba 42
    def testinsertUserHistoryCodNotString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(123,0, 1,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 43
    def testinsertUserHistoryCodNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(None,0, 1,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 44
    def testinsertUserHistoryTypeNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H2',0, None,idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
           
    # Prueba 45
    def testinsertUserHistoryBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, 1,idFound, None,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 46
    def testinsertUserHistoryTypeNoneBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, None,idFound, None,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
              
    # Prueba 47
    def testinsertUserHistoryCodeNoneTypeNoneBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(None,0, None,idFound, None,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
           
    # Prueba 48
    def testinsertUserHistoryTypeNoneBacklogString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, None,idFound, '1',1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
           
    # Prueba 49
    def testinsertUserHistoryTypeStringBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, '1',idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
              
    # Prueba 50
    def testinsertUserHistoryTypeArrayBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H3',0, [],idFound,idBacklog,1)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')        
              
    #############################################      
    #   Suite de Pruebas para searchUserHistory #
    #############################################
        
    #Casos Frontera
       
    # Prueba 51
    def testSearchHistoryExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H1')
        self.assertTrue(searchHist)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 52
    def testSearchHistoryNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        aHist = userHistory()
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H1')
        self.assertEqual([],searchHist)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
            
    # Prueba 53
    def testSearchHistoryLong11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11)
        self.assertNotEqual([],searchHist)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 54
    def testSearchHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound,idBacklog,1)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*((2^31)-1))
        self.assertEqual([],searchHist)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
                
    #Casos Malicia
        
    # Prueba 55
    def testSearchHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory(None,0, 1,idFound,idBacklog,1)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*((2^31)-1))
        self.assertEqual([],searchHist)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
              
    ######################################################      
    #       Suite de Pruebas para deleteUserHistory      #
    ###################################################### 
          
    # Caso Inicial
       
    # Prueba 56
    def testdeleteUserHistoryExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H1')
        self.assertTrue(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Prueba 57
    def testdeleteUserHistoryNotExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
                  
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H1')
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
            
    # Casos Fronteras
   
    # Prueba 58
    def testdeleteUserHistoryLong11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H'*11)
        self.assertTrue(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Prueba 59
    def testdeleteUserHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound,idBacklog,1)
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('H'*((2^31)-1))
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Casos Maliciosos
      
    # Prueba 60
    def testdeleteUserHistoryInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('')
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
           
    # Prueba 61
    def testdeleteUserHistoryNotString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(12345)
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
           
    # Prueba 62  
    def testdeleteUserHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(None)
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry Ycczxn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
           
    ######################################################      
    #       Suite de Pruebas para scaleType              #
    ######################################################
      
    # Casos Frontera
      
    # Prueba 63
    def testScaleTypeExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        aHist.scaleType(idFound1)
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
      
    # Prueba 64    
    def testScaleType(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.scaleType(idFound1)
        # Eliminamos historia, accion y producto
        self.assertNotEqual(result,None)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 65  
    def testScaleTypeNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.scaleType(2)
        # Eliminamos historia, accion y producto
        self.assertEqual(result,None)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
          
    # Prueba 66
    def testScale2History(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        aAcc.insertAccion('Cualquier cosa3',idBacklog)
        search = aAcc.searchAccion('Cualquier cosa3',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,2,idBacklog,1)
        aHist.insertUserHistory('H2',0, 1,idFound,idBacklog,2)
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.scaleType(idFound1)
        # Eliminamos historia, accion y producto
        self.assertNotEqual(result,None)
        aHist.deleteUserHistory('H1')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aAcc.deleteAccion('Cualquier cosa3',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
  
    # Prueba 67
    def testScaleTypeNoParam(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.scaleType(None)
        # Eliminamos historia, accion y producto
        self.assertEqual(result,None)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
          
    # Prueba 68   
    def testScaleType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.scaleType(0)
        # Eliminamos historia, accion y producto
        self.assertEqual(result,None)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 69  
    def testScaleTypeNoHistory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.scaleType(2)
        # Eliminamos historia, accion y producto
        self.assertEqual(result,None)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
  
    ######################################################      
    #       Suite de Pruebas para updatePriority         #
    ######################################################
      
    # Casos Frontera 
     
    # Prueba 70
    def testUpdatePriorityExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        aHist.updatePriority(idFound,1)
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
  
    # Prueba 71
    def testUpdatePriorityTrue(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound,1)
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 72
    def testUpdatePriorityNoIdFound(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(2,1)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 73
    def testUpdatePriority0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,0)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 74     
    def testUpdatePriority20(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,20)
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 75
    def testUpdatePriority21(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,21)
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 76   
    def testUpdatePriorityId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(0,1)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Casos Esquina
  
    # Prueba 77
    def testUpdatePriority11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,1)
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 78        
    def testUpdatePriority020(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(0,20)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 79        
    def testUpdatePriority121(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,21)
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Casos Malicia
     
    # Prueba 80   
    def testUpdatePriorityNoneHistory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(None,20)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 81    
    def testUpdatePriorityNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,None)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 82    
    def testUpdatePriorityNoParam(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(None,None)
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
         
    # ###########################################     
    #      Suite de Pruebas para succesors      #
    ############################################# 
       
    # Prueba 83
    def testExistsSuccesors(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist  = userHistory()
        result = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.succesors(1)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 84
    def testNoExistsSuccesors(self):         
        # Insertamos la historia
        aHist  = userHistory()        
        result = aHist.succesors(1)
        self.assertFalse(result)
                  
        # Eliminamos la historia
        aHist.deleteUserHistory('H1')
         
         
    # Casos Frontera        
    # Prueba 85    
    def testSuccesorsIdZero(self):
       # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Dsjsdn',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia 1
        aHist  = userHistory()
        result = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
         
        # Insertamos la historia 2
        aHist  = userHistory()
        result = aHist.insertUserHistory('H2',1, 1,idFound,idBacklog,1)
         
        # Insertamos la historia 3
        aHist  = userHistory()
        result = aHist.insertUserHistory('H3',1, 1,idFound,idBacklog,1)
         
        result = aHist.succesors(0)
        self.assertEqual(result,[])
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
         
    ######################################################      
    #       Suite de Pruebas para getAllUserHistoryId    #
    ###################################################### 
        
    # Caso Inicial
     
    # Prueba 86
    def test_getAllUserHistoryIdNormal(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId(1)
        self.assertNotEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 87
    def test_getAllUserHistoryIdNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId(2)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Frontera
     
    # Prueba 88
    def test_getAllUserHistoryId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId(0)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
         
    # Prueba 89
    def test_getAllUserHistoryIdMaxNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId((2^31)-1)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
     
    # Casos Malicia
     
    # Prueba 90
    def test_getAllUserHistoryIdNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId(None)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')      
         
    # Prueba 91
    def test_getAllUserHistoryIdNegativeNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId(-1)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Prueba 92
    def test_getAllUserHistoryIdString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId('1')
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')       
         
    # Prueba 93
    def test_getAllUserHistoryIdArray(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        result = aHist.getAllUserHistoryId([])
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    ######################################################      
    #       Suite de Pruebas para isEpic                 #
    ###################################################### 
        
    # Caso Inicial
     
    # Prueba 94
    def testExistsIsEpic(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(idHist)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 95
    def testExistsIsEpicExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(idHist)
        self.assertTrue(idHist)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 96
    def testExistsIsEpicNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(2)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Frontera
     
    # Prueba 97
    def testExistsIsEpic0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(0)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 98
    def testExistsIsEpicMaxInt(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic((2^31)-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Casos Malicia
     
    # Prueba 99
    def testExistsIsEpicNegativeNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
     
    # Prueba 100
    def testExistsIsEpicNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(None)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
     
    # Prueba 101
    def testExistsIsEpicString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic('1')
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    ######################################################      
    #       Suite de Pruebas para historySuccesors       #
    ###################################################### 
        
    # Caso Inicial
     
    # Prueba 102
    def testhistorySuccesors(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(1)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Normal
     
    # Prueba 103
    def testhistorySuccesorsExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(idHist)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 104
    def testhistorySuccesorsNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(idHist)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Frontera
     
    # Prueba 105
    def testhistorySuccesors0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(0)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 106
    def testhistorySuccesorsMaxInt(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors((2^31)-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Casos Malicia
     
    # Prueba 107
    def testhistorySuccesorsNegativeNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
     
    # Prueba 108
    def testhistorySuccesorsNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(None)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
     
    # Prueba 109
    def testhistorySuccesorsString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('H1',0, 1,idFound,idBacklog,1)
        hist   = aHist.searchUserHistory('H1')
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors('1')
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    #########################################################      
    #   Suite de Pruebas para searchidUserHistoryIdAccion   #
    #########################################################     
      
    # Caso Inicial 
       
    # Prueba 110
      
    def testSearchidUserHistoryIdAccion(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
  
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory
          
        # Buscamos id's de historias que contengan asociado una acción por su id
        aHist.searchidUserHistoryIdAccion(idFound) 
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Casos Frontera

    # Prueba 111
     
    def testSearchidUserHistoryIdAccionNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
  
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
                
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(0) 
        self.assertEqual(None,res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Prueba 112
     
    def testSearchidUserHistoryIdAccionOne(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory
         
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(1) 
        self.assertNotEqual(None,res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
               
    # Prueba 113
     
    def testSearchidUserHistoryIdAccionBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory        
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(2**28) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Casos Malicia
     
    # Prueba 114
     
    def testSearchidUserHistoryIdAccionString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion('Patricia') 
        self.assertEqual(None,res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Prueba 115
     
    def testSearchidUserHistoryIdAccionInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(-9898989898) 
        self.assertEqual(None,res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Prueba 116
     
    def testSearchidUserHistoryIdAccionNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1)
        searchHist = aHist.searchUserHistory('lllzz')
        idFound1 = searchHist[0].UH_idUserHistory
 
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
             
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(None) 
        self.assertEqual(None,res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('lllzz')
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')     
             