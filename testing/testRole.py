# -*- coding: utf-8 -*-. 

import unittest

from roleDummy import *

class clsRoleTester(unittest.TestCase):

# Ruta que permite utilizar el módulo model.py

    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def test1InsertExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole('Product Owner','description',1)    
     
     # Casos Normales
           
     # Prueba 2 
    
     def test2InsertElement(self):
         role1   = role()
         result = role1.insertRole('Team Member','Lo que sea',1)
         self.assertTrue(result)
  
    # Prueba 3
     def test3InsertRepeatedElement(self):
         role1   = role()
         result = role1.insertRole('Team Member','Lo que sea',1)
         self.assertFalse(result, "Elemento insertado.")
        
     # Casos Fronteras
      
     # Prueba 4
     def test4InsertLongName50(self):
         role1   = role()
         result = role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M','Mucha longitud',1)
         self.assertFalse(result)
      
      # Prueba 5
     def test5InsertLongName51(self):
         role1   = role()
         result = role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me','Maximo de longitud mas uno',1) 
         self.assertFalse(result, "Elemento insertado.")

             
     # Prueba 6
     def test6InsertShortName0(self):
         role1   = role()
         result = role1.insertRole('','Vacio',1)
         self.assertFalse(result, "Elemento insertado.") 
              
     # Prueba 7
     def test7InsertLongName1(self):
         role1   = role()
         result = role1.insertRole('T','Una sola letra',1)
         self.assertFalse(result)

    # Prueba 8
     def test8InsertDescriptionLong1(self):
        role1 = role()
        result = role1.insertRole('Scrum Master','o',1)
        self.assertTrue(result)

     # Prueba 9
     def test9InsertDescriptionLong140(self):
         role1   = role()
         result = role1.insertRole('Team Member', 70*'La',1)
         self.assertFalse(result)

    # Prueba 10
     def test_10InsertDescriptionLong0(self):
        role1 = role()
        result = role1.insertRole('Scrum Master','',1)
        self.assertFalse(result)

     # Prueba 11
     def test_11InsertDescriptionLong141(self):
         role1   = role()
         result = role1.insertRole('Team Member', 70*'La' + 'a',1)
         self.assertFalse(result)

    # Casos Esquinas
    
     # Prueba 12
     def test_12InsertMinLong(self):
         role1 = role()
         result = role1.insertRole('S','D',1)
         self.assertFalse(result)
         
     # Prueba 13
     def test_13InsertMaxLong(self):
        role1 = role()
        result = role1.insertRole(25*'me', 70*'Lo',1)
        self.assertFalse(result)
        
     # Prueba 14
     def test_14InsertRoleLong0DescriptionLong0(self):
         role1 = role()
         result = role1.insertRole('','',1)
         self.assertFalse(result)

     # Prueba 15
     def test_15InsertRoleLong51DescriptionLong141(self):
        role1 = role()
        result = role1.insertRole(25*'ma' + 'p', 70*'Lo' + 'l',1)
        self.assertFalse(result)
         

     # Casos Maliciosos
      
     # Prueba 16
     def test_16InsertNotRoleString(self):
         role1   = role()
         result = role1.insertRole(1254,'Un numero en vez de string',1)
         self.assertFalse(result,"Elemento insertado.")
    
     # Prueba 17
     def test_17InsertRoleNoneString(self):
         role1   = role()
         result = role1.insertRole(None,'Nombre vacio',1)
         self.assertFalse(result,"No válido.")
         
     # Prueba 18
     def test_18InsertDescriptionNoneString(self):
         role1   = role()
         result = role1.insertRole('Team Member',None,1)
         self.assertFalse(result,"No válido.")

     # Prueba 19
     def test_19InsertNotIDInteger(self):
         role1   = role()
         result = role1.insertRole('Scrum Master','Nombre cualquiera','Cancion')
         self.assertFalse(result,"No válido.")
         
     # Prueba 20
     def test_20InsertRoleDescriptionIdNone(self):
         role1   = role()
         result = role1.insertRole(None,None,None)
         self.assertFalse(result,"No válido.")

     # Prueba 21
     def test_21InsertId0(self):
         role1   = role()
         result = role1.insertRole('Team member','Nombre variable',0)
         self.assertFalse(result,"No válido.")
                  
         
         

     #############################################      
     #       Suite de Pruebas para FindName      #
     #############################################
     
     # Caso Inicial
     
     # Prueba 22 
     def test_22FindNameExists(self):
         role1   = role()
         role1.findNameRole('Product Owner')

            
     # Casos Fronteras
     
     # Prueba 23
     def test_23FindNameEmpty(self):
         role1   = role()
         result = role1.findNameRole('')
         self.assertFalse(result, "Expresión inválida.")
           
     # Prueba 24
     def test_24FindNameShortName1(self):
         role1   = role()
         result = role1.findNameRole('T')
         self.assertEqual(result,[],"Elemento no encontrado")
      
     # Prueba 25
     def test_25FindNameLongName50(self):
         role1   = role()
         result = role1.findNameRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
         self.assertEqual(result,[],"Elemento no encontrado")
           
     # Prueba 26
     def test_26FindNameLongName51(self):
         role1   = role()
         result = role1.findNameRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me') 
         self.assertFalse(result, "Cadena no válida")
         
     # Casos Maliciosos
     
     # Prueba 27
     def test_27FindNameNotString(self):
         role1   = role()
         result = role1.findNameRole(1254)
         self.assertFalse(result,"Elemento Insertado") 
      
     # Prueba 28
     def test_28FindNameNoneString(self):
         role1   = role()
         result = role1.findNameRole(None)
         self.assertFalse(result,"Válido")    

     #############################################      
     #       Suite de Pruebas para UpdateRole    #
     #############################################   
     
     # Caso Inicial
     
     # Prueba 29
     def test_29UpdateRoleExists(self):
         role1   = role()
         role1.updateRole('Product Owner','Scrum Master','Descripcion')
   
     # Casos Normales
     
     #Prueba 30
     def test_30UpdateRole(self):
        role1   = role()
        result = role1.updateRole('Scrum Master','Product Owner','Nueva Descripcion')
        self.assertFalse(result)
          
     # Casos Fronteras
      
     # Prueba 31
     def test_31UpdateRoleLeftLen1(self):
         role1   = role()
         result = role1.updateRole('T','Team Member','New Description')
         self.assertFalse(result)

     
     # Prueba 32         
     def test_32UpdateRoleRightLen1(self):
         role1   = role()
         result = role1.updateRole('Team Member','T','Nueva Descripción')
         self.assertFalse(result)


     # Prueba 33         
     def test_33UpdateRoleRightLen50(self):
         role1   = role()
         result = role1.updateRole('Scrum Master',50*'T','Nueva Descripcion')
         self.assertFalse(result)
         
     # Prueba 34
     def test_34UpdateRoleLeftLen50(self):
         role1   = role()
         result = role1.updateRole(50*'T','M', 'New Description')
         self.assertFalse(result)

     # Prueba 35
     def test_35UpdateRoleDescriptionLen1(self):
         role1   = role()
         result = role1.updateRole('Team Member','Team Member', 'N')
         self.assertFalse(result)

     # Prueba 36
     def test_36UpdateRoleDescriptionLen140(self):
         role1   = role()
         result = role1.updateRole('Team Master','Scrum Master', 70* 'Nw')
         self.assertFalse(result)
         
    # Prueba 37
     def test_37UpdateRoleDescriptionLen0(self):
         role1   = role()
         result = role1.updateRole('Team Member','Team Member', '')
         self.assertFalse(result)

     # Prueba 38         
     def test_38UpdateRoleRightLen51(self):
         role1   = role()
         result = role1.updateRole('Scrum Master',50*'T' + 'a','Nueva Descripcion')
         self.assertFalse(result)

     # Prueba 39         
     def test_39UpdateRoleLeftLen51(self):
         role1   = role()
         result = role1.updateRole(25*'Sc' + 'a','Team Master','Nueva Descripcion')
         self.assertFalse(result)
         
     # Casos Esquinas
     
     # Prueba 40
     def test_40UpdateRoleLeftLen1RightLen50(self):
         role1   = role()
         result = role1.updateRole('M',25*'Us','Description')
         self.assertFalse(result) 

     # Prueba 41
     def test_41UpdateRoleLeftLen50RightLen50(self):
         role1   = role()
         result = role1.updateRole(25*'Us', 25*'Ma','Description')
         self.assertFalse(result) 
 
     # Prueba 42
     def test_42UpdateRoleLeftLen50RightLen1(self):
         role1   = role()
         result = role1.updateRole(25*'Ma','M','Descripciones')
         self.assertFalse(result) 
 
     # Prueba 43
     def test_43UpdateRoleLeftLen1RightLen1(self):
         role1   = role()
         result = role1.updateRole('M','U','Nueva Descripcion')
         self.assertFalse(result) 
 
     # Prueba 44
     def test_44UpdateRoleLeftLen1RightLen50Description1(self):
         role1   = role()
         result = role1.updateRole('M',25*'Us','')
         self.assertFalse(result) 

     # Prueba 45
     def test_45UpdateRoleLeftLen1RightLen50Description140(self):
         role1   = role()
         result = role1.updateRole('M',25*'Us',70*'mo')
         self.assertFalse(result) 

     # Prueba 46
     def test_46UpdateRoleLeftLen50RightLen50Description140(self):
         role1   = role()
         result = role1.updateRole(25*'Us', 25*'Ma',70*'de')
         self.assertFalse(result) 

     # Prueba 47
     def test_47UpdateRoleLeftLen1RightLen1Description1(self):
         role1   = role()
         result = role1.updateRole('s','t','d')
         self.assertFalse(result) 

     # Prueba 48
     def test_48UpdateRoleLeftLen51RightLen51Description141(self):
         role1   = role()
         result = role1.updateRole(25*'se' + 'a',25*'lo'+ 'b',70*'de' + 'a')
         self.assertFalse(result) 

     # Casos Maliciosos
          
     # Prueba 49
     def test_49UpdateRoleLeftLen0RightLen51Description0(self):
         role1   = role()
         result = role1.updateRole('',25*'Pi' + 'p','')
         self.assertFalse(result, "Modificación válida") 
  
     # Prueba 50
     def test_50UpdateRoleLeftLen51RightLen0Description0(self):
         role1   = role()
         result = role1.updateRole(25*'Ma'+ 's','','')
         self.assertFalse(result, "Modificación válida") 
 
     # Prueba 51
     def test_51UpdateRoleLeftNoneRightValidString(self):
         role1   = role()
         result = role1.updateRole(None,'Juana la Iguana','Description')
         self.assertFalse(result,"Modificación válida") 
         
     # Prueba 52
     def test_52UpdateRoleLeftValidStringRightNone(self):
         role1   = role()
         result = role1.updateRole('Juana la Iguana',None,'Nueva Descripcion')
         self.assertFalse(result, "Modificación válida") 
          
     # Prueba 53
     def test_53UpdateRoleLeftValidStringRightDescriptionNone(self):
         role1   = role()
         result = role1.updateRole('Juana la Iguana','Scrum Master',None)
         self.assertFalse(result, "Modificación válida")
         
     # Prueba 54
     def test_54UpdateRoleNone(self):
         role1   = role()
         result = role1.updateRole(None,None,None)
         self.assertFalse(result, "Modificación válida") 
          
     # Prueba 55
     def test_55UpdateRoleLeft0Right0Description0(self):
         role1   = role()
         result = role1.updateRole('','','')
         self.assertFalse(result, "Modificación válida") 
          
         
     #############################################      
     #       Suite de Pruebas para DeleteRole    #
     #############################################   
 
     # Caso Inicial
     
     # Prueba 56
     def test_56DeleteIdExists(self):
         role1   = role()
         role1.deleteRole(4)

     # Casos Normales
 
     # Prueba 57
     def test_57DeleteId(self):
         role1   = role()
         result = role1.deleteRole(2)
         self.assertTrue(result)
          
     # Casos Fronteras
     
     # Prueba 58
     def test_58DeleteId1(self):
         role1   = role()
         result = role1.deleteRole(1)
         self.assertTrue(result)
 
     # Casos Maliciosos
 
     # Prueba 59
     def test_59DeleteIdMin0(self):
         role1   = role()
         result = role1.deleteRole(0)
         self.assertFalse(result,"Id no válido")
 
     # Prueba 60
     def test_60DeleteIdNotInteger(self):
         role1   = role()
         result = role1.deleteRole('AldJos')
         self.assertFalse(result, "Es válida")
