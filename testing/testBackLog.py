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
    def testFindName(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi','Permite localizar un taxi',1)
         aBackLog.findName('Taxi')
         aBackLog.deleteProduct('Taxi')   
          
        # Casos Normales
          
     # Prueba 2
    def testFindNameNotExist(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi','Taxi seguro.',1)
          # Inicio de la prueba.
         result = aBackLog.findName('Nuevo')
         self.assertEqual(result,[])
         aBackLog.deleteProduct('Taxi seguro.')
            
          
     # Casos Fronteras
        
     # Prueba 3
    def testfindNameShortName0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('','Taxi seguro.',1)
         # Inicio de la prueba.        
         result = aBackLog.findName('')
         self.assertEqual(result,[])
          
     # Prueba 4
    def testfindNameShortName1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('T','new t',1)
         # Inicio de la prueba
         result = aBackLog.findName('T')
         self.assertNotEqual(result,[])
         aBackLog.deleteProduct('T')
          
     # Prueba 5
    def testfindNameShortName50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(50*'Z','new z',1)
          # Inicio de la prueba.
         result = aBackLog.findName(50*'Z')
         self.assertNotEqual(result,[],"Accion no encontrada")
         aBackLog.deleteProduct(50*'Z')
  
     # Prueba 6
    def testfindNameShortName51(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(50*'W'+'q','nuevo wq',1)
         # Inicio de la prueba.
         result = aBackLog.findName(50*'W'+'q')
         self.assertEqual(result,[]) 
 
 # Casos Fronteras
        
     # Prueba 7
    def testfindNameShortDesc0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','',1)
         # Inicio de la prueba.        
         result = aBackLog.findName('Taxi seguro')
         self.assertEqual(result,[])
         #aBackLog.deleteProduct('Taxi seguro.')
          
     # Prueba 8
    def testfindNameShortDesc1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Nuevo','T',1)
         # Inicio de la prueba
         result = aBackLog.findName('Nuevo')
         self.assertNotEqual(result,[])
         aBackLog.deleteProduct('Nuevo')
          
     # Prueba 9
    def testfindNameShortDesc140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Nuevo',140*'Z',1)
          # Inicio de la prueba.
         result = aBackLog.findName('Nuevo')
         self.assertNotEqual(result,[],"Accion no encontrada")
         aBackLog.deleteProduct('Nuevo')
  
     # Prueba 10
    def testfindNameShortDesc141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Nuevo',140*'W'+'q',1)
         # Inicio de la prueba.
         result = aBackLog.findName('Nuevo')
         self.assertEqual(result,[]) 
      
     #Casos Esquina
      
     # Prueba 11 
    def testfindNameMinLong(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('T','T',1)
        # Inicio de la prueba
        result = aBackLog.findName('T')
        self.assertNotEqual(result,[])
        aBackLog.deleteProduct('T')
      
     # Prueba 12 
    def testfindNameMaxLong(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'A',140*'T',2)
        # Inicio de la prueba
        result = aBackLog.findName(50*'A')
        self.assertNotEqual(result,[])
        aBackLog.deleteProduct(50*'A')
      
     # Prueba 13 
    def testfindNameMaxLongDescMinLong(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'A','T',2)
        # Inicio de la prueba
        result = aBackLog.findName(50*'A')
        self.assertNotEqual(result,[])
        aBackLog.deleteProduct(50*'A')   
      
     # Prueba 14    
    def testfindName51Desc141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'A'+'B',140*'T'+'S',1)
        # Inicio de la prueba
        result = aBackLog.findName(50*'A'+'B')
        self.assertEqual(result,[])
      
     # Prueba 15 
    def testfindName51Desc141Tipe3(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'A'+'B',140*'T'+'S',3)
        # Inicio de la prueba
        result = aBackLog.findName(50*'A'+'B')
        self.assertEqual(result,[])
     
     # Prueba 16 
    def testfindName51Desc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'A'+'B','T'+'S',1)
        # Inicio de la prueba
        result = aBackLog.findName(50*'A'+'B')
        self.assertEqual(result,[])
      
     #Prueba 17   
    def testfindName1Desc141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('A',140*'T'+'S',1)
        # Inicio de la prueba
        result = aBackLog.findName('A')
        self.assertEqual(result,[])
 
     # Prueba 18 
    def testfindName1Desc1Tipe3(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('A','T',3)
        # Inicio de la prueba
        result = aBackLog.findName('A')
        self.assertEqual(result,[])
    
     # Prueba 19 
    def testfindNameLong0Desc141Tipe3(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('',140*'T'+'S',3)
        # Inicio de la prueba
        result = aBackLog.findName('')
        self.assertEqual(result,[])
 
     # Prueba 20
    def testfindName51DescLong0Tipe3(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'A'+'B','',3)
        # Inicio de la prueba
        result = aBackLog.findName(50*'A'+'B')
        self.assertEqual(result,[])
      
    # Casos Maliciosos
        
    # Prueba 21
    def testfindNameNotString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','un nuevo taxi',1)
         # Inicio de la prueba. 
         result = aBackLog.findName(4350)
         self.assertEqual(result, [],'Accion Encontrada')
         aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 22   
    def testFindNameNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','cualquiera',1)
         # Inicio de la prueba.   
         result = aBackLog.findName(None)
         self.assertEqual(result,[],'Accion Encontrada')
         aBackLog.deleteProduct('Taxi seguro.')
 
          
      #############################################      
      #   Suite de Pruebas para insertBackLog  #
      #############################################
       
    # Caso Inicial
         
    # Prueba 23
    
    def testInsertExist(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('Taxi','Permite localizar un taxi',1)
        aBackLog.deleteProduct('Taxi')   
           
       # Casos Normales
           
    # Prueba 24
    def testInsertBackLogRepeated(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi','Taxi seguro.',1)
        result = aBackLog.insertBackLog('Taxi','Taxi seguro.',1)
         # Inicio de la prueba.
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi')
             
           
    # Casos Fronteras
         
    # Prueba 25
    def testInsertBackLogShortName0(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('','Taxi seguro.',1)
        # Inicio de la prueba.        
        self.assertFalse(result)
           
    # Prueba 26
    def testInsertBackLogShortName1(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('T','new t',1)
        # Inicio de la prueba
        self.assertTrue(result)
        aBackLog.deleteProduct('T')
           
    # Prueba 27
    def testInsertBackLogShortName50(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog(50*'Z','new z',1)
         # Inicio de la prueba.
        self.assertTrue(result)
        aBackLog.deleteProduct(50*'Z')
   
    # Prueba 28
    def testInsertBackLogShortName51(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog(50*'W'+'q','nuevo wq',1)
        # Inicio de la prueba.
        self.assertFalse(result) 
  
# Casos Fronteras
         
    # Prueba 29
    def testInsertBackLogShortDesc0(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('Taxi seguro.','',1)
        # Inicio de la prueba.        
        self.assertFalse(result)
           
    # Prueba 30
    def testInsertBackLogShortDesc1(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('Nuevo','T',1)
        # Inicio de la prueba
        self.assertTrue(result)
        aBackLog.deleteProduct('Nuevo')
           
    # Prueba 31
    def testInsertBackLogShortDesc140(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('Nuevo',140*'Z',1)
         # Inicio de la prueba.
        self.assertTrue(result)
        aBackLog.deleteProduct('Nuevo')
   
    # Prueba 32
    def testInsertBackLogShortDesc141(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('Nuevo',140*'W'+'q',1)
        # Inicio de la prueba.
        self.assertFalse(result) 
       
    #Casos Esquina
       
    # Prueba 33 
    def testInsertBackLogMinLong(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog('T','T',1)
       # Inicio de la prueba
       self.assertTrue(result)
       aBackLog.deleteProduct('T')
       
    # Prueba 34 
    def testInsertBackLogMaxLong(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog(50*'A',140*'T',2)
       # Inicio de la prueba
       self.assertTrue(result)
       aBackLog.deleteProduct(50*'A')
       
    # Prueba 35 
    def testInsertBackLogMaxLongDescMinLong(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog(50*'A','T',2)
       # Inicio de la prueba
       self.assertTrue(result)
       aBackLog.deleteProduct(50*'A')   
       
    # Prueba 36    
    def testInsertBackLog51Desc141(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog(50*'A'+'B',140*'T'+'S',1)
       # Inicio de la prueba
       self.assertFalse(result)
       
    # Prueba 37 
    def testInsertBackLog51Desc141Tipe3(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog(50*'A'+'B',140*'T'+'S',3)
       # Inicio de la prueba
       self.assertFalse(result)
      
    # Prueba 38 
    def testInsertBackLog51Desc1(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog(50*'A'+'B','T'+'S',1)
       # Inicio de la prueba
       self.assertFalse(result)
       
    #Prueba 39  
    def testInsertBackLog1Desc141(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog('A',140*'T'+'S',1)
       # Inicio de la prueba
       self.assertFalse(result)
  
    # Prueba 40 
    def testInsertBackLog1Desc1Tipe3(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog('A','T',3)
       # Inicio de la prueba
       self.assertFalse(result)
     
    # Prueba 41 
    def testInsertBackLogLong0Desc141Tipe3(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog('',140*'T'+'S',3)
       # Inicio de la prueba
       self.assertFalse(result)
  
    # Prueba 42
    def testInsertBackLog51DescLong0Tipe3(self):
       aBackLog = backLog()
       result = aBackLog.insertBackLog(50*'A'+'B','',3)
       # Inicio de la prueba
       self.assertFalse(result)
       
   # Casos Maliciosos
         
   # Prueba 43
    def testInsertBackLogNone(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog(None,None,None)
        # Inicio de la prueba. 
        self.assertFalse(result)
           
   # Prueba 44   
    def testInsertBackLogLong0(self):
        aBackLog = backLog()
        result = aBackLog.insertBackLog('','',1)
        # Inicio de la prueba.  
        self.assertFalse(result)
 
      #############################################      
      #   Suite de Pruebas para deleteProduct  #
      #############################################
       
     # Caso Inicial
      
    # Prueba 45
    def testDeleteProductExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi','Permite localizar un taxi',1)
        aBackLog.deleteProduct('Taxi')   
           
       # Casos Normales
           
    # Prueba 46
    def testDeleteProductRepeated(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi','Taxi seguro.',1)
        aBackLog.insertBackLog('Taxi','Taxi seguro.',1)
         # Inicio de la prueba.
        result = aBackLog.deleteProduct('Taxi')
        self.assertTrue(result)         
           
    # Casos Fronteras
         
    # Prueba 47
    def testDeleteProductShortName0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('','Taxi seguro.',1)
        # Inicio de la prueba.        
        result = aBackLog.deleteProduct('')
        self.assertFalse(result)
           
    # Prueba 48
    def testDeleteProductShortName1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('T','new t',1)
        # Inicio de la prueba
        result = aBackLog.deleteProduct('T')
        self.assertTrue(result)
           
    # Prueba 49
    def testDeleteProductShortName50(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'Z','new z',1)
         # Inicio de la prueba.
        result = aBackLog.deleteProduct(50*'Z')
        self.assertTrue(result)
   
    # Prueba 50
    def testDeleteProductShortName51(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(50*'W'+'q','nuevo wq',1)
        # Inicio de la prueba. 
  
# Casos Fronteras
         
    # Prueba 51
    def testDeleteProductShortDesc0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','',1)
        # Inicio de la prueba.        
        result = aBackLog.deleteProduct('Taxi seguro.')
        self.assertFalse(result)
           
    # Prueba 52
    def testDeleteProductShortDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Nuevo','T',1)
        # Inicio de la prueba 
        result = aBackLog.deleteProduct('Nuevo')
        self.assertTrue(result)
           
    # Prueba 53
    def testDeleteProductShortDesc140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Nuevo',140*'Z',1)
         # Inicio de la prueba.
        result = aBackLog.deleteProduct('Nuevo')
        self.assertTrue(result)
 
   
    # Prueba 54
    def testDeleteProductShortDesc141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Nuevo',140*'W'+'q',1)
        # Inicio de la prueba. 
        result = aBackLog.deleteProduct('Nuevo')
        self.assertFalse(result)
       
    #Casos Esquina
       
    # Prueba 55 
    def testDeleteProductMinLong(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('T','T',1)
       # Inicio de la prueba
       result = aBackLog.deleteProduct('T')
       self.assertTrue(result)
       
    # Prueba 56 
    def testDeleteProductMaxLong(self):
       aBackLog = backLog()
       aBackLog.insertBackLog(50*'A',140*'T',2)
       # Inicio de la prueba
       result = aBackLog.deleteProduct(50*'A')
       self.assertTrue(result)
       
    # Prueba 57 
    def testDeleteProductMaxLongDescMinLong(self):
       aBackLog = backLog()
       aBackLog.insertBackLog(50*'A','T',2)
       # Inicio de la prueba
       result = aBackLog.deleteProduct(50*'A')   
       self.assertTrue(result)
       
    # Prueba 58    
    def testDeleteProduct51Desc141(self):
       aBackLog = backLog()
       aBackLog.insertBackLog(50*'A'+'B',140*'T'+'S',1)
       # Inicio de la prueba
       result = aBackLog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)
       
    # Prueba 59 
    def testDeleteProduct51Desc141Tipe3(self):
       aBackLog = backLog()
       aBackLog.insertBackLog(50*'A'+'B',140*'T'+'S',3)
       # Inicio de la prueba
       result = aBackLog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)
      
    # Prueba 60 
    def testDeleteProduct51Desc1(self):
       aBackLog = backLog()
       aBackLog.insertBackLog(50*'A'+'B','T'+'S',1)
       # Inicio de la prueba
       
    #Prueba 61  
    def testDeleteProduct1Desc141(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('A',140*'T'+'S',1)
       # Inicio de la prueba
       result = aBackLog.deleteProduct('A')
       self.assertFalse(result)
  
    # Prueba 62 
    def testDeleteProduct1Desc1Tipe3(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('A','T',3)
       # Inicio de la prueba
       result = aBackLog.deleteProduct('A')
       self.assertFalse(result)
     
    # Prueba 63 
    def testDeleteProductLong0Desc141Tipe3(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('',140*'T'+'S',3)
       # Inicio de la prueba
       result = aBackLog.deleteProduct('')
       self.assertFalse(result)
  
    # Prueba 64
    def testDeleteProduct51DescLong0Tipe3(self):
       aBackLog = backLog()
       aBackLog.insertBackLog(50*'A'+'B','',3)
       # Inicio de la prueba
       result = aBackLog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)
       
   # Casos Maliciosos
         
   # Prueba 65
    def testDeleteProductNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog(None,None,None)
        # Inicio de la prueba. 
        result = aBackLog.deleteProduct(None)
        self.assertFalse(result)
   
   # Prueba 66   
    def testDeleteProductLong0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('','',1)
        # Inicio de la prueba.  
        result = aBackLog.deleteProduct('')
        self.assertFalse(result)
 
                 
     #############################################      
      #   Suite de Pruebas para modifyDescription  #
      #############################################  
 
       
     # Caso Inicial
      
     # Prueba 24
    def testmodifyNameExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','un nuevo taxi',1)
         # Inicio de la prueba.   
         aBackLog.modifyBackLog('Taxi seguro.','reservar un taxi o varios.','el mismo taxi',2)
         aBackLog.deleteProduct('reservar un taxi o varios.')           
     # Casos Normales
      
     # Prueba 25 
    def testmodifyName(self):
          aBackLog = backLog()
          aBackLog.insertBackLog('Permite localizar un taxi','Taxi nuevo',1)
          # Inicio de la prueba.
          result = aBackLog.modifyBackLog('Permite localizar un taxi','Atención las 24 horas del día','descripcion',2)
          self.assertTrue(result)
          aBackLog.deleteProduct('Atención las 24 horas del día')
 
  
     # Prueba 26 
    def testmodifyNameNotExist(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi Seguro','descripcion',1)
          # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Llegar lo mas pronto posible','Ir comodo y seguro','nuevo',2)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi Seguro')
          
     # Casos Fronteras
         
     # Prueba 27
    def testmodifyNameRigthLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('A','nuevo',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('A','Buscar al cliente donde esté','nuevo 1',2)
         self.assertTrue(result)
         aBackLog.deleteProduct('Buscar al cliente donde esté')
         
     # Prueba 28
    def testmodifyNameLeftLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Buscar al cliente donde esté','nuevo',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Buscar al cliente donde esté','A','descripcion',1)
         self.assertTrue(result)
         aBackLog.deleteProduct('A')
          
     # Prueba 29        
    def testmodifyNameRightLen50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Atención las 24 horas del día','descripcion',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Atención las 24 horas del día',50*'T','descripcion',1)
         self.assertTrue(result)    
         aBackLog.deleteProduct(50*'T')
          
     # Prueba 30
    def testmodifyNameLeftLen50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(50*'T','descripcion',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog(50*'T','Atención las 24 horas del día','nuevo',2)
         self.assertTrue(result)
         aBackLog.deleteProduct('Atención las 24 horas del día')
 
   
    def testmodifyBackLog140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Name',140*'A',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Name','A','nuevo',2)
         self.assertTrue(result)
         aBackLog.deleteProduct('A')
 
    def testmodifyBackLog1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Name','A',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Name','Atención las 24 horas del día',140*'N',2)
         self.assertTrue(result)
         aBackLog.deleteProduct('Atención las 24 horas del día')
 
    def testmodifyNoType0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Name',140*'A',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Name','Atención las 24 horas del día','nuevo',0)
         self.assertFalse(result)
         aBackLog.deleteProduct('Atención las 24 horas del día')
 
    def testmodifyNoType3(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Name',140*'A',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Name','Atención las 24 horas del día','nuevo',3)
         self.assertFalse(result)
         aBackLog.deleteProduct('Atención las 24 horas del día')    
  
  
 
 
     # Casos Esquina
 
 
     # Prueba 31
    def testmodifyName50DescriptionLen140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(50*'A',140*'T',2)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog(50*'A','S','T',1)
         self.assertTrue(result)
         aBackLog.deleteProduct(50*'A')
  
     # Prueba 32
    def testmodifyName51Len141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(51*'O',141*'T',2)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog(51*'O','O',141*'T',2)
         self.assertFalse(result)
 
     # Prueba 32
    def testmodifyName51Len141Type3(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(51*'O',141*'T',3)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog(51*'O','O',141*'T',2)
         self.assertFalse(result)
          
          
     # Prueba 33
    def testmodifyBackLogLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('T','S',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('T','R','G',1)
         self.assertTrue(result)
         aBackLog.deleteProduct('R')
  
     # Prueba 34
    def testmodifyBackLogLeftLen0RightLen140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('','D',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('','O',140*'R',1)
         self.assertFalse(result)
          
     # Prueba 35
    def testmodifyBackLogLeftLenRightLen0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog(50*'T','desc',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog(50*'T','R','',1)
         self.assertFalse(result)
         aBackLog.deleteProduct(50*'T')
  
     # Prueba 34
    def testmodifyBackLogLeftLen0RightLen(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('T','D',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('T','',140*'R',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('T')
 
     # Prueba 36
    def testmodifyBackLogLen0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Name','Description',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Name','','',0)
         self.assertFalse(result)         
         aBackLog.deleteProduct('Name')
 
     # Casos Maliciosos
      
     # Prueba 37
    def testmodifyBackLogSameName(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Reservar un taxi.','Descripcion',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Reservar un taxi.','Reservar un taxi.','Descripcion',1)
         self.assertTrue(result,"Modificación Válida")
         aBackLog.deleteProduct('Reservar un taxi.')
 
     # Prueba 39
    def testmodifyBackLogLeftValidStringRightNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Reservar un taxi.','Descripcion',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Reservar un taxi.',None,'desc',2)
         self.assertFalse(result, "Modificación válida") 
         aBackLog.deleteProduct('Reservar un taxi.') 
                
     # Prueba 40
    def testmodifyBackLogNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Name','Descripcion',1)
         # Inicio de la prueba.
         result = aBackLog.modifyBackLog('Name',None,None,None)
         self.assertFalse(result, "Modificación válida")
         aBackLog.deleteProduct('Name')    
    
    
               
     ####################################################      
     #   Suite de Pruebas para actorsAsociatedToProduct #
     ####################################################  
    
     # Casos Frontera
    
    # Prueba 41    
    def testActorAsociatedBackLogExists(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct(1)
        arole.deleteRole('Role1')
        arole.deleteRole('Role2')
        aBackLog.deleteProduct('Taxi Seguro')     
                                       
     # Prueba 42
    def testActorAsociatedBackLogTrue(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',1)
        result = aBackLog.actorsAsociatedToProduct(1)
        self.assertNotEqual([],result)
        arole.deleteRole('Role1')
        arole.deleteRole('Role2')
        aBackLog.deleteProduct('Taxi Seguro')                                        
               
     # Prueba 43                                   
    def testActorAsociatedBackLogFalse(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct(2)
        self.assertEqual([],result)
        arole.deleteRole('Role1')
        aBackLog.deleteProduct('Taxi Seguro')

    # Casos Malicia
    
     # Prueba 44
    def testActorAsociatedBackLogNoRole(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        arole.insertRole('Role1',None,1)
        result = aBackLog.actorsAsociatedToProduct(1)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Taxi Seguro')
        
     # Prueba 45    
    def testActorAsociatedBackLogNoneId(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        arole.insertRole('Role1','nuevo role1',1)
        arole.insertRole('Role2','nuevo role2',2)
        result = aBackLog.actorsAsociatedToProduct(None)
        self.assertEqual([],result)
        arole.deleteRole('Role1')
        aBackLog.deleteProduct('Taxi Seguro')
        
     # Prueba 46    
    def testActorAsociatedBackLogString(self):
        aBackLog = backLog()
        arole = role()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
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
    
    # Prueba 47    
    def testAccionAsociatedBackLogExists(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct(1)
        oAccion.deleteAccion('nuevo accions1')
        oAccion.deleteAccion('nuevo accions2')
        aBackLog.deleteProduct('Taxi Seguro')     
    
     # Prueba 48                                   
    def testAccionAsociatedBackLogTrue(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',1)
        result = aBackLog.accionsAsociatedToProduct(1)
        self.assertNotEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        oAccion.deleteAccion('nuevo accions2')
        aBackLog.deleteProduct('Taxi Seguro')                                        
               
     # Prueba 49                                   
    def testAccionAsociatedBackLogFalse(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct(3)
        self.assertEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        aBackLog.deleteProduct('Taxi Seguro')

     # Casos Malicia
    
     # Prueba 50
    def testAccionAsociatedBackLogNoAccion(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oAccion.insertAccion(None,1)
        result = aBackLog.accionsAsociatedToProduct(1)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Taxi Seguro')
        
     # Prueba 51    
    def testAccionAsociatedBackLogNoneId(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct(None)
        self.assertEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        aBackLog.deleteProduct('Taxi Seguro')
     
     # Prueba 52    
    def testAccionAsociatedBackLogString(self):
        aBackLog = backLog()
        oAccion = accions()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oAccion.insertAccion('nuevo accions1',1)
        oAccion.insertAccion('nuevo accions2',2)
        result = aBackLog.accionsAsociatedToProduct('')
        self.assertEqual([],result)
        oAccion.deleteAccion('nuevo accions1')
        aBackLog.deleteProduct('Taxi Seguro')

        
     #######################################################      
     #   Suite de Pruebas para objectiveAsociatedToProduct #
     #######################################################  
    
    # Casos Frontera
    
     # Prueba 53    
    def testObjectiveAsociatedBackLogExists(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct(1)
        oObjective.deleteObjective('nuevo objectives1')
        oObjective.deleteObjective('nuevo objectives2')
        aBackLog.deleteProduct('Taxi Seguro')
               
     # Prueba 54                                   
    def testObjectiveAsociatedBackLogTrue(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',1)
        result = aBackLog.objectivesAsociatedToProduct(1)
        self.assertNotEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        oObjective.deleteObjective('nuevo objectives2')
        aBackLog.deleteProduct('Taxi Seguro')                                        
               
     # Prueba 55                                   
    def testObjectiveAsociatedBackLogFalse(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct(3)
        self.assertEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        aBackLog.deleteProduct('Taxi Seguro')

    # Casos Malicia

     # Prueba 56
    def testObjectiveAsociatedBackLogNoObjective(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oObjective.insertObjective(None,1)
        result = aBackLog.objectivesAsociatedToProduct(1)
        self.assertEqual([],result)
        aBackLog.deleteProduct('Taxi Seguro')  
        
     # Prueba 57    
    def testObjectiveAsociatedBackLogNoneId(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct(None)
        self.assertEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        aBackLog.deleteProduct('Taxi Seguro')
    
     # Prueba 58    
    def testObjectiveAsociatedBackLogString(self):
        aBackLog = backLog()
        oObjective = objective()
        aBackLog.insertBackLog('Taxi Seguro','Descripcion',1)
        oObjective.insertObjective('nuevo objectives1',1)
        oObjective.insertObjective('nuevo objectives2',2)
        result = aBackLog.objectivesAsociatedToProduct('')
        self.assertEqual([],result)
        oObjective.deleteObjective('nuevo objectives1')
        aBackLog.deleteProduct('Taxi Seguro')
           