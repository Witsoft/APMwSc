import unittest

import os
import sys

# Ruta que permite utilizar el módulo py
sys.path.append('../app/scrum')

from objective import *
from backLog   import * 

class TestObjective(unittest.TestCase):
    
    #############################################      
    #       Suite de Pruebas para Objective     #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def test1InsertExists(self):
         newBL = clsBackLog('Taxi Seguro','Permite reservar un taxi.')
         session.add(newBL)
         session.commit()
         
#          
#          aObj = objective()
#          aObj.insertObjective('Permite autenticar.',1)    
     
     # Casos Normales
           
     # Prueba 2 
      
#      def test2InsertElement(self):
#          aObj = objective()
#          aObj = aObj.insertObjective('Permite autenticar un usuario.',1)
#          self.assertTrue(aObj)
#                      
#      # Prueba 3
#      def test3InsertRepeatedElement(self):
#          role   = clsRole()
#          result = role.insertRole('Team Member')
#          self.assertFalse(result, "Elemento insertado.")
#            
#      # Casos Fronteras
#       
#      # Prueba 4
#      def test4InsertLongName50(self):
#          role   = clsRole()
#          result = role.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
#          self.assertFalse(result)
#       
#      # Prueba 5
#      def test5InsertLongName51(self):
#          role   = clsRole()
#          result = role.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me') 
#          self.assertFalse(result, "Elemento insertado.")
#               
#      # Prueba 6
#      def test6InsertShortName0(self):
#          role   = clsRole()
#          result = role.insertRole('')
#          self.assertFalse(result, "Elemento insertado.") 
#               
#      # Prueba 7
#      def test7InsertLongName1(self):
#          role   = clsRole()
#          result = role.insertRole('T')
#          self.assertFalse(result)
#           
#      # Casos Maliciosos
#       
#      # Prueba 8
#      def test8InsertNotString(self):
#          role   = clsRole()
#          result = role.insertRole(1254)
#          self.assertFalse(result,"Elemento insertado.")
#  
#      # Prueba 9
#      def test9InsertNoneString(self):
#          role   = clsRole()
#          result = role.insertRole(None)
#          self.assertFalse(result,"No válido.")
#         
#      #############################################      
#      #       Suite de Pruebas para FindName      #
#      #############################################
#      
#      # Caso Inicial
#      
#      # Prueba 10 
#      def test_10FindNameExists(self):
#          role   = clsRole()
#          role.findNameRole('Product Owner')
#             
#      # Casos Fronteras
#      
#      # Prueba 11
#      def test_11FindNameEmpty(self):
#          role   = clsRole()
#          result = role.findNameRole('')
#          self.assertFalse(result, "Expresión válida.")
#            
#      # Prueba 12
#      def test_12FindNameShortName1(self):
#          role   = clsRole()
#          result = role.findNameRole('T')
#          self.assertEqual(result,[],"Elemento no encontrado")
#       
#      # Prueba 13
#      def test_13FindNameLongName50(self):
#          role   = clsRole()
#          result = role.findNameRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
#          self.assertEqual(result,[],"Elemento no encontrado")
#            
#      # Prueba 14
#      def test_14FindNameLongName51(self):
#          role   = clsRole()
#          result = role.findNameRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me') 
#          self.assertFalse(result, "Cadena no válida")
#          
#      # Casos Maliciosos
#      
#      # Prueba 15
#      def test_15FindNameNotString(self):
#          role   = clsRole()
#          result = role.findNameRole(1254)
#          self.assertFalse(result,"Elemento Insertado") 
#       
#      # Prueba 16
#      def test_16FindNameNoneString(self):
#          role   = clsRole()
#          result = role.findNameRole(None)
#          self.assertFalse(result,"Válido") 
#                     
#      #############################################      
#      #       Suite de Pruebas para FindId        #
#      #############################################  
#  
#      # Caso Inicial
#     
#      # Prueba 17
#      def test_17FindIdExists(self):
#          role   = clsRole()
#          role.findIdRole(2)
#           
#      # Casos Normales
#      
#      # Prueba 18
#      def test_18FindIdValidId(self):
#          role   = clsRole()
#          result = role.findIdRole(2)
#          self.assertTrue(result)
#           
#      # Casos Fronteras
#       
#      # Prueba 19
#      def test_19FindIdMinValue(self):
#          role   = clsRole()
#          result = role.findIdRole(1)
#          self.assertTrue(result)
#       
#      # Casos Maliciosos
#       
#      # Caso 20
#      def test_20FindIdMinId0(self):
#          role   = clsRole()
#          result = role.findIdRole(0)
#          self.assertEqual(result,[],"Es válido")
#           
#      # Prueba 21
#      def test_21FindIdNotInteger(self):
#          role   = clsRole()
#          result = role.findIdRole('AldJos')
#          self.assertFalse(result, "Es válida")
# 
#      # Prueba 22
#      def test_22InsertNoneString(self):
#          role   = clsRole()
#          result = role.findIdRole(None)
#          self.assertFalse(result,"Válido")
#  
#      #############################################      
#      #       Suite de Pruebas para ModifyName    #
#      #############################################   
#      
#      # Caso Inicial
#      
#      # Prueba 23
#      def test_23ModifyNameExists(self):
#          role   = clsRole()
#          role.modifyNameRole('Product Owner','Scrum Master')
#           
#      # Casos Normales
#      
#      # Prueba 24
#      def test_24ModifyName(self):
#          role   = clsRole()
#          result = role.modifyNameRole('Scrum Master','Product Owner')
#          self.assertTrue(result)
#           
#      # Casos Fronteras
#       
#      # Prueba 25
#      def test_25ModifyNameLeftLen1(self):
#          role   = clsRole()
#          result = role.modifyNameRole('T','Team Member')
#          self.assertFalse(result)
#      
#      # Prueba 26         
#      def test_26ModifyNameRightLen1(self):
#          role   = clsRole()
#          result = role.modifyNameRole('Team Member','T')
#          self.assertFalse(result)
# 
#      # Prueba 27         
#      def test_27ModifyNameRightLen50(self):
#          role   = clsRole()
#          result = role.modifyNameRole('Scrum Master',50*'T')
#          self.assertFalse(result)
#          
#      # Prueba 28
#      def test_28ModifyNameLeftLen50(self):
#          role   = clsRole()
#          result = role.modifyNameRole(50*'T','M')
#          self.assertFalse(result)
# 
#      # Casos Esquinas
#      
#      # Prueba 29
#      def test_29ModifyNameLeftLen1RightLen50(self):
#          role   = clsRole()
#          result = role.modifyNameRole('M',25*'Us')
#          self.assertFalse(result) 
# 
#      # Prueba 30
#      def test_30ModifyNameLeftLen50RightLen50(self):
#          role   = clsRole()
#          result = role.modifyNameRole(25*'Us', 25*'Ma')
#          self.assertFalse(result) 
#  
#      # Prueba 31
#      def test_31ModifyNameLeftLen50RightLen1(self):
#          role   = clsRole()
#          result = role.modifyNameRole(25*'Ma','M')
#          self.assertFalse(result) 
#  
#      # Prueba 32
#      def test_32ModifyNameLeftLen1RightLen1(self):
#          role   = clsRole()
#          result = role.modifyNameRole('M','U')
#          self.assertFalse(result) 
#  
#      # Casos Maliciosos
#           
#      # Prueba 33
#      def test_33ModifySameName(self):
#          role   = clsRole()
#          result = role.modifyNameRole('Master','Master')
#          self.assertFalse(result,"Modificación Válida")
#           
#      # Prueba 34
#      def test_34ModifyNameLeftLen0RightLen51(self):
#          role   = clsRole()
#          result = role.modifyNameRole('',25*'Pi' + 'p')
#          self.assertFalse(result, "Modificación válida") 
#  
#      # Prueba 35
#      def test_35ModifyNameLeftLen51RightLen51(self):
#          role   = clsRole()
#          result = role.modifyNameRole(25*'Pi' + "p",25*'Ma' + 's')
#          self.assertFalse(result, "Modificación Válida") 
#  
#      # Prueba 36
#      def test_36ModifyNameLeftLen51RightLen0(self):
#          role   = clsRole()
#          result = role.modifyNameRole(25*'Ma'+ 's','')
#          self.assertFalse(result, "Modificación válida") 
#  
#      # Prueba 37
#      def test_37ModifyNameLeftNoneRightValidString(self):
#          role   = clsRole()
#          result = role.modifyNameRole(None,'Juana la Iguana')
#          self.assertFalse(result,"Modificación válida") 
#           
#      # Prueba 38
#      def test_38ModifyNameLeftValidStringRightNone(self):
#          role   = clsRole()
#          result = role.modifyNameRole("Juana la Iguana",None)
#          self.assertFalse(result, "Modificación válida") 
#           
#      #############################################      
#      #       Suite de Pruebas para DeleteId      #
#      #############################################   
#  
#      # Caso Inicial
#      
#      # Prueba 39
#      def test_39DeleteIdExists(self):
#          role   = clsRole()
#          role.deleteIdRole(4)
# 
#      # Casos Normales
#  
#      # Prueba 40
#      def test_40DeleteId(self):
#          role   = clsRole()
#          result = role.deleteIdRole(2)
#          self.assertTrue(result)
#           
#      # Casos Fronteras
#      
#      # Prueba 41
#      def test_41DeleteId1(self):
#          role   = clsRole()
#          result = role.deleteIdRole(1)
#          self.assertTrue(result)
#  
#      # Casos Maliciosos
#  
#      # Prueba 42
#      def test_42DeleteIdMin0(self):
#          role   = clsRole()
#          result = role.deleteIdRole(0)
#          self.assertFalse(result,"Id no válido")
#  
#      # Prueba 43
#      def test_43DeleteIdNotInteger(self):
#          role   = clsRole()
#          result = role.deleteIdRole('AldJos')
#          self.assertFalse(result, "Es válida")