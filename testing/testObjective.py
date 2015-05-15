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
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         aObj = objective()
         aObj.insertObjective('Permite reservar un taxi.',1)
         
    # Casos Normales
           
     # Prueba 2     
     def test2InsertObjectiveElement(self):
         aObj = objective()
         result = aObj.insertObjective('Permite elegir.',1)
         self.assertTrue(result)
                     
     # Prueba 3
     #def test3InsertRepeatedElement(self):
     #    role   = clsRole()
     #    result = role.insertRole('Team Member')
     #    self.assertFalse(result, "Elemento insertado.")
         
           