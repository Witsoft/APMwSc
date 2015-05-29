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
 
    # Prueba 0
    def testinsertActorAsociatedInUserHistory(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Cualquier cosa2',1)
        search = aAcc.searchAccion('Cualquier cosa2')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('Hist300',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('Hist300')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Scrum Master', 'Descripcion', 1)
        searchAct = aAct.findNameRole('Scrum Master')
        idFound2 = searchAct[0].idrole 
        
        #Inicio de caso de prueba
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('Hist300')
        aAcc.deleteAccion('Cualquier Cosa2')
        aBackLog.deleteProduct('Taxi seguro.')

    # Casos Normales
    
    # Prueba 1
    
    def testinsertActorAsociatedInUserHistory1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        #Inicio de caso de prueba
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        self.assertTrue(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
         
     # Casos Fronteras
     
     # Prueba 2
    def testinsertActorAsociatedInUserHistoryIdActorNoExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        #Inicio de caso de prueba
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(0, idFound1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')

     # Prueba 3
    def testinsertActorAsociatedInUserHistoryIdHistoryNoExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        #Inicio de caso de prueba
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, 0) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 4
    def testinsertActorAsociatedInUserHistoryIdActorBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        #Inicio de caso de prueba
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory((2**31)-1, idFound1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        

    # Prueba 5
    def testinsertActorAsociatedInUserHistoryIdActorBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound1, (2**31)-1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')        
        
    # Caso Esquina
    
    # Prueba 6   
    
    def testinsertActorAsociatedInUserHistoryNotExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(0, 0) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 
   
    # Prueba 7
    def testinsertActorAsociatedInUserHistoryIdActorAndIdHIstoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory((2**31)-1, (2**31)-1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 8
    def testinsertActorAsociatedInUserHistoryIdActorNotExistIdHIstoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(0, (2**31)-1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')        
        
    # Prueba 9
    def testinsertActorAsociatedInUserHistoryIdActorBigIdHIstoryNotExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory((2**31)-1, 0) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
     
     
    # Casos Malicia 
     
     # Prueba 10   
    def testinsertActorAsociatedInUserHistoryNoExists(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(-1, -1) 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
                
      # Prueba 11   
    def testinsertActorAsociatedInUserHistoryString(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory('1', '0') 
        self.assertFalse(result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')  
        
     # Prueba 12   
    def testinsertActorAsociatedInUserHistoryIdActorNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(None, idFound1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')      

     # Prueba 13   
    def testinsertActorAsociatedInUserHistoryIduserHIstoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, None) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')      
 
      # Prueba 14   
    def testinsertActorAsociatedInUserHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory
         
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(None, None) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.') 
        
    #########################################################      
    #   Suite de Pruebas para idActorsAsociatedToUserHistory   #
    #########################################################     
      
    # Caso Inicial 
     
    # Prueba 15
    
    def testidActorsAsociatedToUserHistory(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H1',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H1')
        idFound1 = searchHist[0].id_userHistory 
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1)
         
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        aAccAs.idActorsAsociatedToUserHistory(idFound1)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H1')
        aAcc.deleteAccion('Otra Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Caso Frontera
    
    # Prueba 16    
    def testidActorsAsociatedToUserHistoryid_userHistory1(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory(idFound1)
        self.assertNotEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')
    
      # Prueba 17   
    def testidActorsAsociatedToUserHistoryid_userHistory0(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory(0)
        self.assertEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 18   
    def testidActorsAsociatedToUserHistoryid_userHistoryBig(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory((2**31)-1)
        self.assertEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')

    # Casos Malicia

      # Prueba 19   
    def testidActorsAsociatedToUserHistoryid_userHistoryNoExist(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory(-1)
        self.assertEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')

      # Prueba 20   
    def testidActorsAsociatedToUserHistoryid_userHistoryNoInt(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory('1')
        self.assertEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 21   
    def testidActorsAsociatedToUserHistoryid_userHistoryNone(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory(None)
        self.assertEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')
        
      # Prueba 22   
    def testidActorsAsociatedToUserHistoryid_userHistoryStringInvalid(self):
        # Insertamos Producto
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Otra Accion',1)
        search = aAcc.searchAccion('Otra Accion')
        idFound = search[0].idaccion
        
        # Insertamos Actor
        aAct = role()
        aAct.insertRole('Team Member', 'Descripcion1', 1)
        searchAct = aAct.findNameRole('Team Member')
        idFound2 = searchAct[0].idrole   
    
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H10',0, 1,idFound, 1)
        searchHist = aHist.searchUserHistory('H10')
        idFound1 = searchHist[0].id_userHistory 
                      
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs = actorsUserHistory()
        result = aAccAs.idActorsAsociatedToUserHistory('')
        self.assertEqual([],result)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H10')
        aAcc.deleteAccion('Una Accion')
        aBackLog.deleteProduct('Taxi seguro.')