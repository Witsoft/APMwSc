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
        newBL = clsBackLog("Toyota Corola")
        db.session.add(newBL)
        db.session.commit()

        
        newBL = clsBackLog("Restaurante")
        db.session.add(newBL)
        db.session.commit()

        newBL = clsBackLog("Hoteleria")
        db.session.add(newBL)
        db.session.commit()
        
        newBL = clsBackLog("Cines")
        db.session.add(newBL)
        db.session.commit()

        newBL = clsBackLog("Celular")
        db.session.add(newBL)
        db.session.commit()
        
    