# -*- coding: utf-8 -*-. 
 
import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog                import *
from actorsUserHistory      import *
from userHistory            import *
from accions                import *   
from model                  import *  
from task                   import *
from category               import *

class TestTask(unittest.TestCase):
       
#     #############################################      
#     #      Suite de Pruebas para insertTask     #
#     #############################################
#               
#     # Caso Inicial
#           
#     # Prueba 1
#     def testInserTaskExists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#     
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',idFound0)
#         search = aAcc.searchAccion('cinrohbwidia',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)
#         
#         # Insertamos la tarea    
#         aTarea = task()
#         aTarea.insertTask('dwidjw',1,1,idFound1)
#                       
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#     # Prueba 2
#     
#     def testInsertTaskElementNotExist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#                
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra Accion',idFound0)
#         search = aAcc.searchAccion('Otra Accion',idFound0)
#         idFound = search[0].AC_idAccion
#                
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#          
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)
#          
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,1,idFound1)
#         self.assertTrue(result)
#                        
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#                 
#     # Prueba 3
#     def testInsertTaskRepeatedElement(self):
#          # Insertamos Producto
#          aBacklog = backlog()
#          aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#          searchBacklog = aBacklog.findName('Podn fjdd.')
#          idFound0 = searchBacklog[0].BL_idBacklog
#                
#          # Insertamos la accion
#          aAcc = accions()
#          aAcc.insertAccion('Otra cosa',idFound0)
#          search = aAcc.searchAccion('Otra cosa',idFound0)
#          idFound = search[0].AC_idAccion
#                
#          # Insertamos la historia
#          aHist = userHistory()
#          aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#          searchHist = aHist.searchUserHistory('hIDBW')
#          idFound1 = searchHist[0].UH_idUserHistory 
#          
#          # Insertamos la categoria
#          aCategory = category()
#          aCategory.insertCategory('wofhweoifh',5)
#          
#          # Insertamos la tarea    
#          aTarea = task()
#          aTarea.insertTask('dwidjw',1,1,idFound1)
#          result = aTarea.insertTask('dwidjw',1,1,idFound1)
#          self.assertFalse(result)
#    
#          # Eliminamos la tarea, categoria, historia, accion y producto
#          aTarea.deleteTask('dwidjw')
#          aCategory.deleteCategory('wofhweoifh')
#          aHist.deleteUserHistory('hIDBW')
#          aAcc.deleteAccion('Otra cosa', idFound0)
#          aBacklog.deleteProduct('Podn fjdd.')
#                       
#                 
#     # Casos Fronteras
#              
#     # Prueba 4
#     def testInsertTaskShortDesc0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea   
#         aTarea = task()
#         result = aTarea.insertTask('', 1, 1,idFound1)
#         self.assertFalse(result)
#                    
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aCategory.deleteCategory('wofhweoifh')                           
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#               
#     # Prueba 5
#     def testInsertTaskShortDesc1(self):
#            
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('T', 1, 1, idFound1)
#         self.assertTrue(result)
#            
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask('T')
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 6
#     def test4InsertTaskShortDesc140(self):
#          
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask(140*'T',1,1,idFound1)
#         self.assertTrue(result)
# 
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#     # Prueba 7
#     def testInsertHistoryLong141(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask(141*'T',1,1,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')        
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#     # Prueba 8
#     def testInsertTaskId0(self):
#         # Insertamos Producto    
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,1,0)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#     # Prueba 9
#     def testInsertTaskNoHistory(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,1,3)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#       
#     # Prueba 10
#     def testInsertTaskLongId(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,1,2**31)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
#     # Prueba 
#     def testInsertTaskIdCategory0(self):
#         # Insertamos Producto    
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',0,1,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#     # Prueba
#     def testInsertTaskNoCategory(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',100,1,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#       
#     # Prueba 
#     def testInsertTaskLongIdCategory(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',2**31,1,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')        
# 
#     # Prueba 
#     def testInsertTaskWeight0(self):
#         # Insertamos Producto    
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,0,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#               
#     # Prueba 
#     def testInsertTaskNegativeWeight(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,-1,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#       
#     # Prueba
#     def testInsertTaskLongWeight(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#               
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#               
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',5)
# 
#         # Insertamos la tarea    
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,2**31,idFound1)
#         self.assertTrue(result)
# 
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')        
#            
#     # Casos Esquinas
#             
#     # Prueba
#     def testinsertTaskODJdbeidbww1Id1(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('T',1,1,idFound1)
#         self.assertTrue(result)
# 
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask('T')
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#            
#     # Prueba 
#     def testInsertTask140Id1(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(140*'A',1,1,idFound1)
#         self.assertTrue(result)
#            
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask(140*'A')
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#      
#     # Prueba 
#     def testInsertTask141NoId(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result  = aTarea.insertTask(141*'A',1,1,3)
#         self.assertFalse(result)        
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#              
#     # Prueba 
#     def testInsertTask140NoId(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(140*'H',1,1,3)
#         self.assertFalse(result)        
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#            
#     # Prueba 
#     def testInserTask0Id1(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('',1,1,idFound1)
#         self.assertFalse(result)        
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#            
#     # Prueba 
#     def testInserTaskDescription1Id0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('T',1,1,0)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#              
#     # Prueba 
#     def testInsertTaskDescription141Id0(self):    
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(141*'H',1,1,0)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testInsertTaskDescriptionE140Id1(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result  = aTarea.insertTask(140*'T',1,1,idFound1)
#         self.assertTrue(result)
#            
#         # Eliminamos la tarea, categoria, historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aCategory.deleteCategory('wofhweoifh')
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
#     # Prueba
#     def testinsertTaskDesc1IdCWeightIdHBig(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('T',2**31,2**31,2**31)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')     
# 
#     # Prueba
#     def testinsertTaskDesc140IdCWeightIdHBig(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(140*'T',2**31,2**31,2**31)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')     
# 
#         # Prueba
#     def testinsertTaskDesc1IdC0Weight0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('T',0,0,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')  
# 
#     # Prueba
#     def testinsertTaskDesc0IdCWeightIdH0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('',2**31,2**31,0)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')             
#   
#         # Prueba
#     def testinsertTaskDesc0IdCBigWeightNegativeIdHValid(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('T',2**31,-1,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
#     # Prueba
#     def testinsertTaskDesc140IdC1Weight0IdH0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(140*'T',1,0,0)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
#     # Prueba
#     def testinsertTaskDesc0IdC1WeightBigIdHValid(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('',1,2**31,idFound1)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
# 
#     # Prueba
#     def testinsertTaskDesc140IdCBigWeight1IdH0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(140*'T',2**31,1,0)
#         self.assertFalse(result)
# 
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion', idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')        
# 
#     # Casos Malicia
#   
#     # Prueba 
#     def testInsertTaskDesc0IdC0W0IdH0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('',0,0,0)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#            
#     # Prueba 20
#     def testInsertTaskDescNoneIdCNoneWNoneIdHNone(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#         
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result  = aTarea.insertTask(None,None,None,None)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')  
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 21
#     def testInsertTaskNoneDescIdCValidWValidIdHValid(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask(None,1,1,idFound1)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
#              
#     # Prueba 22
#     def testInsertTaskDescValidIdCValidWValidIdHBone(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,1,None)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
#     # Prueba
#     def testInsertTaskIdCString(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw','gjasdfio',1,None)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')        
# 
#     # Prueba
#     def testInsertTaskIdCInvalid(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',-98989562321,1,None)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')
# 
# # Prueba
#     def testInsertTaskWeightString(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,'gjasdfio',None)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')        
# 
#     # Prueba
#     def testInsertTaskWeightInvalid(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#         searchBacklog = aBacklog.findName('Podn fjdd.')
#         idFound0 = searchBacklog[0].BL_idBacklog
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',idFound0)
#         search = aAcc.searchAccion('Otra cosa',idFound0)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
# 
#         # Insertamos la categoria
#         aCategory = category()
#         aCategory.insertCategory('wofhweoifh',1)   
#            
#         # Insertamos la tarea  
#         aTarea = task()
#         result = aTarea.insertTask('dwidjw',1,-99559523232,None)
#         self.assertFalse(result)
#            
#         # Eliminamos la categoria, historia, accion y producto
#         aCategory.deleteCategory('wofhweoifh')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',idFound0)
#         aBacklog.deleteProduct('Podn fjdd.')                
                          
