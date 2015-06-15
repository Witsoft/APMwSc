# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from user import *
from role import *

class TestUsers(unittest.TestCase):

    ##########################################      
    #   Suite de Pruebas para InsertUser     #
    ##########################################
    
    # Caso Inicial
 
    # Prueba 1
      
    def testUserInsertExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah','ehfah','al', '@ls', 1)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso frontera

    # Prueba 2   
    def testUserInsertTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah','ehfahw','alir893b1','@ls',1)
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
                   
    # Prueba 3
    def testUserInsertFalse(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah','ehfah','al', '@ls',6)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 4
    def testUserInsertNoUser(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah','','al','@?lds',1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 5
    def testUserInsert1char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid', 'a','1223478364', 'xxx@gmail.com',1)
        self.assertTrue(result)
        user1.deleteUser('a')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')  
   
    # Prueba 6
    def testUserInsert17char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 7
    def testUserInsert16char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid', 'jksjdfdjvkjdfuhf','122346768', 'yzyyxxx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jksjdfdjvkjdfuhf')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 8
    def testUserInsert15char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid', 'wjfr9olpsmfkreo','1225676834', 'xfeexx@fgmail.com', 1)
        self.assertTrue(result) 
        user1.deleteUser('wjfr9olpsmfkreo')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 9
    def testUserInsert8char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid', 'wiekfprm','1223463637', 'yffe@ldv.gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('wiekfprm')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
             
    # Prueba 10
    def testUserInserFullnamet51char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sxhyd Pxtrycyx Rryfs Vrlrncyu kjhdj kjhvjfdbhjdcmkd', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com', 1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 11
    def testUserInserFullnamet50char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result =  user1.insertUser('sdhtd Pdtrycrt Rtyys Vslcncta kjhdj kjhvjfdbhjdcmk', 'jksjdfdj__','1223485953', 'xx__x@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jksjdfdj__') 
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')      
                  
    # Prueba 12
    def testUserInserFullnamet49char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', 'jpvkjdfuhf','8475312234', 'xyyy@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('jpvkjdfuhf') 
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
         
    # Prueba 13
    def testUserInserFullnamet25char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('Pxtrscre Rtyts Vqlfncfa25', 'patkjdfuhf','1223467843', 'patx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('patkjdfuhf')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 14
    def testUserInserNoFullname(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('', 'patkjdfuhf','12234', 'patx@gmail.com', 1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 15
    def testUserInserFullnamet1char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('P', 'patkfhf_1','122374834', 'paddtx@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('patkfhf_1')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 16
    def testUserInsertEmail31char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sxhyd Pxtrycyx', 'tdd ','12d234', '10-10603-10-10916ing@ldc.usb.ve', 1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 17
    def testUserInsertNoEmail(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sxhyd Pxtrycyx', 'tdd ','12d234', '', 1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 18
    def testUserInsertEmail1char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sxhyd Pxtrycyx', 'tdd_1','12d2345678','@', 1)
        self.assertTrue(result)
        user1.deleteUser('tdd_1')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')        
         
    # Prueba 19
    def testUserInsertEmail30char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sxhyd Pxtrycyx', 'tdd_2','12d2356784', '123167890patricia_v@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('tdd_2')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 20
    def testUserInsertEmail29char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sxhyd Pxtrycyx', 'tdd_3','12d2343434', '123167890patriciav@gmail.com', 1)
        self.assertTrue(result)
        user1.deleteUser('tdd_3')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 21
    def testUserInsertPassword201(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('pat', 'ehfer_23',100*'12' + 'e', '2@ls',1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 22
    def testUserInsertNoPassword(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah', 'ehfadh_2','', '3@ls', 1)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 23
    def testUserInsertPassword199(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah', 'ehf_1',199*'e', 'po@rls', 1)
        self.assertTrue(result)
        user1.deleteUser('ehf_1')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 24
    def testUserInsertPassword1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sr', 'er3r_1','1', 'desm@ld.s', 1)
        self.assertTrue(result)
        user1.deleteUser('er3r_1')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 25
    def testUserInsertPassword2(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sah', 'frkfe_1','qi', 'fefef_t@l.ss', 1)
        self.assertTrue(result)
        user1.deleteUser('frkfe_1')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 26
    def testUserInsertNoRole(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('srgfer', 'pw74b_r','efoewfwe1', 'tarea@hot.com', None)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 27
    def testUserInsertnNoRoleString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('utdf R', 'olpo','efefefr3', 'nonemail@,mail.cpom', 80)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Caso Malicia

    # Prueba 28
    def testUserInsertidroleChar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('sahid', 'a','12234', 'xxx@gmail.com','b')
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 29
    def testUserInsertNochar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('', '','', '', None)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
       
    # Prueba 30
    def testUserInsertNoParam(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser(None, None,None, None,None)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
                      
    # Caso esquina

    # Prueba 31
    def testUserInsertNoForeign(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.insertUser('fiee0 ee', 'q84-g0gs','wdwd94', 'ffjfor@w.pol',  60)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
  
     ##########################################      
     #   Suite de Pruebas para searchUser     #
     ##########################################
      
    # Caso Inicial

    # Prueba 32
    def testsearchUserExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        user1 = user()
        result = user1.searchUser('ehfah')
  
    #Caso Frontera
    
    # Prueba 33
    def testsearchUserTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('nombre','ehfah','12345678','ef@fg.com',1)
        result = user1.searchUser('ehfah')
        self.assertNotEqual([],result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
             
    # Prueba 34
    def testsearchUser1Char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('nombreA','a','12345678','a@g.com',1)
        result = user1.searchUser('a')
        self.assertNotEqual([],result)
        user1.deleteUser('a')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
     
    # Prueba 35
    def testsearchUser16Char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('new uswer','jksjdfdjvkjdfuhf','12345678','nuevo@.com',1)
        result = user1.searchUser('jksjdfdjvkjdfuhf')
        self.assertNotEqual([],result)
        user1.deleteUser('new uswer')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
  
    # Prueba 36
    def testSearchUserNotChar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.searchUser('') 
        self.assertEqual([],result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
      
    # Prueba 37
    def testsearchUser17Char(self):  
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('fullname','jksjdfdj vkjdfuhf','12345678','email@',1)
        result = user1.searchUser('jksjdfdj vkjdfuhf')
        self.assertEqual([],result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
  
    # Caso Esquina

    # Prueba 38
    def testsearchUserNotInsert(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.searchUser('PatriciaValencia')
        self.assertEqual([],result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
  
    # Prueba 39
    def testsearchUser8Char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('fullname','wiekfprm','123456784','eail@nuevo',1)
        result = user1.searchUser('wiekfprm')
        self.assertNotEqual([],result)
        user1.deleteUser('wiekfprm')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
  
    # Caso Malicia 

    # Prueba 40
    def testsearchUserNoChar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.searchUser('')
        self.assertEqual([],result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 41            
    def testsearchUserNoParam(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.searchUser(None)
        self.assertEqual([],result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
  
    ##########################################      
    #   Suite de Pruebas para UpdateUser     #
    ##########################################

    # Caso Inicial

    # Prueba 42        
    def testupdateUserTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('loquesea','ehfah','12345678','cosa',1)
        result = user1.updateUser('xd','ehfah','ldow1qeqt', 'o123ifhweief@ef',1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Frontera

    # Prueba 43 
    def testupdateUserFalse(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('valido', 'ehfah', 'ldowf4r42q', 'oifhwe@fw', 1)
        result = user1.updateUser(None, 'ehfah', 'ldowqeq', 'oifhweiofw',  1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 44    
    def testupdateUserNonepass(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('yloqdd', 'ehfah', '123456789', 'oieeniofefw',  1)
        result = user1.updateUser('y', 'ehfah', None, 'oieeniofefw',  1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 45        
    def testupdateUserNonedescription(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('loqwew', 'ehfah', 'ldoee22wqeq', 'nuevoemaild', 1)
        result = user1.updateUser('loq', 'ehfah', 'ldowqeq', '', 1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 46           
    def testupdateUserIntermedio(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('loer3q', 'ehfah', '123163r378012wd', 'frrwfwfe', 1)
        result = user1.updateUser('loq', 'ehfah','123167891012wd', 'fwfwfe', 1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 47    
    def testupdateUserNorole(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.updateUser( 'lfoqefe', 'ehfah', '12312331wd', 'fw3rfe', 1)
        result = user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfefwfe', 4000)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 48
    def testupdateUserChar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        self.assertFalse(user1.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfe@fwfe',  'a'))
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')    

    # Prueba 49     
    def testupdateUserNoUser(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.updateUser( 'lfoqeffe', 'ehfah', '123161efef2wd', 'fwf@@efeffwfe', 1)
        result = user1.updateUser( 'lfoq', None, '1231612wd', 'fwf@@efwfe',  1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 50     
    def testupdateUserBlancs(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( '', '', '', '', None)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 51     
    def testupdateUserNoParam(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( None, None,  None, None, None)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 52     
    def testupdateUserNoChange(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( None, 'ehfah', None, None, None)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 53     
    def testupdateUsermaxchar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser(50*'a','ehfah','condieciseischar','cuenta30a@prueba.usb.ve', 1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 54 
    def testupdateUserFronteraExt(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser('mas cincuenta caracteres en el nombre con espacios_','ehfah','condieci_seischar','cuenta30charpara@_prueba.usb.ve',1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 55     
    def testupdateUserFronteraInt(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser('mas cincuenta caracteres en el nombre con espacio','ehfah','condieciseischa','cuenta30charpar@prueba.usb.ve',1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 56     
    def testupdateUserNotfound(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@', 1)
        result = user1.updateUser( 'mas cincuenta caracteres ', 'prueba_admin', 'condieciseischar', 'cuentanueva@prueba.usb.ve', 1)
        self.assertFalse(result)
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
     
    ##########################################      
    #   Suite de Pruebas para DeleteUser     #
    ##########################################
     
    # Caso Inicial

    # Prueba 57     
    def testUserDeleteExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        user1 = user()
        user1.deleteUser('ehfah')

    #vCaso Frontera

    # Prueba 58     
    def testUserDeleteTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('urown','wiekfprm','1234322249','email@nee',1)
        result = user1.deleteUser('wiekfprm')
        self.assertTrue(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
      
    # Prueba 59     
    def testUserDeleteFalse(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.deleteUser('wiekfprm')
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 60         
    def testUserDelete1char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('nombrea','a','passworda12','emaila',1)
        result = user1.deleteUser('a')
        self.assertTrue(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 61       
    def testUserDelete16char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('nombre','jksjdfdjvkjdfuhf','1234567890','emaildwd@',1)
        result = user1.deleteUser('jksjdfdjvkjdfuhf')
        self.assertTrue(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 62       
    def testUserDelete17char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.deleteUser('jksjdfdj vkjdfuhf')
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 63
    def testUserDelete15char(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('nombre','wjfr9olpsmfkreo','1234567890','emailen',1)
        result = user1.deleteUser('wjfr9olpsmfkreo')
        self.assertTrue(result) 
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Malicia

    # Prueba 64     
    def testUserDeleteNoUser(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.deleteUser('')
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 65         
    def testUserDeleteNoParam(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.deleteUser(None)
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')     
     
    # Prueba 66     
    def testUserDeleteNoChar(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result = user1.deleteUser('')
        self.assertFalse(result)
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs') 

    ##########################################      
    #   Suite de Pruebas para findEmail      #
    ##########################################
    
    # Caso Inicial
 
    # Prueba 67      
    def testUserFindEmailExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfah','al', '@ls', 1)
        result = user1.findEmail('@ls')
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso normal

    # Prueba 68   
    def testUserFindEmailTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','@ls',1)
        result = user1.findEmail('@ls')
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso frontera
                   
    # Prueba 69
    def testUserFindEmailString1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','l',1)
        result = user1.findEmail('l')
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 70
    def testUserFindEmailString2(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','ls',1)
        result = user1.findEmail('ls')
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 71
    def testUserFindEmailString30(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1',10*'@ls',1)
        result = user1.findEmail(10*'@ls')
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 72
    def testUserFindEmailString29(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1',7*'@las'+ 's',1)
        result = user1.findEmail(7*'@las'+ 's')
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Malicia
    
    # Prueba 73
    def testUserFindEmailString0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1',7*'@las'+ 's',1)
        result = user1.findEmail('')
        self.assertFalse(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 74
    def testUserFindEmailNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','alas',1)
        result = user1.findEmail(None)
        self.assertFalse(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 75
    def testUserFindEmailInteger(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','alas',1)
        result = user1.findEmail(1)
        self.assertFalse(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    ##########################################      
    #   Suite de Pruebas para isFound        #
    ##########################################
    
    # Caso Inicial
 
    # Prueba 76
    def testUserIsFoundExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfah','al', '@ls', 1)
        result = user1.isFound('ehfah')
        user1.deleteUser('ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso normal

    # Prueba 77   
    def testUserIsFoundTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','@ls',1)
        result = user1.isFound('ehfahw')
        self.assertTrue(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso frontera
                   
    # Prueba 78
    def testUserIsFoundString1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','e','alir893b1','ldddf',1)
        result = user1.isFound('e')
        self.assertTrue(result)
        user1.deleteUser('e')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 79
    def testUserIsFoundString2(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','eh','alir893b1','lfdfs',1)
        result = user1.isFound('eh')
        self.assertTrue(result)
        user1.deleteUser('eh')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 80
    def testUserFindEmailString16(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah',4*'ehfa','alir893b1','@ls',1)
        result = user1.isFound(4*'ehfa')
        self.assertTrue(result)
        user1.deleteUser(4*'ehfa')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 81
    def testUserIsFoundString15(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah',3*'ehfah','alir893b1','@las',1)
        result = user1.isFound(3*'ehfah')
        self.assertTrue(result)
        user1.deleteUser(3*'ehfah')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Malicia
    
    # Prueba 82
    def testUserIsFoundString0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1',7*'@las'+ 's',1)
        result = user1.isFound('')
        self.assertFalse(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 83
    def testUserIsFoundNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','alas',1)
        result = user1.isFound(None)
        self.assertFalse(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 84
    def testUserIsFoundInteger(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = aBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba. 
        role1 = role()
        user1 = user()
        role1.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        user1.insertUser('sah','ehfahw','alir893b1','alas',1)
        result = user1.isFound(1)
        self.assertFalse(result)
        user1.deleteUser('ehfahw')
        role1.deleteActor('Xsxyrvz',idBacklog)
        aBacklog.deleteProduct('Pxrsynzjxs')