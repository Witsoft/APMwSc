# -*- coding: utf-8 -*-. 

import unittest

from objectiveDummy import *

class TestObjective(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertObjective   #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def testInsertObjectiveExists(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj = objective()
         aObj.insertObjective('Permite reservar un taxi.',1)
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite reservar un taxi.')
         aBackLog.deleteProduct('Taxi seguro.')
        
         
     # Casos Normales
            
     # Prueba 2     
     def testInsertObjectiveElement(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective('Permite elegir.',1)
         self.assertTrue(result)
         #Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite elegir')
         aBackLog.deleteProduct('Taxi seguro.')
          
                      
     # Prueba 3
     def testInsertRepeatedElement(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj    = objective()
         result  = aObj.insertObjective('Permite seleccionar.',1)
         result1 = aObj.insertObjective('Permite seleccionar.',1)
         self.assertFalse(result1)
         #Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite seleccionar.')
         aBackLog.deleteProduct('Taxi seguro.')
       
          
     # Casos Fronteras
     
     # Prueba 4
     def testInsertObjectiveShortDesc0(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective('',1)
         self.assertFalse(result)
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
         
     # Prueba 5
     def testInsertObjectiveLongDesc1(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective('P',1)
         self.assertTrue(result)
         #Eliminacion del elemento insertado.
         aObj.deleteObjective('P')
         aBackLog.deleteProduct('Taxi seguro.')
       
     # Prueba 6
     def testInsertObjectiveLongDesc140(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .',1)
         self.assertTrue(result)
         #Eliminacion del elemento insertado.
         aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .')
         aBackLog.deleteProduct('Taxi seguro.')
          
     # Prueba 7
     def testInsertObjectiveLongDesc141(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2',1)
         self.assertFalse(result)
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
         
          
     # Casos Maliciosos
      
     # Prueba 8
     def testInsertNotString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective(1254,1)
         self.assertFalse(result,"Objetivo agregado.")
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
  
     # Prueba 9
     def testInsertNoneString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.insertObjective(None,1)
         self.assertFalse(result,"Objetivo agregado.")
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
         
     
      #############################################      
      #   Suite de Pruebas para searchObjective   #
      #############################################
      
    # Caso Inicial
     
     # Prueba 10 
     def testSearchObjectiveExists(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj = objective()
         aObj.insertObjective('Permite reservar un taxi.',1)
         res  = aObj.searchObjective('Permite reservar un taxi')
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')         
               
                
    # Casos Fronteras
      
     # Prueba 11
     def testSearchObjectiveShortDesc0(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.         
         aObj   = objective()
         aObj.insertObjective('',1)
         result = aObj.searchObjective('')
         self.assertFalse(result, "Objetivo Encontrado.")
         #Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
            
     # Prueba 12
     def testSearchObjectiveShortDesc1(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.         
         aObj   = objective()
         aObj.insertObjective('P',1)
         result = aObj.searchObjective('P')
         self.assertNotEqual(result,[],"Objetivo no encontrado")
         #Eliminacion del elemento insertado.
         aObj.deleteObjective('P')
         aBackLog.deleteProduct('Taxi seguro.')
       
     # Prueba 13
     def testSearchObjectiveShortDesc140(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.   
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .',1)
         result = aObj.searchObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertNotEqual(result,[],"Objetivo no encontrado")
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .')
         aBackLog.deleteProduct('Taxi seguro.')
            
     # Prueba 14
     def testSearchObjectiveShortDesc141(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.   
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .2',1)
         result = aObj.searchObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result, "Objetivo Encontrado.")
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
          
          
    # Casos Maliciosos
      
     # Prueba 15
     def testSearchObjectiveNotString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.   
         aObj   = objective()
         aObj.insertObjective(1245,1)
         result = aObj.searchObjective(1245)
         self.assertFalse(result, "Objetivo Encontrado.")
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
       
     # Prueba 16
     def testFindNameNoneString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.  
         aObj   = objective()
         aObj.insertObjective(None,1)
         result = aObj.searchObjective(None)
         self.assertFalse(result,"Objetivo Encontrado.") 
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')
                     
      #############################################      
      #   Suite de Pruebas para updateObjective   #
      #############################################  
  
    # Caso Inicial
     
     # Prueba 17
     def testUpdateObjectiveExists(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj = objective()
         aObj.insertObjective('Permite reservar un taxi.',1)
         aObj.updateObjective('Permite reservar un taxi.','Permite reservar un taxi o varios.')   
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite reservar un taxi o varios.')
         aBackLog.deleteProduct('Taxi seguro.')   
          
    # Casos Normales
            
     # Prueba 18   
     def testUpdateObjectiveDesc(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Permite elegir.',1)
         result = aObj.updateObjective('Permite elegir.','Permite obtener.')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite elegir.')
         aBackLog.deleteProduct('Taxi seguro.')  
                      
     # Prueba 19
     def testUpdateRepeatedDesc(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Permite obtener.',1)
         result = aObj.updateObjective('Permite obtener.','Permite obtener.')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite elegir.')
         aBackLog.deleteProduct('Taxi seguro.')  
 
    # Casos Fronteras
      
     # Prueba 20
     def testUpdateObjectiveShortDesc0(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('',1)
         result = aObj.updateObjective('','Permite obtener.')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
          
     # Prueba 21    
     def testUpdateObjectiveShortNewDesc0(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Permite obtener.',1)
         result = aObj.updateObjective('Permite obtener.','')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
          
              
     # Prueba 22
     def testUpdateObjectiveShortDesc1(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('P',1)
         result = aObj.updateObjective('P','Permite modificar.')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite modificar.')
         aBackLog.deleteProduct('Taxi seguro.')  
          
     # Prueba 23
     def testUpdateObjectiveShortNewDesc1(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Permite modificar.',1)
         result = aObj.updateObjective('Permite modificar.','U')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('U')
         aBackLog.deleteProduct('Taxi seguro.')  
             
     # Prueba 24
     def testUpdateObjectiveLongDesc140(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .',1)
         result = aObj.updateObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .','Permite eliminar.')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Permite eliminar.')
         aBackLog.deleteProduct('Taxi seguro.')  
          
     # Prueba 25
     def testUpdateObjectiveLongNewDesc140(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Permite eliminar.',1)
         result = aObj.updateObjective('Permite eliminar.','Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertTrue(result) 
         # Eliminacion del elemento insertado.
         aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .')
         aBackLog.deleteProduct('Taxi seguro.')         
                
     # Prueba 26
     def testUpdateObjectiveLongDesc141(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .2',1)
         result = aObj.updateObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2','Permite verificar.')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')   
          
     # Prueba 27
     def testUpdateObjectiveLongNewDesc141(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Permite verificar.',1)
         result = aObj.updateObjective('Permite verificar.','Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result)  
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')    
          
    # Casos Esquina
     
     # Prueba 28    
     def testUpdateObjectiveBothDesc0(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('',1)
         result = aObj.updateObjective('','')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
          
     # Prueba 29
     def testUpdateObjectiveBothDesc141(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .2',1)
         result = aObj.updateObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2','Producto que permite,'+
                                       ' a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .2')
         self.assertFalse(result)           
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
          
    # Casos Maliciosos
       
     # Prueba 30
     def testUpdateNotString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba. 
         aObj   = objective()
         aObj.insertObjective(1254,1)
         result = aObj.updateObjective(1254,199262)
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
   
     # Prueba 31
     def testUpdateNoneString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective(None,1)
         result = aObj.updateObjective(None,None)
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
   
     #############################################      
     #   Suite de Pruebas para deleteObjective   #
     #############################################
   
    # Caso Inicial
 
     # Prueba 32
     def testDeleteObjectiveElement(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective('Permite intercambiar informacion.',1)
         result = aObj.deleteObjective('Permite intercambiar informacion.')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.')  
                      
     # Prueba 33
     def testDeleteElementNotExist(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         result = aObj.deleteObjective('Permite elegir los actores.')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
        
    # Casos Fronteras
      
     # Prueba 34
     def testDeleteObjectiveShortDesc0(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective('',1)
         result = aObj.deleteObjective('')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
           
     # Prueba 35
     def testDeleteObjectiveShortDesc1(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective('U',1)
         result = aObj.deleteObjective('U')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
        
     # Prueba 36
     def testDeleteObjectiveLongDesc140(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .',1)
         result = aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .')
         self.assertTrue(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
           
     # Prueba 37
     def testDeleteObjectiveLongDesc141(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective('Producto que permite, a traves de una aplicacion movil,'+
                              'hacer reservaciones de taxis desde cualquier lugar'+
                              ' que estes y sin importar la hora .3',1)
         result = aObj.deleteObjective('Producto que permite, a traves de una aplicacion movil,'+
                                       'hacer reservaciones de taxis desde cualquier lugar'+
                                       ' que estes y sin importar la hora .3')
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
           
           
    # Casos Maliciosos
        
     # Prueba 38
     def test_38DeleteNotString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective(1254,1)
         result = aObj.deleteObjective(1254)
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
    
     # Prueba 39
     def test_39DeleteNoneString(self):
         # Insercion de producto en la tabla pila.
         aBackLog = backLog()
         aBackLog.insertBackLog('Taxi seguro.','Permite localizar un taxi')
         # Inicio de la prueba.
         aObj   = objective()
         aObj.insertObjective(None,1)
         result = aObj.deleteObjective(None)
         self.assertFalse(result)
         # Eliminacion del elemento insertado.
         aBackLog.deleteProduct('Taxi seguro.') 
       