#     #############################################      
#     #      Suite de Pruebas para getAllTask     #
#     #############################################
#           
#      #Casos Frontera
#       
#     # Prueba 
#     def testGetAllTaskExist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         aTarea.getAllTask(idFound1)
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#    
#     # Prueba 
#     def testGetAllTaskValid(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.getAllTask(idFound1)
#         self.assertNotEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.') 
#    
#     # Prueba 
#     def testGetAllTaskNoId(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.getAllTask(2)
#         self.assertEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.')  
#           
#     # Prueba 
#     def testGetAllTaskNoTask(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         result = aTarea.getAllTask(idFound1)
#         self.assertEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.') 
#   
#     # Prueba 
#     def testGetAllTaskMaxId(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.getAllTask(2**31)
#         self.assertEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#   
#     # Casos Malicia
#       
#     # Prueba 
#     def testGetAllTaskNone(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.getAllTask(None)
#         self.assertEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testGetAllTaskid0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.getAllTask(0)
#         self.assertEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.')      
#       
#     # Prueba 
#     def testGetAllTaskString(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('Otra cosa',1)
#         search = aAcc.searchAccion('Otra cosa',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('hIDBW')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.getAllTask("uno")
#         self.assertEqual(result,[])
#           
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion',1)
#         aBacklog.deleteProduct('Podn fjdd.') 
#   
#     #############################################      
#     #   Suite de Pruebas para updateTask    #
#     #############################################
               
    # Caso Inicial
           
    # Prueba 
    def testUpdateTaskExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
             
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
              
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        aTarea.updateTask('dwidjw','diifneo',1,1)
                     
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('diifneo')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba 2
   
    def testUpdateTaskTrue(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',1,1)
        self.assertTrue(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('diifneo')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
                  
                
    # Casos Fronteras
             
    # Prueba 
    def testUpdateTaskShortDesc0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
            
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1) 
            
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('','diifneo',1,1)
        self.assertFalse(result)
                    
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        aTarea = task()
    
        # Eliminamos accion y producto
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
               
             
    # Prueba 
    def testUpdateTaskShortDesc1(self):
            
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
            
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1) 
          
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','T',1,1)
        self.assertTrue(result)
            
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 
    def testUpdateTaskShortDesc140(self):
          
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
          
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
            
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw',140*'T',1,1)
        self.assertTrue(result)
            
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
               
    # Prueba 7
    def testUpdateHistoryLong141(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
          
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
            
        aTarea = task()
        aTarea.insertTask(141*'T',idFound1,1,1)
        result  = aTarea.updateTask(141*'T',140*'T',1,1)        
        self.assertFalse(result)
            
        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
               
    # Prueba 
    def testUpdateTaskNew0(self):
        # Insertamos Producto    
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
          
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','',1,1)        
        self.assertFalse(result)
            
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
    
               
    # Prueba 
    def testUpdateTaskNoDesc(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
            
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('OEdfeenfr','diifneo',1,1)
        self.assertFalse(result)
            
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
       
    # Prueba 
    def testUpdateTaskLongNew(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
          
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
            
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw',140*'T',1,1)
        self.assertTrue(result)
            
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
 
 
    def testUpdateTaskCategory0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',0,1)
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
 
    def testUpdateTaskNoCategory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',2,1)
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
 
    def testUpdateTaskNoneCategory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',None,1)
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
 
    def testUpdateTaskStringCategory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo','',1)
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
 
    def testUpdateTaskWeight0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',1,0)
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
     
    def testUpdateTaskWeightMax(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',1,2**32)
        self.assertTrue(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
 
    def testUpdateTaskNoneWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',1,None)
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
         
    def testUpdateTaskStringWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)  
           
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw','diifneo',1,'')
        self.assertFalse(result)
           
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
          
     # Casos Esquinas
            
    # Prueba 
    def testUpdateTaskNew1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('T',1,1,idFound1)
        result  = aTarea.updateTask('T','A',1,1)
        self.assertTrue(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('A')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testUpdateTaskNewDescLong0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask(140*'A',1,1,idFound1)
        result  = aTarea.updateTask(140*'A','',0,0)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'A')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
  
    # Prueba 
    def testUpdateTask140long141(self):
                # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask(140*'A',1,1,idFound1)
        result  = aTarea.updateTask(140*'A',141*'T',1,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'A')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 
    def testUpdateTask140None(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask(140*'H',1,1,idFound1)
        result  = aTarea.updateTask(140*'H',None,1,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'H')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testUpdateTask0NewDesc1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('',1,1,idFound1)
        result  = aTarea.updateTask('','T',1,1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testUpdateTaskDesc1New0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('T',1,1,idFound1)
        result  = aTarea.updateTask('T','',1,1)        
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 
    def testUpdateTaskDesc141New0(self):    
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        result  = aTarea.updateTask(141*'T','',1,1)        
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
          
    # Prueba 
    def testUpdateTaskDescE140New1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T','T',1,1)        
        self.assertTrue(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
  
    # Casos Malicia
  
    # Prueba 
    def testUpdateTaskDesc0New0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('OEdfeenfr',1,1,idFound1)
        result  = aTarea.updateTask('','',1,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('OEdfeenfr')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testUpdateTaskDescNoneNewNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
          
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask(None,None,1,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
          
    # Prueba
    def testUpdateTaskNoneDescNewValid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask(None,'diifneo',1,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 
    def testUpdateTaskDescIntNew(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
          
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        result  = aTarea.updateTask('dwidjw',1234,1,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba
    def testUpdateTaskMaxValues(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('T',1,1,idFound1)
        result  = aTarea.updateTask('T',140*'A',1,2**31)
        self.assertTrue(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'A')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateTaskMaxWeightMaxString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',1,2**31)
        self.assertTrue(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'A')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTaskMaxDescMaxWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(141*'T',1,1,idFound1)
        result  = aTarea.updateTask(141*'T','A',1,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTaskMaxNewMaxWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('T',1,1,idFound1)
        result  = aTarea.updateTask('T',141*'A',1,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTaskMaxNoCategory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',2**31,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateTaskMaxNoWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(141*'T',1,1,idFound1)
        result  = aTarea.updateTask(141*'T',141*'A',2**31,1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateTaskMaxNoDesc(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('T',1,1,idFound1)
        result  = aTarea.updateTask('T',141*'A',2**31,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateTaskLong0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('T',1,1,idFound1)
        result  = aTarea.updateTask('T','',1,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
  
    #Prueba
    
    def testUpdateTaskLong0All(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('',1,1,idFound1)
        result  = aTarea.updateTask('','',1,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTaskNUm0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',0,2**31)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')  
        
    #Prueba
    
    def testUpdateTaskNum0All(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',0,0)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')        

    #Prueba
    
    def testUpdateTask1None(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',1,None)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTask2None(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',None,None)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateTask3None(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',None,None,None)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateTaskMinAllParams(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask('',1,1,idFound1)
        result  = aTarea.updateTask('','',0,0)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTask2String(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',140*'a',140*'a')
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')   
        
    #Prueba
    
    def testUpdateTask1String(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',1,140*'A')
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    #Prueba
    
    def testUpdateTask1StringLeft(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',140*'A',1)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos Malicia
    
    #Prueba
    
    def testUpdateTaskNoParams(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask('','','','')
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')
    
    #Prueba
    
    def testUpdateAllNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(None,None,None,None)
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

    #Prueba
    
    def testUpdateAllString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',1)
        search = aAcc.searchAccion('Otra cosa',1)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, 1,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
       
        #Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
  
        aTarea = task()
        aTarea.insertTask(140*'T',1,1,idFound1)
        result  = aTarea.updateTask(140*'T',140*'A',140*'S',140*'R')
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',1)
        aBacklog.deleteProduct('Podn fjdd.')

#     #############################################      
#     #   Suite de Pruebas para searchTask        #
#     #############################################
#             
#     # Caso Inicial
#         
#     # Prueba
#     def testSearchTask(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         aTarea.searchTask('dwidjw')
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTaskExists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask('dwidjw')
#         self.assertTrue(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTaskNotExists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask('diifneo')
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Casos Frontera
#      
#     # Prueba
#     def testSearchTask1Exists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)
#         result = aTarea.searchTask('T')
#         self.assertTrue(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#      
#     # Prueba
#     def testSearchTask140Exists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('T'*140,idFound1)
#         result = aTarea.searchTask('T'*140)
#         self.assertTrue(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTask0Exists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('',idFound1)
#         result = aTarea.searchTask('')
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#      
#     # Prueba
#     def testSearchTask1NotExists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)
#         result = aTarea.searchTask('A')
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#      
#     # Prueba
#     def testSearchTask140NotExists(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('T'*140,idFound1)
#         result = aTarea.searchTask('A'*140)
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Casos Malicia
#      
#     # Prueba
#     def testSearchTaskNone(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask(None)
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTaskStringSpace(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask(' ')
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTaskNotString(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask(88)
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTaskArray(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask([])
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#      
#     # Prueba
#     def testSearchTaskDisctionary(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask({})
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testSearchTaskStringLong(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)
#         result = aTarea.searchTask('a'*((2^31)-1))
#         self.assertFalse(result)
#          
#                      
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     #############################################      
#     #   Suite de Pruebas para deleteTask        #
#     #############################################
#             
#     # Caso Inicial
#      
#     # Prueba
#     def testdeleteTaskExist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)      
#          
#                      
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('dwidjw')
#         self.assertTrue(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testdeleteTaskNotExist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#              
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#              
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#            
#         aTarea = task()
#         aTarea.insertTask('dwidjw',idFound1)      
#          
#                      
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('diifneo')
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')    
#      
#     # Casos Frontera
#      
#     # Prueba
#     def testdeleteTask1Exist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('T')
#         self.assertTrue(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTask140Exist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T'*140,idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('T'*140)
#         self.assertTrue(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTask1NotExist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('A')
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTask140NotExist(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T'*140,idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('A'*140)
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTask0(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('')
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTask(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('')
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Casos Malicia
#     
#     # Prueba
#     def testdeleteTaskStringSpace(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask(' ',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask(' ')
#         self.assertTrue(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTaskNotString(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask(88)
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTaskNone(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask(None)
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTaskArray(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask([])
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTaskDictionary(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask({})
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#         
#     # Prueba
#     def testdeleteTaskLong(self):
#         # Insertamos Producto
#         aBacklog = backlog()
#         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
#             
#         # Insertamos la accion
#         aAcc = accions()
#         aAcc.insertAccion('cinrohbwidia',1)
#         search = aAcc.searchAccion('cinrohbwidia',1)
#         idFound = search[0].AC_idAccion
#             
#         # Insertamos la historia
#         aHist = userHistory()
#         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, 1,1)
#         searchHist = aHist.searchUserHistory('BIEEIEB1')
#         idFound1 = searchHist[0].UH_idUserHistory 
#           
#         aTarea = task()
#         aTarea.insertTask('T',idFound1)      
#         
#                     
#         # Eliminamos historia, accion y producto
#         result = aTarea.deleteTask('T'*((2^31)-1))
#         self.assertFalse(result)
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')

    #########################################################      
    #         Suite de Pruebas para historyWeight           #
    #########################################################     
      
    # Caso Inicial 
       
    # Prueba 
    def testHistoryWeightExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()   
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound1)
        self.assertEqual(1, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
         
    # Casos Frontera

    # Prueba 
    def testHistoryWeightNotExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(0)
        self.assertEqual(0, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 
    def testHistoryWeightIdOneEpic(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        aHist.insertUserHistory('BIEEIEB12',1, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        searchHist2 = aHist.searchUserHistory('BIEEIEB12')
        idFound2 = searchHist2[0].UH_idUserHistory
    
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound2)
        aTarea.insertTask('dwasidjw',1,5,idFound2)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound1)
        self.assertEqual("", result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwasidjw')
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB12')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 
    def testHistoryWeightIdOneNotEpic(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        aCategory.insertCategory('uweuwwqe',6)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
        aTarea.insertTask('dwasidjw',1,5,idFound1)
        aTarea.insertTask('uyrwuwry',2,9,idFound1)
        aTarea.insertTask('iophkjmbnb',2,6,idFound1)
        aTarea.insertTask('qazxc',1,8,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound1)
        self.assertEqual(29, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('qazxc')
        aTarea.deleteTask('iophkjmbnb')
        aTarea.deleteTask('uyrwuwry')
        aTarea.deleteTask('dwasidjw')
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('uweuwwqe')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 
    def testHistoryWeightNotEpic(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        aHist.insertUserHistory('BIEEIEB12',1, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        searchHist2 = aHist.searchUserHistory('BIEEIEB12')
        idFound2 = searchHist2[0].UH_idUserHistory
    
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        aCategory.insertCategory('jiokl',6)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound2)
        aTarea.insertTask('dwasidjw',2,6,idFound2)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound2)
        self.assertEqual(7, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwasidjw')
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('jiokl')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB12')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 
    def testHistoryWeightIdBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(2**31)
        self.assertEqual(0, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Casos Malicia

    # Prueba 
    def testHistoryWeightIdString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight('uasshj')
        self.assertEqual(0, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
                 
    # Prueba 
    def testHistoryWeightIdInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(-215848774)
        self.assertEqual(0, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 
    def testHistoryWeightIdNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('BIEEIEB1')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        
        # Insertamos las tareas    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(None)
        self.assertEqual(0, result)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
