# -*- coding: utf-8 -*-

from selenium                       import webdriver
from selenium.webdriver.common.by   import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui  import Select
from selenium.common.exceptions     import NoSuchElementException
from selenium.common.exceptions     import NoAlertPresentException
from time                           import sleep

import unittest, time, re
import sys

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog   import *
from user      import *
from role      import * 
from accions   import *
from objective import *
from userHistory import *


class CasosPrueba(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_casos_prueba(self):
        driver = self.driver
        
        # Eliminamos los datos de prueba introducidos
        
        oBacklog   = backlog()
        oUser      = user()
        oActor     = role()
        oAccion    = accions()
        oObjective = objective()
        oHistory   = userHistory()
        
        result    = oBacklog.findName('Taxi Seguro')
        idBacklog = result[0].BL_idBacklog
        result    = oUser.deleteUser('usuario')
        print('Eliminar usuario',result)
 #       result    = oActor.deleteActor('Actor 1',idBacklog)
  #      print('Eliminar Actor',result)
        result    = oAccion.deleteAccion('Accion',idBacklog)
        print('Eliminar Accion',result)
        result    = oAccion.deleteAccion('Accion 1',idBacklog)
        print('Eliminar Accion',result) 
        result    = oObjective.deleteObjective('Objetivo2',idBacklog)
        print('Eliminar obj',result)  
        result    = oObjective.deleteObjective('Objetivo1',idBacklog)
        print('Eliminar obj',result) 
        result    = oBacklog.deleteProduct('Producto 1')
        print('Eliminar obj',result) 
        result   = oHistory.deleteUserHistory('H1')
         
              
        # Casos de prueba para registrar un usuario en la aplicacion.
        
        driver.get(self.base_url + "/#/VRegistro")
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Usuario Prueba")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("usuario")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("1234.ABC")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("1234.ABC")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuarioP@gmail.com")
        Select(driver.find_element_by_id("fUsuario_actorScrum")).select_by_visible_text("Dueño de producto")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Casos de prueba para el inicio de sesion de un usuario.
        
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("usuario")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("1234.ABC")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Caso de prueba para Crear categorias
        driver.find_element_by_link_text(u"Categorías de tareas").click()
        driver.find_element_by_id("fCategoria_nombre").clear()
        driver.find_element_by_id("fCategoria_nombre").send_keys("Categoria1")
        driver.find_element_by_id("fCategoria_peso").clear()
        driver.find_element_by_id("fCategoria_peso").send_keys("2")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()

        
        # Casos de prueba para agregar Producto
        driver.find_element_by_link_text("+Producto").click()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("Producto 1")
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("Nuevo Producto")
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Alta/Media/Baja")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)


        # Casos de prueba ver datos de un producto.
        sleep(2)
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[3]").click()
        sleep(2)
        
        # Caso de prueba para crear un actor.

#         driver.find_element_by_link_text("+Actor").click()       
#         driver.find_element_by_id("fActor_nombre").clear()
#         driver.find_element_by_id("fActor_nombre").send_keys("Actor1")
#         sleep(2)
#         driver.find_element_by_id("fActor_descripcion").clear()
#         driver.find_element_by_id("fActor_descripcion").send_keys("Nuevo actor")
#         sleep(2)
#         driver.find_element_by_xpath("//button[@type='submit']").click()
#         sleep(3)
#         
#         # Caso de prueba para Modificar actor.
         
#         driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[4]").click()
#         driver.find_element_by_name("html").click()
#         driver.find_element_by_id("taHtmlElement").clear()
#         driver.find_element_by_id("taHtmlElement").send_keys("Nuevo actor 1")
#         sleep(1)
#         driver.find_element_by_xpath("//button[@type='submit']").click()
#         sleep(1)
#         driver.find_element_by_link_text("Salir").click()
#         sleep(1)
#         

