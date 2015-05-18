# -*- coding: utf-8 -*-. 
'''
Fecha:    14/05/2015.
'''

import unittest

import os
import sys

# Ruta que permite utilizar el módulo objective.py
sys.path.append('../app/scrum')
from model import *
from backLog import *

class TestclsBackLog(unittest.TestCase):
    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################

    # Caso Inicial
    
    # Prueba 1
    def test1InsertExists(self):
        newBL = clsBackLog("Toyota Corola","Automotriz")
        db.session.add(newBL)
        db.session.commit()

        
        newBL = clsBackLog("Pizza","Restaurante")
        db.session.add(newBL)
        db.session.commit()

        newBL = clsBackLog("Taxi Hotel","Hoteleria")
        db.session.add(newBL)
        db.session.commit()
        
        newBL = clsBackLog("Entrada cine","Cines")
        db.session.add(newBL)
        db.session.commit()

        newBL = clsBackLog("Celular","Operadoras Moviles")
        db.session.add(newBL)
        db.session.commit()
        
    