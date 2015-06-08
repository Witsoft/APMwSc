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
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia dificil',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Pasar con cinco',1,True)
        oObj.deleteObjective('Pasar con cinco')
        oBacklog.deleteProduct('Estructuras Discretas II')        

    # Casos Normales
    
    # Prueba 2          
     def testInsertObjectiveElement(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Profesores dificiles',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Estudiar con constancia',1,False)
        self.assertTrue(result)
        oObj.deleteObjective('Estudiar con constancia')
        oBacklog.deleteProduct('Estructuras Discretas II')
                          
    # Prueba 3
     def testInsertObjectiveRepeatedElement(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dañan el pensum',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Estudiar con constancia',1,True)
        result1 = oObj.insertObjective('Estudiar con constancia',1,True)
        self.assertFalse(result1)
        oObj.deleteObjective('Estudiar con constancia')
        oBacklog.deleteProduct('Estructuras Discretas II')
               
    # Casos Fronteras

    # Prueba 4
     def testInsertObjectiveShortDesc0(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Imposible sacar 5',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('',1,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
                           
    # Prueba 5
     def testInsertObjectiveLongDesc1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Cursar 4 veces',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('A',1,False)
        self.assertTrue(result)
        oObj.deleteObjective('A')
        oBacklog.deleteProduct('Estructuras Discretas II')
                  
    # Prueba 6
     def testInsertObjectiveLongDesc140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Pertece a computacion',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llamare',1,False)
        self.assertTrue(result)
        oObj.deleteObjective(20*'Llamare')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 7
     def testInsertObjectiveLongDesc141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','De 4 creditos',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llamare' + 's',1,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
                
    # Prueba 8
     def testInsertObjectiveIdBacklogInvalid(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Quita horas de sueño',1)
        # Inicio de la prueba.
        oObj   = objective()
        result  =oObj.insertObjective('Estudiar y pasar',0,False)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 9
     def testInsertObjectiveObjTypeInvalid(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Quita horas de sueño',1)
        # Inicio de la prueba.
        oObj   = objective()
        result  =oObj.insertObjective('Estudiar y pasar',1,'Falseee')
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Casos Esquinas
       
    # Prueba 10
     def testInsertObjectiveIdBacklogNoExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Demasiado complicada',1)
        # Inicio de la prueba.
        oObj   = objective()
        result  =oObj.insertObjective('Psar con dos parciales',2,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 11
     def testInsertObjectiveLongDesc140AndIdBacklogNoExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Demasiado pesada',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llamare',3,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 12
     def testInsertObjectiveLongDesc140AndIdBacklogExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Demasiado pesada',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(20*'Llamare',1,False)
        self.assertTrue(result)
        oObj.deleteObjective(20*'Llamare')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 13
     def testInsertObjectiveLongDesc1AndIdBacklogExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Pocos profesores',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('L',1,True)
        self.assertTrue(result)
        oObj.deleteObjective('L')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 14
     def testInsertObjectiveLongDesc1AndIdBacklogNotExistsObjTypeExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Pocos profesores',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('L',7,False)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 15
     def testInsertObjectiveLongDesc0AndIdBacklogExistsObjTypeExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Demasiada pesada',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('',1,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
       
    # Casos Maliciosos
      
    # Prueba 16
     def testInsertNotString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Demasiado pasada',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(4350,1,True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
           
    # Prueba 17
     def testInsertNoneString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia extensa',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(None,1,False)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 18
     def testInsertWrongObjType(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia extensa',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Estudiar bastante',1,'Falseeeee')
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 19
     def testInsertWrongAllParameters(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(13500,0,'True or False')
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 20
     def testInsertNoneAllParameters(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective(None,0,None)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    #############################################      
    #   Suite de Pruebas para searchObjective   #
    #############################################
       
    # Caso Inicial
       
    # Prueba 21 
     def testsearchObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Estudiar con prudencia',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,True)
        oObj.searchObjective('Subir el indice academico')

    # Casos Fronteras
       
    # Prueba 22
     def testsearchObjectiveShortDesc0(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Trabajar 24 horas',1)
        # Inicio de la prueba.        
        oObj   = objective()
        oObj.insertObjective('',1,False)
        result = oObj.searchObjective('')
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
      
    # Prueba 23
     def testsearchObjectiveShortDesc1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Terminar de pasar',1)
        # Inicio de la prueba
        oObj   = objective()
        oObj.insertObjective('A',1,True)
        result = oObj.searchObjective('A')
        self.assertTrue(result)
        oObj.deleteObjective('A')
        oBacklog.deleteProduct('Estructuras Discretas II')
           
    # Prueba 24
     def testsearchObjectiveShortDesc140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Trabajar',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llamare',1,True)
        result = oObj.searchObjective(20*'Llamare')
        self.assertNotEqual(result,[],"Objectivo no encontrado")
        oObj.deleteObjective(20*'Llamare')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 25
     def testsearchObjectiveShortDesc141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Estructura de la materia',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llamare'+'s',1,False)
        result = oObj.searchObjective(20*'Llamare'+'s')
        self.assertFalse(result, "Objective no encontrado")
        oBacklog.deleteProduct('Estructuras Discretas II')
  
    # Caso Normal
      
    # Prueba 26
     def testsearchObjectiveDescNotExist(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Relacion con el profesor',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.searchObjective('Comunicarse via correo electronico')
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
  
    # Casos Maliciosos
       
     # Prueba 27
     def testsearchObjectiveNotString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Vacaciones',1)
        # Inicio de la prueba. 
        oObj   = objective()
        oObj.insertObjective(4350,1,True)
        result = oObj.searchObjective(4350)
        self.assertEqual(result, [],'Objectivo encontrado')
        oBacklog.deleteProduct('Estructuras Discretas II')
 
    # Prueba 28 
     def testSearchNameNoneString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Rapidez',1)
        # Inicio de la prueba.   
        oObj   = objective()
        result = oObj.searchObjective(None)
        self.assertEqual(result, [],'objective encontrado')
        oBacklog.deleteProduct('Estructuras Discretas II')
          
    #############################################      
    #   Suite de Pruebas para searchIdObjective#
    #############################################  
    # Caso Inicial
          
    # Prueba 29  
     def testsearchIdObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,True)
        oObj.searchIdObjective(1)

    # Caso Normal
          
    # Prueba 30 
     def testsearchValidIdObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,False)
        result = oObj.searchIdObjective(1)
        self.assertNotEqual([],result)
        oObj.deleteObjective('Subir el indice academico')
        oBacklog.deleteProduct('Estructuras Discretas II')
              
    # Caso Frontera
          
    # Prueba 31 
     def testsearchIdObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,True)
        result = oObj.searchIdObjective(1)
        self.assertNotEqual([],result)
        oObj.deleteObjective('Subir el indice academico')
        oBacklog.deleteProduct('Estructuras Discretas II')
          
    # Prueba 32
     def testsearchInValidIdObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,False)
        result = oObj.searchIdObjective(5)
        self.assertEqual([],result)
        oObj.deleteObjective('Subir el indice academico')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 33
     def testSearchIdEmpty(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObjective   = objective()
        oObjective.insertObjective('',1,True)
        result = oObjective.searchIdObjective(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        oBacklog.deleteProduct('Estructuras Discretas II')
                    
    # Casos Maliciosos
     
    # Prueba 34
     def testSearchIdString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Pesadillas al dormir',1)
        # Inicio de la prueba.
        oObjective   = objective()
        oObjective.insertObjective(1254,1,False)
        result = oObjective.searchIdObjective('')
        self.assertEqual(result,[],"Elemento Insertado") 
        oBacklog.deleteProduct('Estructuras Discretas II')       

    # Prueba 35
     def testSearchIdNoneString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Disciplina',1)
        # Inicio de la prueba.        
        oObjective   = objective()
        oObjective.insertObjective(None,1,False)
        result = oObjective.searchIdObjective(None)
        self.assertEqual(result,[],"Válido")    
        oBacklog.deleteProduct('Estructuras Discretas II')           
         
    #############################################      
    #   Suite de Pruebas para updateObjective   #
    #############################################  
    # Caso Inicial
      
    # Prueba 36
     def testupdateObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Descripcion',1)
        # Inicio de la prueba.   
        oObj   = objective()
        oObj.insertObjective('Pasar con cinco.',1,True)
        oObj.updateObjective('Pasar con cinco','Pasar con cinco o varios',False)
        oBacklog.deleteProduct('Estructuras Discretas II')  

    # Casos Normales
      
    # Prueba 37
     def testupdateObjectiveDesc(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Universidad',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Estudiar con constancia',1,True)
        result = oObj.updateObjective('Estudiar con constancia','Ir a consultas',False)
        self.assertTrue(result)
        oObj.deleteObjective('Ir a consultas')
        oBacklog.deleteProduct('Estructuras Discretas II')                                  
           
    # Prueba 38     
     def testupdateObjectiveDescNotExist(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        result = oObj.updateObjective('Llegar lo mas pronto posible','Ir por lo seguro',True)
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Casos Fronteras
        
    # Prueba 39
     def testupdateObjectiveLeftLen1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Busqueda',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',1,False)
        result = oObj.updateObjective('A','Buscar al profesor donde esté',True)
        self.assertTrue(result)
        oObj.deleteObjective('Buscar al profesor donde esté')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 40
     def testupdateObjectiveLeftLong1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Busqueda',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Buscar al profesor donde esté',1, False)
        result = oObj.updateObjective('Buscar al profesor donde esté','A',True)
        self.assertTrue(result)
        oObj.deleteObjective('A')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 41         
     def testupdateObjectiveRightLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Muchas materias',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Cursar en paralelo',1,True)
        result = oObj.updateObjective('Cursar en paralelo',140*'T',False)
        self.assertTrue(result)    
        oObj.deleteObjective(140*'T')
        oBacklog.deleteProduct('Estructuras Discretas II')
                                  
    # Prueba 42
     def testupdateObjectiveLeftLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materias',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(140*'T',1, False)
        result = oObj.updateObjective(140*'T','Materias a cursar',True)
        self.assertTrue(result)
        oObj.deleteObjective('Materias a cursar')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Casos Esquinas
       
    # Prueba 43
     def testupdateObjectiveLeftLen1RightLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Verla muchas veces',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',1,False)
        result = oObj.updateObjective('A',70*'Us',True)
        self.assertTrue(result)
        oObj.deleteObjective('A')
        oBacklog.deleteProduct('Estructuras Discretas II') 

    # Prueba 44
     def testupdateObjectiveLeftLen140RightLen140(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materias de computo',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(140*'U',1,True)
        result = oObj.updateObjective(140*'U', 140*'M',False)
        self.assertTrue(result) 
        oObj.deleteObjective(140*'M')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 45
     def testupdateObjectiveLeftLen140RightLen1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Vale cuatro creditos',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llamare',1,True)
        result = oObj.updateObjective(20*'Llamare','M',False)
        self.assertTrue(result)
        oObj.deleteObjective('M')
        oBacklog.deleteProduct('Estructuras Discretas II')
           
    # Prueba 46
     def testupdateObjectiveLeftLen1RightLen1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Profesores',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('X',1,True)
        result = oObj.updateObjective('X','U',False)
        self.assertTrue(result)
        oObj.deleteObjective('U')
        oBacklog.deleteProduct('Estructuras Discretas II') 
           
    # Casos Maliciosos
       
    # Prueba 47
     def testupdateSameName(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Temas de la materia',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Pasar con cinco',1,True)
        result = oObj.updateObjective('Pasar con cinco','Pasar con cinco',False)
        self.assertTrue(result)
        oObj.deleteObjective('Pasar con cinco')
        oBacklog.deleteProduct('Estructuras Discretas II')
           
    # Prueba 48
     def testupdateObjectiveLeftLen1RightLen141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',1,False)
        result = oObj.updateObjective('',20*'Llamare'+'s',True)
        self.assertFalse(result, "Modificación válida") 
        oObj.deleteObjective('A')
        oBacklog.deleteProduct('Estructuras Discretas II')
 
    # Prueba 49
     def testupdateObjectiveLeftLen140RightLen141(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Ruedas',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llamare',1,False)
        result = oObj.updateObjective(20*'Llamare',70*'Ma' + 's',False)
        self.assertFalse(result, "Modificación Válida") 
        oObj.deleteObjective(20*'Llamare')
        oBacklog.deleteProduct('Estructuras Discretas II')
           
    # Prueba 50
     def testupdateObjectiveLeftLen140RightLen0(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia valida',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective(20*'Llamare',1,True)
        result = oObj.updateObjective(20*'Llamare','',False)
        self.assertFalse(result, "Modificación válida") 
        oObj.deleteObjective(20*'Llamare')
        oBacklog.deleteProduct('Estructuras Discretas II')  

    # Prueba 51
     def testupdateObjectiveLeftNoneRightValidString(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Recorrer diagrama',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.updateObjective(None,'Comunicarse via correo electronico',True)
        self.assertFalse(result,"Modificación válida") 
        oBacklog.deleteProduct('Estructuras Discretas II')  
 
    # Prueba 52
     def testupdateObjectiveLeftValidStringRightNone(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Recorrer diagrama',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Pasar con cinco',1,False)
        result = oObj.updateObjective('Pasar con cinco',None,True)
        self.assertFalse(result, "Modificación válida") 
        oObj.deleteObjective('Pasar con cinco')
        oBacklog.deleteProduct('Estructuras Discretas II')    

    #############################################      
    #    Suite de Pruebas para deleteObjective  #
    ############################################# 
       
    # Caso Inicial
       
    # Prueba 53
     def testDeleteObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materia discreta',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Reservar cupo',1,True)
        oObj.deleteObjective('Reservar cupo')
        oBacklog.deleteProduct('Estructuras Discretas II')
           
        # Casos Normales
   
    # Prueba 54
     def testDeleteObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Cursar',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('U',1,False)
        result = oObj.deleteObjective('U')
        self.assertTrue(result)
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Casos Fronteras

    # Prueba 55
     def testDeleteObjective1(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Faltan 2 mas',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('A',1,True)
        result = oObj.deleteObjective('A')
        self.assertTrue(result)
        oBacklog.deleteProduct('Estructuras Discretas II')          
  
    # Prueba 56      
     def testDeleteObjectiveNoObjective(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Materias de cadena',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('yyy',1,True)
        result = oObj.deleteObjective('xxx')
        self.assertFalse(result)
        oObj.deleteObjective('yyy')
        oBacklog.deleteProduct('Estructuras Discretas II')
     
    # Casos Maliciosos
  
    # Prueba 57
     def testDeleteObjectiveInvalid(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.deleteObjective('')
        self.assertFalse(result,"Id no válido")
        oBacklog.deleteProduct('Estructuras Discretas II')
           
    # Prueba 58
     def testDeleteObjectiveNotString(self):
       oBacklog = backlog()
       oBacklog.insertBacklog('Estructuras Discretas II','Determinacion',1)
       # Inicio de la prueba.
       oObj   = objective()
       oObj.insertObjective(12345,1,False)
       result = oObj.deleteObjective(12345)
       self.assertFalse(result,"Id no válido")
       oBacklog.deleteProduct('Estructuras Discretas II')

    # Prueba 59    
     def testDeleteObjectiveNotExist(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.deleteObjective('Terminar de pasar')
        self.assertFalse(result)
        oBacklog.deleteProduct('Estructuras Discretas II')
         
    ###################################################      
    # Suite de Pruebas para VerifyObjectiveTransverse #
    ###################################################

   # Caso Inicial
  
    # Prueba 60
     def testVerifyObjectiveExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Mueve promedio',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Pasar con cinco',1,True)
        transverse = oObj.verifyObjectiveTransverse(1)
        self.assertTrue(transverse)
        oObj.deleteObjective('Pasar con cinco')
        oBacklog.deleteProduct('Estructuras Discretas II')
        
    # Caso Normal
          
    # Prueba 61 
     def testVerifyValidIdObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,False)
        transverse = oObj.verifyObjectiveTransverse(1)
        self.assertTrue(transverse)
        oObj.deleteObjective('Subir el indice academico')
        oBacklog.deleteProduct('Estructuras Discretas II')

    # Caso Frontera
          
    # Prueba 62 
     def testVerifyIdObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Dificil de olvidar',1)
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Subir el indice academico',1,True)
        transverse = oObj.verifyObjectiveTransverse(1)
        self.assertTrue(transverse)
        oObj.deleteObjective('Subir el indice academico')
        oBacklog.deleteProduct('Estructuras Discretas II')
              # Casos Maliciosos
     
    # Prueba 63
     def testVerifyIdStringObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Teoria de conjuntos',1)
        # Inicio de la prueba.
        oObj   = objective()
        oObj.insertObjective('Asegurar trimestre',1,False)
        transverse = oObj.verifyObjectiveTransverse('')
        self.assertFalse([],transverse) 
        oObj.deleteObjective('Asegurar trimestre')
        oBacklog.deleteProduct('Estructuras Discretas II')       

    # Prueba 64
     def testVerifyIdNoneStringObjectiveTransverse(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Estructuras Discretas II','Conocimiento',1)
        # Inicio de la prueba.        
        oObj   = objective()
        oObj.insertObjective('Desarrollar conjuntos',1,False)
        transverse = oObj.searchIdObjective(None)
        self.assertEqual([],transverse)    
        oObj.deleteObjective('Desarrollar conjuntos')
        oBacklog.deleteProduct('Estructuras Discretas II')                   