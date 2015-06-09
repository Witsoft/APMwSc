# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo accions.py
sys.path.append('../app/scrum')

from accions import *

class TestAccions(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertAccion      #
    #############################################
          
    # Caso Inicial
  
    # Prueba 1
    def testInserAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        aAcc = accions()
        aAcc.insertAccion('VtXcyr pvntgs dw wydz',1)
        aAcc.deleteAccion('VtXcyr pvntgs dw wydz',1)
        aBacklog.deleteProduct('Bxtyllz')        

    # Casos Normales
      
    # Prueba 2
    def testInsertAccionElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Pqrmyt3 zlngfr',1)
        self.assertTrue(result)
        aAcc.deleteAccion('Pqrmyt3 zlngfr',1)
        aBacklog.deleteProduct('Bxtyllz')
                   
    # Prueba 3
    def testInsertAccionRepeatedElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Pqrmyt3 zlngfr',1)
        result1 = aAcc.insertAccion('Pqrmyt3 zlngfr',1)
        self.assertFalse(result1)
        aAcc.deleteAccion('Pqrmyt3 zlngfr',1)
        aBacklog.deleteProduct('Bxtyllz')
                
    # Casos Fronteras
       
    # Prueba 4
    def testInsertAccionShortDesc0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 5
    def testInsertAccionLongDesc1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('@',1)
        self.assertTrue(result)
        aAcc.deleteAccion('@',1)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 6
    def testInsertAccionLongDesc140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(20*'LlWmcrl',1)
        self.assertTrue(result)
        aAcc.deleteAccion(20*'LlWmcrl',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 7
    def testInsertAccionLongDesc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(20*'LlWmcrl' + 'x',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 8
    def testInsertAccionIdBackLogInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result  =aAcc.insertAccion('Wtqczr ul mds dfbyl',0)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Esquinas
        
    # Prueba 9
    def testInsertAccionIdBacklogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc    = accions()
        result  = aAcc.insertAccion('DwfEndqr cun fw3rzv',2)
        self.assertFalse(result)
        #Eliminacion del elemento insertado.
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 10
    def testInsertAccionLongDesc140AndIdBackLogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(20*'LlWmcrl',3)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
                       
    # Casos Maliciosos
       
    # Prueba 11
    def testInsertNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(4350,1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 12
    def testInsertNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion(None,1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 13
    def testInsertIdNegative(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Nxn3zzzz',-1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 14
    def testInsertIdString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Nxn3zzzz','1')
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
            
    #############################################      
    #   Suite de Pruebas para searchAccion      #
    #############################################
   
    # Caso Inicial
        
    # Prueba 15 
    def testsearchAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('Vsdr mgjyq',1)
        aAcc.searchAccion('Vsdr mgjyq',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Fronteras
        
    # Prueba 16
    def testsearchAccionShortDesc0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.        
        aAcc   = accions()
        result = aAcc.searchAccion('',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 17
    def testsearchAccionShortDesc1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba
        aAcc   = accions()
        aAcc.insertAccion('@',1)
        result = aAcc.searchAccion('@',1)
        self.assertTrue(result)
        aAcc.deleteAccion('@',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 18
    def testsearchAccionShortDesc140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'LlWmcrl',1)
        result = aAcc.searchAccion(20*'LlWmcrl',1)
        self.assertNotEqual(result,[],"Accion no encontrada")
        aAcc.deleteAccion(20*'LlWmcrl',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 19
    def testsearchAccionShortDesc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions() 
        aAcc.insertAccion(20*'LlWmcrl' + 'm',1)
        result = aAcc.searchAccion(20*'LlWmcrl' + 'm',1)
        self.assertFalse(result, "Accion Encontrada")
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 20
    def testsearchAccionIdBackLogInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.insertAccion('Wtqczr ul mds dfbyl',0)
        result = aAcc.searchAccion('Wtqczr ul mds dfbyl',0)
        self.assertFalse(result, "Accion Encontrada")
        aBacklog.deleteProduct('Bxtyllz')
        
    # Casos Esquinas

    # Prueba 21
    def testsearchAccionIdBacklogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Wtqczr ul mds dfbyl',1)
        result = aAcc.searchAccion('Wtqczr ul mds dfbyl',2)
        self.assertFalse(result)
        #Eliminacion del elemento insertado.
        aAcc.deleteAccion('Wtqczr ul mds dfbyl',1)
        aBacklog.deleteProduct('Bxtyllz')        
 
    # Prueba 22
    def testsearchAccionLongDesc140AndIdBackLogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'LlWmcrl',1)
        result = aAcc.searchAccion(20*'LlWmcrl',3)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
        aAcc.deleteAccion(20*'LlWmcrl',1)
   
    # Caso Normal
       
    # Prueba 23
    def testsearchAccionDescNotExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchAccion('Lxdhvr cyn cqnfyznzs',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Maliciosos
        
    # Prueba 24
    def testsearchAccionNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba. 
        aAcc   = accions()
        aAcc.insertAccion(4350,1)
        result = aAcc.searchAccion(4350,1)
        self.assertEqual(result, [],'Accion Encontrada')
        aBacklog.deleteProduct('Bxtyllz')
  
    # Prueba 25 
    def testSearchNameNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.   
        aAcc   = accions()
        result = aAcc.searchAccion(None,1)
        self.assertEqual(result, [],'Accion Encontrada')
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 26 
    def testSearchNameIdNegative(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.   
        aAcc   = accions()
        result = aAcc.searchAccion('Nxnczzz',-1)
        self.assertEqual(result, [],'Accion Encontrada')
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 27
    def testSearchNameIdString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.   
        aAcc   = accions()
        result = aAcc.searchAccion('Nxn3zzzz','1')
        self.assertEqual(result, [],'Accion Encontrada')
        aBacklog.deleteProduct('Bxtyllz')
                 
                 
    #############################################      
    #   Suite de Pruebas para searchIdAccion    #
    #############################################  
    # Caso Inicial
           
    # Prueba 28  
    def testsearchIdAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('VsAr cdmzndqs qspxcywlts',1)
        aAcc.searchIdAccion(1)
 
    # Caso Normal
 
    # Prueba 29
    def testSearchIdTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('N@sEwx T',1)
        result = aAcc.searchIdAccion(1)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAcc.deleteAccion('N@sEwx T',1)
        aBacklog.deleteProduct('Bxtyllz') 
 
    # Prueba 30                
    def testSearchIdNoAccion(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba. 
        aAcc   = accions()
        result = aAcc.searchIdAccion(2)
        self.assertEqual(result,[],"Elemento no encontrado")
        aBacklog.deleteProduct('Bxtyllz') 
 
    # Casos Maliciosos
 
    # Prueba 31
    def testSearchIdInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchIdAccion(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 32
    def testSearchIdString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.searchIdAccion('')
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Bxtyllz') 
       
    # Prueba 33
    def testSearchIdNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        aAcc   = accions()
        result = aAcc.searchIdAccion(None)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 34
    def testSearchIdNegative(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        aAcc   = accions()
        result = aAcc.searchIdAccion(-1)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Bxtyllz')
        
          
    #############################################      
    #   Suite de Pruebas para updateAccion      #
    #############################################  

    # Caso Inicial
       
    # Prueba 35
    def testupdateAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.   
        aAcc   = accions()
        aAcc.insertAccion('Yntdcvr an miqn',1)
        aAcc.updateAccion('Yntdcvr an miqn','Tnbdc3r xrmq asrtdmp',1)
        aAcc.deleteAccion('Tnbdc3r xrmq asrtdmp',1)
        aBacklog.deleteProduct('Bxtyllz')  
  
    # Casos Normales
       
    # Prueba 36
    def testupdateAccionDesc(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Altomy Tnvfcgcyqn',1)
        result = aAcc.updateAccion('Altomy Tnvfcgcyqn','T3rmynAr portwdp o txempz',1)
        self.assertTrue(result)
        aAcc.deleteAccion('T3rmynAr portwdp o txempz',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 37     
    def testupdateAccionDescNOtExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.updateAccion('Vsrr fvWjo','Usqr rpyD',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Fronteras
         
    # Prueba 38
    def testupdateAccionLeftLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@',1)
        result = aAcc.updateAccion('@','Bvscqr pontfs ddbyl3z',1)
        self.assertTrue(result)
        aAcc.deleteAccion('Bvscqr pontfs ddbyl3z',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 39
    def testupdateAccionRightLong1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@jutdr tqdf lu mpgya',1)
        result = aAcc.updateAccion('@jutdr tqdf lu mpgya','@',1)
        self.assertTrue(result)
        aAcc.deleteAccion('@',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 40         
    def testupdateAccionRightLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@jutdr tqdf lu mpgya',1)
        result = aAcc.updateAccion('@jutdr tqdf lu mpgya',140*'T',1)
        self.assertTrue(result)    
        aAcc.deleteAccion(140*'T',1)
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 41
    def testupdateAccionLeftLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(140*'T',1)
        result = aAcc.updateAccion(140*'T','@jutdr tqdf lu mpgya',1)
        self.assertTrue(result)
        aAcc.deleteAccion('@jutdr tqdf lu mpgya',1)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 42
    def testupdateAccionIdBackLogInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.updateAccion('Wtqczr ul mds dfbyl','@jutdr tqdf lu mpgya',0)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Esquinas
        
    # Prueba 43
    def testupdateAccionLeftLen1RightLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@',1)
        result = aAcc.updateAccion('@',140*'V',1)
        self.assertTrue(result)
        aAcc.deleteAccion(140*'V',1)
        aBacklog.deleteProduct('Bxtyllz') 
 
    # Prueba 44
    def testupdateAccionLeftLen140RightLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(140*'U',1)
        result = aAcc.updateAccion(140*'U', 140*'M',1)
        self.assertTrue(result) 
        aAcc.deleteAccion(140*'M',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 45
    def testupdateAccionLeftLen140RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llcmvr3',1)
        result = aAcc.updateAccion(20*'Llcmvr3','@',1)
        self.assertTrue(result)
        aAcc.deleteAccion('@',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 46
    def testupdateAccionLeftLen1RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@',1)
        result = aAcc.updateAccion('@','U',1)
        self.assertTrue(result)
        aAcc.deleteAccion('U',1)
        aBacklog.deleteProduct('Bxtyllz') 

    # Prueba 47
    def testupdateAccionLongDesc140AndIdBackLogNoExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.updateAccion(140*'U', 140*'M',3)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Maliciosos
        
    # Prueba 48
    def testupdateSameName(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Bvscqr pontfs ddbyl3z',1)
        result = aAcc.updateAccion('Bvscqr pontfs ddbyl3z','Bvscqr pontfs ddbyl3z',1)
        self.assertTrue(result,"Modificación Válida")
        aAcc.deleteAccion('Bvscqr pontfs ddbyl3z',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 49
    def testupdateAccionLeftLen0RightLen141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('',1)
        result = aAcc.updateAccion('',20*'Llcmvr3' + 's',1)
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Bxtyllz')
  
    # Prueba 50
    def testupdateAccionLeftLen141RightLen141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llcmvr3' + 's',1)
        result = aAcc.updateAccion(20*'Llcmvr3' + 's',20*'M@lcvra' + 's',1)
        self.assertFalse(result, "Modificación Válida") 
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 51
    def testupdateAccionLeftLen141RightLen0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Llcmvr3',1)
        result = aAcc.updateAccion(20*'Llcmvr3','',1)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion(20*'Llcmvr3',1)
        aBacklog.deleteProduct('Bxtyllz')  
  
    # Prueba 52
    def testupdateAccionLeftNoneRightValidString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.updateAccion(None,'Plxnyfyc@r 3strvtbjoia',1)
        self.assertFalse(result,"Modificación válida") 
        aBacklog.deleteProduct('Bxtyllz')  
  
    # Prueba 53
    def testupdateAccionLeftValidStringRightNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@patvr ponytgs do vodn',1)
        result = aAcc.updateAccion('@patvr ponytgs do vodn',None,1)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion('@patvr ponytgs do vodn',1)
        aBacklog.deleteProduct('Bxtyllz') 
        
    # Prueba 54
    def testupdateAccionIdNegative(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('@patvr ponytgs do vodn',1)
        result = aAcc.updateAccion('@patvr ponytgs do vodn','Nzzzcxn3',-1)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteAccion('@patvr ponytgs do vodn',1)
        aBacklog.deleteProduct('Bxtyllz')    
            
            
    #############################################      
    #   Suite de Pruebas para deleteAccion      #
    #############################################
     
    # Caso Inicial
        
    # Prueba 55
    def testDeleteAccionExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Us@r m2jop vlanct',1)
        aAcc.deleteAccion('Us@r m2jop vlanct',1)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Normales
    
    # Prueba 56      
    def testDeleteAccionDesc(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Dysdñvr prm@s',1)
        result = aAcc.deleteAccion('Dysdñvr prm@s',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 57
    def testDeleteAccionDescNotExits(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion('Dysdñvr prm@s',1)
        result = aAcc.deleteAccion('Dysdñvr v3styfzzos',1)
        self.assertFalse(result)
        aAcc.deleteAccion('Dysdñvr prm@s',1)
        aBacklog.deleteProduct('Bxtyllz')
    
    # Casos Fronteras
    
    # Prueba 58
    def testDeleteAccionDescLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('U',1)
        result = aAcc.deleteAccion('U',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 59
    def testDeleteAccionDescLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Zewftsx',1)
        result = aAcc.deleteAccion(20*'Zewftsx',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 60
    def testDeleteAccionDescLen0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc = accions()
        aAcc.insertAccion('',1)
        result = aAcc.deleteAccion('',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')  
        
    # Prueba 61
    def testDeleteAccionDescLen141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        aAcc.insertAccion(20*'Zewftsx'+'r',1)
        result = aAcc.deleteAccion(20*'Zewftsx'+'r',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')        
        
    # Prueba 62
    def testDeleteAccionIdBacklogInvalid(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion(20*'Zewftsx'+'r',0)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')    
  
    # Casos Maliciosos
   
    # Prueba 63
    def testDeleteAccionDescNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion(None,1)
        self.assertFalse(result,"Descripcion válida")
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 64
    def testDeleteAccionNotString(self):
       aBacklog = backlog()
       aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
       # Inicio de la prueba.
       aAcc   = accions()
       aAcc.insertAccion(12345,1)
       result = aAcc.deleteAccion(12345,1)
       self.assertFalse(result,"Descripcion válida")
       aBacklog.deleteProduct('Bxtyllz')
  
    # Prueba 65    
    def testDeleteAccionNotExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion('Lys@a dp 3nfmsgzs xn vactayta',2)
        self.assertFalse(result)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 66
    def testDeleteAccionDescIdNegative(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc   = accions()
        result = aAcc.deleteAccion('Lys@a dp 3nfmsgzs',-1)
        self.assertFalse(result,"Id válida")
        aBacklog.deleteProduct('Bxtyllz')
        