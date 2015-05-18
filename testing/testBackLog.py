# -*- coding: utf-8 -*-. 
'''
Fecha:    14/05/2015.
'''

import unittest

import os
import sys

# Ruta que permite utilizar el módulo py
sys.path.append('../')

from backLog import *

class TestclsBackLog(unittest.TestCase):
    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################

    # Caso Inicial
    
    # Prueba 1
    def test1InsertExists(self):
        newBL = clsBackLog("Toyota Corola")
        session.add(newBL)
        session.commit()
        
        newBL = clsBackLog("Pizza")
        session.add(newBL)
        session.commit()

        newBL = clsBackLog("Taxi Hotel")
        session.add(newBL)
        session.commit()
        
        newBL = clsBackLog("Entrada cine")
        session.add(newBL)
        session.commit()

        newBL = clsBackLog("Celular")
        session.add(newBL)
        session.commit()
        
    