# -*- coding: utf-8 -*-. 

import unittest

from objectiveDummy import *

class TestObjectives(unittest.TestCase):
    
     #############################################      
     #   Suite de Pruebas para insertObjective   #
     #############################################
          
     # Caso Inicial
  
     # Prueba 1
     def testInserObjectiveExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         aAcc = objective()
         aAcc.insertObjective('Reservar un taxi.',1)
         aAcc.deleteObjective('Reservar un taxi.')
         aBackLog.deleteProduct('Taxi seguro.')        
    # Casos Normales
     
    # Prueba 2
     def testInsertObjectiveElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Permite localizar un taxi')
        aAcc   = objective()
        result = aAcc.insertObjective('Permite elegir.',1)
        self.assertTrue(result)
        aAcc.deleteObjective('Permite elegir')
        aBackLog.deleteProduct('Permite localizar un taxi')
                  
    # Prueba 3
     def testInsertObjectiveRepeatedElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        aAcc   = objective()
        result = aAcc.insertObjective('Permite elegir.',1)
        result1 = aAcc.insertObjective('Permite elegir.',1)
        self.assertFalse(result1)
        aAcc.deleteObjective('Permite seleccionar.')
        aBackLog.deleteProduct('Taxi seguro.')
               
    # Casos Fronteras
      
     # Prueba 4
     def test4InsertObjectiveShortDesc0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result = aAcc.insertObjective('',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
          
           
    # Prueba 5
     def testInsertObjectiveLongDesc1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result = aAcc.insertObjective('A',1)
         self.assertTrue(result)
         aAcc.deleteObjective('A')
         aBackLog.deleteProduct('Taxi seguro.')
       
    # Prueba 6
     def test6InsertObjectiveLongDesc140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         aAcc   = objective()
         result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem',1)
         self.assertTrue(result)
         aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
         aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 7
     def testInsertObjectiveLongDesc141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 8
     def testInsertObjectiveIdBackLogInvalid(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         aAcc   = objective()
         result  =aAcc.insertObjective('Movlizarme desde mi casa',0)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
      
      
     # Casos Esquinas
       
    # Prueba 9
     def testInsertObjectiveIdBackLogNoExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result  =aAcc.insertObjective('Trasladarse rápido',2)
         self.assertFalse(result)
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 10
     def testInsertObjectiveLongDesc140AndIdBackLogNoExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin proble1',3)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
      
    # Casos Maliciosos
      
    # Prueba 11
     def testInsertNotString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result = aAcc.insertObjective(4350,1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 12
     def testInsertNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         result = aAcc.insertObjective(None,1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
           
  
     #############################################      
     #   Suite de Pruebas para searchObjective   #
     #############################################
       
     # Caso Inicial
       
    # Prueba 13 
     def testsearchObjectiveExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc = objective()
         aAcc.insertObjective('Permite reservar un taxi',1)
         aAcc.searchObjective('Permite reservar un taxi')
           
    # Casos Fronteras
       
    # Prueba 14
     def testsearchObjectiveShortDesc0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.        
         aAcc   = objective()
         aAcc.insertObjective('',1)
         result = aAcc.searchObjective('')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 15
     def test_15searchObjectiveShortDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba
        aAcc   = objective()
        aAcc.insertObjective('A',1)
        result = aAcc.searchObjective('A')
        self.assertTrue(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 16
     def testsearchObjectiveShortDesc140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem',1)
        result = aAcc.searchObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        self.assertNotEqual(result,[],"Objective no encontrada")
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 17
     def testsearchObjectiveShortDesc141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1)
 
         result = aAcc.searchObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema')
         self.assertFalse(result, "Objective Encontrada.")
         aBackLog.deleteProduct('Taxi seguro.')
  
     # Caso Normal
      
     # Prueba 18
     def testsearchObjectiveDescNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.searchObjective('Comunicarse via correo electronico')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
           
  
    # Casos Maliciosos
       
     # Prueba 19
     def testsearchObjectiveNotString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba. 
         aAcc   = objective()
         aAcc.insertObjective(4350,1)
         result = aAcc.searchObjective(4350)
         self.assertEqual(result, [],'Objective Encontrada')
         aBackLog.deleteProduct('Taxi seguro.')
 
     #Prueba 20 
     def testSearchNameNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.   
         aAcc   = objective()
         result = aAcc.searchObjective(None)
         self.assertEqual(result, [],'Objective Encontrada')
         aBackLog.deleteProduct('Taxi seguro.')
          
    #############################################      
     #   Suite de Pruebas para searchIdObjective   #
     #############################################  
    # Caso Inicial
          
     #Prueba 21  
     def testsearchIdObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1)
        aAcc.searchObjective('Permite reservar un taxi')
                          
     #############################################      
     #   Suite de Pruebas para updateObjective   #
     #############################################  
    # Caso Inicial
      
    # Prueba 22
     def testupdateObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.   
        aAcc   = objective()
        aAcc.insertObjective('reservar un taxi.',1)
        aAcc.updateObjective('reservar un taxi.','reservar un taxi o varios.')
        aBackLog.deleteProduct('Taxi seguro.')  
 
    # Casos Normales
      
     # Prueba 23
     def testupdateObjectiveDesc(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         aAcc.insertObjective('Permite elegir.',1)
         result = aAcc.updateObjective('Permite elegir.','Atención las 24 horas del día')
         self.assertTrue(result)
         aAcc.deleteObjective('Atención las 24 horas del día')
         aBackLog.deleteProduct('Taxi seguro.')
           
     #Prueba 24     
     def testupdateObjectiveDescNOtExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
        aAcc = objective()
        result = aAcc.updateObjective('Llegar lo mas pronto posible','Ir comodo y seguro')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Casos Fronteras
        
    # Prueba 25
     def testupdateObjectiveLeftLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('A',1)
        result = aAcc.updateObjective('A','Buscar al cliente donde esté')
        self.assertTrue(result)
        aAcc.deleteObjective('Buscar al cliente donde esté')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 26
     def testupdateObjectiveLeftLong1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Buscar al cliente donde esté',1)
        result = aAcc.updateObjective('Buscar al cliente donde esté','A')
        self.assertTrue(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 27         
     def testupdateObjectiveRightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Atención las 24 horas del día',1)
        result = aAcc.updateObjective('Atención las 24 horas del día',140*'T')
        self.assertTrue(result)    
        aAcc.deleteObjective(140*'T')
        aBackLog.deleteProduct('Taxi seguro.')
  
    # Prueba 28
     def testupdateObjectiveLeftLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective(140*'T',1)
        result = aAcc.updateObjective(140*'T','Atención las 24 horas del día')
        self.assertTrue(result)
        aAcc.deleteObjective('Atención las 24 horas del día')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Casos Esquinas
       
    # Prueba 29
     def testupdateObjectiveLeftLen1RightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('A',1)
        result = aAcc.updateObjective('A',140*'Us')
        self.assertFalse(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro.') 


    # Prueba 30
     def testupdateObjectiveLeftLen140RightLen140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
         aAcc   = objective()
         aAcc.insertObjective(140*'Us',1)
         result = aAcc.updateObjective(140*'Us', 140*'Ma')
         self.assertFalse(result) 
         aAcc.deleteObjective(140*'Us')
         aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 31
     def testupdateObjectiveLeftLen140RightLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem',1)
        result = aAcc.updateObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem','M')
        self.assertTrue(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 32
     def testupdateObjectiveLeftLen1RightLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('X',1)
        result = aAcc.updateObjective('X','U')
        self.assertTrue(result)
        aAcc.deleteObjective('U')
        aBackLog.deleteProduct('Taxi seguro.') 
           
    # Casos Maliciosos
       
    # Prueba 33
     def testupdateSameName(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Reservar un taxi.',1)
        result = aAcc.updateObjective('Reservar un taxi.','Reservar un taxi.')
        self.assertFalse(result,"Modificación Válida")
        aAcc.deleteObjective('Reservar un taxi.')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 34
     def testupdateObjectiveLeftLen0RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('',1)
        result = aAcc.updateObjective('','Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problems')
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteObjective('')
        aBackLog.deleteProduct('Taxi seguro.')
 
    # Prueba 35
     def testupdateObjectiveLeftLen141RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema',1)
        result = aAcc.updateObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema',25*'Ma' + 's')
        self.assertFalse(result, "Modificación Válida") 
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 36
     def testupdateObjectiveLeftLen141RightLen0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas',1)
        result = aAcc.updateObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas','')
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas')
        aBackLog.deleteProduct('Taxi seguro.')  
 
    # Prueba 37
     def testupdateObjectiveLeftNoneRightValidString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.updateObjective(None,'Comunicarse via correo electronico')
        self.assertFalse(result,"Modificación válida") 
        aBackLog.deleteProduct('Taxi seguro.')  
 
    # Prueba 38
     def testupdateObjectiveLeftValidStringRightNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Reservar un taxi.',1)
        result = aAcc.updateObjective('Reservar un taxi.',None)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteObjective('Reservar un taxi.')
        aBackLog.deleteProduct('Taxi seguro.')    
           
    #############################################      
    #       Suite de Pruebas para deleteObjective      #
    ############################################# 
       
    # Caso Inicial
       
    # Prueba 39
     def testDeleteObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Reservar un Taxi',1)
        aAcc.deleteObjective('Reservar un Taxi')
        aBackLog.deleteProduct('Taxi seguro.')
           
        # Casos Normales
   
    # Prueba 40
     def testDeleteObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('U',1)
        result = aAcc.deleteObjective('U')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')
    # Casos Fronteras
       
    # Prueba 41
     def testDeleteObjective1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('A',1)
        result = aAcc.deleteObjective('A')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')          
  
    # Prueba 42      
     def testDeleteObjectiveNoObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('yyy',1)
        result = aAcc.deleteObjective('xxx')
        self.assertFalse(result)
        aAcc.deleteObjective('yyy')
        aBackLog.deleteProduct('Taxi seguro.')

    # Casos Maliciosos
  
    # Prueba 43
     def testDeleteObjectiveInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.deleteObjective('')
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Prueba 44
     def testDeleteObjectiveNotString(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('Taxi seguro.')
       # Inicio de la prueba.
       aAcc   = objective()
       aAcc.insertObjective(12345,1)
       result = aAcc.deleteObjective(12345)
       self.assertFalse(result,"Id no válido")
       aBackLog.deleteProduct('Taxi seguro.')
 
    # Prueba 45    
     def testDeleteObjectiveNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.deleteObjective('Legar rápido')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
         
     ##############################################      
     #       Suite de Pruebas para SearchIdObjective #
     ##############################################
    
     # Prueba 46  
     def testSearchIdExist(self):
         oObjective = objective()
         oObjective.searchIdObjective(1)
  
     # Casos Fronteras
     
     # Prueba 47
     def testSearchIdTrue(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         oObjective   = objective()
         oObjective.insertObjective('Nuevo T',1)
         searchAcc = oObjective.searchObjective('Nuevo T')
         idFound = searchAcc[0].idobjective
         result = oObjective.searchIdObjective(idFound)
         self.assertNotEqual(result,[],"Elemento no encontrado")
         oObjective.deleteObjective('Nuevo T')
         aBackLog.deleteProduct('Taxi seguro.') 
     
     # Prueba 48
     def testSearchIdEmpty(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         oObjective   = objective()
         oObjective.insertObjective('',1)
         result = oObjective.searchIdObjective(0)
         self.assertEqual(result,[], "Elemento no encontrado")
         aBackLog.deleteProduct('Taxi seguro.')
           
     # Prueba 49
     def testSearchIdNoObjective(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         oObjective   = objective()
         oObjective.insertObjective('T',1)
         result = oObjective.searchIdObjective(2)
         self.assertEqual(result,[],"Elemento no encontrado")
         oObjective.deleteObjective('T')
         aBackLog.deleteProduct('Taxi seguro.') 
 
     # Casos Maliciosos
     
     # Prueba 50
     def testSearchIdString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         oObjective   = objective()
         oObjective.insertObjective(1254,1)
         result = oObjective.searchIdObjective('')
         self.assertEqual(result,[],"Elemento Insertado") 
         aBackLog.deleteProduct('Taxi seguro.') 
      
     # Prueba 51
     def testSearchIdNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         oObjective   = objective()
         oObjective.insertObjective(None,1)
         result = oObjective.searchIdObjective(None)
         self.assertEqual(result,[],"Válido")    
         aBackLog.deleteProduct('Taxi seguro.')
           