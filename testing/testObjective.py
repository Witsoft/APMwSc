# -*- coding: utf-8 -*-. 

import unittest

from objectiveDummy import *

class TestObjectives(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertObjective   #
    #############################################
          
    # Caso Inicial
  
    # Prueba 1
     def testInsertObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Mueve personas',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Reservar un taxi',1,True)
        aAcc.deleteObjective('Reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')        

    # Casos Normales
    
    # Prueba 2          
     def testInsertObjectiveElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Pasa ciudades',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('Permite elegir',1,False)
        self.assertTrue(result)
        aAcc.deleteObjective('Permite elegir')
        aBackLog.deleteProduct('Taxi seguro')
                          
    # Prueba 3
     def testInsertObjectiveRepeatedElement(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Pasa ciudades',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('Permite elegir',1,True)
        result1 = aAcc.insertObjective('Permite elegir',1,True)
        self.assertFalse(result1)
        aAcc.deleteObjective('Permite elegir')
        aBackLog.deleteProduct('Taxi seguro')
               
    # Casos Fronteras

    # Prueba 4
     def testInsertObjectiveShortDesc0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rueda de caras negras',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('',1,True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
                           
    # Prueba 5
     def testInsertObjectiveLongDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Motor fuerte',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('A',1,False)
        self.assertTrue(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro')
       
    # Prueba 6
     def testInsertObjectiveLongDesc140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Pertece a linea movistar',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem',1,False)
        self.assertTrue(result)
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 7
     def testInsertObjectiveLongDesc141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','De color rojo',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1,True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
                
    # Prueba 8
     def testInsertObjectiveIdBackLogInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result  =aAcc.insertObjective('Movilizarme desde mi casa',0,False)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 9
     def testInsertObjectiveObjTypeInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result  =aAcc.insertObjective('Movilizarme desde mi casa',1,'Falseee')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Casos Esquinas
       
    # Prueba 10
     def testInsertObjectiveIdBackLogNoExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rapido y Furioso',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result  =aAcc.insertObjective('Trasladarse rápido',2,True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
            
    # Prueba 11
     def testInsertObjectiveLongDesc140AndIdBackLogNoExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Via rapida',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin proble1',3,True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 12
     def testInsertObjectiveLongDesc140AndIdBackLogExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Via rapida',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin proble1',1,False)
        self.assertTrue(result)
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 13
     def testInsertObjectiveLongDesc1AndIdBackLogExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Via rapida',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('L',1,True)
        self.assertTrue(result)
        aAcc.deleteObjective('L')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 14
     def testInsertObjectiveLongDesc1AndIdBackLogNotExistsObjTypeExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Via rapida',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('L',7,False)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 15
     def testInsertObjectiveLongDesc0AndIdBackLogExistsObjTypeExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Via rapida',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('',1,True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
       
    # Casos Maliciosos
      
    # Prueba 16
     def testInsertNotString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Vuelo alto',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective(4350,1,True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 17
     def testInsertNoneString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Velocidad maxima',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective(None,1,False)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 18
     def testInsertWrongObjType(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Velocidad maxima',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective('7 ruedas',1,'Falseeeee')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 19
     def testInsertWrongAllParameters(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Velocidad media',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective(13500,'Ramas','True or False')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 20
     def testInsertNoneAllParameters(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Velocidad media',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.insertObjective(None,None,None)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
  
    #############################################      
    #   Suite de Pruebas para searchObjective   #
    #############################################
       
    # Caso Inicial
       
    # Prueba 21 
     def testsearchObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Manejar con prudencia',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,True)
        aAcc.searchObjective('Permite reservar un taxi')

    # Casos Fronteras
       
    # Prueba 22
     def testsearchObjectiveShortDesc0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilizacion',1)
        # Inicio de la prueba.        
        aAcc   = objective()
        aAcc.insertObjective('',1,False)
        result = aAcc.searchObjective('')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
      
    # Prueba 23
     def testsearchObjectiveShortDesc1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Desplazamiento',1)
        # Inicio de la prueba
        aAcc   = objective()
        aAcc.insertObjective('A',1,True)
        result = aAcc.searchObjective('A')
        self.assertTrue(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 24
     def testsearchObjectiveShortDesc140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Trabajar',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem',1,True)
        result = aAcc.searchObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        self.assertNotEqual(result,[],"Objective no encontrada")
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problem')
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 25
     def testsearchObjectiveShortDesc141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Estructura del carro',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema',1,False)
 
        result = aAcc.searchObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problema')
        self.assertFalse(result, "Objective Encontrada.")
        aBackLog.deleteProduct('Taxi seguro')
  
    # Caso Normal
      
    # Prueba 26
     def testsearchObjectiveDescNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Relacion con el cliente',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.searchObjective('Comunicarse via correo electronico')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
  
    # Casos Maliciosos
       
     # Prueba 27
     def testsearchObjectiveNotString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Viajes',1)
        # Inicio de la prueba. 
        aAcc   = objective()
        aAcc.insertObjective(4350,1,True)
        result = aAcc.searchObjective(4350)
        self.assertEqual(result, [],'Objective Encontrada')
        aBackLog.deleteProduct('Taxi seguro')
 
    # Prueba 28 
     def testSearchNameNoneString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rapidez',1)
        # Inicio de la prueba.   
        aAcc   = objective()
        result = aAcc.searchObjective(None)
        self.assertEqual(result, [],'Objective Encontrada')
        aBackLog.deleteProduct('Taxi seguro')
          
    #############################################      
    #   Suite de Pruebas para searchIdObjective#
    #############################################  
    # Caso Inicial
          
    # Prueba 29  
     def testsearchIdObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,True)
        aAcc.searchIdObjective(1)

    # Caso Normal
          
    # Prueba 30 
     def testsearchValidIdObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,False)
        result = aAcc.searchIdObjective(1)
        self.assertNotEqual([],result)
        aAcc.deleteObjective('Permite reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')

    # Caso Frontera
          
    # Prueba 31 
     def testsearchIdObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,True)
        result = aAcc.searchIdObjective(1)
        self.assertNotEqual([],result)
        aAcc.deleteObjective('Permite reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')
          
    # Prueba 32
     def testsearchInValidIdObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,False)
        result = aAcc.searchIdObjective(5)
        self.assertEqual([],result)
        aAcc.deleteObjective('Permite reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 33
     def testSearchIdEmpty(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        oObjective   = objective()
        oObjective.insertObjective('',1,True)
        result = oObjective.searchIdObjective(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        aBackLog.deleteProduct('Taxi seguro')
                    
    # Casos Maliciosos
     
    # Prueba 34
     def testSearchIdString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Ruedas de cara blanca',1)
        # Inicio de la prueba.
        oObjective   = objective()
        oObjective.insertObjective(1254,1,False)
        result = oObjective.searchIdObjective('')
        self.assertEqual(result,[],"Elemento Insertado") 
        aBackLog.deleteProduct('Taxi seguro')       

    # Prueba 35
     def testSearchIdNoneString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rapidez',1)
        # Inicio de la prueba.        
        oObjective   = objective()
        oObjective.insertObjective(None,1,False)
        result = oObjective.searchIdObjective(None)
        self.assertEqual(result,[],"Válido")    
        aBackLog.deleteProduct('Taxi seguro')           
         
    #############################################      
    #   Suite de Pruebas para updateObjective   #
    #############################################  
    # Caso Inicial
      
    # Prueba 36
     def testupdateObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Descripcion',1)
        # Inicio de la prueba.   
        aAcc   = objective()
        aAcc.insertObjective('Reservar un taxi.',1,True)
        aAcc.updateObjective('Reservar un taxi','Reservar un taxi o varios',False)
        aBackLog.deleteProduct('Taxi seguro')  

    # Casos Normales
      
    # Prueba 37
     def testupdateObjectiveDesc(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Carretera',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Permite elegir',1,True)
        result = aAcc.updateObjective('Permite elegir','Atención las 24 horas del día',False)
        self.assertTrue(result)
        aAcc.deleteObjective('Atención las 24 horas del día')
        aBackLog.deleteProduct('Taxi seguro')                                  
           
    # Prueba 38     
     def testupdateObjectiveDescNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        result = aAcc.updateObjective('Llegar lo mas pronto posible','Ir comodo y seguro',True)
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Casos Fronteras
        
    # Prueba 39
     def testupdateObjectiveLeftLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rapidez',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('A',1,False)
        result = aAcc.updateObjective('A','Buscar al cliente donde esté',True)
        self.assertTrue(result)
        aAcc.deleteObjective('Buscar al cliente donde esté')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 40
     def testupdateObjectiveLeftLong1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Desplazamiento',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Buscar al cliente donde esté',1, False)
        result = aAcc.updateObjective('Buscar al cliente donde esté','A',True)
        self.assertTrue(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 41         
     def testupdateObjectiveRightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Carretera',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Atención las 24 horas del día',1,True)
        result = aAcc.updateObjective('Atención las 24 horas del día',140*'T',False)
        self.assertTrue(result)    
        aAcc.deleteObjective(140*'T')
        aBackLog.deleteProduct('Taxi seguro')
                                  
    # Prueba 42
     def testupdateObjectiveLeftLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Tipo de taxi',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective(140*'T',1, False)
        result = aAcc.updateObjective(140*'T','Atención las 24 horas del día',True)
        self.assertTrue(result)
        aAcc.deleteObjective('Atención las 24 horas del día')
        aBackLog.deleteProduct('Taxi seguro')

    # Casos Esquinas
       
    # Prueba 43
     def testupdateObjectiveLeftLen1RightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Neumàticos de cara negra',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('A',1,False)
        result = aAcc.updateObjective('A',140*'Us',True)
        self.assertFalse(result)
        aAcc.deleteObjective('A')
        aBackLog.deleteProduct('Taxi seguro') 

    # Prueba 44
     def testupdateObjectiveLeftLen140RightLen140(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Ruedas de cara blanca',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective(140*'Us',1,True)
        result = aAcc.updateObjective(140*'Us', 140*'Ma',False)
        self.assertFalse(result) 
        aAcc.deleteObjective(140*'Us')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 45
     def testupdateObjectiveLeftLen140RightLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rueda 250 km',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem',1,True)
        result = aAcc.updateObjective('Llamar al centro de atencion de servicios de taxis a '+
                                       'cualquier hora del dia, para poder dirigirse a '+
                                       'cualquier lugar de la ciudad sin problem','M',False)
        self.assertTrue(result)
        aAcc.deleteObjective('M')
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 46
     def testupdateObjectiveLeftLen1RightLen1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Semàforo',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('X',1,True)
        result = aAcc.updateObjective('X','U',False)
        self.assertTrue(result)
        aAcc.deleteObjective('U')
        aBackLog.deleteProduct('Taxi seguro') 
           
    # Casos Maliciosos
       
    # Prueba 47
     def testupdateSameName(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Partes de un taxi',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Reservar un taxi',1,True)
        result = aAcc.updateObjective('Reservar un taxi','Reservar un taxi',False)
        self.assertTrue(result)
        aAcc.deleteObjective('Reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 48
     def testupdateObjectiveLeftLen0RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('',1,False)
        result = aAcc.updateObjective('','Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problems',True)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteObjective('')
        aBackLog.deleteProduct('Taxi seguro')
 
    # Prueba 49
     def testupdateObjectiveLeftLen141RightLen141(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Ruedas',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema',1,False)
        result = aAcc.updateObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema',25*'Ma' + 's',False)
        self.assertFalse(result, "Modificación Válida") 
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problema')
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 50
     def testupdateObjectiveLeftLen141RightLen0(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Ruedas caras',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas',1,True)
        result = aAcc.updateObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas','',False)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteObjective('Llamar al centro de atencion de servicios de taxis a '+
                                      'cualquier hora del dia, para poder dirigirse a '+
                                      'cualquier lugar de la ciudad sin problemas')
        aBackLog.deleteProduct('Taxi seguro')  

    # Prueba 51
     def testupdateObjectiveLeftNoneRightValidString(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Recorrer ciudades',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.updateObjective(None,'Comunicarse via correo electronico',True)
        self.assertFalse(result,"Modificación válida") 
        aBackLog.deleteProduct('Taxi seguro')  
 
    # Prueba 52
     def testupdateObjectiveLeftValidStringRightNone(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Recorrer estados',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Reservar un taxi',1,False)
        result = aAcc.updateObjective('Reservar un taxi',None,True)
        self.assertFalse(result, "Modificación válida") 
        aAcc.deleteObjective('Reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')    

    #############################################      
    #    Suite de Pruebas para deleteObjective  #
    ############################################# 
       
    # Caso Inicial
       
    # Prueba 53
     def testDeleteObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movimiento Lineal',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Reservar un Taxi',1,True)
        aAcc.deleteObjective('Reservar un Taxi')
        aBackLog.deleteProduct('Taxi seguro')
           
        # Casos Normales
   
    # Prueba 54
     def testDeleteObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Asiento',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('U',1,False)
        result = aAcc.deleteObjective('U')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro')

    # Casos Fronteras

    # Prueba 55
     def testDeleteObjective1(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Peatones',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('A',1,True)
        result = aAcc.deleteObjective('A')
        self.assertTrue(result)
        aBackLog.deleteProduct('Taxi seguro')          
  
    # Prueba 56      
     def testDeleteObjectiveNoObjective(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rayado',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('yyy',1,True)
        result = aAcc.deleteObjective('xxx')
        self.assertFalse(result)
        aAcc.deleteObjective('yyy')
        aBackLog.deleteProduct('Taxi seguro')
     
    # Casos Maliciosos
  
    # Prueba 57
     def testDeleteObjectiveInvalid(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.deleteObjective('')
        self.assertFalse(result,"Id no válido")
        aBackLog.deleteProduct('Taxi seguro')
           
    # Prueba 58
     def testDeleteObjectiveNotString(self):
       aBackLog = backLog()
       aBackLog.insertBackLog('Taxi seguro','Desplazamiento',1)
       # Inicio de la prueba.
       aAcc   = objective()
       aAcc.insertObjective(12345,1,False)
       result = aAcc.deleteObjective(12345)
       self.assertFalse(result,"Id no válido")
       aBackLog.deleteProduct('Taxi seguro')

    # Prueba 59    
     def testDeleteObjectiveNotExist(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc   = objective()
        result = aAcc.deleteObjective('Llegar rápido')
        self.assertFalse(result)
        aBackLog.deleteProduct('Taxi seguro')
         
    ###################################################      
    # Suite de Pruebas para VerifyObjectiveTransverse #
    ###################################################

   # Caso Inicial
  
    # Prueba 60
     def testVerifyObjectiveExists(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Mueve personas',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Reservar un taxi',1,True)
        transverse = aAcc.verifyObjectiveTransverse(1)
        self.assertTrue(transverse)
        aAcc.deleteObjective('Reservar un Taxi')
        aBackLog.deleteProduct('Taxi seguro')
        
    # Caso Normal
          
    # Prueba 61 
     def testVerifyValidIdObjectiveTransverse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,False)
        transverse = aAcc.verifyObjectiveTransverse(1)
        self.assertTrue(transverse)
        aAcc.deleteObjective('Permite reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')

    # Caso Frontera
          
    # Prueba 62 
     def testVerifyIdObjectiveTransverse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,True)
        transverse = aAcc.verifyObjectiveTransverse(1)
        self.assertTrue(transverse)
        aAcc.deleteObjective('Permite reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')
          
    # Prueba 63
     def testVerifyInvalidIdObjectiveTransverse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc = objective()
        aAcc.insertObjective('Permite reservar un taxi',1,False)
        transverse = aAcc.verifyObjectiveTransverse(5)
        self.assertEqual([],transverse)
        aAcc.deleteObjective('Permite reservar un taxi')
        aBackLog.deleteProduct('Taxi seguro')

    # Prueba 64
     def testVerifyIdEmptyObjectiveTransverse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Movilidad',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Terminar todo',1,True)
        transverse = aAcc.verifyObjectiveTransverse(0)
        self.assertEqual([],transverse)
        aAcc.deleteObjective('Terminar todo')        
        aBackLog.deleteProduct('Taxi seguro')
                    
    # Casos Maliciosos
     
    # Prueba 65
     def testVerifyIdStringObjectiveTransverse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Ruedas de cara blanca',1)
        # Inicio de la prueba.
        aAcc   = objective()
        aAcc.insertObjective('Asegurar el cinturon',1,False)
        transverse = aAcc.verifyObjectiveTransverse('')
        self.assertFalse([],transverse) 
        aAcc.deleteObjective('Asegurar el cinturon')
        aBackLog.deleteProduct('Taxi seguro')       

    # Prueba 66
     def testVerifyIdNoneStringObjectiveTransverse(self):
        aBackLog = backLog()
        aBackLog.insertBackLog('Taxi seguro','Rapidez',1)
        # Inicio de la prueba.        
        aAcc   = objective()
        aAcc.insertObjective('Desarrollar partes de un carro',1,False)
        transverse = aAcc.searchIdObjective(None)
        self.assertEqual([],transverse)    
        aAcc.deleteObjective('Desarrollar partes de un carro')
        aBackLog.deleteProduct('Taxi seguro')                   