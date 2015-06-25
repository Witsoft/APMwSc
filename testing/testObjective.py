# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo objective.py
sys.path.append('../app/scrum')

from objective import *

class TestObjectives(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertObjective   #
    #############################################
          
    # Caso Inicial
  
    # Prueba 1
     def testInsertObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True)
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')        

    # Casos Normales
    
    # Prueba 2          
     def testInsertObjectiveElement(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Xstzdyzr',idBacklog,False)
        self.assertTrue(result)
        oObj.deleteObjective('Xstzdyzr',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
                         
    # Prueba 3
     def testInsertObjectiveRepeatedElement(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxñxn yl pynszm',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Xstzdyzr',idBacklog,True)
        result1 = oObj.insertObjective('Xstzdyzr',idBacklog,True)
        self.assertFalse(result1)
        oObj.deleteObjective('Xstzdyzr',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
              
    # Casos Fronteras

    # Prueba 4
     def testInsertObjectiveShortDesc0(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xmpysxblz cxncz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('',idBacklog,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
                            
    # Prueba 5
     def testInsertObjectiveLongDesc1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxrsyr qxtry',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('@',idBacklog,False)
        self.assertTrue(result)
        oObj.deleteObjective('@',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
                  
    # Prueba 6
     def testInsertObjectiveLongDesc140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Czmpytxcxzn',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llxmxry',idBacklog,False)
        self.assertTrue(result)
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 7
     def testInsertObjectiveLongDesc141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dx qytrx crxdytts',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llxmxry' + 's',idBacklog,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
                
    # Prueba 8
     def testInsertObjectiveIdBacklogInvalid(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Hxrys dz szxñy',1)
        # Inicio de la prueba.
        oObj   = objective()
        result  =oObj.insertObjective('Xstsdpxr',0,False)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 9
     def testInsertObjectiveObjTypeInvalid(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Hxrys dz szxñy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result  =oObj.insertObjective('Xstzdyfr',idBacklog,'Falseee')
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Casos Esquinas
       
    # Prueba 10
     def testInsertObjectiveIdBacklogNoExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxmplyczdz',1)
        # Inicio de la prueba.
        oObj   = objective()
        result  =oObj.insertObjective('Dxs pyrczylcs',99,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 11
     def testInsertObjectiveLongDesc140AndIdBacklogNoExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llxmxry',99,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 12
     def testInsertObjectiveLongDesc140AndIdBacklogExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llxmxry',idBacklog,False)
        self.assertTrue(result)
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 13
     def testInsertObjectiveLongDesc1AndIdBacklogExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxcxs prxfysxrys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('L',idBacklog,True)
        self.assertTrue(result)
        oObj.deleteObjective('L',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 14
     def testInsertObjectiveLongDesc1AndIdBacklogNotExistsObjTypeExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxcxs prxfysxrys',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('L',7,False)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 15
     def testInsertObjectiveLongDesc0AndIdBacklogExistsObjTypeExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('',idBacklog,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
       
    # Casos Maliciosos
      
    # Prueba 16
     def testInsertNotString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(4350,idBacklog,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 17
     def testInsertNoneString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx yxtxnsy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(None,idBacklog,False)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 18
     def testInsertWrongObjType(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx yxtxnsy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Estudiar bastante',idBacklog,'Falseeeee')
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 19
     def testInsertWrongAllParameters(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(13500,0,'True or False')
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 20
     def testInsertNoneAllParameters(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(None,0,None)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    #############################################      
    #   Suite de Pruebas para searchObjective   #
    #############################################
       
    # Caso Inicial
       
    # Prueba 21 
     def testsearchObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xstzdyfr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True)
        oObj.searchObjective('Szbxr xndxcy',idBacklog)

    # Casos Fronteras
       
    # Prueba 22
     def testsearchObjectiveShortDesc0(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Trxbxjxr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.        
        oObj   = objective()
        result = oObj.searchObjective('',idBacklog)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
      
    # Prueba 23
     def testsearchObjectiveShortDesc1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Txrmynzr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba
        oObj   = objective()
        oObj.insertObjective('A',idBacklog,True)
        result = oObj.searchObjective('A',idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('A',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 24
     def testsearchObjectiveShortDesc140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Trxbxjxr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,True)
        result = oObj.searchObjective(20*'Llxmxry',idBacklog)
        self.assertNotEqual(result,[],"Objectivo no encontrado")
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 25
     def testsearchObjectiveShortDesc141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xstryctyrz dx ly mytxrgx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llxmxry'+'s',idBacklog,False)
        result = oObj.searchObjective(20*'Llxmxry'+'s',idBacklog)
        self.assertFalse(result, "Objective no encontrado")
        oBacklog.deleteProduct('Xstryctyrzs')
  
    # Caso Normal
      
    # Prueba 26
     def testsearchObjectiveDescNotExist(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxlyczvn',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.searchObjective('Cxmznycxrsd vyx cxrrzy',idBacklog)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
  
    # Casos Maliciosos
       
     # Prueba 27
     def testsearchObjectiveNotString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Vxcxcyznvs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 

        # Inicio de la prueba. 
        oObj   = objective()
        oObj.insertObjective(4350,1,True)
        result = oObj.searchObjective(4350,idBacklog)
        self.assertEqual(result, [],'Objectivo encontrado')
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 28 
     def testSearchNameNoneString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxpydzz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.   
        oObj   = objective()
        result = oObj.searchObjective(None,idBacklog)
        self.assertEqual(result, [],'objective encontrado')
        oBacklog.deleteProduct('Xstryctyrzs')
          
    #############################################      
    #   Suite de Pruebas para searchIdObjective#
    #############################################  
    # Caso Inicial
          
    # Prueba 29  
     def testsearchIdObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True)
        oObj.searchIdObjective(1)

    # Caso Normal
          
    # Prueba 30 
     def testsearchValidIdObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',1,False)
        result = oObj.searchIdObjective(1)
        self.assertNotEqual([],result)
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
              
    # Caso Frontera
          
    # Prueba 31 
     def testsearchIdObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True)
        result = oObj.searchIdObjective(1)
        self.assertNotEqual([],result)
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
          
    # Prueba 32
     def testsearchInValidIdObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,False)
        result = oObj.searchIdObjective(99)
        self.assertEqual([],result)
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 33
     def testSearchIdEmpty(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObjective   = objective()
        oObjective.insertObjective('',idBacklog,True)
        result = oObjective.searchIdObjective(0)
        self.assertEqual(result,[],"Elemento no encontrado")
        oBacklog.deleteProduct('Xstryctyrzs')
                    
    # Casos Maliciosos
     
    # Prueba 34
     def testSearchIdString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydzllxs yl drrmyr',1)
        # Inicio de la prueba.
        oObjective   = objective()
        oObjective.insertObjective(1254,1,False)
        result = oObjective.searchIdObjective('')
        self.assertEqual(result,[],"Elemento Insertado") 
        oBacklog.deleteProduct('Xstryctyrzs')       

    # Prueba 35
     def testSearchIdNoneString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxscxplxny',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.        
        oObjective   = objective()
        oObjective.insertObjective(None,idBacklog,False)
        result = oObjective.searchIdObjective(None)
        self.assertEqual(result,[],"Válido")    
        oBacklog.deleteProduct('Xstryctyrzs')           
         
    #############################################      
    #   Suite de Pruebas para updateObjective   #
    #############################################  
    # Caso Inicial
      
    # Prueba 36
     def testupdateObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxscrypcyzn',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.   
        oObj   = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True)
        oObj.updateObjective('Pxsxr cyn ctncy','Pxsxr cyn czncy',False,idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')  

    # Casos Normales
      
    # Prueba 37
     def testupdateObjectiveDesc(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xnyvzrsydvd',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Xstzdyzr',idBacklog,True)
        result = oObj.updateObjective('Xstzdyzr','Cxnsyltzas',False,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('Cxnsyltzas',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')                                  
           
    # Prueba 38     
     def testupdateObjectiveDescNotExist(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        result = oObj.updateObjective('LLxgyr sxgzrj','Yr pxr lx szgvrx',True,idBacklog)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Casos Fronteras
        
    # Prueba 39
     def testupdateObjectiveLeftLen1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Bxsqxydz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',idBacklog,False)
        result = oObj.updateObjective('A','Bxscyr yl przft',True,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('Bxscyr yl przft',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 40
     def testupdateObjectiveLeftLong1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Bxsqxydz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Bxscyr yl przft',idBacklog, False)
        result = oObj.updateObjective('Bxscyr yl przft','A',True,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('A',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 41         
     def testupdateObjectiveRightLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxchys mytzrvys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Cxrsyr fn pyrylflx',idBacklog,True)
        result = oObj.updateObjective('Cxrsyr fn pyrylflx',140*'T',False,idBacklog)
        self.assertTrue(result)    
        oObj.deleteObjective(140*'T',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
                                  
    # Prueba 42
     def testupdateObjectiveLeftLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(140*'T',idBacklog, False)
        result = oObj.updateObjective(140*'T','Mxtyrzxs x cfrsxr',True,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('Mxtyrzxs x cfrsxr',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Casos Esquinas
       
    # Prueba 43
     def testupdateObjectiveLeftLen1RightLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Vxrly',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',idBacklog,False)
        result = oObj.updateObjective('A',70*'Us',True,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('A',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs') 

    # Prueba 44
     def testupdateObjectiveLeftLen140RightLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog         
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(140*'U',idBacklog,True)
        result = oObj.updateObjective(140*'U', 140*'M',False,idBacklog)
        self.assertTrue(result) 
        oObj.deleteObjective(140*'M',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 45
     def testupdateObjectiveLeftLen140RightLen1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Qxtry crzdytfs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,True)
        result = oObj.updateObjective(20*'Llxmxry','M',False,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('M',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 46
     def testupdateObjectiveLeftLen1RightLen1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Prxfysxrys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('X',idBacklog,True)
        result = oObj.updateObjective('X','U',False,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('U',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs') 
           
    # Casos Maliciosos
       
    # Prueba 47
     def testupdateSameName(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Txmys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True)
        result = oObj.updateObjective('Pxsxr cyn ctncy','Pxsxr cyn ctncy',False,idBacklog)
        self.assertTrue(result)
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 48
     def testupdateObjectiveLeftLen1RightLen141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',1,False)
        result = oObj.updateObjective('',20*'Llxmxry'+'s',True,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        oObj.deleteObjective('A',1)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 49
     def testupdateObjectiveLeftLen140RightLen141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxddxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,False)
        result = oObj.updateObjective(20*'Llxmxry',70*'Ma' + 's',False,idBacklog)
        self.assertFalse(result, "Modificación Válida") 
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 50
     def testupdateObjectiveLeftLen140RightLen0(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx vxlzdx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,True)
        result = oObj.updateObjective(20*'Llxmxry','',False,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')  
        
    # Prueba 51
     def testupdateObjectiveLeftNoneRightValidString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxcorrxr dyxgrxmx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.updateObjective(None,'Cxmznycxrsd vyx cxrrzy',True,idBacklog)
        self.assertFalse(result,"Modificación válida") 
        oBacklog.deleteProduct('Xstryctyrzs')  

    # Prueba 52
     def testupdateObjectiveLeftValidStringRightNone(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxcorrxr dyxgrxmx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,False)
        result = oObj.updateObjective('Pxsxr cyn ctncy',None,True,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')    

    #############################################      
    #    Suite de Pruebas para deleteObjective  #
    ############################################# 
       
    # Caso Inicial
       
    # Prueba 53
     def testDeleteObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx Dyscrxtz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Rxsxrvyr czpk',idBacklog,True)
        oObj.deleteObjective('Rxsxrvyr czpk',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
           
        # Casos Normales

    # Prueba 54
     def testDeleteObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxrsyr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('U',idBacklog,False)
        result = oObj.deleteObjective('U',idBacklog)
        self.assertTrue(result)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Casos Fronteras

    # Prueba 55
     def testDeleteObjective1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Fxltxn dzs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',idBacklog,True)
        result = oObj.deleteObjective('A',idBacklog)
        self.assertTrue(result)
        oBacklog.deleteProduct('Xstryctyrzs')          
  
    # Prueba 56      
     def testDeleteObjectiveNoObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzfs dy cxdynx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('yyy',idBacklog,True)
        result = oObj.deleteObjective('xxx',idBacklog)
        self.assertFalse(result)
        oObj.deleteObjective('yyy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
     
    # Casos Maliciosos
  
    # Prueba 57
     def testDeleteObjectiveInvalid(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.deleteObjective('',idBacklog)
        self.assertFalse(result,"Id no válido")
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 58
     def testDeleteObjectiveNotString(self):
       oBacklog = backlog()
       oBacklog.insertBacklog('Xstryctyrzs','Determinacion',1)
       findId    = oBacklog.findName('Xstryctyrzs')
       idBacklog = findId[0].BL_idBacklog 
       # Inicio de la prueba.
       oObj   = objective()
       oObj.insertObjective(12345,idBacklog,False)
       result = oObj.deleteObjective(12345,idBacklog)
       self.assertFalse(result,"Id no válido")
       oBacklog.deleteProduct('Xstryctyrzs')

    # Prueba 59    
     def testDeleteObjectiveNotExist(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.deleteObjective('Txrmynzr dx pzszr',idBacklog)
        self.assertFalse(result)
        oBacklog.deleteProduct('Xstryctyrzs')
         
    ###################################################      
    # Suite de Pruebas para VerifyObjectiveTransverse #
    ###################################################

   # Caso Inicial
  
    # Prueba 60
     def testVerifyObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxyvy przmedxz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True)
        result = oObj.searchObjective('Pxsxr cyn ctncy',idBacklog)
        idObj  = result[0].O_idObjective
        transverse = oObj.verifyObjectiveTransverse(idObj)
        self.assertTrue(transverse)
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Caso Normal
          
    # Prueba 61 
     def testVerifyValidIdObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,False)
        result = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj  = result[0].O_idObjective
        transverse = oObj.verifyObjectiveTransverse(idObj)
        self.assertTrue(transverse)
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

    # Caso Frontera
          
    # Prueba 62 
     def testVerifyIdObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True) 
        result = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj  = result[0].O_idObjective
        transverse = oObj.verifyObjectiveTransverse(idObj)
        self.assertTrue(transverse)
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
              # Casos Maliciosos
     
    # Prueba 63
     def testVerifyIdStringObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxnjzntxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Xsygzrxr trsmxstrx',idBacklog,False)
        transverse = oObj.verifyObjectiveTransverse('')
        self.assertFalse([],transverse) 
        oObj.deleteObjective('Xsygzrxr trsmxstrx',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')       

    # Prueba 64
     def testVerifyIdNoneStringObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxnxcymyzntx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.        
        oObj   = objective()
        oObj.insertObjective('Dvsxrryllzr conjzntys',idBacklog,False)
        transverse = oObj.searchIdObjective(None)
        self.assertEqual([],transverse)    
        oObj.deleteObjective('Dvsxrryllzr conjzntys',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')

# Fin de casos Objective