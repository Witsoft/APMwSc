# -*- coding: utf-8 -*-. 

import unittest

from userDummy import *

class clsUserTester(unittest.TestCase):
   
    # CASOS DE PRUEBA FUNCION INSERTUSER
#     
#     def testUserInsertExist(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah','ehfah','al', '@ls', 1)
#         user1.deleteUser('ehfah')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     # Caso frontera
#     def testUserInsertTrue(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah','ehfahw','alir893b1', '@ls', 1)
#         self.assertTrue(result)
#         user1.deleteUser('ehfahw')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#      
#     # Caso frontera
#     def testUserInsertFalse(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah', 'ehfah','al', '@ls', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Caso frontera externa
#     def testUserInsertNoUser(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah', '','al', '@?lds', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#       
#     # Caso frontera interna 
#     def testUserInsert1char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid', 'a','1223478364', 'xxx@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('a')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')  
# 
#     # Caso frontera Externa 
#     def testUserInsert17char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#         
#     # Caso frontera Externa 
#     def testUserInsert16char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid', 'jksjdfdjvkjdfuhf','122346768', 'yzyyxxx@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('jksjdfdjvkjdfuhf')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Caso frontera Externa 
#     def testUserInsert15char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid', 'wjfr9olpsmfkreo','1225676834', 'xfeexx@fgmail.com', 1)
#         self.assertTrue(result) 
#         user1.deleteUser('wjfr9olpsmfkreo')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     # Caso frontera
#     def testUserInsert8char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid', 'wiekfprm','1223463637', 'yffe@ldv.gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('wiekfprm')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#           
#     # Caso frontera Externa 
#     def testUserInserFullnamet51char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmkd', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#       
#     #caso frontera
#     def testUserInserFullnamet50char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result =  user1.insertUser('sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmk', 'jksjdfdj__','1223485953', 'xx__x@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('jksjdfdj__') 
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')      
#       
#       
#     #caso frontera Interna 
#     def testUserInserFullnamet49char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', 'jpvkjdfuhf','8475312234', 'xyyy@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('jpvkjdfuhf') 
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#       
#     #caso frontera Externa 
#     def testUserInserFullnamet25char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('Patricia Reyes Valencia25', 'patkjdfuhf','1223467843', 'patx@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('patkjdfuhf')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso frontera Externa 
#     def test9_0UserInserNoFullname(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('', 'patkjdfuhf','12234', 'patx@gmail.com', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     #caso frontera Externa 
#     def testUserInserFullnamet1char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('P', 'patkfhf_1','122374834', 'paddtx@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('patkfhf_1')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso frontera Externa
#     def testUserInsertEmail31char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia', 'tdd ','12d234', '10-10603-10-10916ing@ldc.usb.ve', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso frontera Externa
#     def testUserInsertNoEmail(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia', 'tdd ','12d234', '', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso frontera Interna
#     def testUserInsertEmail1char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia', 'tdd_1 ','12d2345678', '@', 1)
#         self.assertTrue(result)
#         user1.deleteUser('tdd_1')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')        
#       
#     #caso frontera Interna
#     def testUserInsertEmail30char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia', 'tdd_2','12d2356784', '123167890patricia_v@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('tdd_2')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso frontera Interna
#     def testUserInsertEmail29char(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid Patricia', 'tdd_3','12d2343434', '123167890patriciav@gmail.com', 1)
#         self.assertTrue(result)
#         user1.deleteUser('tdd_3')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#      #caso frontera externa
#     def testUserInsertPassword17(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('pat', 'ehfer_23','12316789qwertyuai', '2@ls', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     #caso frontera externa
#     def testUserInsertNoPassword(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah', 'ehfadh_2','', '3@ls', 1)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#        
#     #caso frontera interna
#     def testUserInsertPassword15(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah', 'ehf_1','eifko09olpedft5', 'po@rls', 1)
#         self.assertTrue(result)
#         user1.deleteUser('ehf_1')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#        
#     #caso frontera interna
#     def testUserInsertPassword8(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sr', 'er3r_1','12345678', 'desm@ld.s', 1)
#         self.assertTrue(result)
#         user1.deleteUser('er3r_1')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#        
#     #caso frontera
#     def testUserInsertPasword16(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah', 'frkfe_1','qiejdp0t4jmds21l', 'fefef_t@l.ss', 1)
#         self.assertTrue(result)
#         user1.deleteUser('frkfe_1')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso frontera
#     def testUserInsertPassword8(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sah', 'lowdn','kdiopw34', 'efmefm@l.c', 1)
#         self.assertTrue(result)
#         user1.deleteUser('lowdn')
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #Caso Malicia
#     def testUserInsertidroleChar(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('sahid', 'a','12234', 'xxx@gmail.com','b')
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso malicia
#     def testUserInsertNochar(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('', '','', '', None)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#     
#     #caso malicia   
#     def testUserInsertNoParam(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser(None, None,None, None,None)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #caso Frontera
#     def testUserInsertNoRole(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('srgfer', 'pw74b_r','efoewfwe1', 'tarea@hot.com', None)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
# 
#     #caso Frontera
#     def testUserInsertNoRole(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('utdf R', 'olpo','efefefr3', 'nonemail@,mail.cpom', 80)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')
#         
#     #Caso esquina
#     def testUserInsertNoForeign(self):
#         aBackLog = backLog()
#         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
#         role1 = role()
#         user1 = user()
#         role1.insertRole('Product Owner','description',1)
#         result = user1.insertUser('fiee0 ee', 'q84-g0gs','wdwd94', 'ffjfor@w.pol',  60)
#         self.assertFalse(result)
#         role1.deleteRole('Product Owner')
#         aBackLog.deleteProduct('Taxi seguro.')


     ##########################################      
     #   Suite de Pruebas para searchUser     #
     ##########################################
    
    #Caso Frontera
    def testsearchUserExist(self):
        user1 = user()
        result = user1.searchUser('ehfah')

    #Caso Frontera
    def test_23searchUserTrue(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')

        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('nombre','ehfah','12345678','ef@fg.com',1)
        result = user1.searchUser('ehfah')
        self.assertNotEqual([],result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #Caso Frontera 
    def test_24searchUser1Char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('nombreA','a','12345678','a@g.com',1)
        result = user1.searchUser('a')
        self.assertNotEqual([],result)
        user1.deleteUser('a')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
'''   
    #Caso Frontera
    def test_25searchUser16Char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertNotEqual([],user1.searchUser('jksjdfdjvkjdfuhf'))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')

    #Caso Frontera externa
    def test_26SearchUserNotChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1) 
        self.assertEqual([],user1.searchUser(''))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
    
    #Caso Frontera externa
    def test_27searchUser17Char(self):

        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertEqual([],user1.searchUser('jksjdfdj vkjdfuhf'))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')

    #Caso Esquina
    def test_28searchUserNotInsert(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertEqual([],user1.searchUser('PatriciaValencia'))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')

    #Caso INtermedio
    def test_29searchUser8Char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertNotEqual([],user1.searchUser('wiekfprm'))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')

    #caso Malicia 
    def test_29_1searchUserNoChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertEqual([],user1.searchUser(''))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
          
    def test_29_2searchUserNoParam(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertEqual([],user1.searchUser(None))
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')

    


    ###############################################################################################    
   
     #CASOS DE PRUEBA FUNCION UPDATEUSER


       
    def test_30updateUserTrue(self):
        user1 = user()
        self.assertTrue(user1.updateUser('xd', 'ehfah','ldowqeq', 'o123ifhweief@ef',1))
   
    def test_31_1updateUserFalse(self):
         user1 = user()
         self.assertFalse(user1.updateUser(None, 'ehfah', 'ldowqeq', 'oifhweiofw',  1))
   
    def test_32_2updateUserTrue(self):
         user1 = user()
         self.assertFalse(user1.updateUser('y', 'ehfah', None, 'oieeniofefw',  1))
       
    def test_33_3updateUserTrue(self):
        user1 = user()
        self.assertFalse(user1.updateUser('loq', 'ehfah', 'ldowqeq', '', 1))
                            
    def test_34_4updateUserTrue(self):
        user1 = user()
        self.assertTrue(user1.updateUser('loq', 'ehfah', '123167891012wd', 'fwfwfe', 1))
   
    def test_35_5updateUserTrue(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfefwfe', 4000))
   
    def test_35_6updateUserNoId(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwf@2efwfe', 1))
  
    def test_35_7updateUserNoRole(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfe!_fwfe',  4000)) 
    
    def test_35_8updateUserChar(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfe@fwfe',  'a'))    
    
    def test_35_9updateUserNoUser(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'lfoq', None, '1231612wd', 'fwf@@efwfe',  1))
    
    def test_36_1updateUserBlancs(self):
        user1 = user()
        self.assertFalse(user1.updateUser( '', '', '', '', None,  None))
    
    def test_36_2updateUserNoParam(self):
        user1 = user()
        self.assertFalse(user1.updateUser( None, None,  None, None, None,  None))
    
    def test_36_3updateUserNoChange(self):
        user1 = user()
        self.assertFalse(user1.updateUser( None, 'ehfah', None, None, None,  None))
    
    def test_36_4updateUsermaxchar(self):
        user1 = user()
        self.assertTrue(user1.updateUser( 'mas cincuenta caracteres en el nombre con espacios', 'ehfah', 'condieciseischar', 'cuenta30charpara@prueba.usb.ve',   1))

    def test_36_5updateUserFronteraExt(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'mas cincuenta caracteres en el nombre con espacios_', 'ehfah', 'condieci_seischar', 'cuenta30charpara@_prueba.usb.ve',   1))
    
    def test_36_6updateUserFronteraInt(self):
        user1 = user()
        self.assertTrue(user1.updateUser( 'mas cincuenta caracteres en el nombre con espacio', 'ehfah', 'condieciseischa', 'cuenta30charpar@prueba.usb.ve',   1))
    
    def test_36_7updateUserNotfound(self):
        user1 = user()
        self.assertFalse(user1.updateUser( 'mas cincuenta caracteres ', 'prueba_admin', 'condieciseischar', 'cuentanueva@prueba.usb.ve',   1))
    
    
    ################################################################################################
    #CASOS DE PRUEBA FUNCION DELETEUSER
        
    #Caso Frontera
    def test_40UserDeleteTrue(self):
        user1 = user()
        self.assertTrue(user1.deleteUser('wiekfprm'))
      
    #caso Frontera     
    def test_41UserDeleteFalse(self):
        user1 = user()
        self.assertFalse(user1.deleteUser('wiekfprm'))
      
    #caso malicia    
    def test_42UserDeleteNoUser(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(''))
      
    #caso frontera Interna 
    def test_43UserDelete1char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser('a'))
      
    #caso frontera     
    def test_44UserDelete16char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser('jksjdfdjvkjdfuhf'))
              
    #Caso frontera Externa        
    def test_45UserDelete17char(self):
        user1 = user()
        self.assertFalse(user1.deleteUser('jksjdfdj vkjdfuhf'))
              
    #caso frontera Interna 
    def test_46UserDelete15char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser('wjfr9olpsmfkreo')) 
      
    #caso Malicia
    def test_47UserDeleteNoParam(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(None))     
     
    #caso Malicia
    def test_48UserDeleteNoChar(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(''))
'''         