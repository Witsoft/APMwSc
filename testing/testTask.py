# -*- coding: utf-8 -*-. 
  
import unittest

from accionsDummy import *
from taskDummy import *
  
class TestHistory(unittest.TestCase):
      
#     #############################################      
#     #   Suite de Pruebas para insertTask    #
#     #############################################
#             
#     # Caso Inicial
#         
#     # Prueba 1
#     def testInserTaskExists(self):
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
#           
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#                     
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#     # Prueba 2
#  
#     def testInsertTaskElementNotExist(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('Tarea1',idFound1)
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#               
#     # Prueba 3
#     def testInsertTaskRepeatedElement(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.insertTask('Tarea1',idFound1)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#                    
#              
#     # Casos Fronteras
#           
#     # Prueba 4
#     def testInsertTaskShortDesc0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('',idFound1)
#         self.assertFalse(result)
#                  
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         aTarea = task()
#  
#         # Eliminamos accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#           
#     # Prueba 5
#     def testInsertTaskShortDesc1(self):
#          
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('T',idFound1)
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 6
#     def test4InsertTaskShortDesc140(self):
#        
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(140*'T',idFound1)
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#     # Prueba 7
#     def testInsertHistoryLong141(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(141*'T',idFound1)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#     # Prueba 8
#     def testInsertTaskId0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('Tarea1',0)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#  
#             
#     # Prueba 9
#     def testInsertTaskNoHistory(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('Tarea1',3)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba 10
#     def testInsertTaskLongId(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('Tarea1',2**31)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Casos Esquinas
#            
#     # Prueba 11
#     def testinsertTaskDescripcion1Id1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('T',idFound1)
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 12
#     def testInsertTask140Id1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(140*'A',idFound1)
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'A')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     # Prueba 13
#     def testInsertTask141NoId(self):
#                 # Insertamos Producto
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(141*'A',3)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#     # Prueba 14
#     def testInsertTask140NoId(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(140*'H',3)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 15
#     def testInserTask0Id1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('',idFound1)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 16
#     def testInserTaskDescription1Id0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('T',0)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#     # Prueba 17
#     def testInsertTaskDescription141Id0(self):    
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(141*'H',0)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 18
#     def testInsertTaskDescriptionE140Id1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(140*'T',idFound1)
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#  
#     # Casos Malicia
#  
#     # Prueba 19
#     def testInsertTaskDesc0Id0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('',0)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Prueba 20
#     def testInsertTaskDescNoneIdNone(self):
#                 # Insertamos Producto
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(None,None)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 21
#     def testInsertTaskNoneDescIdValid(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask(None,idFound1)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#             
#     # Prueba 22
#     def testInsertTaskDescNoneid(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result  = aTarea.insertTask('Tarea1',None)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#                          
#     #############################################      
#     #   Suite de Pruebas para getAllTask    #
#     #############################################
#          
#      #Casos Frontera
#      
#     # Prueba 
#     def testGetAllTaskExist(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         aTarea.getAllTask(idFound1)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#   
#     # Prueba 
#     def testGetAllTaskValid(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result = aTarea.getAllTask(idFound1)
#         self.assertNotEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#   
#     # Prueba 
#     def testGetAllTaskNoId(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result = aTarea.getAllTask(2)
#         self.assertEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')  
#          
#     # Prueba 
#     def testGetAllTaskNoTask(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         result = aTarea.getAllTask(idFound1)
#         self.assertEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
#  
#     # Prueba 
#     def testGetAllTaskMaxId(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result = aTarea.getAllTask(2**31)
#         self.assertEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#  
#     # Casos Malicia
#      
#     # Prueba 
#     def testGetAllTaskNone(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result = aTarea.getAllTask(None)
#         self.assertEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 
#     def testGetAllTaskid0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result = aTarea.getAllTask(0)
#         self.assertEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')      
#      
#     # Prueba 
#     def testGetAllTaskString(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result = aTarea.getAllTask("uno")
#         self.assertEqual(result,[])
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.') 
# 
#     #############################################      
#     #   Suite de Pruebas para updateTask    #
#     #############################################
#            
#     # Caso Inicial
#        
#     # Prueba 
#     def testUpdateTaskExists(self):
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
#          
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         aTarea.updateTask('Tarea1','Tarea2')
#                  
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea2')
#         aHist.deleteUserHistory('H1')
#         aAcc.deleteAccion('Cualquier cosa2')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#     # Prueba 2
# 
#     def testUpdateTaskElementNotExist(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea1','Tarea2')
#         self.assertTrue(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea2')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#                
#             
#     # Casos Fronteras
#          
#     # Prueba 
#     def testUpdateTaskShortDesc0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('','Tarea2')
#         self.assertFalse(result)
#                 
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         aTarea = task()
# 
#         # Eliminamos accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#          
#     # Prueba 
#     def testUpdateTaskShortDesc1(self):
#         
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea1','T')
#         self.assertTrue(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 
#     def testUpdateTaskShortDesc140(self):
#       
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea1',140*'T')
#         self.assertTrue(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#     # Prueba 7
#     def testUpdateHistoryLong141(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask(141*'T',idFound1)
#         result  = aTarea.updateTask(141*'T',140*'T')        
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#     # Prueba 
#     def testUpdateTaskNew0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea1','')        
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#            
#     # Prueba 
#     def testUpdateTaskNoDesc(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea','Tarea2')
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#    
#     # Prueba 
#     def testUpdateTaskLongNew(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea1',140*'T')
#         self.assertTrue(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Casos Esquinas
#           
#     # Prueba 
#     def testUpdateTaskNew1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)
#         result  = aTarea.updateTask('T','A')
#         self.assertTrue(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('A')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 
#     def testUpdateTaskNewDescLong0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask(140*'A',idFound1)
#         result  = aTarea.updateTask(140*'A','')
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'A')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     # Prueba 
#     def testUpdateTask141None(self):
#                 # Insertamos Producto
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask(140*'A',idFound1)
#         result  = aTarea.updateTask(140*'A',141*'T')
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'A')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#     # Prueba 
#     def testUpdateTask140None(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask(140*'H',idFound1)
#         result  = aTarea.updateTask(140*'H',None)
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'H')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 
#     def testUpdateTask0NewDesc1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('',idFound1)
#         result  = aTarea.updateTask('','T')
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 
#     def testUpdateTaskDesc1New0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)
#         result  = aTarea.updateTask('T','')        
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#     # Prueba 
#     def testUpdateTaskDesc141New0(self):    
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         result  = aTarea.updateTask(141*'T','')        
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba 
#     def testUpdateTaskDescE140New1(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask(140*'T',idFound1)
#         result  = aTarea.updateTask(140*'T','T')        
#         self.assertTrue(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     # Casos Malicia
# 
#     # Prueba 
#     def testUpdateTaskDesc0New0(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea',idFound1)
#         result  = aTarea.updateTask('','')
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#          
#     # Prueba 
#     def testUpdateTaskDescNoneNewNone(self):
#                 # Insertamos Producto
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask(None,None)
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Prueba
#     def testUpdateTaskNoneDescNewValid(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask(None,'Tarea2')
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')
#            
#     # Prueba 
#     def testUpdateTaskDescIntNew(self):
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
#         aHist.insertUserHistory('H2',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('H2')
#         idFound1 = searchHist[0].id_userHistory
#         
#         aTarea = task()
#         aTarea.insertTask('Tarea1',idFound1)
#         result  = aTarea.updateTask('Tarea1',1234)
#         self.assertFalse(result)
#         
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('Tarea1')
#         aHist.deleteUserHistory('H2')
#         aAcc.deleteAccion('Otra Accion')
#         aBackLog.deleteProduct('Taxi seguro.')

    #############################################      
    #   Suite de Pruebas para searchTask        #
    #############################################
           
    # Caso Inicial
       
    # Prueba
    def testSearchTask(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        aTarea.searchTask('Tarea1')
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTaskExists(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask('Tarea1')
        self.assertTrue(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTaskNotExists(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask('Tarea2')
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Casos Frontera
    
    # Prueba
    def testSearchTask1Exists(self):
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
          
        aTarea = task()
        aTarea.insertTask('T',idFound1)
        result = aTarea.searchTask('T')
        self.assertTrue(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
    
    # Prueba
    def testSearchTask140Exists(self):
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
          
        aTarea = task()
        aTarea.insertTask('T'*140,idFound1)
        result = aTarea.searchTask('T'*140)
        self.assertTrue(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTask0Exists(self):
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
          
        aTarea = task()
        aTarea.insertTask('',idFound1)
        result = aTarea.searchTask('')
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
    
    # Prueba
    def testSearchTask1NotExists(self):
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
          
        aTarea = task()
        aTarea.insertTask('T',idFound1)
        result = aTarea.searchTask('A')
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
    
    # Prueba
    def testSearchTask140NotExists(self):
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
          
        aTarea = task()
        aTarea.insertTask('T'*140,idFound1)
        result = aTarea.searchTask('A'*140)
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Casos Malicia
    
    # Prueba
    def testSearchTaskNone(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask(None)
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTaskStringSpace(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask(' ')
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTaskNotString(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask(88)
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTaskArray(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask([])
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
    
    # Prueba
    def testSearchTaskDisctionary(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask({})
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba
    def testSearchTaskStringLong(self):
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
          
        aTarea = task()
        aTarea.insertTask('Tarea1',idFound1)
        result = aTarea.searchTask('a'*((2^31)-1))
        self.assertFalse(result)
        
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('Tarea1')
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Cualquier cosa2')
        aBackLog.deleteProduct('Taxi seguro.')
        
        