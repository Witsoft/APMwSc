# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from login import *

class TestLogin(unittest.TestCase):

     #############################################      
     #    Suite de Pruebas para validPassword   #
     ############################################

    #Prueba 1: String de longitud 8
    def testValid8Caracteres(self):
        object = login()
        string = "acD34@.R"
        result = object.validPassword(string) 
        self.assertTrue(result)
        
    #Prueba 2: String de longitud 16
    def testValid16Caracteres(self):
        object = login()
        string = "acD34@.RF23pwQsx"
        result = object.validPassword(string) 
        self.assertTrue(result)

    #Prueba 3: String vacío
    def testValidStringVacio(self):
        object = login()
        string = ""
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    #Prueba 4: String muy grande, longitud (2^31)-1
    def testValidMasGrande(self):
        object = login()
        string = ((2**31)-1)*"p"
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    #Prueba Esquina
    
    #Prueba 5: String de longitud 7
    def testValid7Caracteres(self):
        object = login()
        string = "acD34@."
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    #Prueba 6: String de longitud 17
    def testValid17Caracteres(self):
        object = login()
        string = "acD34@.1235ufjD.u"
        result = object.validPassword(string) 
        self.assertFalse(result)
        
    #Prueba Normal
    
    #Prueba 7: String de longitud 1
    def testNoValid1Char(self):
        object = login()
        string = "a"
        result = object.validPassword(string) 
        self.assertFalse(result)
    
   
    #Prueba 8: String de longitud 9
    def testValid9Caracteres(self):
        object = login()
        string = "acD34@.12"
        result = object.validPassword(string) 
        self.assertTrue(result)

        
    #Prueba 9: String de longitud 15
    def testValid15Caracteres(self):
        object = login()
        string = "acD34@.12e87@sh"
        result = object.validPassword(string) 
        self.assertTrue(result)
        
     #############################################      
     #    Suite de Pruebas para length_password  #
     #############################################

    #Prueba Frontera 
   
    #Prueba 10: String de longitud 8
    def testLongitud8Caracteres(self):
        object = login()
        string = "acD34@.R"
        result = object.length_password(string) 
        self.assertEqual(result,8,"Longitud Invalida")
        
    #Prueba 11: String de longitud 16
    def testLongitud16Caracteres(self):
        object = login()
        string = "acD34@.RF23pwQsx"
        result = object.length_password(string) 
        self.assertEqual(result,16,"Longitud Invalida")

    #Prueba 12: String vacío
    def testLongitudStringVacio(self):
        object = login()
        string = ""
        result = object.length_password(string) 
        self.assertEqual(result,0,"Longitud Invalida")
        
    #Prueba 13: String muy grande, longitud (2^31)-1
    def testLongitudMasGrande(self):
        object = login()
        string = ((2**31)-1)*"p"
        result = object.length_password(string) 
        self.assertEqual(result,(2**31)-1,"Longitud Invalida")
        
        
    #Prueba Esquina
    
    #Prueba 14: String de longitud 7
    def testLongitud7Caracteres(self):
        object = login()
        string = "acD34@."
        result = object.length_password(string) 
        self.assertEqual(result,7,"Longitud Invalida")

    #Prueba 15: String de longitud 17
    def testLongitud17Caracteres(self):
        object = login()
        string = "acD34@.1235ufjD.u"
        result = object.length_password(string) 
        self.assertEqual(result,17,"Longitud Invalida")
        
    #Prueba Normal
    
    #Prueba 16: String de longitud 1
    def testLongitud1Char(self):
        object = login()
        string = "a"
        result = object.length_password(string) 
        self.assertEqual(result,1,"Longitud Invalida")
    
    
    #Prueba 17: String de longitud 9
    def testLongitud9Caracteres(self):
        object = login()
        string = "acD34@.12"
        result = object.length_password(string) 
        self.assertEqual(result,9,"Longitud Invalida")
        
    #Prueba 18: String de longitud 15
    def testLongitud15Caracteres(self):
        object = login()
        string = "acD34@.12e87@sh"
        result = object.length_password(string) 
        self.assertEqual(result,15,"Longitud Invalida")
        
     #######################################      
     #    Suite de Pruebas para Encript    #
     #######################################    
    

    #Pruebas Fronteras
    
    #Prueba 19: Clave que cumple con los requisitos y de longitud 8.
    def testClaveValidalong8(self):
        object = login()
        string = "Hola123*"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")
    
    #Prueba 20: Clave que cumple con los requisitos y de longitud 16.
    def testclaveValidalong16(self):
        object = login()
        string = "Estoes1prueb@.Xy"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")   
        
    #Prueba 21: Clave que cumple con los requisitos y de longitud 7.
    #       (Frontera externa del dominio de la funcion)
    def testClaveInvalidalong7(self):
        object = login()
        string = "clav1#7"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")

    #Prueba 22: Clave que cumple con los requisitos y de longitud 17.
    #        (Frontera externa del dominio de la funcion)         
    def testClaveInvalidalong17(self):
        object = login()
        string = "Clavede#17digitos"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
    
    # Pruebas Esquina
    
    #Prueba 23: Clave de longitud 8 con ausencia de mayusculas.
    def testClaveFaltaMayuscula(self):
        object = login()
        string = "hola156#"
        result = object.encript(string)
        self.assertFalse(result,"Clave válida") 
        
    #Prueba 24: Clave de longitud 8 con asusencia de letras.
    def testClaveFaltanLetras(self):
        object = login()
        string = "1234#567."
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
    #Prueba 25: Clave de longitud 8 con ausencia de numeros.
    def testClaveFaltanNumeros(self):
        object = login()
        string = ".abCD$ef"
        result = object.encript(string)
        self.assertFalse(result,"Clave válida") 
        
    #Prueba 26: Clave de longitud 8 con ausencia de caracteres especiales.
    def testClaveFaltanCaracteresEspeciales(self):
        object = login()
        string = "4ald56Z"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
        
    #Pruebas Normales
    
    #Prueba 27: Clave que cumple con los requisitos y de longitud 10.
    def testClaveValidaLargo10(self):
        objeto = login()
        cadena = "h*l4Any$91"
        resultado = objeto.encript(cadena)
        self.assertTrue(resultado,"La clave no es valida.")
       
    #Prueba 28: Clave que no contiene letras minusculas y cumple con los requisitos.
    def testClaveValidaSinMinusculas(self):
        object = login()
        string = "1XZABC@W"
        result = object.encript(string) 
        self.assertTrue(result, "Clave Invalida")
        
    #Prueba 29: Clave de longitud 11 que cumple con los requisitos.
    def testClaveValidaSoloCaracteresEspecialesUnaMayusculaUnNumero(self):
        object = login()
        string = "@*+.1$+#.L%"
        result = object.encript(string) 
        self.assertTrue(result, "Clave válida")
 
    #Prueba 30: Clave de longitud 12 que cumple con los requisitos.
    def testclaveSoloNumerosUnaMayusculaUnCaracterEspecial(self):
        object = login()
        string = "123$4568965P"
        result = object.encript(string) 
        self.assertTrue(result, "Clave Invalida")
        
        
    #Pruebas Maliciosos
    
    #Prueba 31: Clave sin caracteres de ningun tipo.
    def testClaveVacia(self):
        object = login()
        string = ""
        result = object.encript(string)
        self.assertFalse(result,"Clave Valida")
        
    #Prueba 32: Clave con solo 8 espacios.
    def testClaveLargo8ConSoloEspacios(self):
        objeto = login()
        cadena = "        "
        resultado = objeto.encript(cadena)
        self.assertFalse(resultado,"Clave Valida")
        
    #Prueba 33: Clave de longitud 9 que tiene un espacio entre dos palabras.
    def testClaveLargo8ConCaracterEspacio(self):
        objeto = login()
        cadena = "Alifo 13#"
        resultado = objeto.encript(cadena)
        self.assertFalse(resultado,"Clave Valida")
        
    #Prueba 34: Clave de longitud 8 que contiene un caracter \t no imprimible
    def testClaveLargo8ConCaracterNoImprimible(self):
        objeto = login()
        cadena = "Alif13m\t"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Prueba 35: Clave de longitud 8 que contiene solo numeros.       
    def testClaveLargo8ConSoloNumeros(self):
        objeto = login()
        cadena = "56789142"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Prueba 36: Clave de longitud 8 que contiene solo letras minusculas.        
    def testClaveLargo8ConSoloLetras(self):
        objeto = login()
        cadena = "abcdefgh"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
    #Prueba 37: Clave de longitud 8 que contiene solo letras mayusculas.        
    def testClaveLargo8ConSoloLetrasMayusculas(self):
        objeto = login()
        cadena = "ABCDEFGH"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Prueba 38: Clave de longitud 8 que contiene solo caracteres especiales.
    def testClaveLargo8ConSoloCaracteres(self):
        objeto = login()
        cadena = "#$.*+@++"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
    #Prueba 39: Clave inválida con caracteres diferentes a los solicitados 
    def testClaveInvalidaCaractereSIncorrectos(self):
        objeto = login()
        cadena = "Gft%u!i56*"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
            
     #############################################      
     #    Suite de Pruebas para check_password  #
     #############################################
 
    #Pruebas Fronteras
    
    #Prueba 40: La clave de encript y la nueva clave a verificar coinciden.
    #        (Ambas claves son de largo 8)
    def testHashValidoCorrespodeAClaveCorrectaLong8(self):
        object = login()
        password = "1XZABC@W"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
    #Prueba 41: La clave de encript y la nueva clave a verificar coinciden.
    #        (Ambas claves son de largo 16)
    def testHashValidoCorrespodeAClaveCorrectaLong16(self):
        object = login()
        password = "1abcdXZABC@W123@"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
    #Prueba 42: La clave de encript y la nueva clave (invalida) a verificar no coinciden.
    #        (Ambas claves son de largo 8)
    def testHashValidoClaveInvalidaLargo8(self):
        object = login()
        password = "abcd@123" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Prueba 43: La clave de encript y la nueva clave (invalida) a verificar no coinciden.
    #        (Ambas claves son de largo 16)
    def testHashValidoClaveInvalidaLargo16(self):
        object = login()
        password = "afxx@123987pa.+*" 
        passwordValid = "AB*.+1254aCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
        
    #Pruebas Normales
    
    #Prueba 44: La clave de encript y la nueva clave a verificar coinciden.
    #        (Ambas claves son de largo 15)
    def testHashValidoCorrespondeAClaveCorrectaLong15(self):
        object = login()
        password = "fggAaksh#123.s1"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
    #Prueba 45: La clave de encript y la nueva clave a verificar coinciden.
    #        (Ambas claves son de largo 9)
    def testHashValidoCorrespondeAClaveCorrectaLong9(self):
        object = login()
        password = "fgAh#1.s1"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")


    #Prueba Esquina
    
    #Prueba 46: Clave de longitud 9, con un hash de una clave diferente a la anterior 
    #        por solo una letra
    def testHashyClaveDiferentePorUnaLetra(self):
        object = login()
        password = "1ZA3BC@Ws"
        passwordInvalid = "1ZA3C@Ws" 
        encriptar = object.encript(passwordInvalid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Prueba 47: Clave de longitud 7 con su hash correspondiente
    def testHashValidoClaveLong7(self):
        object = login()
        password = "xYz2#15" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
     
     #Prueba 48: Clave de longitud 17 con su hash correspondiente
    def testHashValidoClaveLong17(self):
        object = login()
        password = "xYz2#15gsgshshsah" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Prueba Malicioso
    
    #Prueba 49: Clave sin caracteres de ningún tipo, con hash de una clave válida
    def testHashValidoClaveVacia(self):
        object = login()
        password = "" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Prueba 50: Clave de string vacio, con hash de una clave válida
    def testHashValidoClaveConSoloEspacios(self):
        object = login()
        password = "        " 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")     

#Fin de Casos Login 