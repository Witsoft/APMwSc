# -*- coding: utf-8 -*-. 

import unittest

from userDummy import *

class clsUserTester(unittest.TestCase):

     ##########################################      
     #   Suite de Pruebas para InsertUser     #
     ##########################################
      
    def testUserInsertExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah','ehfah','al', '@ls', 1)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
    # Caso frontera
    def testUserInsertTrue(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah','ehfahw','alir893b1', '@ls', 1)
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
        
    # Caso frontera
    def testUserInsertFalse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah', 'ehfah','al', '@ls', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Caso frontera externa
    def testUserInsertNoUser(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah', '','al', '@?lds', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
         
    # Caso frontera interna 
    def testUserInsert1char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid', 'a','1223478364', 'xxx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('a')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')  
   
    # Caso frontera Externa 
    def testUserInsert17char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
           
    # Caso frontera Externa 
    def testUserInsert16char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid', 'jksjdfdjvkjdfuhf','122346768', 'yzyyxxx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jksjdfdjvkjdfuhf')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Caso frontera Externa 
    def testUserInsert15char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid', 'wjfr9olpsmfkreo','1225676834', 'xfeexx@fgmail.com', 1)
        self.assertTrue(result) 
        user1.deleteUser('wjfr9olpsmfkreo')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    # Caso frontera
    def testUserInsert8char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid', 'wiekfprm','1223463637', 'yffe@ldv.gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('wiekfprm')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
             
    # Caso frontera Externa 
    def testUserInserFullnamet51char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmkd', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
         
    #caso frontera
    def testUserInserFullnamet50char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result =  user1.insertUser('sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmk', 'jksjdfdj__','1223485953', 'xx__x@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jksjdfdj__') 
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')      
         
         
    #caso frontera Interna 
    def testUserInserFullnamet49char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', 'jpvkjdfuhf','8475312234', 'xyyy@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jpvkjdfuhf') 
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
         
    #caso frontera Externa 
    def testUserInserFullnamet25char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('Patricia Reyes Valencia25', 'patkjdfuhf','1223467843', 'patx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('patkjdfuhf')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso frontera Externa 
    def test9_0UserInserNoFullname(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('', 'patkjdfuhf','12234', 'patx@gmail.com', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
    #caso frontera Externa 
    def testUserInserFullnamet1char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('P', 'patkfhf_1','122374834', 'paddtx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('patkfhf_1')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso frontera Externa
    def testUserInsertEmail31char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia', 'tdd ','12d234', '10-10603-10-10916ing@ldc.usb.ve', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso frontera Externa
    def testUserInsertNoEmail(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia', 'tdd ','12d234', '', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso frontera Interna
    def testUserInsertEmail1char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia', 'tdd_1 ','12d2345678', '@', 1)
        self.assertTrue(result)
        user1.deleteUser('tdd_1')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')        
         
    #caso frontera Interna
    def testUserInsertEmail30char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia', 'tdd_2','12d2356784', '123167890patricia_v@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('tdd_2')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso frontera Interna
    def testUserInsertEmail29char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid Patricia', 'tdd_3','12d2343434', '123167890patriciav@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('tdd_3')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
     #caso frontera externa
    def testUserInsertPassword17(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('pat', 'ehfer_23','12316789qwertyuai', '2@ls', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
    #caso frontera externa
    def testUserInsertNoPassword(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah', 'ehfadh_2','', '3@ls', 1)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
          
    #caso frontera interna
    def testUserInsertPassword15(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah', 'ehf_1','eifko09olpedft5', 'po@rls', 1)
        self.assertTrue(result)
        user1.deleteUser('ehf_1')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
          
    #caso frontera interna
    def testUserInsertPassword8(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sr', 'er3r_1','12345678', 'desm@ld.s', 1)
        self.assertTrue(result)
        user1.deleteUser('er3r_1')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
          
    #caso frontera
    def testUserInsertPasword16(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah', 'frkfe_1','qiejdp0t4jmds21l', 'fefef_t@l.ss', 1)
        self.assertTrue(result)
        user1.deleteUser('frkfe_1')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso frontera
    def testUserInsertPassword8(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sah', 'lowdn','kdiopw34', 'efmefm@l.c', 1)
        self.assertTrue(result)
        user1.deleteUser('lowdn')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #Caso Malicia
    def testUserInsertidroleChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('sahid', 'a','12234', 'xxx@gmail.com','b')
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso malicia
    def testUserInsertNochar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('', '','', '', None)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
       
    #caso malicia   
    def testUserInsertNoParam(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser(None, None,None, None,None)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #caso Frontera
    def testUserInsertNoRole(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('srgfer', 'pw74b_r','efoewfwe1', 'tarea@hot.com', None)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
   
    #caso Frontera
    def testUserInsertNoRole(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('utdf R', 'olpo','efefefr3', 'nonemail@,mail.cpom', 80)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
           
    #Caso esquina
    def testUserInsertNoForeign(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.insertUser('fiee0 ee', 'q84-g0gs','wdwd94', 'ffjfor@w.pol',  60)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
  
  
     ##########################################      
     #   Suite de Pruebas para searchUser     #
     ##########################################
      
    #Caso Frontera
    def testsearchUserExist(self):
        user1 = user()
        result = user1.searchUser('ehfah')
  
    #Caso Frontera
    def testsearchUserTrue(self):
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
    def testsearchUser1Char(self):
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
     
    #Caso Frontera
    def testsearchUser16Char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('new uswer','jksjdfdjvkjdfuhf','12345678','nuevo@.com',1)
        result = user1.searchUser('jksjdfdjvkjdfuhf')
        self.assertNotEqual([],result)
        user1.deleteUser('new uswer')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
  
    #Caso Frontera externa
    def testSearchUserNotChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.searchUser('') 
        self.assertEqual([],result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
      
    #Caso Frontera externa
    def testsearchUser17Char(self):
  
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('fullname','jksjdfdj vkjdfuhf','12345678','email@',1)
        result = user1.searchUser('jksjdfdj vkjdfuhf')
        self.assertEqual([],result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
  
    #Caso Esquina
    def testsearchUserNotInsert(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.searchUser('PatriciaValencia')
        self.assertEqual([],result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
  
    #Caso Intermedio
    def testsearchUser8Char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('fullname','wiekfprm','123456784','eail@nuevo',1)
        result = user1.searchUser('wiekfprm')
        self.assertNotEqual([],result)
        user1.deleteUser('wiekfprm')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
  
    #caso Malicia 
    def testsearchUserNoChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.searchUser('')
        self.assertEqual([],result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
            
    def testsearchUserNoParam(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.searchUser(None)
        self.assertEqual([],result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
  
      
 
 
     ##########################################      
     #   Suite de Pruebas para UpdateUser     #
     ##########################################
 
        
    def testupdateUserTrue(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         user1 = user()
         role1.insertRole('Product Owner','description',1)
         user1.insertUser('loquesea','ehfah','12345678','cosa',1)
         result = user1.updateUser('xd', 'ehfah','ldowqeq', 'o123ifhweief@ef',1)
         self.assertTrue(result)
         user1.deleteUser('ehfah')
         role1.deleteRole('Product Owner')
         aBackLog.deleteProduct('Taxi seguro.')
 
    def testupdateUserFalse(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         user1 = user()
         role1.insertRole('Product Owner','description',1)
         user1.insertUser('valido', 'ehfah', 'ldowf4r42q', 'oifhwe@fw', 1)
         result = user1.updateUser(None, 'ehfah', 'ldowqeq', 'oifhweiofw',  1)
         self.assertFalse(result)
         user1.deleteUser('ehfah')
         role1.deleteRole('Product Owner')
         aBackLog.deleteProduct('Taxi seguro.')
    
    def testupdateUserNonepass(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         user1 = user()
         role1.insertRole('Product Owner','description',1)
         user1.insertUser('yloqdd', 'ehfah', '123456789', 'oieeniofefw',  1)
         result = user1.updateUser('y', 'ehfah', None, 'oieeniofefw',  1)
         self.assertFalse(result)
         user1.deleteUser('ehfah')
         role1.deleteRole('Product Owner')
         aBackLog.deleteProduct('Taxi seguro.')
        
    def testupdateUserNonedescription(self):
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         role1 = role()
         user1 = user()
         role1.insertRole('Product Owner','description',1)
         user1.insertUser('loqwew', 'ehfah', 'ldoee22wqeq', 'nuevoemaild', 1)
         result = user1.updateUser('loq', 'ehfah', 'ldowqeq', '', 1)
         self.assertFalse(result)
         user1.deleteUser('ehfah')
         role1.deleteRole('Product Owner')
         aBackLog.deleteProduct('Taxi seguro.')
                             
    def testupdateUserIntermedio(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('loer3q', 'ehfah', '123163r378012wd', 'frrwfwfe', 1)
        result = user1.updateUser('loq', 'ehfah', '123167891012wd', 'fwfwfe', 1)
        self.assertTrue(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
    
    def testupdateUserNorole(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.updateUser( 'lfoqefe', 'ehfah', '12312331wd', 'fw3rfe', 1)
        result = user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfefwfe', 4000)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
 
    def testupdateUserChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        self.assertFalse(user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfe@fwfe',  'a'))
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')    
     
    def testupdateUserNoUser(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.updateUser( 'lfoqeffe', 'ehfah', '123161efef2wd', 'fwf@@efeffwfe', 1)
        result = user1.updateUser( 'lfoq', None, '1231612wd', 'fwf@@efwfe',  1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    def testupdateUserBlancs(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( '', '', '', '', None)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    def testupdateUserNoParam(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( None, None,  None, None, None)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    def testupdateUserNoChange(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( None, 'ehfah', None, None, None)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    def testupdateUsermaxchar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser('mas cincuenta caracteres en el nombre con espacios','ehfah','condieciseischar','cuenta30charpara@prueba.usb.ve', 1)
        self.assertTrue(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
 
    def testupdateUserFronteraExt(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser('mas cincuenta caracteres en el nombre con espacios_','ehfah','condieci_seischar','cuenta30charpara@_prueba.usb.ve',1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    def testupdateUserFronteraInt(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser('mas cincuenta caracteres en el nombre con espacio','ehfah','condieciseischa','cuenta30charpar@prueba.usb.ve',1)
        self.assertTrue(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    def testupdateUserNotfound(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( 'mas cincuenta caracteres ', 'prueba_admin', 'condieciseischar', 'cuentanueva@prueba.usb.ve', 1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
     
    
     ##########################################      
     #   Suite de Pruebas para DeleteUser     #
     ##########################################
     
    #Caso Frontera
    def testUserDeleteExist(self):
        user1 = user()
        user1.deleteUser('ehfah')

    #Caso Frontera
    def testUserDeleteTrue(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('urown','wiekfprm','1234322249','email@nee',1)
        result = user1.deleteUser('wiekfprm')
        self.assertTrue(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
      
    #caso Frontera     
    def testUserDeleteFalse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.deleteUser('wiekfprm')
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
      
    #caso malicia    
    def testUserDeleteNoUser(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.deleteUser('')
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
      
    #caso frontera Interna 
    def testUserDelete1char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('nombrea','a','passworda12','emaila',1)
        result = user1.deleteUser('a')
        self.assertTrue(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
      
    #caso frontera     
    def testUserDelete16char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('nombre','jksjdfdjvkjdfuhf','1234567890','emaildwd@',1)
        result = user1.deleteUser('jksjdfdjvkjdfuhf')
        self.assertTrue(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
              
    #Caso frontera Externa        
    def testUserDelete17char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.deleteUser('jksjdfdj vkjdfuhf')
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
              
    #caso frontera Interna 
    def testUserDelete15char(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        user1.insertUser('nombre','wjfr9olpsmfkreo','1234567890','emailen',1)
        result = user1.deleteUser('wjfr9olpsmfkreo')
        self.assertTrue(result) 
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
      
    #caso Malicia
    def testUserDeleteNoParam(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.deleteUser(None)
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')     
     
    #caso Malicia
    def testUserDeleteNoChar(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        user1 = user()
        role1.insertRole('Product Owner','description',1)
        result = user1.deleteUser('')
        self.assertFalse(result)
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')  