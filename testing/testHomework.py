# -*- coding: utf-8 -*-. 
  
import unittest

from accionsDummy import *
from homeworkDummy import *
  
class TestHistory(unittest.TestCase):
      
    #############################################      
    #   Suite de Pruebas para insertHomework    #
    #############################################
           
    # Caso Inicial
       
    # Prueba 1
    def testInserHomeworkExists(self):
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
        aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        aTarea = homework()
        aTarea.insertHomework('Tarea1',idFound1)
                   
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 2
    # Insertando una historia en un idBacklog que no existe
    def testInsertHomeworkElementNotExist(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('Tarea1',idFound1)
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework('Tarea1')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
             
    # Prueba 3
    def testInsertHomeworkRepeatedElement(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        aTarea.insertHomework('Tarea1',idFound1)
        result  = aTarea.insertHomework('Tarea1',idFound1)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework('Tarea1')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
                  
            
    # Casos Fronteras
         
    # Prueba 4
    def testInsertHomeworkShortDesc0(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('',idFound1)
        self.assertFalse(result)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        aTarea = homework()

        # Eliminamos accion y producto
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
         
    # Prueba 5
    def testInsertHomeworkShortDesc1(self):
        
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('T',idFound1)
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework('T')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
         
    # Prueba 6
    def test4InsertHomeworkShortDesc140(self):
      
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework(140*'T',idFound1)
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework(140*'T')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 7
    def testInsertHistoryLong141(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework(141*'T',idFound1)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 8
    def testInsertHomeworkId0(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('Tarea1',0)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')

           
    # Prueba 9
    def testInsertHomeworkNoHistory(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('Tarea1',3)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
   
    # Prueba 10
    def testInsertHomeworkLongId(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('Tarea1',2**31)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Casos Esquinas
          
    # Prueba 11
    def testinsertHomeworkDescripcion1Id1(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('T',idFound1)
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework('T')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
         
    # Prueba 12
    def testInsertHomework140Id1(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework(140*'A',idFound1)
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework(140*'A')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
   
    # Prueba 14
    def testInsertUserHistoryLongCod11AndIdBackLogBig(self):
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
        searchHist = aHist.searchUserHistory('H2')
        idFound1 = searchHist[0].id_userHistory
        
        aTarea = homework()
        result  = aTarea.insertHomework('Tarea1',idFound1)
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aTarea.deleteHomework('Tarea1')
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
'''           
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
         
#     # Prueba 16
#     def testinsertUserHistory0Cod11AndTypeBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 17
#     def testinsertUserHistoryLongCod11AndType0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 18
#     def testinsertUserHistory0Cod11AndType0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 19
#     def testinsertUserHistoryLongCod11AndType0AndBackLog0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 0,idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 20
#     def testinsertUserHistoryLongBackLog0AndType0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 0,idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 21
#     def testinsertUserHistoryLongCod0AndType0AndBackLog0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('',0, 0,idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 22
#     def testinsertUserHistoryLongCodBigAndType0AndBackLog0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*((2^31)-1),0, 0,idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 23
#     def testinsertUserHistoryLongCodBigAndTypeBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#        
#     # Prueba 24
#     def testinsertUserHistoryLongCod1AndTypeBigAndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 25
#     def testinsertUserHistoryLongCod1AndType1AndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 1,idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 26
#     def testinsertUserHistoryLongCod0AndType1AndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('',0, 1,idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 27
#     def testinsertUserHistoryLongCod1AndType1AndBackLog0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 1,idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#              
#     # Prueba 28
#     def testinsertUserHistoryLongCod1AndType0AndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 0,idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 29
#     def testinsertUserHistoryLongCod1AndType1AndBackLog1(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 30
#     def testinsertUserHistoryLongCod1AndType0AndBackLog1(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H',0, 0,idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#       
#     # Prueba 31
#     def testinsertUserHistoryLongCod11AndType0AndBackLog1(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 0,idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#              
#     # Prueba 32
#     def testinsertUserHistoryLongCod11AndType0AndBackLog00(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 0,idFound, 00,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')      
#         
#     # Prueba 33
#     def testinsertUserHistoryLongCod11AndType1AndBackLog0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1,idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')    
#         
#     # Prueba 34
#     def testinsertUserHistoryLongCod11AndType1AndBackLog1(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
#         self.assertTrue(result)
#                   
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H'*11)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')     
#        
#     # Prueba 35
#     def testinsertUserHistoryLongCod11AndTypeBigAndBackLog1(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 36
#     def testinsertUserHistoryLongCod11AndType1AndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 37
#     def testinsertUserHistoryLongCod11AndType0AndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 0,idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 38
#     def testinsertUserHistoryLongCod11AndTypeBigAndBackLog0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 0,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#         
#     # Prueba 39
#     def testinsertUserHistoryLongCod11AndTypeBigAndBackLog11(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 11,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')    
#         
#     # Prueba 40
#     def testinsertUserHistoryLongCod11AndTypeBigAndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')   
#         
#     # Prueba 41
#     def testinsertUserHistoryLongCodBigAndTypeBigAndBackLogBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 1*((2^31)-1),1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#         
#         
#         
#     # Casos Maliciosos
#         
#     # Prueba 42
#     def testinsertUserHistoryCodNotString(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory(123,0, 1,idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 43
#     def testinsertUserHistoryCodNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory(None,0, 1,idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 44
#     def testinsertUserHistoryTypeNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H2',0, None,idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')   
#           
#     # Prueba 45
#     def testinsertUserHistoryBackLogNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H3',0, 1,idFound, None,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 46
#     def testinsertUserHistoryTypeNoneBackLogNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H3',0, None,idFound, None,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#              
#     # Prueba 47
#     def testinsertUserHistoryCodeNoneTypeNoneBackLogNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory(None,0, None,idFound, None,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')     
#           
#     # Prueba 48
#     def testinsertUserHistoryTypeNoneBackLogString(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H3',0, None,idFound, '1',1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')    
#           
#     # Prueba 49
#     def testinsertUserHistoryTypeStringBackLogNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H3',0, '1',idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#              
#     # Prueba 50
#     def testinsertUserHistoryTypeArrayBackLogNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         result = aHist.insertUserHistory('H3',0, [],idFound, 1,1)
#         self.assertFalse(result)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')        
#   
#            
#            
#     #############################################      
#     #   Suite de Pruebas para searchUserHistory #
#     #############################################
#        
#     #Casos Frontera
#       
#     # Prueba 51
#     def testSearchHistoryExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H1')
#         self.assertTrue(searchHist)
#         idFound1 = searchHist[0].id_userHistory
#                   
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 52
#     def testSearchHistoryNotExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         aHist = userHistory()
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H1')
#         self.assertEqual([],searchHist)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#            
#     # Prueba 53
#     def testSearchHistoryLong11(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H'*11)
#         self.assertNotEqual([],searchHist)
#         idFound1 = searchHist[0].id_userHistory
#                   
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H'*11)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#           
#     # Prueba 54
#     def testSearchHistoryBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound, 1,1)
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H'*((2^31)-1))
#         self.assertEqual([],searchHist)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#         
#        
#     #Casos Malicia
#        
#     # Prueba 55
#     def testSearchHistoryNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory(None,0, 1,idFound, 1,1)
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H'*((2^31)-1))
#         self.assertEqual([],searchHist)
#                   
#         # Eliminamos historia, accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#   
#            
#            
#     ######################################################      
#     #       Suite de Pruebas para deleteUserHistory      #
#     ###################################################### 
#          
#     # Caso Inicial
#       
#     # Prueba 56
#     def testdeleteUserHistoryExists(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#                   
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory('H1')
#         self.assertTrue(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#   
#     # Prueba 57
#     def testdeleteUserHistoryNotExists(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#                  
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory('H1')
#         self.assertFalse(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#   
#          
#     # Casos Fronteras
#   
#     # Prueba 58
#     def testdeleteUserHistoryLong11(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H'*11,0, 1,idFound, 1,1)
#           
#         # Buscamos el codigo de la historia
#         searchHist = aHist.searchUserHistory('H'*11)
#         idFound1 = searchHist[0].id_userHistory
#                   
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory('H'*11)
#         self.assertTrue(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#   
#     # Prueba 59
#     def testdeleteUserHistoryBig(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound, 1,1)
#                   
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory('H'*((2^31)-1))
#         self.assertFalse(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#   
#     # Casos Maliciosos
#      
#     # Prueba 60
#     def testdeleteUserHistoryInvalid(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#   
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory('')
#         self.assertFalse(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#           
#     # Prueba 61
#     def testdeleteUserHistoryNotString(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#                   
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory(12345)
#         self.assertFalse(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#           
#     # Prueba 62  
#     def testdeleteUserHistoryNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#           
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa')
#         idFound = search[0].idaccion
#           
#         # Insertamos la historia
#         aHist = userHistory()
#                   
#         # Eliminamos historia, accion y producto
#         result = aHist.deleteUserHistory(None)
#         self.assertFalse(result)
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#           
#     ######################################################      
#     #       Suite de Pruebas para scaleType              #
#     ######################################################
#      
#     # Casos Frontera
#      
#     # Prueba 63
#     def testScaleTypeExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         aHist.scaleType(idFound1)
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#      
#     # Prueba 64    
#     def testScaleType(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.scaleType(idFound1)
#         # Eliminamos historia, accion y producto
#         self.assertNotEqual(result,None)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#       
#     # Prueba 65  
#     def testScaleTypeNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.scaleType(2)
#         # Eliminamos historia, accion y producto
#         self.assertEqual(result,None)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 66
#     def testScale2History(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         aAcc.insertAccion('Cualquier cosa3',1)
#         search = aAcc.searchAccion('Cualquier cosa3')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,2, 1,1)
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,2)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.scaleType(idFound1)
#         # Eliminamos historia, accion y producto
#         self.assertNotEqual(result,None)
#         aHist.deleteUserHistory('H1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aAcc.deleteAccion('Cualquier cosa3')
#         aBackLog.deleteProduct('Taxi seguro.')
#  
#     # Prueba 67
#     def testScaleTypeNoParam(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.scaleType(None)
#         # Eliminamos historia, accion y producto
#         self.assertEqual(result,None)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 68   
#     def testScaleType0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.scaleType(0)
#         # Eliminamos historia, accion y producto
#         self.assertEqual(result,None)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#       
#     # Prueba 69  
#     def testScaleTypeNoHistory(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.scaleType(2)
#         # Eliminamos historia, accion y producto
#         self.assertEqual(result,None)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#  
#     ######################################################      
#     #       Suite de Pruebas para updatePriority         #
#     ######################################################
#      
#     # Casos Frontera 
#     
#     # Prueba 
#     def testUpdatePriorityExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         aHist.updatePriority(idFound,1)
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#  
#     # Prueba
#     def testUpdatePriorityTrue(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound,1)
#         # Eliminamos historia, accion y producto
#         self.assertTrue(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba
#     def testUpdatePriorityNoIdFound(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(2,1)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba
#     def testUpdatePriority0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound1,0)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba     
#     def testUpdatePriority20(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound1,20)
#         # Eliminamos historia, accion y producto
#         self.assertTrue(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba
#     def testUpdatePriority21(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound1,21)
#         # Eliminamos historia, accion y producto
#         self.assertTrue(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba   
#     def testUpdatePriorityId0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(0,1)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     # Casos Esquina
#  
#     # Prueba
#     def testUpdatePriority11(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound1,1)
#         # Eliminamos historia, accion y producto
#         self.assertTrue(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     def testUpdatePriority020(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(0,20)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     def testUpdatePriority121(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound1,21)
#         # Eliminamos historia, accion y producto
#         self.assertTrue(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Casos Malicia
#     
#     # Prueba   
#     def testUpdatePriorityNoneHistory(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(None,20)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba    
#     def testUpdatePriorityNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(idFound1,None)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba    
#     def testUpdatePriorityNoParam(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H1')
#         idFound1 = searchHist[0].id_userHistory
#         result = aHist.updatePriority(None,None)
#         # Eliminamos historia, accion y producto
#         self.assertFalse(result)
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')  
#         
#     # ###########################################     
#     #      Suite de Pruebas para succesors      #
#     ############################################# 
#       
#     # Prueba 63
#     def testExistsSuccesors(self):
#        # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia
#         aHist  = userHistory()
#         result = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.succesors(1)
#                  
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
# 
#     # Prueba 65
#     def testNoExistsSuccesors(self):         
#         # Insertamos la historia
#         aHist  = userHistory()        
#         result = aHist.succesors(1)
#         self.assertFalse(result)
#                  
#         # Eliminamos la historia
#         aHist.deleteUserHistory('H1')
#         
#         
#     # Casos Frontera        
#     
#     def testSuccesorsIdZero(self):
#        # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#          
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#          
#         # Insertamos la historia 1
#         aHist  = userHistory()
#         result = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         
#         # Insertamos la historia 2
#         aHist  = userHistory()
#         result = aHist.insertUserHistory('H2',1, 1,idFound, 1,1)
#         
#         # Insertamos la historia 3
#         aHist  = userHistory()
#         result = aHist.insertUserHistory('H3',1, 1,idFound, 1,1)
#         
#         result = aHist.succesors(0)
#         self.assertEqual(result,[])
#                  
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')     
#         
#     ######################################################      
#     #       Suite de Pruebas para getAllUserHistoryId    #
#     ###################################################### 
#        
#     # Caso Inicial
#     
#     # Prueba 63
#     def test_getAllUserHistoryIdNormal(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId(1)
#         self.assertNotEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 64
#     def test_getAllUserHistoryIdNotExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId(2)
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Casos Frontera
#     
#     # Prueba 65
#     def test_getAllUserHistoryId0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId(0)
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')   
#         
#     # Prueba 66
#     def test_getAllUserHistoryIdMaxNumber(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId((2^31)-1)
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')     
#     
#     # Casos Malicia
#     
#     # Prueba 67
#     def test_getAllUserHistoryIdNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId(None)
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')      
#         
#     # Prueba 68
#     def test_getAllUserHistoryIdNegativeNumber(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId(-1)
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')    
#         
#     # Prueba 69
#     def test_getAllUserHistoryIdString(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId('1')
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')       
#         
#     # Prueba 70
#     def test_getAllUserHistoryIdArray(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         aHist = userHistory()
#         temp = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         result = aHist.getAllUserHistoryId([])
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     ######################################################      
#     #       Suite de Pruebas para isEpic                 #
#     ###################################################### 
#        
#     # Caso Inicial
#     
#     # Prueba 71
#     def testExistsIsEpic(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic(idHist)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 72
#     def testExistsIsEpicExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic(idHist)
#         self.assertTrue(idHist)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 73
#     def testExistsIsEpicNotExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic(2)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Casos Frontera
#     
#     # Prueba 74
#     def testExistsIsEpic0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic(0)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 75
#     def testExistsIsEpicMaxInt(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic((2^31)-1)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')    
#         
#     # Casos Malicia
#     
#     # Prueba 76
#     def testExistsIsEpicNegativeNumber(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic(-1)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')  
#     
#     # Prueba 77
#     def testExistsIsEpicNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic(None)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')    
#     
#     # Prueba 78
#     def testExistsIsEpicString(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.isEpic('1')
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#         ######################################################      
#     #       Suite de Pruebas para historySuccesors       #
#     ###################################################### 
#        
#     # Caso Inicial
#     
#     # Caso 79
#     def testhistorySuccesors(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors(1)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Casos Normal
#     
#     # Caso 80
#     def testhistorySuccesorsExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors(idHist)
#         self.assertEqual(result,[])
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 81
#     def testhistorySuccesorsNotExist(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors(idHist)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Casos Frontera
#     
#     # Prueba 82
#     def testhistorySuccesors0(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors(0)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 83
#     def testhistorySuccesorsMaxInt(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors((2^31)-1)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')    
#         
#     # Casos Malicia
#     
#     # Prueba 84
#     def testhistorySuccesorsNegativeNumber(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors(-1)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')  
#     
#     # Prueba 85
#     def testhistorySuccesorsNone(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors(None)
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')    
#     
#     # Prueba 86
#     def testhistorySuccesorsString(self):
#         # Insertamos Producto
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Descripcion',1)
#         
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Cualquier cosa2',1)
#         search  = aAcc.searchAccion('Cualquier cosa2')
#         idFound = search[0].idaccion
#         
#         # Insertamos la historia
#         aHist  = userHistory()
#         temp   = aHist.insertUserHistory('H1',0, 1,idFound, 1,1)
#         hist   = aHist.searchUserHistory('H1')
#         idHist = hist[0].id_userHistory
#         result = aHist.historySuccesors('1')
#         self.assertFalse(result)
#                 
#         # Eliminamos producto
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
'''