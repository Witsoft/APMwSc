# -*- coding: utf-8 -*-. 

import unittest

import os
import sys

from modelDummy   import *
from backLogDummy import *

class TestclsBackLog(unittest.TestCase):
    
    #############################################      
    #    Suite de Pruebas para findDescription  #
    #############################################

    # Caso Inicial
    
    # Prueba 1
    def testFindDescription(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Permite localizar un taxi')
        aBackLog.findDescription('Permite localizar un taxi')
        aBackLog.deleteProduct('Permite localizar un taxi')   
        
       # Casos Normales
       
    # Prueba 2
    def testFindDescNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
         # Inicio de la prueba.
        result = aBackLog.findDescription('Comunicarse via correo electronico')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
          
        
    # Casos Fronteras
      
    # Prueba 3
    def testfindDescriptionShortDesc0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro')
        # Inicio de la prueba.        
        result = aBackLog.findDescription('')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 4
    def testfindDescriptionShortDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('T')
        # Inicio de la prueba
        result = aBackLog.findDescription('T')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro.')
        
    # Prueba 5
    def testfindDescriptionShortDesc140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni lim')
         # Inicio de la prueba.
        result = aBackLog.findDescription('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni lim')
        self.assertNotEqual(result,[],"Accion no encontrada")
        aBackLog.deleteProduct('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni lim')

    # Prueba 6
    def testfindDescriptionShortDesc141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni limi')
        # Inicio de la prueba.
        result = aBackLog.findDescription('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni limi')
        self.assertFalse(result, "Accion Encontrada.")
        aBackLog.deleteProduct('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni limi')
          

    
   # Casos Maliciosos
      
     # Prueba 7
    def testfindDescriptionNotString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba. 
        result = aBackLog.findDescription(4350)
        self.assertEqual(result, [],'Accion Encontrada')
        aBackLog.deleteProduct('Taxi seguro.')
        
     #Prueba 8
      
    def testFindDescriptionNoneString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.   
        result = aBackLog.findDescription(None)
        self.assertEqual(result, [],'Accion Encontrada')
        aBackLog.deleteProduct('Taxi seguro.')
        
     #############################################      
     #   Suite de Pruebas para insertBackLog  #
     #############################################
     
       # Caso Inicial
    
     # Prueba 9
    def testInserBackLogExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.')
         aBackLog.deleteProduct('Reservar un taxi.')  
         
    # Casos Normal
    
    # Prueba 10
    def testInsertBackLogElement(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('Permite localizar un taxi')
        self.assertTrue(result)
        aBackLog.deleteProduct('Permite localizar un taxi')
    

     #Casos Frontera
    
    # Prueba 11   
    def testInsertBackLoglong140(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog(140*'a')
        self.assertTrue(result)
        aBackLog.deleteProduct(140*'a')
    
    # Prueba 12    
    def testInsertBackloglong141(self):    
        aBackLog = backLog()
        result = aBackLog.insertBackLog(140*'a' + 'b')
        self.assertFalse(result)
        aBackLog.deleteProduct(140*'a' + 'b')
    
    # Prueba 13
    def testInsertBackloglong1(self):    
        aBackLog = backLog()
        result = aBackLog.insertBackLog('a')
        self.assertTrue(result)
        aBackLog.deleteProduct('a')
        
    # Prueba 14
    def testInsertBackloglong0(self):    
        aBackLog = backLog()
        result = aBackLog.insertBackLog('')
        self.assertFalse(result)
        aBackLog.deleteProduct('')
    
     #Casos Malicia
    
    # Prueba 15   
    def testInsertBacklogNone(self):    
        aBackLog = backLog()
        result = aBackLog.insertBackLog(None)
        self.assertFalse(result)
        aBackLog.deleteProduct(None)
        
    # Prueba 16    
    def testInsertBacklogNoString(self):    
        aBackLog = backLog()
        result = aBackLog.insertBackLog(140)
        self.assertFalse(result)
        aBackLog.deleteProduct(140)                     
        
     #############################################      
     #   Suite de Pruebas para deleteProduct  #
     #############################################
     
    # Caso Inicial
      # Prueba 17
    def testDeleteProductExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        aBackLog.deleteProduct('Taxi seguro.')
       
           # Casos Normales
  
    # Prueba 18
    def testDeleteProduct(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Permite localizar un taxi')
        # Inicio de la prueba.
        result = aBackLog.deleteProduct('Permite localizar un taxi')
        self.assertTrue(result)
        
    # Prueba 19      
    def testDeleteProductNoExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Reservar un taxi')
        # Inicio de la prueba.
        result = aBackLog.deleteProduct('Taxi seguro.')
        self.assertFalse(result)
       
        # Casos Fronteras
      
    # Prueba 20
    def testDeleteProductString1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('T')
        # Inicio de la prueba.
        result = aBackLog.deleteProduct('T')
        self.assertTrue(result)
        
    # Prueba 21
    def testDeleteProductString140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni lim')
        # Inicio de la prueba.
        result = aBackLog.deleteProduct('Taxi seguro que permite localizar un taxi a ' +
                                'cualquier hora del dia, para poder dirigirse a '+
                                'cualquier lugar de la ciudad sin problemas ni lim')
        self.assertTrue(result)
       
    # Casos Maliciosos
  
    # Prueba 22
    def testDeleteProductInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.
        result = aBackLog.deleteProduct('')
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro.')
       
    # Prueba 23
    def testDeleteProductNotString(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('Permite localizar un taxi')
       # Inicio de la prueba.
       result = aBackLog.deleteProduct(12345)
       self.assertFalse(result,"Id no válido")
       aBackLog.deleteProduct('Permite localizar un taxi')
      



       

       

       
                  