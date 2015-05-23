# -*- coding: utf-8 -*-. 

import unittest

from userDummy import *

class clsUserTester(unittest.TestCase):
    
    # CASOS DE PRUEBA FUNCION INSERTUSER
    
    def testUserInsertExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        role1.insertRole('Product Owner','description',1)
        user1 = user()
        result = user1.insertUser('sah','ehfah','al', '@ls', 1)
        user1.deleteUser('ehfah')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')

    # Caso frontera
    def testUserInsertTrue(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
        role1 = role()
        role1.insertRole('Product Owner','description',1)
        user1 = user()
        result = user1.insertUser('sah','ehfahw','al', '@ls', 1)
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteRole('Product Owner')
        aBackLog.deleteProduct('Taxi seguro.')
        
'''     
    # Caso frontera
    def testUserInsertFalse(self):
        user1  = user()
        result = user1.insertUser('sah', 'ehfah','al', '@ls', 1)
        self.assertFalse(result)
        
    # Caso frontera externa
    def testUserInsertNoUser(self):
        user1  = user()
        result = user1.insertUser('sah', '','al', '@?lds', 1)
        self.assertFalse(result)
      
    # Caso frontera interna 
    def testUserInsert1char(self):
        user1  = user()
        result = user1.insertUser('sahid', 'a','12234', 'xxx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('a')
          
    # Caso frontera Externa 
    def testUserInsert17char(self):
        user1  = user()
        result = user1.insertUser('sahid', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
        self.assertFalse(result)
        
    # Caso frontera Externa 
    def testUserInsert16char(self):
        user1  = user()
        result = user1.insertUser('sahid', 'jksjdfdjvkjdfuhf','12234', 'yzyyxxx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jksjdfdjvkjdfuhf')
      
    # Caso frontera Externa 
    def testUserInsert15char(self):
        user1  = user()
        result = user1.insertUser('sahid', 'wjfr9olpsmfkreo','12234', 'xfeexx@fgmail.com', 1)
        self.assertTrue(result) 
        user1.deleteUser('wjfr9olpsmfkreo')
        
    # Caso frontera
    def testUserInsert8char(self):
        user1  = user()
        result = user1.insertUser('sahid', 'wiekfprm','12234', 'yffe@ldv.gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('wiekfprm')
          
    # Caso frontera Externa 
    def testUserInserFullnamet51char(self):
        user1  = user()
        result = user1.insertUser('sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmkd', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
        self.assertFalse(result)

      
    #caso frontera
    def test7UserInserFullnamet50char(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmk', 'jksjdfdj__','12234', 'xx__x@gmail.com', 1))   
      
    #caso frontera Interna 
    def test8UserInserFullnamet49char(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', 'jpvkjdfuhf','12234', 'xyyy@gmail.com', 1))
      
    #caso frontera Externa 
    def test9UserInserFullnamet25char(self):
        user1 = user()
        self.assertTrue(user1.insertUser('Patricia Reyes Valencia25', 'patkjdfuhf','12234', 'patx@gmail.com', 1))
      
    #caso frontera Externa 
    def test9_0UserInserNoFullname(self):
        user1 = user()
        self.assertFalse(user1.insertUser('', 'patkjdfuhf','12234', 'patx@gmail.com', 1))
      
       #caso frontera Externa 
    def test9_1UserInserFullnamet1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser('P', 'patkfhf_1','12234', 'paddtx@gmail.com', 1))
      
    #caso frontera Externa
    def test_10UserInsertEmail31char(self):
        user1 = user()
        self.assertFalse(user1.insertUser('sahid Patricia', 'tdd ','12d234', '10-10603-10-10916ing@ldc.usb.ve', 1))
  
    #caso frontera Externa
    def test_11UserInsertNoEmail(self):
        user1 = user()
        self.assertFalse(user1.insertUser('sahid Patricia', 'tdd ','12d234', '', 1))
       
    #caso frontera Interna
    def test_12UserInsertEmail1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sahid Patricia', 'tdd_1 ','12d234', '@', 1))
        
      #caso frontera Interna
    def test_13UserInsertEmail30char(self):
         user1 = user()
         self.assertTrue(user1.insertUser('sahid Patricia', 'tdd_2','12d234', '123167890patricia_v@gmail.com', 1))
        
      #caso frontera Interna
    def test_14UserInsertEmail29char(self):
         user1 = user()
         self.assertTrue(user1.insertUser('sahid Patricia', 'tdd_3','12d234', '123167890patriciav@gmail.com', 1))
       
     #caso frontera externa
    def test_15UserInsertPassword17(self):
         user1 = user()
         self.assertFalse(user1.insertUser('pat', 'ehfer_23','12316789qwertyuai', '2@ls', 1))
       
    #caso frontera externa
    def test_16UserInsertNoPassword(self):
        user1 = user()
        self.assertFalse(user1.insertUser('sah', 'ehfadh_2','', '3@ls', 1))
       
    #caso frontera interna
    def test_17UserInsertPassword15(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sah', 'ehf_1','eifko09olpedft5', 'po@rls', 1))
       
    #caso frontera interna
    def test_18UserInsertPassword1(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sr', 'er3r_1','1', 'desm@ld.s', 1))
       
    #caso frontera
    def test_19UserInsertPasword16(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sah', 'frkfe_1','qiejdp0t4jmds21l', 'fefef_t@l.ss', 1))
       
    #caso frontera
    def test_20UserInsertPassword8(self):
        user1 = user()
        self.assertTrue(user1.insertUser('sah', 'lowdn','kdiopw34', 'efmefm@l.c', 1))
       
    #Caso Malicia5
    def test_21UserInsertiddptChar(self):
        user1 = user()
        self.assertFalse(user1.insertUser('sahid', 'a','12234', 'xxx@gmail.com', , 'b'))
                  
    #caso malicia
    def test_22UserInsertNochar(self):
        user1 = user()
        self.assertFalse(user1.insertUser('', '','', '', e, None))
       
    #caso malicia   
    def test_22_1UserInsertNoParam(self):
        user1 = user()
        self.assertFalse(user1.insertUser(None, None,None, None, e, None))
 
    #caso Frontera
    def test_22_2UserInsertNoDpt(self):
        user1 = user()
        self.assertFalse(user1.insertUser('srgfer', 'pw74b_r','efoewfwe1', 'tarea@hot.com',  1))

    #caso Frontera
    def test_22_3UserInsertNoRole(self):
        user1 = user()
        self.assertFalse(user1.insertUser('utdf R', 'olpo','efefefr3', 'nonemail@,mail.cpom', 80))
    
    #Caso esquina
    def test_22_4UserInsertNoForeign(self):
        user1 = user()
        self.assertFalse(user1.insertUser('fiee0 ee', 'q84-g0gs','wdwd94', 'ffjfor@w.pol',  60))

    ##################################################################################
       
    #CASOS DE PRUEBA SEARCHUSER
       
    #Caso Frontera
    def test_23searchUserTrue(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser('ehfah'))
           
    #Caso Frontera 
    def test_24searchUser1Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser('a'))
       
    #Caso Frontera
    def test_25searchUser16Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser('jksjdfdjvkjdfuhf'))
       
    #Caso Frontera externa
    def test_26SearchUserNotChar(self): 
        user1 = user()
        self.assertEqual([],user1.searchUser(''))
       
    #Caso Frontera externa
    def test_27searchUser17Char(self):
       user1 = user()
       self.assertEqual([],user1.searchUser('jksjdfdj vkjdfuhf'))
          
    #Caso Esquina
    def test_28searchUserNotInsert(self):
        user1 = user()
        self.assertEqual([],user1.searchUser('PatriciaValencia'))
           
    #Caso INtermedio
    def test_29searchUser8Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser('wiekfprm'))
      
    #caso Malicia 
    def test_29_1searchUserNoChar(self):
        user1 = user()
        self.assertEqual([],user1.searchUser(''))
          
    def test_29_2searchUserNoParam(self):
        user1 = user()
        self.assertEqual([],user1.searchUser(None))
     
    ###############################################################################################    
   
     #CASOS DE PRUEBA FUNCION UPDATEUSER
       
    def test_30updateUserTrue(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_'xd', 'ehfah',new_'ldowqeq', 'o123ifhweief@ef', new_1))
   
    def test_31_1updateUserFalse(self):
         user1 = user()
         self.assertFalse(user1.updateUser(new_None, 'ehfah',new_'ldowqeq', 'oifhweiofw', new_1))
   
    def test_32_2updateUserTrue(self):
         user1 = user()
         self.assertFalse(user1.updateUser(new_'y', 'ehfah',new_None, 'oieeniofefw', new_1))
       
    def test_33_3updateUserTrue(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'loq', 'ehfah',new_'ldowqeq', '',new_1))
                            
    def test_34_4updateUserTrue(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_'loq', 'ehfah',new_'123167891012wd', 'fwfwfe', , new_1))
   
    def test_35_5updateUserTrue(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'lfoq', 'ehfah',new_'1231612wd', 'fwfefwfe', new_4000))
   
    def test_35_6updateUserNoId(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'lfoq', 'ehfah',new_'1231612wd', 'fwf@2efwfe', new_1))
  
    def test_35_7updateUserNoRole(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'lfoq', 'ehfah',new_'1231612wd', 'fwfe!_fwfe', new_4000)) 
    
    def test_35_8updateUserChar(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'lfoq', 'ehfah',new_'1231612wd', 'fwfe@fwfe', new_'a'))    
    
    def test_35_9updateUserNoUser(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'lfoq', None,new_'1231612wd', 'fwf@@efwfe', new_1))
    
    def test_36_1updateUserBlancs(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'', '',new_'', '', one, new_None))
    
    def test_36_2updateUserNoParam(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_None, None, new_None, None, ne, new_None))
    
    def test_36_3updateUserNoChange(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_None, 'ehfah',new_None, None, one, new_None))
    
    def test_36_4updateUsermaxchar(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_'mas cincuenta caracteres en el nombre con espacios', 'ehfah',new_'condieciseischar', 'cuenta30charpara@prueba.usb.ve',  new_1))

    def test_36_5updateUserFronteraExt(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'mas cincuenta caracteres en el nombre con espacios_', 'ehfah',new_'condieci_seischar', 'cuenta30charpara@_prueba.usb.ve',  new_1))
    
    def test_36_6updateUserFronteraInt(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_'mas cincuenta caracteres en el nombre con espacio', 'ehfah',new_'condieciseischa', 'cuenta30charpar@prueba.usb.ve',  new_1))
    
    def test_36_7updateUserNotfound(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_'mas cincuenta caracteres ', 'prueba_admin',new_'condieciseischar', 'cuentanueva@prueba.usb.ve',  new_1))
    
    
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