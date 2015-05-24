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
     def testInsertExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole('Product Owner','description',1)
         role1.deleteRole('Product Owner')
         aBackLog.deleteProduct('Taxi seguro.')    
         
     # Casos Normales
           
     # Prueba 2 
    
     def testInsertElement(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Team Member','Lo que sea',1)
         self.assertTrue(result)
         role1.deleteRole('Team Member')
         aBackLog.deleteProduct('Taxi seguro.')
          
    # Prueba 3
     def testInsertRepeatedElement(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Scrum Master','Lo que sea',1)
         result1 = role1.insertRole('Scrum Master','Lo que sea',1)
         self.assertFalse(result1, "Elemento insertado.")
         aBackLog.deleteProduct('Taxi seguro.') 
     # Casos Fronteras
      
     # Prueba 4
     def testInsertLongName50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M','Mucha longitud',1)
         self.assertTrue(result)
         role1.deleteRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 5
     def testInsertLongName51(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me','Maximo de longitud mas uno',1) 
         self.assertFalse(result, "Elemento insertado.")
         aBackLog.deleteProduct('Taxi seguro.') 
             
     # Prueba 6
     def testInsertShortName0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('','Vacio',1)
         self.assertFalse(result, "Elemento insertado.") 
         aBackLog.deleteProduct('Taxi seguro.') 
              
     # Prueba 7
     def testInsertLongName1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('T','Una sola letra',1)
         self.assertTrue(result)
         role1.deleteRole('T')
         aBackLog.deleteProduct('Taxi seguro.') 
         
    # Prueba 8
     def testInsertDescriptionLong1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi') 
         role1 = role()
         result = role1.insertRole('Scrum M','o',1)
         self.assertTrue(result)
         role1.deleteRole('Scrum M')
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 9
     def testInsertDescriptionLong140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Member', 70*'La',1)
         self.assertTrue(result)
         role1.deleteRole('Member')
         aBackLog.deleteProduct('Taxi seguro.') 
         
    # Prueba 10
     def testInsertDescriptionLong0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         result = role1.insertRole('Role','',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 11
     def testInsertDescriptionLong141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Team', 70*'La' + 'a',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
    # Casos Esquinas
    
     # Prueba 12
     def testInsertMinLong(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         result = role1.insertRole('S','D',1)
         self.assertTrue(result)
         role1.deleteRole('S')
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 13
     def testInsertMaxLong(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         result = role1.insertRole(25*'me', 70*'Lo',1)
         self.assertTrue(result)
         role1.deleteRole(25*'me')
         aBackLog.deleteProduct('Taxi seguro.') 
        
     # Prueba 14
     def testInsertRoleLong0DescriptionLong0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         result = role1.insertRole('','',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 15
     def testInsertRoleLong51DescriptionLong141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         result = role1.insertRole(25*'ma' + 'p', 70*'Lo' + 'l',1)
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 

     # Casos Maliciosos
      
     # Prueba 16
     def testInsertNotRoleString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole(1254,'Un numero en vez de string',1)
         self.assertFalse(result,"Elemento insertado.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 17
     def testInsertRoleNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole(None,'Nombre vacio',1)
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 18
     def testInsertDescriptionNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Team Member',None,1)
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.')
          
     # Prueba 19
     def testInsertNotIDInteger(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Nuevo Role','Nombre cualquiera','Cancion')
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 20
     def testInsertRoleDescriptionIdNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole(None,None,None)
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 21
     def testInsertId0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole('Rolenuevo','Nombre variable',0)
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.')          
         
     #############################################      
     #       Suite de Pruebas para FindName      #
     #############################################
     
     # Caso Inicial
     
     # Prueba 22 
     def testFindNameExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Nuevo Product Owner','descripcion',1)
         role1.findNameRole('Nuevo Product Owner')
         role1.deleteRole('Nuevo Product Owner')
         aBackLog.deleteProduct('Taxi seguro.') 
            
     # Casos Fronteras
     
     # Prueba 23
     def testFindNameEmpty(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.findNameRole('')
         self.assertEqual(result,[], "Expresión inválida.")
         aBackLog.deleteProduct('Taxi seguro.')
           
     # Prueba 24
     def testFindNameShortName1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Nuevo T','Desc',1)
         result = role1.findNameRole('Nuevo T')
         self.assertNotEqual(result,[],"Elemento no encontrado")
         role1.deleteRole('Nuevo T')
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 25
     def testFindNameLongName50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Team Scrum Team MemberTeam MemberTeam MemberScrumS','Nuevo',1)
         result = role1.findNameRole('Team Scrum Team MemberTeam MemberTeam MemberScrumS')
         self.assertNotEqual(result,[],"Elemento no encontrado")
         role1.deleteRole('Team Scrum Team MemberTeam MemberTeam MemberScrumS')
         aBackLog.deleteProduct('Taxi seguro.') 
           
     # Prueba 26
     def testFindNameLongName51(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Team Scrum Team MemberTeam MemberTeam MemberScrumST','caracteres',1)
         result = role1.findNameRole('Team Scrum Team MemberTeam MemberTeam MemberScrumST') 
         self.assertEqual(result,[],"Cadena no válida")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Casos Maliciosos
     
     # Prueba 27
     def testFindNameNotString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         result = role1.insertRole(1254,'numeros',1)
         result = role1.findNameRole(1254)
         self.assertEqual(result,[],"Elemento Insertado") 
         aBackLog.deleteProduct('Taxi seguro.') 
      
     # Prueba 28
     def testFindNameNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(None,'nada',1)
         result = role1.findNameRole(None)
         self.assertEqual(result,[],"Válido")    
         aBackLog.deleteProduct('Taxi seguro.') 

     #############################################      
     #       Suite de Pruebas para UpdateRole    #
     #############################################   
     
     # Caso Inicial
     
     # Prueba 29
     def testUpdateRoleExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Dueño de producto','Nueva descripcion',1)
         role1.updateRole('Dueño de producto','Cliente','Descripcion reciente')
         role1.deleteRole('Cliente')
         aBackLog.deleteProduct('Taxi seguro.') 
   
     # Casos Normales
     
     #Prueba 30
     def testUpdateRole(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Maestro Scrum','scrum master',1)
         result = role1.updateRole('Maestro Scrum','Un nuevo maestro','Nueva Descripcion')
         self.assertTrue(result)
         role1.deleteRole('Un nuevo maestro')
         aBackLog.deleteProduct('Taxi seguro.') 
          
     # Casos Fronteras
      
     # Prueba 31
     def testUpdateRoleLeftLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('X','X',1)
         result = role1.updateRole('X','roleX','New Description')
         self.assertTrue(result)
         role1.deleteRole('roleX')
         aBackLog.deleteProduct('Taxi seguro.') 
    
     # Prueba 32         
     def testUpdateRoleRightLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('roleZ','Z',1)
         result = role1.updateRole('roleZ','Z','Nueva Descripción')
         self.assertTrue(result)
         role1.deleteRole('Z')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 33         
     def testUpdateRoleRightLen50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('UnNuevoRole','role',1)
         result = role1.updateRole('UnNuevoRole',50*'R','Nueva Descripcion')
         self.assertTrue(result)
         role1.deleteRole(50*'R')
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 34
     def testUpdateRoleLeftLen50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(50*'A','soloA',1)
         result = role1.updateRole(50*'A','M', 'New Description')
         self.assertTrue(result)
         role1.deleteRole('M')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 35
     def testUpdateRoleDescriptionLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Arole','Description for a',1)
         result = role1.updateRole('Arole','Brole', 'N')
         self.assertTrue(result)
         role1.deleteRole('Brole')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 36
     def testUpdateRoleDescriptionLen140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('pro role','pro description',1)
         result = role1.updateRole('pro role','simple role', 70* 'Nw')
         self.assertTrue(result)
         role1.deleteRole('simple role')
         aBackLog.deleteProduct('Taxi seguro.') 
         
    # Prueba 37
     def testUpdateRoleDescriptionLen0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('role non description','some description',1)
         result = role1.updateRole('role non description','role description', '')
         self.assertFalse(result)
         role1.deleteRole('role non description')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 38         
     def testUpdateRoleRightLen51(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('any new role','a new description',1)
         result = role1.updateRole('any new role',50*'P' + 'a','Nueva Descripcion')
         self.assertFalse(result)
         role1.deleteRole('any new role')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 39         
     def test_39UpdateRoleLeftLen51(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(25*'Sc' + 'a','description',1)
         result = role1.updateRole(25*'Sc' + 'a','cS','Nueva Descripcion')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
     # Casos Esquinas
     
     # Prueba 40
     def test_40UpdateRoleLeftLen1RightLen50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('O','new',1)
         result = role1.updateRole('O',25*'Pq','Description')
         self.assertTrue(result) 
         role1.deleteRole('O')
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 41
     def test_41UpdateRoleLeftLen50RightLen50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(25*'Us','x',1)
         result = role1.updateRole(25*'Us', 25*'Ma','Description')
         self.assertTrue(result)
         role1.deleteRole(25*'Ma') 
         aBackLog.deleteProduct('Taxi seguro.') 
 
     # Prueba 42
     def test_42UpdateRoleLeftLen50RightLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(25*'LL','l',1)
         result = role1.updateRole(25*'LL','E','Descripciones')
         self.assertTrue(result)
         role1.deleteRole('E')
         aBackLog.deleteProduct('Taxi seguro.')  
 
     # Prueba 43
     def test_43UpdateRoleLeftLen1RightLen1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('V','new v',1)
         result = role1.updateRole('V','G','Nueva Descripcion')
         self.assertTrue(result)
         role1.deleteRole('G') 
         aBackLog.deleteProduct('Taxi seguro.') 
 
     # Prueba 44
     def test_44UpdateRoleLeftLen1RightLen50Description1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('J','j',1)
         result = role1.updateRole('J',25*'fr','a')
         self.assertTrue(result)
         role1.deleteRole(25*'fr')
         aBackLog.deleteProduct('Taxi seguro.')  

     # Prueba 45
     def test_45UpdateRoleLeftLen1RightLen50Description140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('k','K',1)
         result = role1.updateRole('k',25*'gb',70*'mo')
         self.assertTrue(result) 
         role1.deleteRole(25*'gb')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 46
     def test_46UpdateRoleLeftLen50RightLen50Description140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(25*'li','li',1)
         result = role1.updateRole(25*'li', 25*'IL',70*'de')
         self.assertTrue(result)
         role1.deleteRole(25*'IL') 
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 47
     def test_47UpdateRoleLeftLen1RightLen1Description1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('s','t',1)
         result = role1.updateRole('s','t','d')
         self.assertTrue(result)
         role1.deleteRole('t') 
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 48
     def test_48UpdateRoleLeftLen51RightLen51Description141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(25*'se','es',1)
         result = role1.updateRole(25*'se' + 'a',25*'lo'+ 'b',70*'de' + 'a')
         self.assertFalse(result)
         role1.deleteRole(25*'se') 
         aBackLog.deleteProduct('Taxi seguro.') 

     # Casos Maliciosos
          
     # Prueba 49
     def test_49UpdateRoleLeftLen0RightLen51Description0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('','d',1)
         result = role1.updateRole('',25*'Pi' + 'p','')
         self.assertFalse(result, "Modificación válida")
         aBackLog.deleteProduct('Taxi seguro.')  
  
     # Prueba 50
     def test_50UpdateRoleLeftLen51RightLen0Description0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(25*'Ma'+ 's','g',1)
         result = role1.updateRole(25*'Ma'+ 's','','')
         self.assertFalse(result, "Modificación válida") 
         aBackLog.deleteProduct('Taxi seguro.') 
 
     # Prueba 51
     def test_51UpdateRoleLeftNoneRightValidString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(None,'nada',1)
         result = role1.updateRole(None,'Juana la Iguana','Description')
         self.assertFalse(result,"Modificación válida") 
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 52
     def test_52UpdateRoleLeftValidStringRightNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Juana la Iguana','j',1)
         result = role1.updateRole('Juana la Iguana',None,'Nueva Descripcion')
         self.assertFalse(result, "Modificación válida")
         role1.deleteRole('Juana la Iguana') 
         aBackLog.deleteProduct('Taxi seguro.') 
          
     # Prueba 53
     def test_53UpdateRoleLeftValidStringRightDescriptionNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('nuevorolenuevo','x',1)
         result = role1.updateRole('nuevorolenuevo','ROLEPerson',None)
         self.assertFalse(result, "Modificación válida")
         role1.deleteRole('nuevorolenuevo')
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 54
     def test_54UpdateRoleNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(None,'nada',1)
         result = role1.updateRole(None,None,None)
         self.assertFalse(result, "Modificación válida")
         aBackLog.deleteProduct('Taxi seguro.')  
          
     # Prueba 55
     def test_55UpdateRoleLeft0Right0Description0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('','nada',1)
         result = role1.updateRole('','','')
         self.assertFalse(result, "Modificación válida") 
         aBackLog.deleteProduct('Taxi seguro.')  
         
     #############################################      
     #       Suite de Pruebas para DeleteRole    #
     #############################################   
 
     # Caso Inicial
     
     # Prueba 56
     def test_56DeleteRoleExists(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Role a','descripcion a',1)
         role1.deleteRole('Role a')
         aBackLog.deleteProduct('Taxi seguro.') 

     # Casos Normales
 
     # Prueba 57
     def testDeleteLongName50(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M','Mucha longitud',1)
         result = role1.deleteRole('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
         self.assertTrue(result)
         aBackLog.deleteProduct('Taxi seguro.') 

     # Prueba 58
     def testDeleteLongName51(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me','Maximo de longitud mas uno',1) 
         result = role1.deleteRole('Team MemberTeam MemberTeam MemberTeam MemberTeam Me')
         self.assertFalse(result, "Elemento insertado.")
         aBackLog.deleteProduct('Taxi seguro.')  
             
     # Prueba 59
     def testDeleteShortName0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('','Vacio',1)
         result = role1.deleteRole('')
         self.assertFalse(result, "Elemento insertado.") 
         aBackLog.deleteProduct('Taxi seguro.') 
              
     # Prueba 60
     def testDeleteLongName1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('T','Una sola letra',1)
         result = role1.deleteRole('T')
         self.assertTrue(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 61
     def testDeleteDescriptionLong1(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi') 
         role1 = role()
         role1.insertRole('Scrum M','o',1)
         result = role1.deleteRole('Scrum M')
         self.assertTrue(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 62
     def testDeleteDescriptionLong140(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Member', 70*'La',1)
         result = role1.deleteRole('Member')
         self.assertTrue(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
    # Prueba 63
     def testDeleteDescriptionLong0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole('Role','',1)
         result = role1.deleteRole('Role')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 64
     def testDeleteDescriptionLong141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Team', 70*'La' + 'a',1)
         result = role1.deleteRole('Team')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
    # Casos Esquinas
    
     # Prueba 65
     def testDeleteMinLong(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole('S','D',1)
         result = role1.deleteRole('S')
         self.assertTrue(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 66
     def testDeleteMaxLong(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole(25*'me', 70*'Lo',1)
         result = role1.deleteRole(25*'me')
         self.assertTrue(result)
         aBackLog.deleteProduct('Taxi seguro.') 
        
     # Prueba 67
     def testDeleteRoleLong0DescriptionLong0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole('','',1)
         result = role1.deleteRole('')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 68
     def testDeleteRoleLong51DescriptionLong141(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         role1.insertRole(25*'ma' + 'p', 70*'Lo' + 'l',1)
         result = role1.deleteRole(25*'ma'+'p')
         self.assertFalse(result)
         aBackLog.deleteProduct('Taxi seguro.') 

     # Casos Maliciosos
      
     # Prueba 69
     def testDeleteNotRoleString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(1254,'Un numero en vez de string',1)
         result = role1.deleteRole(25*'me')
         self.assertFalse(result,"Elemento insertado.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 70
     def testDeleteRoleNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(None,'Nombre vacio',1)
         result = role1.deleteRole(None)
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 71
     def testDeleteDescriptionNoneString(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Team Member',None,1)
         result = role1.deleteRole('Team Member')
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.')
          
     # Prueba 72
     def testDeleteNotIDInteger(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Nuevo Role','Nombre cualquiera','Cancion')
         result = role1.deleteRole('Nuevo Role')
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 73
     def testDeleteRoleDescriptionIdNone(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole(None,None,None)
         result = role1.deleteRole(None)
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.') 
         
     # Prueba 74
     def testDeleteId0(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1   = role()
         role1.insertRole('Rolenuevo','Nombre variable',0)
         result = role1.deleteRole('Rolenuevo')
         self.assertFalse(result,"No válido.")
         aBackLog.deleteProduct('Taxi seguro.')       