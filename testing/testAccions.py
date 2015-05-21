# -*- coding: utf-8 -*-. 

import unittest

from accionsDummy import *

class TestAccions(unittest.TestCase):
    
     #############################################      
     #   Suite de Pruebas para insertAccion   #
     #############################################
         
     # Caso Inicial
 
     # Prueba 1
     def test1InserAccionExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         aAcc = accions()
         aAcc.insertAccion('Reservar un taxi.',1)
                  
    # Casos Normales
    
    # Prueba 2
     def test2InsertAccionElement(self):
        aAcc   = accions()
        result = aAcc.insertAccion('Permite elegir.',1)
        self.assertTrue(result)
                
     # Prueba 3
     def test3InsertAccionRepeatedElement(self):
         aAcc   = accions()
         result = aAcc.insertAccion('Permite elegir.',1)
         self.assertFalse(result)
             
    # Casos Fronteras
    
     # Prueba 4
     def test4InsertAccionShortDesc0(self):
         aAcc   = accions()
         result = aAcc.insertAccion('',1)
         self.assertFalse(result)
         
     # Prueba 5
     def test5InsertAccionLongDesc1(self):
         aAcc   = accions()
         result = aAcc.insertAccion('A',1)
         self.assertTrue(result)
     
     # Prueba 6
     def test6InsertAccionLongDesc140(self):
         aAcc   = accions()
         result = aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem',1)
         self.assertTrue(result)
         
    # Prueba 7
     def test7InsertObjectiveLongDesc141(self):
         aAcc   = accions()
         result = aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1)
         self.assertFalse(result)
    
    # Prueba 8
     def test8InsertAccionIdBackLogInvalid(self):
         aAcc   = accions()
         result  =aAcc.insertAccion('Movlizarme desde mi casa',0)
         self.assertFalse(result)
    
    
     # Casos Esquinas
     
    # Prueba 9
     def test9InsertAccionIdBackLogNoExists(self):
         aAcc   = accions()
         result  =aAcc.insertAccion('Trasladarse rápido',2)
         self.assertFalse(result)
    
    # Prueba 10
     def test_10InsertAccionLongDesc140AndIdBackLogNoExists(self):
         aAcc   = accions()
         result = aAcc.insertAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin proble1',3)
         self.assertFalse(result)
    
    # Casos Maliciosos
    
    # Prueba 11
     def test_11InsertNotString(self):
         aAcc   = accions()
         result = aAcc.insertAccion(4350,1)
         self.assertFalse(result)
         
    # Prueba 12
     def test_12InsertNoneString(self):
         aAcc   = accions()
         result = aAcc.insertAccion(None,1)
         self.assertFalse(result)
         

     #############################################      
     #   Suite de Pruebas para searchAccion   #
     #############################################
     
     # Caso Inicial
     
    # Prueba 13 
     def test_13searchAccionExists(self):
         aAcc = accions()
         aAcc.searchAccion('Permite reservar un taxi')
         
     # Casos Fronteras
     
     # Prueba 14
     def test_14searchAccionShortDesc0(self):
         aAcc   = accions()
         result = aAcc.searchAccion('')
         self.assertFalse(result)
    
     # Prueba 15
     def test_15searchAccionShortDesc1(self):
         aAcc   = accions()
         result = aAcc.searchAccion('A')
         self.assertTrue(result)
         
     # Prueba 16
     def test_16searchAccionShortDesc140(self):
         aAcc   = accions()
         result = aAcc.searchAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem')
         self.assertNotEqual(result,[],"Accion no encontrada")
         
    # Prueba 17
     def test_17searchAccionShortDesc141(self):
         aAcc   = accions()
         result = aAcc.searchAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema')
         self.assertFalse(result, "Accion Encontrada.")

    # Caso Normal
     def test_18searchAccionDescNotExist(self):
         aAcc   = accions()
         result = aAcc.searchAccion('Comunicarse via correo electronico')
         self.assertFalse(result)
         

    # Casos Maliciosos
     
     # Prueba 19
     def test_19searchAccionNotString(self):
         aAcc   = accions()
         result = aAcc.searchAccion(4350)
         self.assertEqual(result, [],'Accion Encontrada')
         
     #Prueba 20
     
     def test_20FindNameNoneString(self):
         aAcc   = accions()
         result = aAcc.searchAccion(None)
         self.assertEqual(result, [],'Accion Encontrada')
      
                        
     #############################################      
     #   Suite de Pruebas para updateAccion   #
     #############################################  
    # Caso Inicial
    
     # Prueba 17
     def test_21updateAccionExists(self):
         aAcc   = accions()
         aAcc.updateAccion('reservar un taxi.','reservar un taxi o varios.')
         
    # Casos Normales
    
     def test_22updateAccionName(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Permite elegir.','Atención las 24 horas del día')
         self.assertTrue(result)
         
     def test_23updateAccionDescNOtExist(self):
         aAcc = accions()
         result = aAcc.updateAccion('Llegar lo mas pronto posible','Ir comodo y seguro')
         self.assertFalse(result)
         
     # Casos Fronteras
      
     # Prueba 24
     def test_23updateAccionLeftLen1(self):
         aAcc   = accions()
         result = aAcc.updateAccion('A','Buscar al cliente donde esté')
         self.assertTrue(result)
         
     # Prueba 25
     def test_25updateAccionLeftLen1(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Buscar al cliente donde esté','A')
         self.assertTrue(result)
         
     # Prueba 26         
     def test_26updateAccionRightLen140(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Atención las 24 horas del día',140*'T')
         self.assertTrue(result)    

     # Prueba 27
     def test_27updateAccionLeftLen140(self):
         aAcc   = accions()
         result = aAcc.updateAccion(140*'T','Atención las 24 horas del día')
         self.assertTrue(result)
         
     # Casos Esquinas
     
     # Prueba 28
     def test_28updateAccionLeftLen1RightLen140(self):
         aAcc   = accions()
         result = aAcc.updateAccion('A',140*'Us')
         self.assertFalse(result) 

    # Prueba 29
     def test_29updateAccionLeftLen140RightLen140(self):
         aAcc   = accions()
         result = aAcc.updateAccion(140*'Us', 140*'Ma')
         self.assertFalse(result) 
         
    # Prueba 30
     def test_30updateAccionLeftLen140RightLen1(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem','M')
         self.assertTrue(result)
         
     # Prueba 31
     def test_31updateAccionLeftLen1RightLen1(self):
         aAcc   = accions()
         result = aAcc.updateAccion('M','U')
         self.assertTrue(result) 
         
     # Casos Maliciosos
     
     # Prueba 32
     def test_32updateSameName(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Reservar un taxi.','Reservar un taxi.')
         self.assertFalse(result,"Modificación Válida")
         
     # Prueba 33
     def test_33updateAccionLeftLen0RightLen141(self):
         aAcc   = accions()
         result = aAcc.updateAccion('','Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problems')
         self.assertFalse(result, "Modificación válida") 
         
     # Prueba 34
     def test_34updateAccionLeftLen141RightLen141(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',25*'Ma' + 's')
         self.assertFalse(result, "Modificación Válida") 
         
     # Prueba 35
     def test_35updateAccionLeftLen141RightLen0(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema'+ 's','')
         self.assertFalse(result, "Modificación válida") 
         
     # Prueba 36
     def test_36updateAccionLeftNoneRightValidString(self):
         aAcc   = accions()
         result = aAcc.updateAccion(None,'Comunicarse via correo electronico')
         self.assertFalse(result,"Modificación válida") 
         
     # Prueba 37
     def test_37updateAccionLeftValidStringRightNone(self):
         aAcc   = accions()
         result = aAcc.updateAccion('Reservar un taxi.',None)
         self.assertFalse(result, "Modificación válida") 
           
         
     #############################################      
     #       Suite de Pruebas para deleteAccion      #
     ############################################# 
     
     # Caso Inicial
     
     # Prueba 38
     def test_38DeleteAccionExists(self):
         aAcc   = accions()
         aAcc.deleteAccion('Reservar un Taxi')
         
         # Casos Normales
 
     # Prueba 39
     def test_39DeleteAccion(self):
         aAcc   = accions()
         result = aAcc.deleteAccion('U')
         self.assertTrue(result)

     # Prueba 40      
     def test_40DeleteAccion(self):
         aAcc   = accions()
         result = aAcc.deleteAccion('xxx')
         self.assertFalse(result)
         
     # Casos Fronteras
     
     # Prueba 41
     def test_41DeleteAccion1(self):
         aAcc   = accions()
         result = aAcc.deleteAccion('A')
         self.assertTrue(result)
         
     # Casos Maliciosos
 
     # Prueba 42
     def test_42DeleteAccionInvalid(self):
         aAcc   = accions()
         result = aAcc.deleteAccion('')
         self.assertFalse(result,"Id no válido")
         
     # Prueba 43
     def test_43DeleteAccionNotString(self):
         aAcc   = accions()
         result = aAcc.deleteAccion(12345)
         self.assertFalse(result,"Id no válido")
    
     # Prueba 44    
     def test_44DeleteAccionNotExist(self):
         aAcc   = accions()
         result = aAcc.deleteAccion('A')
         self.assertFalse(result)
                
         

