# -*- coding: utf-8 -*-. 

import unittest

from accionsDummy import *

class TestAccions(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertAccion      #
    #############################################
          
    # Caso Inicial
  
    # Prueba 1
    def testInserAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        aAcc = accions()
        aAcc.insertAccion('Atacar puntos de vida',1)
        aAcc.deleteAccion('Atacar puntos de vida')
        aBacklog.deleteProduct('Batalla')        

    # Casos Normales
     
    # Prueba 2
    def testInsertAccionElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Permite elegir',1)
        self.assertTrue(result)
        aAcc.deleteAccion('Permite elegir')
        aBacklog.deleteProduct('Batalla')
                  
    # Prueba 3
    def testInsertAccionRepeatedElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Permite elegir.',1)
        result1 = aAcc.insertAccion('Permite elegir.',1)
        self.assertFalse(result1)
        aAcc.deleteAccion('Permite elegir')
        aBacklog.deleteProduct('Batalla')
               
    # Casos Fronteras
      
    # Prueba 4
    def testInsertAccionShortDesc0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
          
           
    # Prueba 5
    def testInsertAccionLongDesc1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('A',1)
        self.assertTrue(result)
        aAcc.deleteAccion('A')
        aBacklog.deleteProduct('Batalla')
       
    # Prueba 6
    def testInsertAccionLongDesc140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(20*'Llamare',1)
        self.assertTrue(result)
        aAcc.deleteAccion(20*'Llamare')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 7
    def testInsertAccionLongDesc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(20*'Llamare' + 's',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
      
    # Prueba 8
    def testInsertAccionIdBackLogInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result  =aAcc.insertAccion('Atacar al mas debil',0)
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
        
    # Casos Esquinas
       
    # Prueba 9
    def testInsertAccionIdBacklogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc    = accions()
        result  = aAcc.insertAccion('Defender con fuerza',2)
        self.assertFalse(result)
        #Eliminacion del elemento insertado.
        aBacklog.deleteProduct('Batalla')

    # Prueba 10
    def testInsertAccionLongDesc140AndIdBackLogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(20*'Llamare',3)
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
                      
    # Casos Maliciosos
      
    # Prueba 11
    def testInsertNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(4350,1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 12
    def testInsertNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(None,1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
           
    #############################################      
    #   Suite de Pruebas para searchAccion      #
    #############################################
    # Caso Inicial
       
    # Prueba 13 
    def testsearchAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('Usar magia',1)
        aAcc.searchAccion('Usar magia')
           
    # Casos Fronteras
       
    # Prueba 14
    def testsearchAccionShortDesc0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.        
        aAcc   = accions()
        result = aAcc.searchAccion('')
        self.assertFalse(result)
        aBacklog.deleteProduct('Enemigos de campo')
      
    # Prueba 15
    def testsearchAccionShortDesc1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.searchAccion('A')
        self.assertTrue(result)
        aAcc.deleteAccion('A')
        aBacklog.deleteProduct('Enemigos de campo')
           
    # Prueba 16
    def testsearchAccionShortDesc140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llamare',1)
        result = aAcc.searchAccion(20*'Llamare')
        self.assertNotEqual(result,[],"Accion no encontrada")
        aAcc.deleteAccion(20*'Llamare')
        aBacklog.deleteProduct('Enemigos de campo')
           
    # Prueba 17
    def testsearchAccionShortDesc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions() 
        result = aAcc.searchAccion(20*'Llamare' + 's')
        self.assertFalse(result, "Accion Encontrada")
        aBacklog.deleteProduct('Enemigos de campo')
  
    # Caso Normal
      
    # Prueba 18
    def testsearchAccionDescNotExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchAccion('Luchar con confianza')
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
           
    # Casos Maliciosos
       
    # Prueba 19
    def testsearchAccionNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba. 
        aAcc   = accions()
        aAcc.insertAccion(4350,1)
        result = aAcc.searchAccion(4350)
        self.assertEqual(result, [],'Accion Encontrada')
        aBacklog.deleteProduct('Batalla')
 
    # Prueba 20 
    def testSearchNameNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.   
        aAcc   = accions()
        result = aAcc.searchAccion(None)
        self.assertEqual(result, [],'Accion Encontrada')
        aBacklog.deleteProduct('Batalla')
                
    #############################################      
    #   Suite de Pruebas para searchIdAccion    #
    #############################################  
    # Caso Inicial
          
    # Prueba 21  
    def testsearchIdAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('Usar comandos especiales',1)
        aAcc.searchIdAccion(1)

    # Caso Normal

    # Prueba 22
    def testSearchIdTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Nuevo T',1)
        result = aAcc.searchIdAccion(1)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAcc.deleteAccion('Nuevo T')
        aBacklog.deleteProduct('Batalla') 

    # Prueba 23                
    def testSearchIdNoAccion(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba. 
        aAcc   = accions()
        result = aAcc.searchIdAccion(2)
        self.assertEqual(result,[],"Elemento no encontrado")
        aBacklog.deleteProduct('Batalla') 

    # Casos Maliciosos

    # Prueba 24
    def testSearchIdEmpty(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchIdAccion(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        aBacklog.deleteProduct('Batalla')
      
    # Prueba 25
    def testSearchIdString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchIdAccion('')
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Batalla') 
      
    # Prueba 26
    def testSearchIdNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        aAcc   = accions()
        result = aAcc.searchIdAccion(None)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Batalla')
                      
    #############################################      
    #   Suite de Pruebas para updateAccion      #
    #############################################  
    # Caso Inicial
      
    # Prueba 27
    def testupdateAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.   
        aAcc   = accions()
        aAcc.insertAccion('Invocar un eon',1)
        aAcc.updateAccion('Invocar un eon','Invocar arma artema')
        aBacklog.deleteProduct('Batalla')  
 
    # Casos Normales
      
    # Prueba 28
    def testupdateAccionDesc(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Ultima invocacion',1)
        result = aAcc.updateAccion('Ultima invocacion','Terminar partida a tiempo')
        self.assertTrue(result)
        aAcc.deleteAccion('Terminar partida a tiempo')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 29     
    def testupdateAccionDescNOtExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc = accions()
        result = aAcc.updateAccion('Usar fuego','Usar rayo')
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')
           
    # Casos Fronteras
        
    # Prueba 30
    def testupdateAccionLeftLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.updateAccion('A','Buscar puntos debiles')
        self.assertTrue(result)
        aAcc.deleteAccion('Buscar puntos debiles')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 31
    def testupdateAccionLeftLong1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Agotar toda la magia',1)
        result = aAcc.updateAccion('Agotar toda la magia','A')
        self.assertTrue(result)
        aAcc.deleteAccion('A')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 32         
    def testupdateAccionRightLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Agotar toda la vitalidad',1)
        result = aAcc.updateAccion('Agotar toda la vitalidad',140*'T')
        self.assertTrue(result)    
        aAcc.deleteAccion(140*'T')
        aBacklog.deleteProduct('Batalla')
  
    # Prueba 33
    def testupdateAccionLeftLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(140*'T',1)
        result = aAcc.updateAccion(140*'T','Agotar toda la vitalidad')
        self.assertTrue(result)
        aAcc.deleteAccion('Agotar toda la vitalidad')
        aBacklog.deleteProduct('Batalla')
           
    # Casos Esquinas
       
    # Prueba 34
    def testupdateAccionLeftLen1RightLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.updateAccion('A',140*'U')
        self.assertTrue(result)
        aAcc.deleteAccion(140*'U')
        aBacklog.deleteProduct('Batalla') 

    # Prueba 35
    def testupdateAccionLeftLen140RightLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(140*'U',1)
        result = aAcc.updateAccion(140*'U', 140*'M')
        self.assertTrue(result) 
        aAcc.deleteAccion(140*'M')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 36
    def testupdateAccionLeftLen140RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llamare',1)
        result = aAcc.updateAccion(20*'Llamare','M')
        self.assertTrue(result)
        aAcc.deleteAccion('M')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 37
    def testupdateAccionLeftLen1RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('X',1)
        result = aAcc.updateAccion('X','U')
        self.assertTrue(result)
        aAcc.deleteAccion('U')
        aBacklog.deleteProduct('Batalla') 
           
    # Casos Maliciosos
       
    # Prueba 38
    def testupdateSameName(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Atacar puntos de vida',1)
        result = aAcc.updateAccion('Atacar puntos de vida','Atacar puntos de vida')
        self.assertTrue(result,"Modificación Válida")
        aAcc.deleteAccion('Atacar puntos de vida')
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 39
    def testupdateAccionLeftLen0RightLen141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('',1)
        result = aAcc.updateAccion('',20*'Llamare' + 's')
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Batalla')
 
    # Prueba 40
    def testupdateAccionLeftLen141RightLen141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llamare' + 's',1)
        result = aAcc.updateAccion(20*'Llamare' + 's',20*'Malcara' + 's')
        self.assertFalse(result, "Modificación Válida") 
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 41
    def testupdateAccionLeftLen141RightLen0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llamare',1)
        result = aAcc.updateAccion(20*'Llamare','')
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion(20*'Llamare')
        aBacklog.deleteProduct('Batalla')  
 
    # Prueba 42
    def testupdateAccionLeftNoneRightValidString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.updateAccion(None,'Planificar estrategia')
        self.assertFalse(result,"Modificación válida") 
        aBacklog.deleteProduct('Batalla')  
 
    # Prueba 43
    def testupdateAccionLeftValidStringRightNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Atacar puntos de vida',1)
        result = aAcc.updateAccion('Atacar puntos de vida',None)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion('Atacar puntos de vida')
        aBacklog.deleteProduct('Batalla')    
           
    #############################################      
    #   Suite de Pruebas para deleteAccion      #
    ############################################# 
    # Caso Inicial
       
    # Prueba 44
    def testDeleteAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Usar magia blanca',1)
        aAcc.deleteAccion('Usar magia blanca')
        aBacklog.deleteProduct('Batalla')
           
    # Casos Normales
   
    # Prueba 45
    def testDeleteAccion(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('U',1)
        result = aAcc.deleteAccion('U')
        self.assertTrue(result)
        aBacklog.deleteProduct('Batalla')

    # Casos Fronteras
       
    # Prueba 46
    def testDeleteAccion1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('A',1)
        result = aAcc.deleteAccion('A')
        self.assertTrue(result)
        aBacklog.deleteProduct('Batalla')          
 
    # Prueba 47      
    def testDeleteAccionNoAccion(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Diseñar armas',1)
        result = aAcc.deleteAccion('Diseñar vestiferas')
        self.assertFalse(result)
        aAcc.deleteAccion('Diseñar armas')
        aBacklog.deleteProduct('Batalla')

    # Casos Maliciosos
  
    # Prueba 48
    def testDeleteAccionInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion('')
        self.assertFalse(result,"Id no válido")
        aBacklog.deleteProduct('Batalla')
           
    # Prueba 49
    def testDeleteAccionNotString(self):
       aBacklog = backlog()
       aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
       # Inicio de la prueba.
       aAcc   = accions()
       result = aAcc.deleteAccion(12345)
       self.assertFalse(result,"Id no válido")
       aBacklog.deleteProduct('Batalla')
 
    # Prueba 50    
    def testDeleteAccionNotExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Batalla','Enemigos de campo',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion('Lista de enemigos en batalla')
        self.assertFalse(result)
        aBacklog.deleteProduct('Batalla')