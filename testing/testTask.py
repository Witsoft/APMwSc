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
       
    #############################################      
    #      Suite de Pruebas para insertTask     #
    #############################################
              
    # Caso Inicial
          
    # Prueba 1
    def testInserTaskExists(self):
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
        
        # Insertamos la tarea    
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1)
                      
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB1')
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba 2
    
    def testInsertTaskElementNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
               
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',idFound0)
        search = aAcc.searchAccion('Otra Accion',idFound0)
        idFound = search[0].AC_idAccion
               
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
         
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
         
        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,1,idFound1)
        self.assertTrue(result)
                       
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
                
    # Prueba 3
    def testInsertTaskRepeatedElement(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog
               
         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('Otra cosa',idFound0)
         search = aAcc.searchAccion('Otra cosa',idFound0)
         idFound = search[0].AC_idAccion
               
         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
         searchHist = aHist.searchUserHistory('hIDBW')
         idFound1 = searchHist[0].UH_idUserHistory 
         
         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)
         
         # Insertamos la tarea    
         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1)
         result = aTarea.insertTask('dwidjw',1,1,idFound1)
         self.assertFalse(result)
   
         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('Otra cosa', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')
                      
                
    # Casos Fronteras
             
    # Prueba 4
    def testInsertTaskShortDesc0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
           
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea   
        aTarea = task()
        result = aTarea.insertTask('', 1, 1,idFound1)
        self.assertFalse(result)
                   
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')                           
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
              
    # Prueba 5
    def testInsertTaskShortDesc1(self):
           
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('T', 1, 1, idFound1)
        self.assertTrue(result)
           
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
            
    # Prueba 6
    def test4InsertTaskShortDesc140(self):
         
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask(140*'T',1,1,idFound1)
        self.assertTrue(result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba 7
    def testInsertHistoryLong141(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask(141*'T',1,1,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')        
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba 8
    def testInsertTaskId0(self):
        # Insertamos Producto    
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,1,0)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba 9
    def testInsertTaskNoHistory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,1,3)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
      
    # Prueba 10
    def testInsertTaskLongId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,1,2**31)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 
    def testInsertTaskIdCategory0(self):
        # Insertamos Producto    
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',0,1,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba
    def testInsertTaskNoCategory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',100,1,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
      
    # Prueba 
    def testInsertTaskLongIdCategory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',2**31,1,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')        

    # Prueba 
    def testInsertTaskWeight0(self):
        # Insertamos Producto    
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,0,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
              
    # Prueba 
    def testInsertTaskNegativeWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,-1,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
      
    # Prueba
    def testInsertTaskLongWeight(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',5)

        # Insertamos la tarea    
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,2**31,idFound1)
        self.assertTrue(result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')        
           
    # Casos Esquinas
            
    # Prueba
    def testinsertTaskODJdbeidbww1Id1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('T',1,1,idFound1)
        self.assertTrue(result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('T')
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testInsertTask140Id1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(140*'A',1,1,idFound1)
        self.assertTrue(result)
           
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask(140*'A')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
     
    # Prueba 
    def testInsertTask141NoId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result  = aTarea.insertTask(141*'A',1,1,3)
        self.assertFalse(result)        
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 
    def testInsertTask140NoId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(140*'H',1,1,3)
        self.assertFalse(result)        
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testInserTask0Id1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('',1,1,idFound1)
        self.assertFalse(result)        
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 
    def testInserTaskDescription1Id0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('T',1,1,0)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 
    def testInsertTaskDescription141Id0(self):    
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(141*'H',1,1,0)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
          
    # Prueba 
    def testInsertTaskDescriptionE140Id1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result  = aTarea.insertTask(140*'T',1,1,idFound1)
        self.assertTrue(result)
           
        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask(140*'T')
        aCategory.deleteCategory('wofhweoifh')
        aTarea.deleteTask(140*'T')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba
    def testinsertTaskDesc1IdCWeightIdHBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('T',2**31,2**31,2**31)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')     

    # Prueba
    def testinsertTaskDesc140IdCWeightIdHBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(140*'T',2**31,2**31,2**31)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')     

        # Prueba
    def testinsertTaskDesc1IdC0Weight0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('T',0,0,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')  

    # Prueba
    def testinsertTaskDesc0IdCWeightIdH0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('',2**31,2**31,0)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')             
  
        # Prueba
    def testinsertTaskDesc0IdCBigWeightNegativeIdHValid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('T',2**31,-1,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba
    def testinsertTaskDesc140IdC1Weight0IdH0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(140*'T',1,0,0)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba
    def testinsertTaskDesc0IdC1WeightBigIdHValid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('',1,2**31,idFound1)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')


    # Prueba
    def testinsertTaskDesc140IdCBigWeight1IdH0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(140*'T',2**31,1,0)
        self.assertFalse(result)

        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')        

    # Casos Malicia
  
    # Prueba 
    def testInsertTaskDesc0IdC0W0IdH0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('',0,0,0)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
           
    # Prueba 20
    def testInsertTaskDescNoneIdCNoneWNoneIdHNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result  = aTarea.insertTask(None,None,None,None)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')  
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
          
    # Prueba 21
    def testInsertTaskNoneDescIdCValidWValidIdHValid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask(None,1,1,idFound1)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
             
    # Prueba 22
    def testInsertTaskDescValidIdCValidWValidIdHBone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,1,None)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba
    def testInsertTaskIdCString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('dwidjw','gjasdfio',1,None)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')        

    # Prueba
    def testInsertTaskIdCInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('dwidjw',-98989562321,1,None)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

# Prueba
    def testInsertTaskWeightString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,'gjasdfio',None)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')        

    # Prueba
    def testInsertTaskWeightInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
             
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra cosa',idFound0)
        search = aAcc.searchAccion('Otra cosa',idFound0)
        idFound = search[0].AC_idAccion
             
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1)
        searchHist = aHist.searchUserHistory('hIDBW')
        idFound1 = searchHist[0].UH_idUserHistory 

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)   
           
        # Insertamos la tarea  
        aTarea = task()
        result = aTarea.insertTask('dwidjw',1,-99559523232,None)
        self.assertFalse(result)
           
        # Eliminamos la categoria, historia, accion y producto
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('hIDBW')
        aAcc.deleteAccion('Otra Accion',idFound0)
        aBacklog.deleteProduct('Podn fjdd.')                
                          
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
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
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.') 
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
#         aTarea.updateTask('dwidjw','diifneo')
#                   
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('diifneo')
#         aHist.deleteUserHistory('BIEEIEB1')
#         aAcc.deleteAccion('cinrohbwidia',1)
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 2
#  
#     def testUpdateTaskElementNotExist(self):
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
#         result  = aTarea.updateTask('dwidjw','diifneo')
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('diifneo')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#                 
#              
#     # Casos Fronteras
#           
#     # Prueba 
#     def testUpdateTaskShortDesc0(self):
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
#         result  = aTarea.updateTask('','diifneo')
#         self.assertFalse(result)
#                  
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#         aTarea = task()
#  
#         # Eliminamos accion y producto
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#           
#     # Prueba 
#     def testUpdateTaskShortDesc1(self):
#          
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
#         result  = aTarea.updateTask('dwidjw','T')
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testUpdateTaskShortDesc140(self):
#        
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
#         result  = aTarea.updateTask('dwidjw',140*'T')
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 7
#     def testUpdateHistoryLong141(self):
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
#         aTarea.insertTask(141*'T',idFound1)
#         result  = aTarea.updateTask(141*'T',140*'T')        
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 
#     def testUpdateTaskNew0(self):
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
#         result  = aTarea.updateTask('dwidjw','')        
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#  
#             
#     # Prueba 
#     def testUpdateTaskNoDesc(self):
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
#         result  = aTarea.updateTask('OEdfeenfr','diifneo')
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#     
#     # Prueba 
#     def testUpdateTaskLongNew(self):
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
#         result  = aTarea.updateTask('dwidjw',140*'T')
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'T')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Casos Esquinas
#            
#     # Prueba 
#     def testUpdateTaskNew1(self):
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
#         aTarea.insertTask('T',idFound1)
#         result  = aTarea.updateTask('T','A')
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('A')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testUpdateTaskNewDescLong0(self):
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
#         aTarea.insertTask(140*'A',idFound1)
#         result  = aTarea.updateTask(140*'A','')
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'A')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#  
#     # Prueba 
#     def testUpdateTask141None(self):
#                 # Insertamos Producto
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
#         aTarea.insertTask(140*'A',idFound1)
#         result  = aTarea.updateTask(140*'A',141*'T')
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'A')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 
#     def testUpdateTask140None(self):
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
#         aTarea.insertTask(140*'H',idFound1)
#         result  = aTarea.updateTask(140*'H',None)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask(140*'H')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testUpdateTask0NewDesc1(self):
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
#         aTarea.insertTask('',idFound1)
#         result  = aTarea.updateTask('','T')
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testUpdateTaskDesc1New0(self):
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
#         aTarea.insertTask('T',idFound1)
#         result  = aTarea.updateTask('T','')        
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 
#     def testUpdateTaskDesc141New0(self):    
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
#         result  = aTarea.updateTask(141*'T','')        
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#          
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba 
#     def testUpdateTaskDescE140New1(self):
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
#         aTarea.insertTask(140*'T',idFound1)
#         result  = aTarea.updateTask(140*'T','T')        
#         self.assertTrue(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('T')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#  
#     # Casos Malicia
#  
#     # Prueba 
#     def testUpdateTaskDesc0New0(self):
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
#         aTarea.insertTask('OEdfeenfr',idFound1)
#         result  = aTarea.updateTask('','')
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('OEdfeenfr')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#           
#     # Prueba 
#     def testUpdateTaskDescNoneNewNone(self):
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
#         result  = aTarea.updateTask(None,None)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#          
#     # Prueba
#     def testUpdateTaskNoneDescNewValid(self):
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
#         result  = aTarea.updateTask(None,'diifneo')
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#             
#     # Prueba 
#     def testUpdateTaskDescIntNew(self):
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
#         result  = aTarea.updateTask('dwidjw',1234)
#         self.assertFalse(result)
#          
#         # Eliminamos historia, accion y producto
#         aTarea.deleteTask('dwidjw')
#         aHist.deleteUserHistory('hIDBW')
#         aAcc.deleteAccion('Otra Accion')
#         aBacklog.deleteProduct('Podn fjdd.')
#  
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