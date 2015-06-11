'''
Created on 7/6/2015

@author: sahid
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        
        driver.get("http://localhost:5000/#/VRegistro")
        elem1 = driver.find_element_by_name("nombre")
        elem1.send_keys("Aldrix")
        elem1 = driver.find_element_by_name("usuario")
        elem1.send_keys("marfil")
        elem1 = driver.find_element_by_name("clave")
        elem1.send_keys("S@hir93")
        elem1 = driver.find_element_by_name("clave2")
        elem1.send_keys("S@hir93")
        elem1 = driver.find_element_by_name("correo")
        elem1.send_keys("aldrix.marfil@gmail.com")
        #sleep(6)
        #elem = driver.find_element_by_name("button.btn.btn-perso.btn-lg.btn-block")
        elem1.send_keys(Keys.RETURN)
        
        
        #driver.get("http://localhost:5000/#/")
        #elem = driver.find_element_by_name("usuario")
        #elem.send_keys("sahidr")
        #elem = driver.find_element_by_name("clave")
        #elem.send_keys("S@hir93")
        #elem.send_keys(Keys.RETURN)
        #self.assertIn("scrum", driver.title)

        

        #assert "No results found." not in driver.page_source



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()