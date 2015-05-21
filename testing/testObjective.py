# -*- coding: utf-8 -*-. 

import unittest

from objectiveDummy import *

class TestObjective(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertObjective   #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def test1InsertObjectiveExists(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         aObj = objective()
         aObj.insertObjective('Permite reservar un taxi.',1)
        
         
    # Casos Normales
           
     # Prueba 2     
     def test2InsertObjectiveElement(self):
         aObj   = objective()
         result = aObj.insertObjective('Permite elegir.',1)
         self.assertTrue(result)
         aObj.deleteObjective('Permite elegir')
         
                     
     # Prueba 3
     def test3InsertRepeatedElement(self):
         aObj   = objective()
         result = aObj.insertObjective('Permite elegir.',1)
         result1 = aObj.insertObjective('Permite elegir.',1)
         self.assertFalse(result1)
      
         
    # Casos Fronteras
    
     # Prueba 4
     def test4InsertObjectiveShortDesc0(self):
         aObj   = objective()
         result = aObj.insertObjective('',1)
         self.assertFalse(result)
         
     # Prueba 5
     def test5InsertObjectiveLongDesc1(self):
         aObj   = objective()
         result = aObj.insertObjective('P',1)
         self.assertTrue(result)
      
     # Prueba 6
     def test6InsertObjectiveLongDesc140(self):
         aObj   = objective()
         result = aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .',1)
         self.assertTrue(result)
         
     # Prueba 7
     def test7InsertObjectiveLongDesc141(self):
         aObj   = objective()
         result = aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2',1)
         self.assertFalse(result)
         
         
    # Casos Maliciosos
      
     # Prueba 8
     def test8InsertNotString(self):
         aObj   = objective()
         result = aObj.insertObjective(1254,1)
         self.assertFalse(result,"Objetivo agregado.")
 
     # Prueba 9
     def test9InsertNoneString(self):
         aObj   = objective()
         result = aObj.insertObjective(None,1)
         self.assertFalse(result,"Objetivo agregado.")
        
    
     #############################################      
     #   Suite de Pruebas para searchObjective   #
     #############################################
     
     # Caso Inicial
     
     # Prueba 10 
     def test_10searchObjectiveExists(self):
         aObj = objective()
         aObj.searchObjective('Permite reservar un taxi')
               
               
     # Casos Fronteras
     
     # Prueba 11
     def test_11searchObjectiveShortDesc0(self):
         aObj   = objective()
         result = aObj.searchObjective('')
         self.assertFalse(result, "Objetivo Encontrado.")
           
     # Prueba 12
     def test_12searchObjectiveShortDesc1(self):
         aObj   = objective()
         result = aObj.searchObjective('P')
         self.assertNotEqual(result,[],"Objetivo no encontrado")
      
     # Prueba 13
     def test_13searchObjectiveShortDesc140(self):
         aObj   = objective()
         result = aObj.searchObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertNotEqual(result,[],"Objetivo no encontrado")
           
     # Prueba 14
     def test_14searchObjectiveShortDesc141(self):
         aObj   = objective()
         result = aObj.searchObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result, "Objetivo Encontrado.")
         
         
     # Casos Maliciosos
     
     # Prueba 15
     def test_15searchObjectiveNotString(self):
         aObj   = objective()
         result = aObj.searchObjective(1245)
         self.assertFalse(result, "Objetivo Encontrado.")
      
     # Prueba 16
     def test_16FindNameNoneString(self):
         aObj   = objective()
         result = aObj.searchObjective(None)
         self.assertFalse(result,"Objetivo Encontrado.") 
                    
     #############################################      
     #   Suite de Pruebas para updateObjective   #
     #############################################  
 
     # Caso Inicial
    
     # Prueba 17
     def test_17UpdateObjectiveExists(self):
         aObj   = objective()
         aObj.updateObjective('Permite reservar un taxi.','Permite reservar un taxi o varios.')      
         
    # Casos Normales
           
     # Prueba 18   
     def test_18UpdateObjectiveDesc(self):
         aObj   = objective()
         result = aObj.updateObjective('Permite elegir.','Permite obtener.')
         self.assertTrue(result)
                     
     # Prueba 19
     def test_19UpdateRepeatedDesc(self):
         aObj   = objective()
         result = aObj.updateObjective('Permite obtener.','Permite reservar un taxi o varios.')
         self.assertFalse(result)

    # Casos Fronteras
     
     # Prueba 20
     def test_20UpdateObjectiveShortDesc0(self):
         aObj   = objective()
         result = aObj.updateObjective('','Permite obtener.')
         self.assertFalse(result)
         
     # Prueba 21    
     def test_21UpdateObjectiveShortNewDesc0(self):
         aObj   = objective()
         result = aObj.updateObjective('Permite obtener.','')
         self.assertFalse(result)
             
     # Prueba 22
     def test_22UpdateObjectiveShortDesc1(self):
         aObj   = objective()
         result = aObj.updateObjective('P','Permite modificar.')
         self.assertTrue(result)
         
     # Prueba 23
     def test_23UpdateObjectiveShortNewDesc1(self):
         aObj   = objective()
         result = aObj.updateObjective('Permite modificar.','U')
         self.assertTrue(result)
            
     # Prueba 24
     def test_24UpdateObjectiveLongDesc140(self):
         aObj   = objective()
         result = aObj.updateObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .','Permite eliminar.')
         self.assertTrue(result)
         
     # Prueba 25
     def test_25UpdateObjectiveLongNewDesc140(self):
         aObj   = objective()
         result = aObj.updateObjective('Permite eliminar.','Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertTrue(result)         
               
     # Prueba 26
     def test_26UpdateObjectiveLongDesc141(self):
         aObj   = objective()
         result = aObj.updateObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2','Permite verificar.')
         self.assertFalse(result)
         
     # Prueba 27
     def test_27UpdateObjectiveLongNewDesc141(self):
         aObj   = objective()
         result = aObj.updateObjective('Permite verificar.','Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result)   
         
    # Casos Esquina
    
     # Prueba 28    
     def test_28UpdateObjectiveBothDesc0(self):
         aObj   = objective()
         result = aObj.updateObjective('','')
         self.assertFalse(result)
         
     # Prueba 29
     def test_29UpdateObjectiveBothDesc141(self):
         aObj   = objective()
         result = aObj.updateObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2','Producto que permite,'+
                                       ' a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result)           
          
    # Casos Maliciosos
       
     # Prueba 30
     def test_30UpdateNotString(self):
         aObj   = objective()
         result = aObj.updateObjective(1254,199262)
         self.assertFalse(result)
  
     # Prueba 31
     def test_31UpdateNoneString(self):
         aObj   = objective()
         result = aObj.updateObjective(None,None)
         self.assertFalse(result)
  
    #############################################      
    #   Suite de Pruebas para deleteObjective   #
    #############################################
    
    # Caso Inicial
 
     # Prueba 32
     def test_32DeleteObjectiveElement(self):
         aObj   = objective()
         aObj.insertObjective('Permite intercambiar informacion.',1)
         result = aObj.deleteObjective('Permite intercambiar informacion.')
         self.assertTrue(result)
                      
     # Prueba 33
     def test_33DeleteElementNotExist(self):
         aObj   = objective()
         result = aObj.deleteObjective('Permite elegir los actores.')
         self.assertFalse(result)
       
    # Casos Fronteras
     
     # Prueba 34
     def test_34DeleteObjectiveShortDesc0(self):
         aObj   = objective()
         result = aObj.deleteObjective('')
         self.assertFalse(result)
          
     # Prueba 35
     def test_35DeleteObjectiveShortDesc1(self):
         aObj   = objective()
         result = aObj.deleteObjective('U')
         self.assertTrue(result)
       
     # Prueba 36
     def test_36DeleteObjectiveLongDesc140(self):
         aObj   = objective()
         result = aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertTrue(result)
          
     # Prueba 37
     def test_37DeleteObjectiveLongDesc141(self):
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .3',1)
         result = aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .3')
         self.assertFalse(result)
          
          
    # Casos Maliciosos
       
     # Prueba 38
     def test_38DeleteNotString(self):
         aObj   = objective()
         result = aObj.deleteObjective(1254)
         self.assertFalse(result)
   
    # Prueba 39
     def test_39DeleteNoneString(self):
         aObj   = objective()
         result = aObj.deleteObjective(None)
         self.assertFalse(result)
          
      