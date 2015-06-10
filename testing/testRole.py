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
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        aAct = role()
        aAct.insertActor('Lxchydzr','Pxlxy dxsczmvnxlmynty',idBacklog)
        result  = aAct.findNameActor('Lxchydzr',idBacklog)
        idActor = result[0].A_idActor
        aAct.deleteActor('Lxchydzr',idActor)
        aBacklog.deleteProduct('Pxrsynzjxs')    
         
    # Casos Normales
           
    # Prueba 2 
     
    def testInsertElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Mxgy','Pvrx mxgyx',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Mxgy',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 3
    def testInsertRepeatedElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct    = role()
        result  = aAct.insertActor('Ystrxtygx','Dxsyñz pxtryn',idBacklog)
        result1 = aAct.insertActor('Ystrxtygx','Dxsyñz pxtryn',idBacklog)
        self.assertFalse(result1, "Elemento insertado")
        aAct.deleteActor('Ystrxtygx',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
     
    # Casos Fronteras
       
    # Prueba 4
    def testInsertLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(10*'Txdys','Dxsyñz dy Trvjy',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor(10*'Txdys',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 5
    def testInsertLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(10*'Txdys' + '1','FFX',idBacklog) 
        self.assertFalse(result, "Elemento insertado")
        aBacklog.deleteProduct('Pxrsynzjxs') 
              
    # Prueba 6
    def testInsertShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('','Atuendos',idBacklog)
        self.assertFalse(result, "Elemento insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
               
    # Prueba 7
    def testInsertLongName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('T','Sxgny',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('T',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 8
    def testInsertDescriptionLong1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1) 
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('Rxnyz','o',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Rxnyz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 9
    def testInsertDescriptionLong140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Dwsxñydzr', 70*'La',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Dwsxñydzr',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 10
    def testInsertDescriptionLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('Xctyr','',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 11
    def testInsertDescriptionLong141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Lxdryn', 70*'La' + 'a',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Casos Esquinas
     
    # Prueba 12
    def testInsertMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
       # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('S','D',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('S',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 13
    def testInsertMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor(10*'Txdys',70*'Lo',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor(10*'Txdys',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 14
    def testInsertActorLong0DescriptionLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('','',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 15
    def testInsertActorLong51DescriptionLong141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor(10*'Clxyd' + 's', 70*'Lo' + 'l',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Casos Maliciosos
       
    # Prueba 16
    def testInsertNotActorString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(1254,'No definido',idBacklog)
        self.assertFalse(result,"Elemento insertado")
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 17
    def testInsertActorNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(None,'No definido',idBacklog)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 18
    def testInsertDescriptionNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Mxgy',None,idBacklog)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 19
    def testInsertNotIDInteger(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Clxyd','Xnygmzs dx jwxgy','Cancion')
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 20
    def testInsertActorDescriptionIdNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
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
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Clxyd','Drxmx yn yl grzpw',idBacklog)
        aAct.findNameActor('Clxyd',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
             
    # Casos Fronteras
      
    # Prueba 23
    def testFindNameEmpty(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor('',idBacklog)
        self.assertEqual(result,[], "Expresión inválida")
        aBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 24
    def testFindNameShortName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('T','No definido',idBacklog)
        result = aAct.findNameActor('T',idBacklog)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor('T',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 25
    def testFindNameLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(10*'Txdys','Zs dxl jyxgw',idBacklog)
        result = aAct.findNameActor(10*'Txdys',idBacklog)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor(10*'Txdys',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
            
    # Prueba 26
    def testFindNameLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(10*'Clxyd' + 's',idBacklog) 
        self.assertEqual(result,[],"Cadena no válida")
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Casos Maliciosos
      
    # Prueba 27
    def testFindNameNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(1254,idBacklog)
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
       
    # Prueba 28
    def testFindNameNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(None,idBacklog)
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
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Xngylz','Atacante de batalla',idBacklog)
        aAct.updateActor('Xngylz','Xdxn','Vtvcvntx dx mxgzx',idBacklog)
        aAct.deleteActor('Xdxn',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
    
    # Casos Normales
      
    #Prueba 30
    def testUpdateActor(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Zxll','Combatiente nato',idBacklog)
        result = aAct.updateActor('Zxll','lzlz','Mxgyx nzgrx',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('lzlz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
           
    # Casos Fronteras
       
    # Prueba 31
    def testUpdateActorLeftLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('X','No definido',idBacklog)
        result = aAct.updateActor('X','Ystrxtygx','Sxtyzcxwn',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Ystrxtygx',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
     
    # Prueba 32         
    def testUpdateActorRightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Clxyd','N',idBacklog)
        result = aAct.updateActor('Clxyd','Txdys','Jxgydzr',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Txdys',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 33         
    def testUpdateActorRightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Drxgyn','Xtxcxnty',idBacklog)
        result = aAct.updateActor('Drxgyn',50*'R','No definido',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor(50*'R',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 34
    def testUpdateActorLeftLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(50*'A','No definido',idBacklog)
        result = aAct.updateActor(50*'A','Yxny', 'Mxgyx Blxncx',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Yxny',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 35
    def testUpdateActorDescriptionLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Sxry','Mxystrz',idBacklog)
        result = aAct.updateActor('Sxry','Xrys', 'N',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Xrys',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 36
    def testUpdateActorDescriptionLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Rxy','Rxyxs',idBacklog)
        result = aAct.updateActor('Rxy','Hxrcylxs', 70* 'Nw',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('Hxrcylxs',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 37
    def testUpdateActorDescriptionLen0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Pxstyr','Xny pyly mynxjyndz',idBacklog)
        result = aAct.updateActor('Pxstyr','Mxgy', '',idBacklog)
        self.assertFalse(result)
        aAct.deleteActor('Pxstyr',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 38         
    def testUpdateActorRightLen51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Cxrbxry','Xtxcx',idBacklog)
        result = aAct.updateActor('Cxrbxry',50*'P' + 'a','No definido',idBacklog)
        self.assertFalse(result)
        aAct.deleteActor('Cxrbxry',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 39         
    def testUpdateActorLeftLen51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'Sc' + 'a','No definido',idBacklog)
        result = aAct.updateActor(25*'Sc' + 'a','Ztymy','Zbsyrbxr',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Casos Esquinas
      
    # Prueba 40
    def testUpdateActorLeftLen1RightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('O','No definido',idBacklog)
        result = aAct.updateActor('O',25*'Pq','No definido',idBacklog)
        self.assertTrue(result) 
        aAct.deleteActor(25*'Pq',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 41
    def testUpdateActorLeftLen50RightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'Us','No definido',idBacklog)
        result = aAct.updateActor(25*'Us', 25*'Ma','No definido',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor(25*'Ma',idBacklog) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
  
    # Prueba 42
    def testUpdateActorLeftLen50RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'LL','No definido',idBacklog)
        result = aAct.updateActor(25*'LL','E','No definido',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('E',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')  
  
    # Prueba 43
    def testUpdateActorLeftLen1RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('V','No definido',idBacklog)
        result = aAct.updateActor('V','G','No definido',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('G',idBacklog) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
  
    # Prueba 44
    def testUpdateActorLeftLen1RightLen50Description1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('J','No definido',idBacklog)
        result = aAct.updateActor('J',25*'fr','No definido',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor(25*'fr',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')  
 
    # Prueba 45
    def testUpdateActorLeftLen1RightLen50Description140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('k','No definido',idBacklog)
        result = aAct.updateActor('k',25*'gb',70*'mo',idBacklog)
        self.assertTrue(result) 
        aAct.deleteActor(25*'gb',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 46
    def testUpdateActorLeftLen50RightLen50Description140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'li','No definido',idBacklog)
        result = aAct.updateActor(25*'li', 25*'IL',70*'de',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor(25*'IL',idBacklog) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 47
    def testUpdateActorLeftLen1RightLen1Description1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('s','No definido',idBacklog)
        result = aAct.updateActor('s','t','d',idBacklog)
        self.assertTrue(result)
        aAct.deleteActor('t',idBacklog) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 48
    def testUpdateActorLeftLen51RightLen51Description141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(25*'se' + 'a',25*'lo'+ 'b',70*'de' + 'a',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Casos Maliciosos
           
    # Prueba 49
    def testUpdateActorLeftLen0RightLen51Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor('',25*'Pi' + 'p','',idBacklog)
        self.assertFalse(result,"Modificación válida")
        aBacklog.deleteProduct('Pxrsynzjxs')  
   
    # Prueba 50
    def testUpdateActorLeftLen51RightLen0Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(25*'Ma'+ 's','','',idBacklog)
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Prueba 51
    def testUpdateActorLeftNoneRightValidString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(None,'Clxyd','Drxmx',idBacklog)
        self.assertFalse(result,"Modificación válida") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 52
    def testUpdateActorLeftValidStringRightNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Xntx Yrtxmy','Mxgyx zscwrx',idBacklog)
        result = aAct.updateActor('Xntx Yrtxmy',None,'No definido',idBacklog)
        self.assertFalse(result, "Modificación válida")
        aAct.deleteActor('Xntx Yrtxmy',idBacklog) 
        aBacklog.deleteProduct('Pxrsynzjxs') 
           
    # Prueba 53
    def testUpdateActorLeftValidStringRightDescriptionNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Vxhn','Cxndyctxr',idBacklog)
        result = aAct.updateActor('Vxhn','Fine',None,idBacklog)
        self.assertFalse(result, "Modificación válida")
        aAct.deleteActor('Vxhn',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 54
    def testUpdateActorNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(None,None,None,idBacklog)
        self.assertFalse(result, "Modificación válida")
        aBacklog.deleteProduct('Pxrsynzjxs')  
           
    # Prueba 55
    def testUpdateActorLeft0Right0Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor('','','',idBacklog)
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
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Tzfy','Peleadora al extremo',idBacklog)
        aAct.deleteActor('Tzfy',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
     # Casos Normales
  
     # Prueba 57
    def testDeleteLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(10*'Teame','Lxcyrz',idBacklog)
        result = aAct.deleteActor(10*'Teame',idBacklog)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
     # Prueba 58
    def testDeleteLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(10*'Clxyd' + 's',idBacklog)
        self.assertFalse(result, "Elemento insertado.")
        aBacklog.deleteProduct('Pxrsynzjxs')  
              
    # Prueba 59
    def testDeleteShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor('',idBacklog)
        self.assertFalse(result, "Elemento insertado") 
        aBacklog.deleteProduct('Pxrsynzjxs') 
               
    # Prueba 60
    def testDeleteLongName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('T','No definido',idBacklog)
        result = aAct.deleteActor('T',idBacklog)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
                   
    # Casos Esquinas
     
    # Prueba 61
    def testDeleteMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor('S','No definido',idBacklog)
        result = aAct.deleteActor('S',idBacklog)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 62
    def testDeleteMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor(25*'me', 'No definido',idBacklog)
        result = aAct.deleteActor(25*'me',idBacklog)
        self.assertTrue(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
         
    # Prueba 63
    def testDeleteActorName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct = role()
        result = aAct.deleteActor('',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 64
    def testDeleteActorLong51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct = role()
        result = aAct.deleteActor(25*'ma'+'p',idBacklog)
        self.assertFalse(result)
        aBacklog.deleteProduct('Pxrsynzjxs') 
 
    # Casos Maliciosos
       
    # Prueba 65
    def testDeleteNotActorString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(1254,idBacklog)
        self.assertFalse(result,"Elemento insertado")
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 66
    def testDeleteActorNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(None,idBacklog)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs') 
          
    # Prueba 67
    def testDeleteDescriptionNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor('Mxgy',idBacklog)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Pxrsynzjxs')
                    
    #############################################      
    #       Suite de Pruebas para findIdActor   #
    #############################################
 
    # Caso Inicial
    
    # Prueba 68  
    def testFindIdExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor('Mxgy','Dxstrcy@ cun mfgtz',idBacklog)
        aAct.findIdActor(1)
        aBacklog.deleteProduct('Pxrsynzjxs') 
   
    # Caso Normal
      
    # Prueba 69
    def testFindIdTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba. 
        aAct   = role()
        aAct.insertActor('Xyrzs','Anciano procedente de hace años',idBacklog)
        result = aAct.findIdActor(1)        
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor('Xyrzs',idBacklog)
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