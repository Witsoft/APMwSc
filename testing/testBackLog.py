# -*- coding: utf-8 -*-. 

import unittest

import os
import sys

from modelDummy   import *
from backLogDummy import *
from roleDummy import *
from accionsDummy import *
from objectiveDummy import *

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
         
       
    #############################################      
     #   Suite de Pruebas para modifyDescription  #
     #############################################  
     
    # Caso Inicial
    
      # Prueba 24
    def testmodifyDescriptionExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.')
        # Inicio de la prueba.   
        aBackLog.modifyDescription('Taxi seguro.','reservar un taxi o varios.')
        aBackLog.deleteProduct('reservar un taxi o varios.')  
        
    # Casos Normales
    
    # Prueba 25 
    def testmodifyDescription(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Permite localizar un taxi')
         # Inicio de la prueba.
         result = aBackLog.modifyDescription('Permite localizar un taxi','Atención las 24 horas del día')
         self.assertTrue(result)
         aBackLog.deleteProduct('Atención las 24 horas del día')

    # Prueba 26 
    def testmodifyDescriptionNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi Seguro')
         # Inicio de la prueba.
        result = aBackLog.modifyDescription('Llegar lo mas pronto posible','Ir comodo y seguro')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi Seguro')
        
    # Casos Fronteras
       
    # Prueba 27
    def testmodifyDescriptionRigthLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('A')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription('A','Buscar al cliente donde esté')
        self.assertTrue(result)
        aBackLog.deleteProduct('Buscar al cliente donde esté')
        
    # Prueba 28
    def testmodifyDescriptionLeftLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Buscar al cliente donde esté')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription('Buscar al cliente donde esté','A')
        self.assertTrue(result)
        aBackLog.deleteProduct('Buscar al cliente donde esté')
        
    # Prueba 29        
    def testmodifyDescriptionRightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Atención las 24 horas del día')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription('Atención las 24 horas del día',140*'T')
        self.assertTrue(result)    
        aBackLog.deleteProduct(140*'T')
        
    # Prueba 30
    def testmodifyDescriptionLeftLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(140*'T')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription(140*'T','Atención las 24 horas del día')
        self.assertTrue(result)
        aBackLog.deleteProduct('Atención las 24 horas del día')

    # Casos Maliciosos
    
    # Prueba 31
    def testmodifyDescriptionSameName(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Reservar un taxi.')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription('Reservar un taxi.','Reservar un taxi.')
        self.assertTrue(result,"Modificación Válida")
        aBackLog.deleteProduct('Reservar un taxi.')
        
   # Prueba 32
    def testmodifyDescriptionLeftLen0RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription('','Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problems')
        self.assertFalse(result, "Modificación válida")
        
    # Prueba 33
    def testmodifyDescriptionLeftValidStringRightNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Reservar un taxi.')
        # Inicio de la prueba.
        result = aBackLog.modifyDescription('Reservar un taxi.',None)
        self.assertFalse(result, "Modificación válida") 
        aBackLog.deleteProduct('Reservar un taxi.')    
      
        
     ####################################################      
     #   Suite de Pruebas para actorsAsociatedToProduct #
     ####################################################  
    
    # Casos Frontera
    
    # Prueba 34    
    def testActorAsociatedBackLogExists(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro')
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct(1)
        arole.deleteRole('Role1')
        arole.deleteRole('Role2')
        aBackLog.deleteProduct('Taxi Seguro')     
                                       
    # Prueba 35
    def testActorAsociatedBackLogTrue(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro')
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',1)
        result = aBackLog.actorsAsociatedToProduct(1)
        self.assertNotEqual([],result)
        arole.deleteRole('Role1')
        arole.deleteRole('Role2')
        aBackLog.deleteProduct('Taxi Seguro')                                        
               
    # Prueba 36                                   
    def testActorAsociatedBackLogFalse(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro')
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct(3)
        self.assertEqual([],result)
        arole.deleteRole('Role1')
        aBackLog.deleteProduct('Taxi Seguro')

    # Casos Malicia
    
    # Prueba 37
    def testActorAsociatedBackLogNoRole(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro')
        arole.insertRole('Role1',None,1)
        result = aBackLog.actorsAsociatedToProduct(1)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Taxi Seguro')
        
    # Prueba 38    
    def testActorAsociatedBackLogNoneId(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro')
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct(None)
        self.assertEqual([],result)
        arole.deleteRole('Role1')
        aBackLog.deleteProduct('Taxi Seguro')
        
    # Prueba 39    
    def testActorAsociatedBackLogString(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro')
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct('')
        self.assertEqual([],result)
        arole.deleteRole('Role1')
        aBackLog.deleteProduct('Taxi Seguro')

        
     ####################################################      
     #   Suite de Pruebas para accionAsociatedToProduct #
     ####################################################  
    
    # Casos Frontera
    
    # Prueba 40    
    def testAccionAsociatedBackLogExists(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro')
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct(1)
        oAccion.deleteAccion('nuevo accions1')
        oAccion.deleteAccion('nuevo accions2')
        aBackLog.deleteProduct('Taxi Seguro')     
    
    # Prueba 41                                   
    def testAccionAsociatedBackLogTrue(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro')
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',1)
        result = aBackLog.accionsAsociatedToProduct(1)
        self.assertNotEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        oAccion.deleteAccion('nuevo accions2')
        aBackLog.deleteProduct('Taxi Seguro')                                        
               
    # Prueba 42                                   
    def testAccionAsociatedBackLogFalse(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro')
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct(3)
        self.assertEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        aBackLog.deleteProduct('Taxi Seguro')

    # Casos Malicia
    
    # Prueba 43
    def testAccionAsociatedBackLogNoAccion(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro')
        oAccion.insertAccion(None,1)
        result = aBackLog.accionsAsociatedToProduct(1)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Taxi Seguro')
        
    # Prueba 44    
    def testAccionAsociatedBackLogNoneId(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro')
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct(None)
        self.assertEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        aBackLog.deleteProduct('Taxi Seguro')
     
    # Prueba 45    
    def testAccionAsociatedBackLogString(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro')
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct('')
        self.assertEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        aBackLog.deleteProduct('Taxi Seguro')

        
     ####################################################      
     #   Suite de Pruebas para objectiveAsociatedToProduct #
     ####################################################  
    
    # Casos Frontera
    
    # Prueba 46    
    def testObjectiveAsociatedBackLogExists(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro')
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct(1)
        oObjective.deleteObjective('nuevo objectives1')
        oObjective.deleteObjective('nuevo objectives2')
        aBackLog.deleteProduct('Taxi Seguro')     
               
    # Prueba 47                                   
    def testObjectiveAsociatedBackLogTrue(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro')
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',1)
        result = aBackLog.objectivesAsociatedToProduct(1)
        self.assertNotEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        oObjective.deleteObjective('nuevo objectives2')
        aBackLog.deleteProduct('Taxi Seguro')                                        
               
    # Prueba 48                                   
    def testObjectiveAsociatedBackLogFalse(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro')
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct(3)
        self.assertEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        aBackLog.deleteProduct('Taxi Seguro')

    # Casos Malicia
    
    # Prueba 49
    def testObjectiveAsociatedBackLogNoObjective(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro')
        oObjective.insertObjective(None,1)
        result = aBackLog.objectivesAsociatedToProduct(1)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Taxi Seguro')
        
    # Prueba 50    
    def testObjectiveAsociatedBackLogNoneId(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro')
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct(None)
        self.assertEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        aBackLog.deleteProduct('Taxi Seguro')
    
    # Prueba 51    
    def testObjectiveAsociatedBackLogString(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro')
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct('')
        self.assertEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        aBackLog.deleteProduct('Taxi Seguro')              