#        driver.find_element_by_css_selector("button.navbar-toggle").click()

        # Caso de prueba para crear una accion.
        sleep(3)
        driver.find_element_by_link_text("+Accion").click()
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("Accion")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
          
        # Caso de prueba para ver la accion.
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[2]").click()
        sleep(3)
        
        # Caso de prueba para modificar la accion.
        #driver.get(self.base_url + "/#/VAccion/"+str(idAccion))
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("Accion 1")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
   
#        # Caso de prueba para ver la accion
#         driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
#         sleep(3)     
#         
#         # Caso de prueba para eliminar accion
#         driver.find_element_by_link_text("-accion").click()
#         sleep(2)

        # Caso de prueba para crear un objetivo.
        driver.find_element_by_link_text("+Objetivo").click()
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("Objetivo2")
        sleep(2)
        Select(driver.find_element_by_id("fObjetivo_transversal")).select_by_visible_text("No")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Caso de prueba para ver el Objetivo
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[3]").click()
        sleep(3)
        
        # Caso de prueba para modificar el objetivo.
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("Objetivo1")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
#         # Caso de prueba para ver el objetivo
#         driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
#         sleep(3)     
#         
#         # Caso de prueba para eliminar el objetivo
#         driver.find_element_by_link_text("-objetivo").click()
#         sleep(2)

        # Caso para agregar Historia_Epica
        driver.find_element_by_link_text("Historias").click()
        sleep(2)
        driver.find_element_by_link_text("Crear").click()
        sleep(2)
        driver.find_element_by_id("fHistoria_codigo").clear()   
        driver.find_element_by_id("fHistoria_codigo").send_keys("H1")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fHistoria_actores | label=Actor1]]
        sleep(2)
        Select(driver.find_element_by_id("fHistoria_actores")).select_by_visible_text("Actor1")
        sleep(2)
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Opcional")
        sleep(2)
        Select(driver.find_element_by_id("fHistoria_accion")).select_by_visible_text("Accion 1")
        sleep(2)
        Select(driver.find_element_by_id("fHistoria_objetivos")).select_by_visible_text("Objetivo1")
        sleep(2)
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fHistoria_objetivos | label=Objetivo1]]
        Select(driver.find_element_by_id("fHistoria_prioridad")).select_by_visible_text("Alta")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)

        # Caso para modificar historia
        driver.find_element_by_link_text("Detalles").click()
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Obligatoria")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Creamos Historia
     #   driver.find_element_by_link_text("Historias").click()
     #   sleep(2)
        driver.find_element_by_link_text("Crear").click()
        sleep(2)
        driver.find_element_by_id("fHistoria_codigo").clear()   
        driver.find_element_by_id("fHistoria_codigo").send_keys("H2")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fHistoria_actores | label=Actor1]]
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_super")).select_by_visible_text("H1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_actores")).select_by_visible_text("Actor1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Obligatoria")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_accion")).select_by_visible_text("Accion 1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_objetivos")).select_by_visible_text("Objetivo1")
        sleep(1)
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fHistoria_objetivos | label=Objetivo1]]
        Select(driver.find_element_by_id("fHistoria_prioridad")).select_by_visible_text("Alta")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)

        
#        driver.find_element_by_css_selector("button.navbar-toggle").click()
#        driver.find_element_by_link_text("Salir").click()


        
        # Eliminamos los datos de prueba introducidos
        
        oBacklog = backlog()
        oUser    = user()
        oActor   = role()
        
        
        result    = oBacklog.findName('Taxi Seguro')
        idBacklog = result[0].BL_idBacklog
        result    = oUser.deleteUser('usuario')
        print('Eliminar usuario',result)
        result    = oActor.deleteActor('Actor 1',idBacklog)
        print('Eliminar Actor',result)
        result    = oAccion.deleteAccion('Accion 1',idBacklog)
        print('Eliminar Accion',result)
        
        # Cerramos la aplicacion.

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
     
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
