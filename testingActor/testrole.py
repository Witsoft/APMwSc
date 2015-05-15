'''
Created on 7/05/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import sys
import unittest
sys.path.append('../app/scrum')
from model import * 
from role import *

class clsRoleTester(unittest.TestCase):

    #CASOS DE PRUEBA FUNCION INSERTROLE
    
    # Caso Frontera
    # Se verifica una entrada válida para funcion insert role inexistente
    def test1RoleInsert(self):
        role1 = role()
        self.assertTrue(role1.insertRole(idrole = 1,namerole = 'Product Owner'))
    
    #Caso Frontera
    # Se verifica una entrada inválida para funcion insert role    
    def test2RoleInsertFalse(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 1,namerole = 'Product Owner'))
    
    #Caso Malicia
    # Se verifica una entrada de idrole vacia
    def test3RoleInsertNotidrole(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = None, namerole = 'Scrum Master'))
    
    #Caso Frontera externa
    # Se verifica una entrada inválida con idrole igual a 0
    def test4RoleInsertidrole0(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 0,namerole = 'Team member'))
    
    #Caso Fronetra 
    # Se verifica una entrada válida muy grande
    def test5RoleInsertidrole(self):
        role1 = role()
        self.assertTrue(role1.insertRole(idrole = (2**31)-1,namerole = 'Scrum Master'))
    
    #Caso ESquina
    # Se verifica una entrada inválida con namerole invalido
    def tesdt6RoleInsertNamerolInvalid(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 587,namerole = 'Computacion'))
    
    #Caso Malicia
    # Se verifica una entrada inválida con namerole vacio
    def test7RoleInsertNotNamerole(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 587,namerole = ''))
    
    #Caso Frontera Externa
    # Se verifica una entrada inválida de 51 caracteres pero namerole invalido
    def test8RoleInsertNameroleChar51(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 300,namerole = 'Departamento de Informacion y Tecnologia Computacio'))
    
    #Caso frontera
    # Se verifica una entrada inválida de 50 caracteres pero namerole invalidoe
    def test9RoleInsertNameroleChar50(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 301,namerole = 'Departamento de Informacion y Tecnologia Computaci'))
    
    #Caso Frontera interna
    # Se verifica una entrada inválida de 49 caracteres pero namerole invalidoe
    def test_10RoleInsertNameroleChar49(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 302,namerole = 'Departamento de Informacion y Tecnologia Computac'))
    
    #Caso Malicia
    # Se verifica una entrada inválida con idrole negativo y namerole invalido
    def test_11RoleInsertNegative(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = -566,namerole = 'mecanica'))
    
    #Caso esquina
    # Se verifica una entrada inválida de 1 caracter
    def test_12RoleInsertminchar(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = 1,namerole = 'x'))
    
    #caso malicia
    # Se verifica una entrada inválida con idrole y namerole vacios   
    def test_13RoleInsertNoparam(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = '' ,namerole = ''))
    
    #caso esquina
    # Se verifica una entrada id role muy grande válida con namerole invalido
    def test_14RoleInsertmax(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = (2**31) ,namerole = 'Departamento de Informacion & Tecnologia Computaci'))
    
    #caso esquina
    #Se verifica una entrada idrole muy grande y namerole valido 
    def test_15RoleInsertmax(self):
        role1 = role()
        self.assertTrue(role1.insertRole(idrole = (2**31) ,namerole = 'Team member'))
    
    #caso malicia   
    #Se verifica una entrada idrole None y namerole vacio 
    def test_16RoleInsertNoparamId(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = None ,namerole = ''))
    
    #caso malicia
    #Se verifica una entrada idrole None y namerole con entero    
    def test_17RoleInsertNoparam(self):
        role1 = role()
        self.assertFalse(role1.insertRole(idrole = None ,namerole = 30))
    
    ###########################################################################
    
    #CASOS DE PRUEBA FUNCION SEARCHROLE
    
    #Caso Frontera
    #Se verifica una entrada valida para funcion searchRole inexistente 
    def test_18searchRole(self):
        role1 = role()
        self.assertNotEqual([],role1.searchRole(idrole = 1))
    
    #Caso Frontera
    def test_19searchRoleidrolebig(self):
        role1 = role()
        self.assertNotEqual([],role1.searchRole(idrole = (2**31)-1))     
    
    #Caso Malicia
    def test_20seacrhRoleidroleNoInt(self):
        role1 = role()
        self.assertEqual([],role1.searchRole(idrole = ''))
    
    #Caso Malicia
    def test_21seacrhRoleidroleNoParam(self):
        role1 = role()
        self.assertEqual([],role1.searchRole(idrole = None))        
    
    #Caso Malicia
    def test_22seacrhRoleidrole0(self):
        role1 = role()
        self.assertEqual([],role1.searchRole(idrole = 0))
    
    #Caso Malicia
    def test_23seacrhRoleidrolenegative(self):
        role1 = role()
        self.assertEqual([],role1.searchRole(idrole = -8))       
    
    #####################################################################
    
    
    #CASOS DE PRUEBA FUNCION UPDATEROLE
    
    #caso Frontera
    def test_23_1updateRoleTrue(self):
        role1 = role()
        self.assertTrue(role1.updateRole(idrole = 1, namerole = 'Product Owner'))
        
    #caso Frontera
    def test_23_2updateRoleFalse(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 2, namerole = 'Team member'))
   
 
    #caso Frontera        
    def test_23_3updateRole49(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = 'Departamento de Informacion & Tecnologia en Compu'))
    
    #caso Frontera
    def test_23_4updateRole50(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = 'Departamento de ingieniria de computacion y techno'))
    
    #caso Frontera
    def test_23_5updateRole51(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = 'departamento of InformacIon & Tecnologia computacio'))
    
    #caso Frontera            
    def test_23_6updateRoleNoChar(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = ''))
    
    #caso Malicia
    def test_23_6updateRoleNone(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = None))
    
    #caso Malicia
    def test_23_7updateRoleNoidNoname(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 0, namerole = ''))
    
    #caso Malicia
    def test_23_8updateRoleNoparam(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = None, namerole = ''))
    
    #caso Frontera        
    def test_23_9updateRole49(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = 'Departamento de Informacion & Tecnologia en Compu'))
    
    #caso Frontera
    def test_23_10updateRole50(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = 'Departamento de ingieniria de computacion y techno'))
    
    #caso Frontera
    def test_23_11updateRole51(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = 'departamento of InformacIon & Tecnologia computacio'))
    
    #caso Frontera            
    def test_23_12updateRoleNoChar(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = ''))
    
    #caso Malicia
    def test_23_13updateRoleNone(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 1, namerole = None))
    
    #caso Malicia
    def test_23_14updateRoleNoidNoname(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = 0, namerole = ''))
    
    #caso Malicia
    def test_23_15updateRoleNoparam(self):
        role1 = role()
        self.assertFalse(role1.updateRole(idrole = None, namerole = ''))
    
   
   

    ######################################################################        
    #CASOS DE PRUEBA FUNCION DELETEROLE
    
    #Caso Frontera
    def test_24deleteRoleTrue(self):
        role1 = role()
        self.assertTrue(role1.deleteRole(idrole = 1))  
    
    #Caso Frontera
    def test_25deleteRoleFalse(self):
        role1 = role()
        self.assertFalse(role1.deleteRole(idrole = 1))  
    
    #Caso Frontera
    def test_26deleteRoleidrolebig(self):
        role1 = role()
        self.assertTrue(role1.deleteRole(idrole = (2**31)-1))     
    
    #Caso Malicia
    def test_27deleteRoleidroleNoInt(self):
        role1 = role()
        self.assertFalse(role1.deleteRole(idrole = ''))
    
    #Caso Malicia
    def test_28deleteRoleidroleNoParam(self):
        role1 = role()
        self.assertFalse(role1.deleteRole(idrole = None))        
    
    #Caso Malicia
    def test_29deleteRoleidrole0(self):
        role1 = role()
        self.assertFalse(role1.deleteRole(idrole = 0))
    
    #Caso Malicia
    def test_30deleteRoleidrolenegative(self):
        role1 = role()
        self.assertFalse(role1.deleteRole(idrole = -8))   
