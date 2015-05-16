# -*- coding: utf-8 -*-. 

'''
Created on 15/05/2015
'''

import unittest
import os
import sys

# Ruta que permite utilizar el módulo objective.py
sys.path.append('../app/scrum')

from objective import *
from backLog   import * 

class TestObjective(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertObjective   #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def test1InserObjectiveExists(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         aObj = objective()
         aObj.insertObjective('Permite reservar un taxi.',1)
      
         
    # Casos Normales
           
     # Prueba 2     
     def test2InsertObjectiveElement(self):
         aObj   = objective()
         result = aObj.insertObjective('Permite elegir.',1)
         self.assertTrue(result)
                     
     # Prueba 3
     def test3InsertRepeatedElement(self):
         aObj   = objective()
         result = aObj.insertObjective('Permite elegir.',1)
         self.assertFalse(result)
      
         
    # Casos Fronteras
    
     # Prueba 4
     def test4InsertObjectiveShortDesc0(self):
         aObj   = objective()
         result = aObj.insertObjective('',1)
         self.assertFalse(result)
         
     # Prueba 5
     def test5InsertObjectiveLongDesc1(self):
         aObj   = objective()
         result = aObj.insertObjective('P',1)
         self.assertTrue(result)
      
     # Prueba 6
     def test6InsertObjectiveLongDesc140(self):
         aObj   = objective()
         result = aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .',1)
         self.assertTrue(result)
         
     # Prueba 7
     def test7InsertObjectiveLongDesc141(self):
         aObj   = objective()
         result = aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2',1)
         self.assertFalse(result)
         
         
    # Casos Maliciosos
      
     # Prueba 8
     def test8InsertNotString(self):
         aObj   = objective()
         result = aObj.insertObjective(1254,1)
         self.assertFalse(result,"Objetivo agregado.")
 
     # Prueba 9
     def test9InsertNoneString(self):
         aObj   = objective()
         result = aObj.insertObjective(None,1)
         self.assertFalse(result,"Objetivo agregado.")
        
    
     #############################################      
     #   Suite de Pruebas para searchObjective   #
     #############################################
     
     # Caso Inicial
     
     # Prueba 10 
     def test_10searchObjectiveExists(self):
         aObj = objective()
         aObj.searchObjective('Permite reservar un taxi')
               
               
     # Casos Fronteras
     
     # Prueba 11
     def test_11searchObjectiveShortDesc0(self):
         aObj   = objective()
         result = aObj.searchObjective('')
         self.assertFalse(result, "Objetivo Encontrado.")
           
     # Prueba 12
     def test_12searchObjectiveShortDesc1(self):
         aObj   = objective()
         result = aObj.searchObjective('P')
         self.assertNotEqual(result,[],"Objetivo no encontrado")
      
     # Prueba 13
     def test_13searchObjectiveShortDesc140(self):
         aObj   = objective()
         result = aObj.searchObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertNotEqual(result,[],"Objetivo no encontrado")
           
     # Prueba 14
     def test_14searchObjectiveShortDesc141(self):
         aObj   = objective()
         result = aObj.searchObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result, "Objetivo Encontrado.")
         
         
     # Casos Maliciosos
     
     # Prueba 15
     def test_15searchObjectiveNotString(self):
         aObj   = objective()
         result = aObj.searchObjective(1245)
         self.assertFalse(result, "Objetivo Encontrado.")
      
     # Prueba 16
     def test_16FindNameNoneString(self):
         aObj   = objective()
         result = aObj.searchObjective(None)
         self.assertFalse(result,"Objetivo Encontrado.") 
                    
     #############################################      
     #   Suite de Pruebas para updateObjective   #
     #############################################  
 
     # Caso Inicial
    
     # Prueba 17
     def test_17updateObjectiveExists(self):
         aObj   = objective()
         aObj.updateObjective('Permite reservar un taxi.','Permite reservar un taxi o varios.')

