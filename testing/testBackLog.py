# -*- coding: utf-8 -*-. 

import unittest

import os
import sys

from modelDummy   import *
from backLogDummy import *

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
        
    