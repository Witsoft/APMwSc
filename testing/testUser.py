# -*- coding: utf-8 -*-. 

import unittest

from userDummy import *

class clsUserTester(unittest.TestCase):
    
    #CASOS DE PRUEBA FUNCION INSERTUSER

    #caso frontera
    def test1UserInsertTrue(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
     
    #caso frontera
    def test2UserInsertFalse(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = 'ehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
      
    #caso frontera externa
    def test3UserInsertNoUser(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = '',password = 'al', email = '@?lds', iddpt = 1, idrole = 1))
      
    #caso frontera interna 
    def test4UserInsert1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 1, idrole = 1))
          
    #caso frontera Externa 
    def test5UserInsert17char(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid', username = 'jksjdfdj vkjdfuhf',password = '12234', email = 'xxx@gmail.com', iddpt = 1, idrole = 1))
      
    #caso frontera Externa 
    def test6_0UserInsert16char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'jksjdfdjvkjdfuhf',password = '12234', email = 'yzyyxxx@gmail.com', iddpt = 1, idrole = 1))
      
    #caso frontera Externa 
    def test6_1UserInsert15char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'wjfr9olpsmfkreo',password = '12234', email = 'xfeexx@fgmail.com', iddpt = 1, idrole = 1)) 
          
    #caso frontera
    def test6_2UserInsert8char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'wiekfprm',password = '12234', email = 'yffe@ldv.gmail.com', iddpt = 1, idrole = 1))
          
    #caso frontera Externa 
    def test6UserInserFullnamet51char(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmkd', username = 'jksjdfdj vkjdfuhf',password = '12234', email = 'xxx@gmail.com', iddpt = 1, idrole = 1))
      
    #caso frontera
    def test7UserInserFullnamet50char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmk', username = 'jksjdfdj__',password = '12234', email = 'xx__x@gmail.com', iddpt = 1, idrole = 1))   
      
    #caso frontera Interna 
    def test8UserInserFullnamet49char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', username = 'jpvkjdfuhf',password = '12234', email = 'xyyy@gmail.com', iddpt = 1, idrole = 1))
      
    #caso frontera Externa 
    def test9UserInserFullnamet25char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'Patricia Reyes Valencia25', username = 'patkjdfuhf',password = '12234', email = 'patx@gmail.com', iddpt = 1, idrole = 1))
      
    #caso frontera Externa 
    def test9_0UserInserNoFullname(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = '', username = 'patkjdfuhf',password = '12234', email = 'patx@gmail.com', iddpt = 1, idrole = 1))
      
       #caso frontera Externa 
    def test9_1UserInserFullnamet1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'P', username = 'patkfhf_1',password = '12234', email = 'paddtx@gmail.com', iddpt = 1, idrole = 1))
      
    #caso frontera Externa
    def test_10UserInsertEmail31char(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd ',password = '12d234', email = '10-10603-10-10916ing@ldc.usb.ve', iddpt = 1, idrole = 1))
  
    #caso frontera Externa
    def test_11UserInsertNoEmail(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd ',password = '12d234', email = '', iddpt = 1, idrole = 1))
       
    #caso frontera Interna
    def test_12UserInsertEmail1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd_1 ',password = '12d234', email = '@', iddpt = 1, idrole = 1))
        
      #caso frontera Interna
    def test_13UserInsertEmail30char(self):
         user1 = user()
         self.assertTrue(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd_2',password = '12d234', email = '123167890patricia_v@gmail.com', iddpt = 1, idrole = 1))
        
      #caso frontera Interna
    def test_14UserInsertEmail29char(self):
         user1 = user()
         self.assertTrue(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd_3',password = '12d234', email = '123167890patriciav@gmail.com', iddpt = 1, idrole = 1))
       
     #caso frontera externa
    def test_15UserInsertPassword17(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = 'pat', username = 'ehfer_23',password = '12316789qwertyuai', email = '2@ls', iddpt = 1, idrole = 1))
       
    #caso frontera externa
    def test_16UserInsertNoPassword(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = 'ehfadh_2',password = '', email = '3@ls', iddpt = 1, idrole = 1))
       
    #caso frontera interna
    def test_17UserInsertPassword15(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ehf_1',password = 'eifko09olpedft5', email = 'po@rls', iddpt = 1, idrole = 1))
       
    #caso frontera interna
    def test_18UserInsertPassword1(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sr', username = 'er3r_1',password = '1', email = 'desm@ld.s', iddpt = 1, idrole = 1))
       
    #caso frontera
    def test_19UserInsertPasword16(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'frkfe_1',password = 'qiejdp0t4jmds21l', email = 'fefef_t@l.ss', iddpt = 1, idrole = 1))
       
    #caso frontera
    def test_20UserInsertPassword8(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'lowdn',password = 'kdiopw34', email = 'efmefm@l.c', iddpt = 1, idrole = 1))
       
    #Caso Malicia5
    def test_21UserInsertiddptChar(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 'a', idrole = 'b'))
                  
    #caso malicia
    def test_22UserInsertNochar(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = '', username = '',password = '', email = '', iddpt = None, idrole = None))
       
    #caso malicia   
    def test_22_1UserInsertNoParam(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = None, username = None,password = None, email = None, iddpt = None, idrole = None))
 
    #caso Frontera
    def test_22_2UserInsertNoDpt(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'srgfer', username = 'pw74b_r',password = 'efoewfwe1', email = 'tarea@hot.com', iddpt = 75, idrole = 1))

    #caso Frontera
    def test_22_3UserInsertNoRole(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'utdf R', username = 'olpo',password = 'efefefr3', email = 'nonemail@,mail.cpom', iddpt = 1, idrole = 80))
    
    #Caso esquina
    def test_22_4UserInsertNoForeign(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'fiee0 ee', username = 'q84-g0gs',password = 'wdwd94', email = 'ffjfor@w.pol', iddpt = 60, idrole = 60))

    ##################################################################################
       
    #CASOS DE PRUEBA SEARCHUSER
       
    #Caso Frontera
    def test_23searchUserTrue(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'ehfah'))
           
    #Caso Frontera 
    def test_24searchUser1Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'a'))
       
    #Caso Frontera
    def test_25searchUser16Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'jksjdfdjvkjdfuhf'))
       
    #Caso Frontera externa
    def test_26SearchUserNotChar(self): 
        user1 = user()
        self.assertEqual([],user1.searchUser(username = ''))
       
    #Caso Frontera externa
    def test_27searchUser17Char(self):
       user1 = user()
       self.assertEqual([],user1.searchUser(username = 'jksjdfdj vkjdfuhf'))
          
    #Caso Esquina
    def test_28searchUserNotInsert(self):
        user1 = user()
        self.assertEqual([],user1.searchUser(username = 'PatriciaValencia'))
           
    #Caso INtermedio
    def test_29searchUser8Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'wiekfprm'))
      
    #caso Malicia 
    def test_29_1searchUserNoChar(self):
        user1 = user()
        self.assertEqual([],user1.searchUser(username = ''))
          
    def test_29_2searchUserNoParam(self):
        user1 = user()
        self.assertEqual([],user1.searchUser(username = None))
     
    ###############################################################################################    
   
     #CASOS DE PRUEBA FUNCION UPDATEUSER
       
    def test_30updateUserTrue(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_fullname = 'xd', username = 'ehfah',new_password = 'ldowqeq', new_email = 'o123ifhweief@ef', new_iddpt = 1, new_idrole = 1))
   
    def test_31_1updateUserFalse(self):
         user1 = user()
         self.assertFalse(user1.updateUser(new_fullname = None, username = 'ehfah',new_password = 'ldowqeq', new_email = 'oifhweiofw', new_iddpt = 1, new_idrole = 1))
   
    def test_32_2updateUserTrue(self):
         user1 = user()
         self.assertFalse(user1.updateUser(new_fullname = 'y', username = 'ehfah',new_password = None, new_email = 'oieeniofefw', new_iddpt = 1, new_idrole = 1))
       
    def test_33_3updateUserTrue(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'loq', username = 'ehfah',new_password = 'ldowqeq', new_email = '', new_iddpt = 1, new_idrole = 1))
                            
    def test_34_4updateUserTrue(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_fullname = 'loq', username = 'ehfah',new_password = '123167891012wd', new_email = 'fwfwfe', new_iddpt = 1, new_idrole = 1))
   
    def test_35_5updateUserTrue(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'lfoq', username = 'ehfah',new_password = '1231612wd', new_email = 'fwfefwfe', new_iddpt =5000, new_idrole = 4000))
   
    def test_35_6updateUserNoId(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'lfoq', username = 'ehfah',new_password = '1231612wd', new_email = 'fwf@2efwfe', new_iddpt =5000, new_idrole = 1))
  
    def test_35_7updateUserNoRole(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'lfoq', username = 'ehfah',new_password = '1231612wd', new_email = 'fwfe!_fwfe', new_iddpt =1, new_idrole = 4000)) 
    
    def test_35_8updateUserChar(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'lfoq', username = 'ehfah',new_password = '1231612wd', new_email = 'fwfe@fwfe', new_iddpt =1, new_idrole = 'a'))    
    
    def test_35_9updateUserNoUser(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'lfoq', username = None,new_password = '1231612wd', new_email = 'fwf@@efwfe', new_iddpt =1, new_idrole = 1))
    
    def test_36_1updateUserBlancs(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = '', username = '',new_password = '', new_email = '', new_iddpt = None, new_idrole = None))
    
    def test_36_2updateUserNoParam(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = None, username = None, new_password = None, new_email = None, new_iddpt =None, new_idrole = None))
    
    def test_36_3updateUserNoChange(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = None, username = 'ehfah',new_password = None, new_email = None, new_iddpt = None, new_idrole = None))
    
    def test_36_4updateUsermaxchar(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_fullname = 'mas cincuenta caracteres en el nombre con espacios', username = 'ehfah',new_password = 'condieciseischar', new_email = 'cuenta30charpara@prueba.usb.ve', new_iddpt =1, new_idrole = 1))

    def test_36_5updateUserFronteraExt(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'mas cincuenta caracteres en el nombre con espacios_', username = 'ehfah',new_password = 'condieci_seischar', new_email = 'cuenta30charpara@_prueba.usb.ve', new_iddpt =1, new_idrole = 1))
    
    def test_36_6updateUserFronteraInt(self):
        user1 = user()
        self.assertTrue(user1.updateUser(new_fullname = 'mas cincuenta caracteres en el nombre con espacio', username = 'ehfah',new_password = 'condieciseischa', new_email = 'cuenta30charpar@prueba.usb.ve', new_iddpt =1, new_idrole = 1))
    
    def test_36_7updateUserNotfound(self):
        user1 = user()
        self.assertFalse(user1.updateUser(new_fullname = 'mas cincuenta caracteres ', username = 'prueba_admin',new_password = 'condieciseischar', new_email = 'cuentanueva@prueba.usb.ve', new_iddpt =1, new_idrole = 1))
    
    
    ################################################################################################
    #CASOS DE PRUEBA FUNCION DELETEUSER
        
    #Caso Frontera
    def test_40UserDeleteTrue(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'wiekfprm'))
      
    #caso Frontera     
    def test_41UserDeleteFalse(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = 'wiekfprm'))
      
    #caso malicia    
    def test_42UserDeleteNoUser(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = ''))
      
    #caso frontera Interna 
    def test_43UserDelete1char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'a'))
      
    #caso frontera     
    def test_44UserDelete16char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'jksjdfdjvkjdfuhf'))
              
    #Caso frontera Externa        
    def test_45UserDelete17char(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = 'jksjdfdj vkjdfuhf'))
              
    #caso frontera Interna 
    def test_46UserDelete15char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'wjfr9olpsmfkreo')) 
      
    #caso Malicia
    def test_47UserDeleteNoParam(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = None))     
     
    #caso Malicia
    def test_48UserDeleteNoChar(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = '')) 