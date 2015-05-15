'''
Created on 7/05/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import sys
sys.path.append('../app/scrum')
import unittest

from role import *

class clsRoleTester(unittest.TestCase):
# -*- coding: utf-8 -*-. 

# Ruta que permite utilizar el módulo model.py

    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def test1InsertExists(self):
         role1 = role()
         role1.insertRole('Product Owner','description',1)    
     
     # Casos Normales
           
     # Prueba 2 
     
     def test2InsertElement(self):
         role1   = role()
         result = role1.insertRole('Team Member')
         self.assertTrue(result)
'''                     
     # Prueba 3
     def test3InsertRepeatedElement(self):
         role1   = role()
         result = role1.insertRole('Team Member')
         self.assertFalse(result, "Elemento insertado.")
           
     # Casos Fronteras
      
     # Prueba 4
     def test4InsertLongName50(self):
         role1   = role()
         result = role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
         self.assertFalse(result)
      
     # Prueba 5
     def test5InsertLongName51(self):
         role1   = role()
         result = role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me') 
         self.assertFalse(result, "Elemento insertado.")
              
     # Prueba 6
     def test6InsertShortName0(self):
         role1   = role()
         result = role1.insertRole('')
         self.assertFalse(result, "Elemento insertado.") 
              
     # Prueba 7
     def test7InsertLongName1(self):
         role1   = role()
         result = role1.insertRole('T')
         self.assertFalse(result)
          
     # Casos Maliciosos
      
     # Prueba 8
     def test8InsertNotString(self):
         role1   = role()
         result = role1.insertRole(1254)
         self.assertFalse(result,"Elemento insertado.")
 
     # Prueba 9
     def test9InsertNoneString(self):
         role1   = role()
         result = role1.insertRole(None)
         self.assertFalse(result,"No válido.")
     #############################################      
     #       Suite de Pruebas para FindName      #
     #############################################
     
     # Caso Inicial
     
     # Prueba 10 
     def test_10FindNameExists(self):
         role1   = role()
         role1.findNameRole('Product Owner')
            
     # Casos Fronteras
     
     # Prueba 11
     def test_11FindNameEmpty(self):
         role1   = role()
         result = role1.findNameRole('')
         self.assertFalse(result, "Expresión válida.")
           
     # Prueba 12
     def test_12FindNameShortName1(self):
         role1   = role()
         result = role1.findNameRole('T')
         self.assertEqual(result,[],"Elemento no encontrado")
      
     # Prueba 13
     def test_13FindNameLongName50(self):
         role1   = role()
         result = role1.findNameRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
         self.assertEqual(result,[],"Elemento no encontrado")
           
     # Prueba 14
     def test_14FindNameLongName51(self):
         role1   = role()
         result = role1.findNameRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me') 
         self.assertFalse(result, "Cadena no válida")
         
     # Casos Maliciosos
     
     # Prueba 15
     def test_15FindNameNotString(self):
         role1   = role()
         result = role1.findNameRole(1254)
         self.assertFalse(result,"Elemento Insertado") 
      
     # Prueba 16
     def test_16FindNameNoneString(self):
         role1   = role()
         result = role1.findNameRole(None)
         self.assertFalse(result,"Válido")         
     
     #############################################      
     #       Suite de Pruebas para ModifyName    #
     #############################################   
     
     # Caso Inicial
     
     # Prueba 23
     def test_23ModifyNameExists(self):
         role1   = role()
         role1.updateRole('Product Owner','Scrum Master')
          
     # Casos Normales
     
     # Prueba 24
     def test_24ModifyName(self):
         role1   = role()
         result = role1.updateRole('Scrum Master','Product Owner')
         self.assertTrue(result)
          
     # Casos Fronteras
      
     # Prueba 25
     def test_25ModifyNameLeftLen1(self):
         role1   = role()
         result = role1.updateRole('T','Team Member')
         self.assertFalse(result)
     
     # Prueba 26         
     def test_26ModifyNameRightLen1(self):
         role1   = role()
         result = role1.updateRole('Team Member','T')
         self.assertFalse(result)

     # Prueba 27         
     def test_27ModifyNameRightLen50(self):
         role1   = role()
         result = role1.updateRole('Scrum Master',50*'T')
         self.assertFalse(result)
         
     # Prueba 28
     def test_28ModifyNameLeftLen50(self):
         role1   = role()
         result = role1.updateRole(50*'T','M')
         self.assertFalse(result)

     # Casos Esquinas
     
     # Prueba 29
     def test_29ModifyNameLeftLen1RightLen50(self):
         role1   = role()
         result = role1.updateRole('M',25*'Us')
         self.assertFalse(result) 

     # Prueba 30
     def test_30ModifyNameLeftLen50RightLen50(self):
         role1   = role()
         result = role1.updateRole(25*'Us', 25*'Ma')
         self.assertFalse(result) 
 
     # Prueba 31
     def test_31ModifyNameLeftLen50RightLen1(self):
         role1   = role()
         result = role1.updateRole(25*'Ma','M')
         self.assertFalse(result) 
 
     # Prueba 32
     def test_32ModifyNameLeftLen1RightLen1(self):
         role1   = role()
         result = role1.updateRole('M','U')
         self.assertFalse(result) 
 
     # Casos Maliciosos
          
     # Prueba 33
     def test_33ModifySameName(self):
         role1   = role()
         result = role1.updateRole('Master','Master')
         self.assertFalse(result,"Modificación Válida")
          
     # Prueba 34
     def test_34ModifyNameLeftLen0RightLen51(self):
         role1   = role()
         result = role1.updateRole('',25*'Pi' + 'p')
         self.assertFalse(result, "Modificación válida") 
 
     # Prueba 35
     def test_35ModifyNameLeftLen51RightLen51(self):
         role1   = role()
         result = role1.updateRole(25*'Pi' + "p",25*'Ma' + 's')
         self.assertFalse(result, "Modificación Válida") 
 
     # Prueba 36
     def test_36ModifyNameLeftLen51RightLen0(self):
         role1   = role()
         result = role1.updateRole(25*'Ma'+ 's','')
         self.assertFalse(result, "Modificación válida") 
 
     # Prueba 37
     def test_37ModifyNameLeftNoneRightValidString(self):
         role1   = role()
         result = role1.updateRole(None,'Juana la Iguana')
         self.assertFalse(result,"Modificación válida") 
          
     # Prueba 38
     def test_38ModifyNameLeftValidStringRightNone(self):
         role1   = role()
         result = role1.updateRole("Juana la Iguana",None)
         self.assertFalse(result, "Modificación válida") 
          
     #############################################      
     #       Suite de Pruebas para DeleteId      #
     #############################################   
 
     # Caso Inicial
     
     # Prueba 39
     def test_39DeleteIdExists(self):
         role1   = role()
         role1.deleteRole(4)

     # Casos Normales
 
     # Prueba 40
     def test_40DeleteId(self):
         role1   = role()
         result = role1.deleteRole(2)
         self.assertTrue(result)
          
     # Casos Fronteras
     
     # Prueba 41
     def test_41DeleteId1(self):
         role1   = role()
         result = role1.deleteRole(1)
         self.assertTrue(result)
 
     # Casos Maliciosos
 
     # Prueba 42
     def test_42DeleteIdMin0(self):
         role1   = role()
         result = role1.deleteRole(0)
         self.assertFalse(result,"Id no válido")
 
     # Prueba 43
     def test_43DeleteIdNotInteger(self):
         role1   = role()
         result = role1.deleteRole('AldJos')
         self.assertFalse(result, "Es válida")
'''