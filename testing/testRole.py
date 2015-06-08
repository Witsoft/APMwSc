# -*- coding: utf-8 -*-. 

import unittest

from roleDummy import *

class TestActors(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertActor       #
    #############################################
    
    # Caso Inicial
 
    # Prueba 1
    def testInsertExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba. 
        aAct = role()
        aAct.insertActor('Luchador','Pelea descomunalmente',1)
        aAct.deleteActor('Luchador')
        aBacklog.deleteProduct('Personajes de juego')    
         
    # Casos Normales
           
    # Prueba 2 
    
    def testInsertElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Mago','Pura magia de cualquier tipo',1)
        self.assertTrue(result)
        aAct.deleteActor('Mago')
        aBacklog.deleteProduct('Personajes de juego')
          
    # Prueba 3
    def testInsertRepeatedElement(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Estratega','Diseña patron de ataque',1)
        result1 = aAct.insertActor('Estratega','Diseña patron de ataque',1)
        self.assertFalse(result1, "Elemento insertado")
        aAct.deleteActor('Estratega')
        aBacklog.deleteProduct('Personajes de juego') 
    
    # Casos Fronteras
      
    # Prueba 4
    def testInsertLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(10*'Tidus','Diseño de Traje',1)
        self.assertTrue(result)
        aAct.deleteActor(10*'Tidus')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 5
    def testInsertLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(10*'Tidus' + '1','FFX',1) 
        self.assertFalse(result, "Elemento insertado.")
        aBacklog.deleteProduct('Personajes de juego') 
             
    # Prueba 6
    def testInsertShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('','Atuendos',1)
        self.assertFalse(result, "Elemento insertado.") 
        aBacklog.deleteProduct('Personajes de juego') 
              
    # Prueba 7
    def testInsertLongName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('T','Signo',1)
        self.assertTrue(result)
        aAct.deleteActor('T')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 8
    def testInsertDescriptionLong1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1) 
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('Rinoa','o',1)
        self.assertTrue(result)
        aAct.deleteActor('Rinoa')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 9
    def testInsertDescriptionLong140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Diseñador', 70*'La',1)
        self.assertTrue(result)
        aAct.deleteActor('Diseñador')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 10
    def testInsertDescriptionLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('Actor','',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 
       
    # Prueba 11
    def testInsertDescriptionLong141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Ladron', 70*'La' + 'a',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Casos Esquinas
    
    # Prueba 12
    def testInsertMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
       # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('S','D',1)
        self.assertTrue(result)
        aAct.deleteActor('S')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 13
    def testInsertMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor(10*'Tidus', 70*'Lo',1)
        self.assertTrue(result)
        aAct.deleteActor(10*'Tidus')
        aBacklog.deleteProduct('Personajes de juego') 
        
    # Prueba 14
    def testInsertActorLong0DescriptionLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor('','',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 15
    def testInsertActorLong51DescriptionLong141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.insertActor(10*'Cloud' + 's', 70*'Lo' + 'l',1)
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 

    # Casos Maliciosos
      
    # Prueba 16
    def testInsertNotActorString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(1254,'No definido',1)
        self.assertFalse(result,"Elemento insertado")
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 17
    def testInsertActorNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(None,'No definido',1)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 18
    def testInsertDescriptionNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Mago',None,1)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Personajes de juego')
          
    # Prueba 19
    def testInsertNotIDInteger(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Cloud','Enigmas de juego','Cancion')
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 20
    def testInsertActorDescriptionIdNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor(None,None,None)
        self.assertFalse(result,"No válido.")
        aBacklog.deleteProduct('Personajes de juego') 
                  
    # Prueba 21
    def testInsertId0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego', 'Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.insertActor('Luchador','Golpe contundente',0)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Personajes de juego')          
         
    #############################################      
    #  Suite de Pruebas para findNameActor      #
    #############################################
     
    # Caso Inicial
     
    # Prueba 22 
    def testFindNameExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Cloud','Drama en el grupo',1)
        aAct.findNameActor('Cloud')
        aAct.deleteActor('Cloud')
        aBacklog.deleteProduct('Personajes de juego') 
            
    # Casos Fronteras
     
    # Prueba 23
    def testFindNameEmpty(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor('')
        self.assertEqual(result,[], "Expresión inválida.")
        aBacklog.deleteProduct('Personajes de juego')
           
    # Prueba 24
    def testFindNameShortName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('T','No definido',1)
        result = aAct.findNameActor('T')
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor('T')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 25
    def testFindNameLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(10*'Tidus','As del juego',1)
        result = aAct.findNameActor(10*'Tidus')
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor(10*'Tidus')
        aBacklog.deleteProduct('Personajes de juego') 
           
    # Prueba 26
    def testFindNameLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(10*'Cloud' + 's') 
        self.assertEqual(result,[],"Cadena no válida")
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Casos Maliciosos
     
    # Prueba 27
    def testFindNameNotString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(1254)
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Personajes de juego') 
      
    # Prueba 28
    def testFindNameNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.findNameActor(None)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Personajes de juego') 

    #############################################      
    #       Suite de Pruebas para updateActor   #
    #############################################   
     
    # Caso Inicial
     
    # Prueba 29
    def testUpdateActorExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Angelo','Atacante de batalla',1)
        aAct.updateActor('Angelo','Eden','Atacante de magia')
        aAct.deleteActor('Eden')
        aBacklog.deleteProduct('Personajes de juego') 
   
    # Casos Normales
     
    #Prueba 30
    def testUpdateActor(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Zell','Combatiente nato',1)
        result = aAct.updateActor('Zell','Lulu','Usuario de la magia negra')
        self.assertTrue(result)
        aAct.deleteActor('Lulu')
        aBacklog.deleteProduct('Personajes de juego') 
          
    # Casos Fronteras
      
    # Prueba 31
    def testUpdateActorLeftLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('X','No definido',1)
        result = aAct.updateActor('X','Estratega','Analisa de la situacion')
        self.assertTrue(result)
        aAct.deleteActor('Estratega')
        aBacklog.deleteProduct('Personajes de juego') 
    
    # Prueba 32         
    def testUpdateActorRightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Cloud','N',1)
        result = aAct.updateActor('Cloud','Tidus','Jugador y peleador')
        self.assertTrue(result)
        aAct.deleteActor('Tidus')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 33         
    def testUpdateActorRightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Dragon','Causa serios problemas',1)
        result = aAct.updateActor('Dragon',50*'R','No definido')
        self.assertTrue(result)
        aAct.deleteActor(50*'R')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 34
    def testUpdateActorLeftLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(50*'A','No definido',1)
        result = aAct.updateActor(50*'A','Yuna', 'Usuario de magia blanca')
        self.assertTrue(result)
        aAct.deleteActor('Yuna')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 35
    def testUpdateActorDescriptionLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Sora','Maestro de la espada',1)
        result = aAct.updateActor('Sora','Ares', 'N')
        self.assertTrue(result)
        aAct.deleteActor('Ares')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 36
    def testUpdateActorDescriptionLen140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Mickey','Rey enigmatico',1)
        result = aAct.updateActor('Mickey','Hercules', 70* 'Nw')
        self.assertTrue(result)
        aAct.deleteActor('Hercules')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 37
    def testUpdateActorDescriptionLen0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Pastor','Una pala manejando',1)
        result = aAct.updateActor('Pastor','Mago', '')
        self.assertFalse(result)
        aAct.deleteActor('Pastor')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 38         
    def testUpdateActorRightLen51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Cerbero','Ataca por donde sea',1)
        result = aAct.updateActor('Cerbero',50*'P' + 'a','No definido')
        self.assertFalse(result)
        aAct.deleteActor('Cerbero')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 39         
    def testUpdateActorLeftLen51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'Sc' + 'a','No definido',1)
        result = aAct.updateActor(25*'Sc' + 'a','Atomo','Absorber entorno')
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 

    # Casos Esquinas
     
    # Prueba 40
    def testUpdateActorLeftLen1RightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('O','No definido',1)
        result = aAct.updateActor('O',25*'Pq','No definido')
        self.assertTrue(result) 
        aAct.deleteActor(25*'Pq')
        aBacklog.deleteProduct('Personajes de juego') 
        
    # Prueba 41
    def testUpdateActorLeftLen50RightLen50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'Us','No definido',1)
        result = aAct.updateActor(25*'Us', 25*'Ma','No definido')
        self.assertTrue(result)
        aAct.deleteActor(25*'Ma') 
        aBacklog.deleteProduct('Personajes de juego') 
 
    # Prueba 42
    def testUpdateActorLeftLen50RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'LL','No definido',1)
        result = aAct.updateActor(25*'LL','E','No definido')
        self.assertTrue(result)
        aAct.deleteActor('E')
        aBacklog.deleteProduct('Personajes de juego')  
 
    # Prueba 43
    def testUpdateActorLeftLen1RightLen1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('V','No definido',1)
        result = aAct.updateActor('V','G','No definido')
        self.assertTrue(result)
        aAct.deleteActor('G') 
        aBacklog.deleteProduct('Personajes de juego') 
 
    # Prueba 44
    def testUpdateActorLeftLen1RightLen50Description1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('J','No definido',1)
        result = aAct.updateActor('J',25*'fr','No definido')
        self.assertTrue(result)
        aAct.deleteActor(25*'fr')
        aBacklog.deleteProduct('Personajes de juego')  

    # Prueba 45
    def testUpdateActorLeftLen1RightLen50Description140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('k','No definido',1)
        result = aAct.updateActor('k',25*'gb',70*'mo')
        self.assertTrue(result) 
        aAct.deleteActor(25*'gb')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 46
    def testUpdateActorLeftLen50RightLen50Description140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor(25*'li','No definido',1)
        result = aAct.updateActor(25*'li', 25*'IL',70*'de')
        self.assertTrue(result)
        aAct.deleteActor(25*'IL') 
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 47
    def testUpdateActorLeftLen1RightLen1Description1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('s','No definido',1)
        result = aAct.updateActor('s','t','d')
        self.assertTrue(result)
        aAct.deleteActor('t') 
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 48
    def testUpdateActorLeftLen51RightLen51Description141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(25*'se' + 'a',25*'lo'+ 'b',70*'de' + 'a')
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 

    # Casos Maliciosos
          
    # Prueba 49
    def testUpdateActorLeftLen0RightLen51Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor('',25*'Pi' + 'p','')
        self.assertFalse(result, "Modificación válida")
        aBacklog.deleteProduct('Personajes de juego')  
  
    # Prueba 50
    def testUpdateActorLeftLen51RightLen0Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(25*'Ma'+ 's','','')
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 51
    def testUpdateActorLeftNoneRightValidString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(None,'Cloud','Drama')
        self.assertFalse(result,"Modificación válida") 
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 52
    def testUpdateActorLeftValidStringRightNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Ente Artema','Magia oscura',1)
        result = aAct.updateActor('Ente Artema',None,'No definido')
        self.assertFalse(result, "Modificación válida")
        aAct.deleteActor('Ente Artema') 
        aBacklog.deleteProduct('Personajes de juego') 
          
    # Prueba 53
    def testUpdateActorLeftValidStringRightDescriptionNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Vahn','Conductor de Zoids',1)
        result = aAct.updateActor('Vahn','Fine',None)
        self.assertFalse(result, "Modificación válida")
        aAct.deleteActor('Vahn')
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 54
    def testUpdateActorNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor(None,None,None)
        self.assertFalse(result, "Modificación válida")
        aBacklog.deleteProduct('Personajes de juego')  
          
    # Prueba 55
    def testUpdateActorLeft0Right0Description0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.updateActor('','','')
        self.assertFalse(result, "Modificación válida") 
        aBacklog.deleteProduct('Personajes de juego')  
         
    #############################################      
    #       Suite de Pruebas para deleteActor   #
    #############################################   
 
    # Caso Inicial
     
    # Prueba 56
    def testDeleteActorExists(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Tifa','Peleadora al extremo',1)
        aAct.deleteActor('Tifa')
        aBacklog.deleteProduct('Personajes de juego') 

     # Casos Normales
 
     # Prueba 57
    def testDeleteLongName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Team MemberTeam MemberTeam MemberTeam MemberTeam M','Mucha longitud',1)
        result = aAct.deleteActor('Team MemberTeam MemberTeam MemberTeam MemberTeam M')
        self.assertTrue(result)
        aBacklog.deleteProduct('Personajes de juego') 

     # Prueba 58
    def testDeleteLongName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(10*'Cloud' + 's')
        self.assertFalse(result, "Elemento insertado.")
        aBacklog.deleteProduct('Personajes de juego')  
             
    # Prueba 59
    def testDeleteShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor('')
        self.assertFalse(result, "Elemento insertado") 
        aBacklog.deleteProduct('Personajes de juego') 
              
    # Prueba 60
    def testDeleteLongName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('T','No definido',1)
        result = aAct.deleteActor('T')
        self.assertTrue(result)
        aBacklog.deleteProduct('Personajes de juego') 
                  
    # Casos Esquinas
    
    # Prueba 61
    def testDeleteMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor('S','No definido',1)
        result = aAct.deleteActor('S')
        self.assertTrue(result)
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 62
    def testDeleteMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor(25*'me', 'No definido',1)
        result = aAct.deleteActor(25*'me')
        self.assertTrue(result)
        aBacklog.deleteProduct('Personajes de juego') 
        
    # Prueba 63
    def testDeleteActorName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.deleteActor('')
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 64
    def testDeleteActorLong51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        result = aAct.deleteActor(25*'ma'+'p')
        self.assertFalse(result)
        aBacklog.deleteProduct('Personajes de juego') 

    # Casos Maliciosos
      
    # Prueba 65
    def testDeleteNotActorString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(1254)
        self.assertFalse(result,"Elemento insertado")
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 66
    def testDeleteActorNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        result = aAct.deleteActor(None)
        self.assertFalse(result,"No válido")
        aBacklog.deleteProduct('Personajes de juego') 
         
    # Prueba 67
    def testDeleteDescriptionNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct   = role()
        aAct.insertActor('Mago',None,1)
        result = aAct.deleteActor('Mago')
        self.assertFalse(result,"No válido.")
        aBacklog.deleteProduct('Personajes de juego')
                   
    #############################################      
    #       Suite de Pruebas para findIdActor   #
    #############################################

    # Caso Inicial
   
    # Prueba 68  
    def testFindIdExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba.
        aAct = role()
        aAct.insertActor('Mago','Destruye con magia',1)
        aAct.findIdActor(1)
        aBacklog.deleteProduct('Personajes de juego') 
  
    # Caso Normal
     
    # Prueba 69
    def testFindIdTrue(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba. 
        aAct   = role()
        aAct.insertActor('Aeris','Anciano procedente de hace años',1)
        result = aAct.findIdActor(1)        
        self.assertNotEqual(result,[],"Elemento no encontrado")
        aAct.deleteActor('Aeris')
        aBacklog.deleteProduct('Personajes de juego') 

    # Prueba 70
    def testFindIdNoActor(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor(2)
        self.assertEqual(result,[],"Elemento no encontrado")
        aBacklog.deleteProduct('Personajes de juego') 

    # Caso Frontera
     
    # Prueba 71
    def testFindIdEmpty(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        aBacklog.deleteProduct('Personajes de juego')
            
    # Casos Maliciosos
     
    # Prueba 72
    def testFindIdString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor('')
        self.assertEqual(result,[],"Elemento Insertado") 
        aBacklog.deleteProduct('Personajes de juego') 
      
    # Prueba 73
    def testFindIdNoneString(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Personajes de juego','Diseño de roles',1)
        # Inicio de la prueba. 
        aAct   = role()
        result = aAct.findIdActor(None)
        self.assertEqual(result,[],"Válido")    
        aBacklog.deleteProduct('Personajes de juego') 