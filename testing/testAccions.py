# -*- coding: utf-8 -*-. 

import unittest

from accionsDummy import *

class TestAccions(unittest.TestCase):
    
     #############################################      
     #   Suite de Pruebas para insertAccion   #
     #############################################
         
     # Caso Inicial
 
     # Prueba 1
     def testInserAccionExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         aAcc = accions()
         aAcc.insertAccion('Reservar un taxi.',1)
         aAcc.deleteAccion('Reservar un taxi.')
         aBackLog.deleteProduct('Reservar un taxi.')        
    # Casos Normales
    
    # Prueba 2
     def testInsertAccionElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc   = accions()
        result = aAcc.insertAccion('Permite elegir.',1)
        self.assertTrue(result)
        aAcc.deleteAccion('Permite elegir')
        aBackLog.deleteProduct('Taxi seguro.')
                 
    # Prueba 3
     def testInsertAccionRepeatedElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        aAcc   = accions()
        result = aAcc.insertAccion('Permite elegir.',1)
        result1 = aAcc.insertAccion('Permite elegir.',1)
        self.assertFalse(result1)
        aAcc.deleteAccion('Permite seleccionar.')
        aBackLog.deleteProduct('Taxi seguro.')
              
    # Casos Fronteras
     
     # Prueba 4
     def test4InsertAccionShortDesc0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result = aAcc.insertAccion('',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
         
          
    # Prueba 5
     def testInsertAccionLongDesc1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result = aAcc.insertAccion('A',1)
         self.assertTrue(result)
         aAcc.deleteAccion('A')
         aBackLog.deleteProduct('Taxi seguro.')
      
    # Prueba 6
     def test6InsertAccionLongDesc140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         aAcc   = accions()
         result = aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem',1)
         self.assertTrue(result)
         aAcc.deleteAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
         aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 7
     def testInsertObjectiveLongDesc141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result = aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
     
    # Prueba 8
     def testInsertAccionIdBackLogInvalid(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         aAcc   = accions()
         result  =aAcc.insertAccion('Movlizarme desde mi casa',0)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
     
     
     # Casos Esquinas
      
    # Prueba 9
     def testInsertAccionIdBackLogNoExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result  =aAcc.insertAccion('Trasladarse rápido',2)
         self.assertFalse(result)
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
     
    # Prueba 10
     def testInsertAccionLongDesc140AndIdBackLogNoExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result = aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin proble1',3)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
     
    # Casos Maliciosos
     
    # Prueba 11
     def testInsertNotString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result = aAcc.insertAccion(4350,1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 12
     def testInsertNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         result = aAcc.insertAccion(None,1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
          
 
     #############################################      
     #   Suite de Pruebas para searchAccion   #
     #############################################
      
     # Caso Inicial
      
    # Prueba 13 
     def testsearchAccionExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc = accions()
         aAcc.insertAccion('Permite reservar un taxi',1)
         aAcc.searchAccion('Permite reservar un taxi')
          
    # Casos Fronteras
      
    # Prueba 14
     def testsearchAccionShortDesc0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.        
         aAcc   = accions()
         aAcc.insertAccion('',1)
         result = aAcc.searchAccion('')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.')
     
    # Prueba 15
     def test_15searchAccionShortDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.searchAccion('A')
        self.assertTrue(result)
        aAcc.deleteAccion('A')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 16
     def testsearchAccionShortDesc140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem',1)
        result = aAcc.searchAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        self.assertNotEqual(result,[],"Accion no encontrada")
        aAcc.deleteAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 17
     def testsearchAccionShortDesc141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1)

         result = aAcc.searchAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema')
         self.assertFalse(result, "Accion Encontrada.")
         aBackLog.deleteProduct('Taxi seguro.')
 
    # Caso Normal
     def testsearchAccionDescNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchAccion('Comunicarse via correo electronico')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
 
    # Casos Maliciosos
      
     # Prueba 19
     def testsearchAccionNotString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aAcc   = accions()
         aAcc.insertAccion(4350,1)
         result = aAcc.searchAccion(4350)
         self.assertEqual(result, [],'Accion Encontrada')
         aBackLog.deleteProduct('Taxi seguro.')

     #Prueba 20
      
     def testFindNameNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.   
         aAcc   = accions()
         result = aAcc.searchAccion(None)
         self.assertEqual(result, [],'Accion Encontrada')
         aBackLog.deleteProduct('Taxi seguro.')
                         
     #############################################      
     #   Suite de Pruebas para updateAccion   #
     #############################################  
    # Caso Inicial
     
    # Prueba 21
     def testupdateAccionExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.   
        aAcc   = accions()
        aAcc.insertAccion('reservar un taxi.',1)
        aAcc.updateAccion('reservar un taxi.','reservar un taxi o varios.')
        aBackLog.deleteProduct('Taxi seguro.')  

    # Casos Normales
     
     def testupdateAccionDesc(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         aAcc.insertAccion('Permite elegir.',1)
         result = aAcc.updateAccion('Permite elegir.','Atención las 24 horas del día')
         self.assertTrue(result)
         aAcc.deleteAccion('Atención las 24 horas del día')
         aBackLog.deleteProduct('Taxi seguro.')
          
     def testupdateAccionDescNOtExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
        aAcc = accions()
        result = aAcc.updateAccion('Llegar lo mas pronto posible','Ir comodo y seguro')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Fronteras
       
    # Prueba 24
     def testupdateAccionLeftLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.updateAccion('A','Buscar al cliente donde esté')
        self.assertTrue(result)
        aAcc.deleteAccion('Buscar al cliente donde esté')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 25
     def testupdateAccionLeftLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Buscar al cliente donde esté',1)
        result = aAcc.updateAccion('Buscar al cliente donde esté','A')
        self.assertTrue(result)
        aAcc.deleteAccion('A')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 26         
     def testupdateAccionRightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Atención las 24 horas del día',1)
        result = aAcc.updateAccion('Atención las 24 horas del día',140*'T')
        self.assertTrue(result)    
        aAcc.deleteAccion(140*'T')
        aBackLog.deleteProduct('Taxi seguro.')
 
    # Prueba 27
     def testupdateAccionLeftLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(140*'T',1)
        result = aAcc.updateAccion(140*'T','Atención las 24 horas del día')
        self.assertTrue(result)
        aAcc.deleteAccion('Atención las 24 horas del día')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Esquinas
      
    # Prueba 28
     def testupdateAccionLeftLen1RightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.updateAccion('A',140*'Us')
        self.assertFalse(result)
        aAcc.deleteAccion('A')
        aBackLog.deleteProduct('Taxi seguro.') 
 
    # Prueba 29
     def testupdateAccionLeftLen140RightLen140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aAcc   = accions()
         aAcc.insertAccion(140*'Us',1)
         result = aAcc.updateAccion(140*'Us', 140*'Ma')
         self.assertFalse(result) 
         aAcc.deleteAccion(140*'Us')
         aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 30
     def testupdateAccionLeftLen140RightLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem',1)
        result = aAcc.updateAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem','M')
        self.assertTrue(result)
        aAcc.deleteAccion('A')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 31
     def testupdateAccionLeftLen1RightLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('X',1)
        result = aAcc.updateAccion('X','U')
        self.assertTrue(result)
        aAcc.deleteAccion('U')
        aBackLog.deleteProduct('Taxi seguro.') 
          
    # Casos Maliciosos
      
    # Prueba 32
     def testupdateSameName(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Reservar un taxi.',1)
        result = aAcc.updateAccion('Reservar un taxi.','Reservar un taxi.')
        self.assertFalse(result,"Modificación Válida")
        aAcc.deleteAccion('Reservar un taxi.')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 33
     def testupdateAccionLeftLen0RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('',1)
        result = aAcc.updateAccion('','Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problems')
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion('')
        aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 34
     def testupdateAccionLeftLen141RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema',1)
        result = aAcc.updateAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema',25*'Ma' + 's')
        self.assertFalse(result, "Modificación Válida") 
        aAcc.deleteAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 35
     def testupdateAccionLeftLen141RightLen0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas',1)
        result = aAcc.updateAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas','')
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas')
        aBackLog.deleteProduct('Taxi seguro.')  

    # Prueba 36
     def testupdateAccionLeftNoneRightValidString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.updateAccion(None,'Comunicarse via correo electronico')
        self.assertFalse(result,"Modificación válida") 
        aBackLog.deleteProduct('Taxi seguro.')  

    # Prueba 37
     def testupdateAccionLeftValidStringRightNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Reservar un taxi.',1)
        result = aAcc.updateAccion('Reservar un taxi.',None)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion('Reservar un taxi.')
        aBackLog.deleteProduct('Taxi seguro.')    
          
    #############################################      
    #       Suite de Pruebas para deleteAccion      #
    ############################################# 
      
    # Caso Inicial
      
    # Prueba 38
     def testDeleteAccionExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Reservar un Taxi',1)
        aAcc.deleteAccion('Reservar un Taxi')
        aBackLog.deleteProduct('Taxi seguro.')
          
        # Casos Normales
  
    # Prueba 39
     def testDeleteAccion(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('U')
        result = aAcc.deleteAccion('U')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')
 
    # Prueba 40      
     def testDeleteAccion(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('yyy',1)
        result = aAcc.deleteAccion('xxx')
        self.assertFalse(result)
        aAcc.deleteAccion('yyy')
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Fronteras
      
    # Prueba 41
     def testDeleteAccion1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.deleteAccion('A')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Casos Maliciosos
  
    # Prueba 42
     def testDeleteAccionInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion('')
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 43
     def testDeleteAccionNotString(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
       # Inicio de la prueba.
       aAcc   = accions()
       aAcc.insertAccion(12345,1)
       result = aAcc.deleteAccion(12345)
       self.assertFalse(result,"Id no válido")
       aBackLog.deleteProduct('Taxi seguro.')

    # Prueba 44    
     def test_44DeleteAccionNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion('Legar rápido')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
                 
          

