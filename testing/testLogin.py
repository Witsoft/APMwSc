# -*- coding: utf-8 -*-. 

import unittest

from loginDummy import *


class clsLoginTester(unittest.TestCase):

    def testclsLoginEncriptFalse(self):
        aclsLogin = clsLogin() 
     
        #Caso malicia
        c0 = ""         #longitud 0
        self.assertEqual("", aclsLogin.encript(c0))
       
        c1 = "M3A0$d8"  #longitud 7    caracteres validos
        self.assertEqual("", aclsLogin.encript(c1))
        
        c2 = "_ko8E{}"  #longitud 7    caracteres invalidos
        self.assertEqual("", aclsLogin.encript(c2))
        
        c3 = "#.LpeW@"  #longitud 7    sin digitos
        self.assertEqual("", aclsLogin.encript(c3))
        
        c4 = "$s@kpf*"  #longitud 7    sin digitos ni mayusculas
        self.assertEqual("", aclsLogin.encript(c4))
        
        c5 = "fToesQp"  #longitud 7    sin digitos ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c5))
        
        c6 = "d#6fo@3"  #longitud 7    sin mayusculas
        self.assertEqual("", aclsLogin.encript(c6))
        
        c7 = "irj120k"  #longitud 7    sin mayusculas ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c7))
        
        c8 = "1F09ir2"  #longitud 7    sin caracteres especiales
        self.assertEqual("", aclsLogin.encript(c8))
        
        c9 = "fpeosnq"  #longitud 7    sin los requisitos minimos
        self.assertEqual("", aclsLogin.encript(c9))
        
        c10 = "C*@d$.3Aca#a3aE+$"    #longitud 17    caracteres validos
        self.assertEqual("", aclsLogin.encript(c10))
        
        c11 = "(-:cpsm09JK\?|{=]"    #longitud 17    caracteres invalidos
        self.assertEqual("", aclsLogin.encript(c11))
        
        c12 = "#.LpeW@+lnkzA.@yl"    #longitud 17    sin digitos
        self.assertEqual("", aclsLogin.encript(c12))
        
        c13 = "k*sdj+fwei..weh@#"    #longitud 17    sin digitos ni mayusculas
        self.assertEqual("", aclsLogin.encript(c13))
        
        c14 = "MJiqJwieALniDGRou"    #longitud 17    sin digitos ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c14))
        
        c15 = "@#$+zj*ic71c22x.."    #longitud 17    sin mayusculas
        self.assertEqual("", aclsLogin.encript(c15))
        
        c16 = "i3u48712384uioiqm"    #longitud 17    sin mayusculas ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c16))
        
        c17 = "JFFefn93kNJK43672"    #longitud 17    sin caracteres especiales
        self.assertEqual("", aclsLogin.encript(c17))
        
        c18 = "00000000000000000"    #longitud 17    sin los requisitos minimos    
        self.assertEqual("", aclsLogin.encript(c18))    
        
        c20 = "_ko8E{?}"  #longitud 8    caracteres invalidos
        self.assertEqual("", aclsLogin.encript(c20))
        
        c21 = "#.LpeWr@"  #longitud 8    sin digitos
        self.assertEqual("", aclsLogin.encript(c21))
        
        c22 = "$s@kp.f*"  #longitud 8    sin digitos ni mayusculas
        self.assertEqual("", aclsLogin.encript(c22))
        
        c23 = "fToesQhp"  #longitud 8    sin digitos ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c23))
        
        c24 = "d#6fo@.3"  #longitud 8    sin mayusculas
        self.assertEqual("", aclsLogin.encript(c24))
        
        c25 = "irj1290k"  #longitud 8    sin mayusculas ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c25))
        
        c26 = "1F09irA2"  #longitud 8    sin caracteres especiales
        self.assertEqual("", aclsLogin.encript(c26))
        
        c27 = "fpeosrnq"  #longitud 8    sin los requisitos minimos
        self.assertEqual("", aclsLogin.encript(c27))
                                  
               
        c29 = "_k?¡[ñ]<z]>o8E{}"  #longitud 16    caracteres invalidos
        self.assertEqual("", aclsLogin.encript(c29))
        
        c30 = "#.LpeWo@lEdff@#*"  #longitud 16    sin digitos
        self.assertEqual("", aclsLogin.encript(c30))
        
        c31 = "$s@kpf#.*rthq+f*"  #longitud 16    sin digitos ni mayusculas
        self.assertEqual("", aclsLogin.encript(c31))
        
        c32 = "fToesQpUGndpwder"  #longitud 16    sin digitos ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c32))
        
        c33 = "d#6fo@3$.+*t34do"  #longitud 16    sin mayusculas
        self.assertEqual("", aclsLogin.encript(c33))
        
        c34 = "irj120k720fnsl0j"  #longitud 16    sin mayusculas ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c34))
        
        c35 = "1F09ir2UNdpw3450"  #longitud 16    sin caracteres especiales
        self.assertEqual("", aclsLogin.encript(c35))
        
        c36 = "fpeosnqjdoengosq"  #longitud 16    sin los requisitos minimos
        self.assertEqual("", aclsLogin.encript(c36))
                
        c38 = "_ko8E{?}¬"  #longitud 9    caracteres invalidos
        self.assertEqual("", aclsLogin.encript(c38))
        
        c39 = "#.LpeWr@t"  #longitud 9    sin digitos
        self.assertEqual("", aclsLogin.encript(c39))
        
        c40 = "$s@kp.f*p"  #longitud 9    sin digitos ni mayusculas
        self.assertEqual("", aclsLogin.encript(c40))
        
        c41 = "fToesQhpI"  #longitud 9    sin digitos ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c41))
        
        c42 = "d#6fo@.3q"  #longitud 9    sin mayusculas
        self.assertEqual("", aclsLogin.encript(c42))
        
        c43 = "irj1290k1"  #longitud 9    sin mayusculas ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c43))
        
        c44 = "1F09irA20"  #longitud 9    sin caracteres especiales
        self.assertEqual("", aclsLogin.encript(c44))
        
        c45 = "fpeosrnql"  #longitud 9    sin los requisitos minimos
        self.assertEqual("", aclsLogin.encript(c45))
        
        c47 = "_k?¡[ñ]<z]o8E{}"  #longitud 15    caracteres invalidos
        self.assertEqual("", aclsLogin.encript(c47))
        
        c48 = "#.LpWo@lEdff@#*"  #longitud 15    sin digitos
        self.assertEqual("", aclsLogin.encript(c48))
        
        c49 = "$s@kp#.*rthq+f*"  #longitud 15    sin digitos ni mayusculas
        self.assertEqual("", aclsLogin.encript(c49))
        
        c50 = "fToesQpUGndpder"  #longitud 15    sin digitos ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c50))
        
        c51 = "d#6o@3$.+*t34do"  #longitud 15    sin mayusculas
        self.assertEqual("", aclsLogin.encript(c51)) 
        
        c52 = "ir120k720fnsl0j"  #longitud 15    sin mayusculas ni caracteres especiales
        self.assertEqual("", aclsLogin.encript(c52))
        
        c53 = "1F09ir2UNdpw350"  #longitud 15    sin caracteres especiales
        self.assertEqual("", aclsLogin.encript(c53))
        
        c54 = "fpeosnqjdengosq"  #longitud 15    sin los requisitos minimos
        self.assertEqual("", aclsLogin.encript(c54))
    
    def testclsLoginEncriptTrue(self): 
        aclsLogin = clsLogin() 
        
        c19= "pa$$w0rD"  #longitud 8    caracteres validos
        self.assertNotEqual("", aclsLogin.encript(c19))
        
        c28 = "16.9rh@Ag5wxQzp0"  #longitud 16    caracteres validos
        self.assertNotEqual("", aclsLogin.encript(c28))   
        
        c37 = "pa$$w0rD."  #longitud 9    caracteres validos
        self.assertNotEqual("", aclsLogin.encript(c37))
        
        c46 = "16.9rh@AgwxQzp0"  #longitud 15    caracteres validos
        self.assertNotEqual("", aclsLogin.encript(c46))
        
    def testclsLoginCheck_passwordEncriptFalse(self):
        aclsLogin = clsLogin() 
        c0 = ""         #longitud 0
        mensajeEncriptado = aclsLogin.encript(c0)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c0))
    
        c1 = "M3A0$d8"  #Longitud 7    caracteres validos
        mensajeEncriptado = aclsLogin.encript(c1)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c1))
        
        c2 = "_ko8E{}"  #longitud 7    caracteres invalidos
        mensajeEncriptado = aclsLogin.encript(c2)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c2))
        
        c3 = "#.LpeW@"  #longitud 7    sin digitos
        mensajeEncriptado = aclsLogin.encript(c3)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c3))
        
        c4 = "$s@kpf*"  #longitud 7    sin digitos ni mayusculas
        mensajeEncriptado = aclsLogin.encript(c4)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c4))
        
        c5 = "fToesQp"  #longitud 7    sin digitos ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c5)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c5))
        
        c6 = "d#6fo@3"  #longitud 7    sin mayusculas
        mensajeEncriptado = aclsLogin.encript(c6)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c6))
        
        c7 = "irj120k"  #longitud 7    sin mayusculas ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c7)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c7))
        
        c8 = "1F09ir2"  #longitud 7    sin caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c8)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c8))
        
        c9 = "fpeosnq"  #longitud 7    sin los requisitos minimos
        mensajeEncriptado = aclsLogin.encript(c9)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c9))
        
        c10 = "C*@d$.3Aca#a3aE+$"    #longitud 17    caracteres validos
        mensajeEncriptado = aclsLogin.encript(c10)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c10))
        
        c11 = "(-:cpsm09JK\?|{=]"    #longitud 17    caracteres invalidos
        mensajeEncriptado = aclsLogin.encript(c11)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c11))
        
        c12 = "#.LpeW@+lnkzA.@yl"    #longitud 17    sin digitos
        mensajeEncriptado = aclsLogin.encript(c12)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c12))
        
        c13 = "k*sdj+fwei..weh@#"    #longitud 17    sin digitos ni mayusculas
        mensajeEncriptado = aclsLogin.encript(c13)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c13))    
        
        c14 = "MJiqJwieALniDGRou"    #longitud 17    sin digitos ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c14)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c14))
        
        c15 = "@#$+zj*ic71c22x.."    #longitud 17    sin mayusculas
        mensajeEncriptado = aclsLogin.encript(c15)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c15))        
        
        c16 = "i3u48712384uioiqm"    #longitud 17    sin mayusculas ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c16)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c16))
                
        c17 = "JFFefn93kNJK43672"    #longitud 17    sin caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c17)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c17))
                
        c18 = "00000000000000000"    #longitud 17    sin los requisitos minimos    
        mensajeEncriptado = aclsLogin.encript(c18)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c18))            

        c20 = "_ko8E{?}"  #longitud 8    caracteres invalidos
        mensajeEncriptado = aclsLogin.encript(c20)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c20))
                
        c21 = "#.LpeWr@"  #longitud 8    sin digitos
        mensajeEncriptado = aclsLogin.encript(c21)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c21))
                
        c22 = "$s@kp.f*"  #longitud 8    sin digitos ni mayusculas
        mensajeEncriptado = aclsLogin.encript(c22)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c22))
                
        c23 = "fToesQhp"  #longitud 8    sin digitos ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c23)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c23))        
        
        c24 = "d#6fo@.3"  #longitud 8    sin mayusculas
        mensajeEncriptado = aclsLogin.encript(c24)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c24))
        
        c25 = "irj1290k"  #longitud 8    sin mayusculas ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c25)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c25))
                
        c26 = "1F09irA2"  #longitud 8    sin caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c26)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c26))
                
        c27 = "fpeosrnq"  #longitud 8    sin los requisitos minimos
        mensajeEncriptado = aclsLogin.encript(c27)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c27))
            
        c29 = "_k?Â¡[Ã±]<z]>o8E{}"  #longitud 16    caracteres invalidos
        mensajeEncriptado = aclsLogin.encript(c29)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c29))
                
        c30 = "#.LpeWo@lEdff@#*"  #longitud 16    sin digitos
        mensajeEncriptado = aclsLogin.encript(c30)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c30))
                
        c31 = "$s@kpf#.*rthq+f*"  #longitud 16    sin digitos ni mayusculas
        mensajeEncriptado = aclsLogin.encript(c31)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c31))
                
        c32 = "fToesQpUGndpwder"  #longitud 16    sin digitos ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c32)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c32))
                
        c33 = "d#6fo@3$.+*t34do"  #longitud 16    sin mayusculas
        mensajeEncriptado = aclsLogin.encript(c33)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c33))
                
        c34 = "irj120k720fnsl0j"  #longitud 16    sin mayusculas ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c34)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c34))
                
        c35 = "1F09ir2UNdpw3450"  #longitud 16    sin caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c35)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c35))
                
        c36 = "fpeosnqjdoengosq"  #longitud 16    sin los requisitos minimos
        mensajeEncriptado = aclsLogin.encript(c36)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c36))
                         
        c38 = "_ko8E{?}Â¬"  #longitud 9    caracteres invalidos
        mensajeEncriptado = aclsLogin.encript(c38)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c38))
        
        c39 = "#.LpeWr@t"  #longitud 9    sin digitos
        mensajeEncriptado = aclsLogin.encript(c39)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c39))
        
        c40 = "$s@kp.f*p"  #longitud 9    sin digitos ni mayusculas
        mensajeEncriptado = aclsLogin.encript(c40)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c40))
        
        c41 = "fToesQhpI"  #longitud 9    sin digitos ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c41)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c41))
                
        c42 = "d#6fo@.3q"  #longitud 9    sin mayusculas
        mensajeEncriptado = aclsLogin.encript(c42)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c42))
                
        c43 = "irj1290k1"  #longitud 9    sin mayusculas ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c43)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c43))
                
        c44 = "1F09irA20"  #longitud 9    sin caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c44)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c44))
                
        c45 = "fpeosrnql"  #longitud 9    sin los requisitos minimos
        mensajeEncriptado = aclsLogin.encript(c45)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c45))     
       
        c47 = "_k?Â¡[Ã±]<z]o8E{}"  #longitud 15    caracteres invalidos
        mensajeEncriptado = aclsLogin.encript(c47)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c47))        
        
        c48 = "#.LpWo@lEdff@#*"  #longitud 15    sin digitos
        mensajeEncriptado = aclsLogin.encript(c48)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c48))        
        
        c49 = "$s@kp#.*rthq+f*"  #longitud 15    sin digitos ni mayusculas
        mensajeEncriptado = aclsLogin.encript(c49)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c49)) 
               
        c50 = "fToesQpUGndpder"  #longitud 15    sin digitos ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c50)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c50))
                
        c51 = "d#6o@3$.+*t34do"  #longitud 15    sin mayusculas
        mensajeEncriptado = aclsLogin.encript(c51)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c51))
                
        c52 = "ir120k720fnsl0j"  #longitud 15    sin mayusculas ni caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c52)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c52))
                
        c53 = "1F09ir2UNdpw350"  #longitud 15    sin caracteres especiales
        mensajeEncriptado = aclsLogin.encript(c53)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c53))
                
        c54 = "fpeosnqjdengosq"  #longitud 15    sin los requisitos minimos
        mensajeEncriptado = aclsLogin.encript(c54)
        self.assertFalse(aclsLogin.check_password(mensajeEncriptado,c54))
            
    def testclsLoginCheck_passwordTrue(self):
        aclsLogin = clsLogin() 
        
        c19= "pa$$w0rD"  #longitud 8    caracteres validos
        mensajeEncriptado = aclsLogin.encript(c19)
        self.assertTrue(aclsLogin.check_password(mensajeEncriptado,c19))
       
        c28 = "16.9rh@Ag5wxQzp0"  #longitud 16    caracteres validos
        mensajeEncriptado = aclsLogin.encript(c28)
        self.assertTrue(aclsLogin.check_password(mensajeEncriptado,c28))
        
        c37 = "pa$$w0rD."  #longitud 9    caracteres validos
        mensajeEncriptado = aclsLogin.encript(c37)
        self.assertTrue(aclsLogin.check_password(mensajeEncriptado,c37))
       
        c46 = "16.9rh@AgwxQzp0"  #longitud 15    caracteres validos
        mensajeEncriptado = aclsLogin.encript(c46)
        self.assertTrue(aclsLogin.check_password(mensajeEncriptado,c46))
        
    def testclsLoginLength_password(self):
        aclsLogin = clsLogin() 
        
        c0 = ""
        self.assertEqual(0, aclsLogin.length_password(c0))
        
        c1 = "M3A0$d8"  #Longitud 7    caracteres validos
        self.assertEqual(7, aclsLogin.length_password(c1))
        
        c2= "pa$$w0rD"  #longitud 8    caracteres validos
        self.assertEqual(8, aclsLogin.length_password(c2))
       
        c3 = "16.9rh@Ag5wxQzp0"  #longitud 16    caracteres validos
        self.assertEqual(16, aclsLogin.length_password(c3))
        
        c4 = "pa$$w0rD."  #longitud 9    caracteres validos
        self.assertEqual(9, aclsLogin.length_password(c4))
       
        c5 = "16.9rh@AgwxQzp0"  #longitud 15    caracteres validos
        self.assertEqual(15, aclsLogin.length_password(c5))
        
        c6 = "C*@d$.3Aca#a3aE+$"    #longitud 17    caracteres validos
        self.assertEqual(17, aclsLogin.length_password(c6))