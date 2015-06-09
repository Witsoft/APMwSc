# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo role.py
sys.path.append('../app/scrum')

from role import *

class TestActors(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertActor       #
    #############################################
    
    # Caso Inicial
 
    # Prueba 1
    def testInsertExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        aAct = role()
        aAct.insertActor('Lxchydzr','Pxlxy dxsczmvnxlmynty',1)
        aAct.deleteActor('Lxchydzr',1)
        aBacklog.deleteProduct('Pxrsynzjxs')    
         
    # Casos Normales
           
    # Prueba 2 
    
    def testInsertElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Mxgy','Pvrx mxgyx',1)
        self.assertTrue(result)
        aAct.deleteActor('Mxgy',1)
        aBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 3
    def testInsertRepeatedElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Ystrxtygx','Dxsyñz pxtryn',1)
        result1 = aAct.insertActor('Ystrxtygx','Dxsyñz pxtryn',1)
        self.assertFalse(result1, "Elemento insertado")
        aAct.deleteActor('Ystrxtygx',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
    
    # Casos Fronteras
      
    # Prueba 4
    def testInsertLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(10*'Txdys','Dxsyñz dy Trvjy',1)
        self.assertTrue(result)
        aAct.deleteActor(10*'Txdys',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 5
    def testInsertLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(10*'Txdys' + '1','FFX',1) 
        self.assertFalse(result, "Elemento insertado")
        aBacklog.deleteProduct('Pxrsynzjxs') 
             
    # Prueba 6
    def testInsertShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('','Atuendos',1)
        self.assertFalse(result, "Elemento insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
              
    # Prueba 7
    def testInsertLongName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('T','Sxgny',1)
        self.assertTrue(result)
        aAct.deleteActor('T',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 8
    def testInsertDescriptionLong1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1) 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('Rxnyz','o',1)
        self.assertTrue(result)
        aAct.deleteActor('Rxnyz',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 9
    def testInsertDescriptionLong140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Dwsxñydzr', 70*'La',1)
        self.assertTrue(result)
        aAct.deleteActor('Dwsxñydzr',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 10
    def testInsertDescriptionLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('Xctyr','',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 11
    def testInsertDescriptionLong141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Lxdryn', 70*'La' + 'a',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Casos Esquinas
    
    # Prueba 12
    def testInsertMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
       # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('S','D',1)
        self.assertTrue(result)
        aAct.deleteActor('S',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 13
    def testInsertMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor(10*'Txdys',70*'Lo',1)
        self.assertTrue(result)
        aAct.deleteActor(10*'Txdys',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
        
    # Prueba 14
    def testInsertActorLong0DescriptionLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('','',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 15
    def testInsertActorLong51DescriptionLong141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor(10*'Clxyd' + 's', 70*'Lo' + 'l',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Casos Maliciosos
      
    # Prueba 16
    def testInsertNotActorString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(1254,'No definido',1)
        self.assertFalse(result,"Elemento insertado")
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 17
    def testInsertActorNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(None,'No definido',1)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 18
    def testInsertDescriptionNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Mxgy',None,1)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 19
    def testInsertNotIDInteger(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Clxyd','Xnygmzs dx jwxgy','Cancion')
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 20
    def testInsertActorDescriptionIdNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(None,None,None)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
                  
    # Prueba 21
    def testInsertId0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs', 'Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Lxchydzr','Gxlpy cxntzndxntx',0)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs')          
         
    #############################################      
    #  Suite de Pruebas para findNameActor      #
    #############################################
                     
    # Caso Inicial
     
    # Prueba 22 
    def testFindNameExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',2)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Clxyd','Drxmx yn yl grzpw',2)
        aAct.findNameActor('Clxyd',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
            
    # Casos Fronteras
     
    # Prueba 23
    def testFindNameEmpty(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor('',1)
        self.assertEqual(result,[], "Expresión inválida")
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 24
    def testFindNameShortName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('T','No definido',1)
        result = aAct.findNameActor('T',1)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor('T',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 25
    def testFindNameLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(10*'Txdys','Zs dxl jyxgw',1)
        result = aAct.findNameActor(10*'Txdys',1)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor(10*'Txdys',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
           
    # Prueba 26
    def testFindNameLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(10*'Clxyd' + 's',1) 
        self.assertEqual(result,[],"Cadena no válida")
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Casos Maliciosos
     
    # Prueba 27
    def testFindNameNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(1254,1)
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
      
    # Prueba 28
    def testFindNameNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(None,1)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Pxrsynzjxs') 

    #############################################      
    #       Suite de Pruebas para updateActor   #
    #############################################   
     
    # Caso Inicial
     
    # Prueba 29
    def testUpdateActorExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Xngylz','Atacante de batalla',1)
        aAct.updateActor('Xngylz','Xdxn','Vtvcvntx dx mxgzx',1)
        aAct.deleteActor('Xdxn',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
   
    # Casos Normales
     
    #Prueba 30
    def testUpdateActor(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Zxll','Combatiente nato',1)
        result = aAct.updateActor('Zxll','lzlz','Mxgyx nzgrx',1)
        self.assertTrue(result)
        aAct.deleteActor('lzlz',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Casos Fronteras
      
    # Prueba 31
    def testUpdateActorLeftLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('X','No definido',1)
        result = aAct.updateActor('X','Ystrxtygx','Sxtyzcxwn',1)
        self.assertTrue(result)
        aAct.deleteActor('Ystrxtygx',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
    
    # Prueba 32         
    def testUpdateActorRightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Clxyd','N',1)
        result = aAct.updateActor('Clxyd','Txdys','Jxgydzr',1)
        self.assertTrue(result)
        aAct.deleteActor('Txdys',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 33         
    def testUpdateActorRightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Drxgyn','Xtxcxnty',1)
        result = aAct.updateActor('Drxgyn',50*'R','No definido',1)
        self.assertTrue(result)
        aAct.deleteActor(50*'R',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 34
    def testUpdateActorLeftLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(50*'A','No definido',1)
        result = aAct.updateActor(50*'A','Yxny', 'Mxgyx Blxncx',1)
        self.assertTrue(result)
        aAct.deleteActor('Yxny',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 35
    def testUpdateActorDescriptionLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Sxry','Mxystrz',1)
        result = aAct.updateActor('Sxry','Xrys', 'N',1)
        self.assertTrue(result)
        aAct.deleteActor('Xrys',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 36
    def testUpdateActorDescriptionLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Rxy','Rxyxs',1)
        result = aAct.updateActor('Rxy','Hxrcylxs', 70* 'Nw',1)
        self.assertTrue(result)
        aAct.deleteActor('Hxrcylxs',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 37
    def testUpdateActorDescriptionLen0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Pxstyr','Xny pyly mynxjyndz',1)
        result = aAct.updateActor('Pxstyr','Mxgy', '',1)
        self.assertFalse(result)
        aAct.deleteActor('Pxstyr',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 38         
    def testUpdateActorRightLen51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Cxrbxry','Xtxcx',1)
        result = aAct.updateActor('Cxrbxry',50*'P' + 'a','No definido',1)
        self.assertFalse(result)
        aAct.deleteActor('Cxrbxry',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 39         
    def testUpdateActorLeftLen51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'Sc' + 'a','No definido',1)
        result = aAct.updateActor(25*'Sc' + 'a','Ztymy','Zbsyrbxr',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Casos Esquinas
     
    # Prueba 40
    def testUpdateActorLeftLen1RightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('O','No definido',1)
        result = aAct.updateActor('O',25*'Pq','No definido',1)
        self.assertTrue(result) 
        aAct.deleteActor(25*'Pq',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 41
    def testUpdateActorLeftLen50RightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'Us','No definido',1)
        result = aAct.updateActor(25*'Us', 25*'Ma','No definido',1)
        self.assertTrue(result)
        aAct.deleteActor(25*'Ma',1) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 42
    def testUpdateActorLeftLen50RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'LL','No definido',1)
        result = aAct.updateActor(25*'LL','E','No definido',1)
        self.assertTrue(result)
        aAct.deleteActor('E',1)
        aBacklog.deleteProduct('Pxrsynzjxs')  
 
    # Prueba 43
    def testUpdateActorLeftLen1RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('V','No definido',1)
        result = aAct.updateActor('V','G','No definido',1)
        self.assertTrue(result)
        aAct.deleteActor('G',1) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 44
    def testUpdateActorLeftLen1RightLen50Description1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('J','No definido',1)
        result = aAct.updateActor('J',25*'fr','No definido',1)
        self.assertTrue(result)
        aAct.deleteActor(25*'fr',1)
        aBacklog.deleteProduct('Pxrsynzjxs')  

    # Prueba 45
    def testUpdateActorLeftLen1RightLen50Description140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('k','No definido',1)
        result = aAct.updateActor('k',25*'gb',70*'mo',1)
        self.assertTrue(result) 
        aAct.deleteActor(25*'gb',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 46
    def testUpdateActorLeftLen50RightLen50Description140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'li','No definido',1)
        result = aAct.updateActor(25*'li', 25*'IL',70*'de',1)
        self.assertTrue(result)
        aAct.deleteActor(25*'IL',1) 
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 47
    def testUpdateActorLeftLen1RightLen1Description1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('s','No definido',1)
        result = aAct.updateActor('s','t','d',1)
        self.assertTrue(result)
        aAct.deleteActor('t',1) 
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 48
    def testUpdateActorLeftLen51RightLen51Description141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(25*'se' + 'a',25*'lo'+ 'b',70*'de' + 'a',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Casos Maliciosos
          
    # Prueba 49
    def testUpdateActorLeftLen0RightLen51Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor('',25*'Pi' + 'p','',1)
        self.assertFalse(result,"Modificación válida")
        aBacklog.deleteProduct('Pxrsynzjxs')  
  
    # Prueba 50
    def testUpdateActorLeftLen51RightLen0Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(25*'Ma'+ 's','','',1)
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 51
    def testUpdateActorLeftNoneRightValidString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(None,'Clxyd','Drxmx',1)
        self.assertFalse(result,"Modificación válida") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 52
    def testUpdateActorLeftValidStringRightNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Xntx Yrtxmy','Mxgyx zscwrx',1)
        result = aAct.updateActor('Xntx Yrtxmy',None,'No definido',1)
        self.assertFalse(result, "Modificación válida")
        aAct.deleteActor('Xntx Yrtxmy',1) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 53
    def testUpdateActorLeftValidStringRightDescriptionNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Vxhn','Cxndyctxr',1)
        result = aAct.updateActor('Vxhn','Fine',None,1)
        self.assertFalse(result, "Modificación válida")
        aAct.deleteActor('Vxhn',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 54
    def testUpdateActorNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(None,None,None,1)
        self.assertFalse(result, "Modificación válida")
        aBacklog.deleteProduct('Pxrsynzjxs')  
          
    # Prueba 55
    def testUpdateActorLeft0Right0Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor('','','',1)
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Pxrsynzjxs')  
         
    #############################################      
    #       Suite de Pruebas para deleteActor   #
    #############################################   
 
    # Caso Inicial
     
    # Prueba 56
    def testDeleteActorExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Tzfy','Peleadora al extremo',1)
        aAct.deleteActor('Tzfy',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

     # Casos Normales
 
     # Prueba 57
    def testDeleteLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(10*'Teame','Lxcyrz',1)
        result = aAct.deleteActor(10*'Teame',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 

     # Prueba 58
    def testDeleteLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(10*'Clxyd' + 's',1)
        self.assertFalse(result, "Elemento insertado.")
        aBacklog.deleteProduct('Pxrsynzjxs')  
             
    # Prueba 59
    def testDeleteShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor('',1)
        self.assertFalse(result, "Elemento insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
              
    # Prueba 60
    def testDeleteLongName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('T','No definido',1)
        result = aAct.deleteActor('T',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
                  
    # Casos Esquinas
    
    # Prueba 61
    def testDeleteMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor('S','No definido',1)
        result = aAct.deleteActor('S',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 62
    def testDeleteMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor(25*'me', 'No definido',1)
        result = aAct.deleteActor(25*'me',1)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
        
    # Prueba 63
    def testDeleteActorName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.deleteActor('',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 64
    def testDeleteActorLong51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.deleteActor(25*'ma'+'p',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Casos Maliciosos
      
    # Prueba 65
    def testDeleteNotActorString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(1254,1)
        self.assertFalse(result,"Elemento insertado")
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 66
    def testDeleteActorNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(None,1)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 67
    def testDeleteDescriptionNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Mxgy',None,1)
        result = aAct.deleteActor('Mxgy',1)
        self.assertTrue(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs')
                   
    #############################################      
    #       Suite de Pruebas para findIdActor   #
    #############################################

    # Caso Inicial
   
    # Prueba 68  
    def testFindIdExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor('Mxgy','Dxstrcy@ cun mfgtz',1)
        aAct.findIdActor(1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
  
    # Caso Normal
     
    # Prueba 69
    def testFindIdTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        aAct   = role()
        aAct.insertActor('Xyrzs','Anciano procedente de hace años',1)
        result = aAct.findIdActor(1)        
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor('Xyrzs',1)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Prueba 70
    def testFindIdNoActor(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor(2**28)
        self.assertEqual(result,[],"Elemento no encontrado")
        aBacklog.deleteProduct('Pxrsynzjxs') 

    # Caso Frontera
     
    # Prueba 71
    def testFindIdEmpty(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        aBacklog.deleteProduct('Pxrsynzjxs')
            
    # Casos Maliciosos
     
    # Prueba 72
    def testFindIdString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor('')
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
      
    # Prueba 73
    def testFindIdNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor(None)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Pxrsynzjxs') 