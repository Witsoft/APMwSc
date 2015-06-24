# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from login import *

class TestLogin(unittest.TestCase):

    #############################################      
    #    Suite de Pruebas para validPassword   #
    ############################################

    # Prueba 1
    def testValid8Caracteres(self):
        object = login()
        string = "acD34@.R"
        result = object.validPassword(string) 
        self.assertTrue(result)
        
    # Prueba 2
    def testValid16Caracteres(self):
        object = login()
        string = "acD34@.RF23pwQsx"
        result = object.validPassword(string) 
        self.assertTrue(result)

    # Prueba 3
    def testValidStringVacio(self):
        object = login()
        string = ""
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    # Prueba 4
    def testValidMasGrande(self):
        object = login()
        string = ((2**31)-1)*"p"
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    # Prueba Esquina
    
    # Prueba 5
    def testValid7Caracteres(self):
        object = login()
        string = "acD34@."
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    # Prueba 6
    def testValid17Caracteres(self):
        object = login()
        string = "acD34@.1235ufjD.u"
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    # Prueba Normal
    
    # Prueba 7
    def testNoValid1Char(self):
        object = login()
        string = "a"
        result = object.validPassword(string) 
        self.assertFalse(result)
    
    # Prueba 8
    def testValid9Caracteres(self):
        object = login()
        string = "acD34@.12"
        result = object.validPassword(string) 
        self.assertTrue(result)
        
    # Prueba 9
    def testValid15Caracteres(self):
        object = login()
        string = "acD34@.12e87@sh"
        result = object.validPassword(string) 
        self.assertTrue(result)
        
# Fin de Casos Login 