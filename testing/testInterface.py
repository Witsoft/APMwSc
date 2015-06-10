# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testLogin(self):
        
        driver = self.driver
        
        driver.get("http://localhost:5000/#/")
        elem = driver.find_element_by_name("usuario")
        elem.send_keys("user")
        elem = driver.find_element_by_name("clave")
        elem.send_keys("NewUser@t3st")
        sleep(1)
        elem.send_keys(Keys.RETURN)
        
    def testRegister(self):
        driver = self.driver
        
        driver.get("http://localhost:5000/#/VRegistro")
        elem1 = driver.find_element_by_name("nombre")
        elem1.send_keys("usuario")
        elem1 = driver.find_element_by_name("usuario")
        elem1.send_keys("user")
        elem1 = driver.find_element_by_name("clave")
        elem1.send_keys("NewUser@t3st")
        elem1 = driver.find_element_by_name("clave2")
        elem1.send_keys("NewUser@t3st")
        elem1 = driver.find_element_by_name("correo")
        elem1.send_keys("usuario@gmail.com")
        sleep(1)
        elem1.send_keys(Keys.RETURN)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()