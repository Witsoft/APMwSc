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
   
    # Prueba 13
    def testInsertHomework141NoId(self):
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
        result  = aTarea.insertHomework(141*'A',3)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 14
    def testInsertHomework140NoId(self):
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
        result  = aTarea.insertHomework(140*'H',3)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
         
    # Prueba 15
    def testInserHomework0Id1(self):
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
         
    # Prueba 16
    def testInserHomeworkDescription1Id0(self):
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
        result  = aTarea.insertHomework('T',0)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 17
    def testInsertHomeworkDescription141Id0(self):    
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
        result  = aTarea.insertHomework(141*'H',0)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 18
    def testInsertHomeworkDescriptionE140Id1(self):
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

    # Casos Malicia

    # Prueba 19
    def testHomeworkDesc0Id0(self):
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
        result  = aTarea.insertHomework('',0)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
         
    # Prueba 20
    def testInsertHomeworkDescNoneIdNone(self):
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
        result  = aTarea.insertHomework(None,None)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 21
    def testInsertHomeworkNoneDescIdValid(self):
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
        result  = aTarea.insertHomework(None,idFound1)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 22
    def testInsertHomeworkDescNoneid(self):
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
        result  = aTarea.insertHomework('Tarea1',None)
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H2')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
                        
    #############################################      
    #   Suite de Pruebas para searchUserHistory #
    #############################################
        
     #Casos Frontera
 