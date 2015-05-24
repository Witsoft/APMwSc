# -*- coding: utf-8 -*-. 

from modelDummy import *
from roleDummy  import *

# Declaracion de constantes.
const_maxUser     = 16
const_maxFullname = 50
const_maxPassword = 16
const_maxEmail    = 30
const_min_long    = 1
const_min_password = 8

class user(object):
    '''Clase que permite manejar usuarios de manera persistente'''
    
    def searchUser(self,username):
        '''Permite buscar un usuario por su nombre'''
        if (type(username) != str):
            return []
        else:
            long_username = len(username)
            if (long_username >const_maxUser or long_username < const_min_long):
                return []
            else:
                auser = clsUser.query.filter_by(username = username).all()
                return auser


    def findEmail(self,email):
        '''Permite saber si un email esta en la base de datos'''
        aemail = clsUser.query.filter_by(email=email).all()
        return aemail != []


    def isFound(self,username):
        '''Permite saber si un usuario esta en la base de datos'''
        auser = clsUser.query.filter_by(username=username).all()
        return auser != []

    def insertUser(self, fullname, username, password, email, idrole):
        '''Permite insertar un usuario en la tabla'''
        
        typefname = (type(fullname) == str) 
        typeuser = (type(username) == str) 
        typepassword = (type(password) == str)
        typemail =(type(email) == str) 
        typerole = (type(idrole) == int)
        
        if (typefname and typeuser and typepassword and typemail and typerole):
            
            longUser = const_min_long <= len(username) <= const_maxUser
            longFullname = const_min_long <= len(fullname) <= const_maxFullname
            longPassword = const_min_password <= len(password) <= const_maxPassword
            longEmail = const_min_long <= len(email) <= const_maxEmail 
            
            if (longUser and longFullname and longPassword and longEmail):
                auser = clsUser.query.filter_by(username=username).all()
                role1 = clsRole.query.filter_by(idrole = idrole).all()
                if ((auser == []) and (role1 != [])):
                    new_user = clsUser(fullname = fullname, username = username, password = password, email =email, idrole = idrole)
                    db.session.add(new_user)
                    db.session.commit()
                    return True
        return False
        
    def updateUser(self, new_fullname, username, new_password, new_email, new_idrole):   
        '''Permite actualizar los valores de un usuario'''    
        if type(username) != str:
            return False
        else:
            auser = clsUser.query.filter_by(username=username).all()
            if auser == []:
                return False
            else:
                auser = clsUser.query.filter_by(username=username).first()
                if ((type(new_fullname) != str or type(new_password) != str or type(new_email) != str\
                      or type(new_idrole) != int)):
                    return False
                else:
                    longFullname = len(new_fullname)
                    longPassword = len(new_password)
                    longEmail = len(new_email)
                    if (longFullname>const_maxFullname or longPassword>const_maxPassword or longEmail>const_maxEmail\
                      or longFullname<const_min_long or longPassword<const_min_long or longEmail<const_min_long):
                        return False
                    else:
                        role1 = clsRole.query.filter_by(idrole = new_idrole).all()
                        if (role1 == []):
                            return False
                        else:
                            auser.fullname = new_fullname
                            auser.password = new_password
                            auser.email = new_email
                            auser.idrole= new_idrole
                            db.session.commit()
                            return True
                        
    def deleteUser(self,username):
        '''Permite eliminar un usuario de la tabla'''
        if type(username) != str:
            return False
        else:
            long_username = len(username)
            if long_username > const_maxUser or long_username < const_min_long:
                return False
            else:
                auser = clsUser.query.filter_by(username=username).all()
                if auser == []:
                    return False
                else:
                    for i in auser:    
                        db.session.delete(i)
                    db.session.commit()
                    return True
# Fin Clase user