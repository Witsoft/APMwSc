# -*- coding: utf-8 -*-
from flask           import request, session, Blueprint, json
from app.scrum.role  import *
from app.scrum.user  import *
from app.scrum.login import *

ident = Blueprint('ident', __name__)

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño de producto'], "actor":"duenoProducto"}, {'label':'/VMaestroScrum', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"}, {'label':'/VDesarrollador', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"}, {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    res     = results[0]
    # Action code goes here, res should be a list with a label and a message
    if request.method == 'POST':
        newUser     = params['usuario']
        newPassword = params['clave']
        oUser       = user()

        # Buscamos el usuario en la base de datos
        userLogin   = oUser.searchUser(newUser)

        if userLogin:
            encriptPassword = userLogin[0].password
            # Creamos instancia de la clase login
            logPass = clsLogin();
            isValid = logPass.check_password(encriptPassword, newPassword)

            if isValid:
                res = results[0]
            else:
                res = results[3]
        else:
            res = results[3]

     #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


 
@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, ]

    #Action code goes here, res should be a list with a label and a message
    if request.method == 'POST':
        # Se precargan los roles en la base de datos.
        oRole   = role()
        isEmpty = oRole.emptyTable()
        if isEmpty:
            result = oRole.insertRole(1,'Product Owner')
            if result: print('Se guardo role Product Owner.')
            result = oRole.insertRole(2,'Scrum Master')
            if result: print('Se guardo role Scrum Master.')
            result = oRole.insertRole(3,'Team Member')
            if result: print('Se guardo role Team Member.')
            

        print('Valores de Role:')
        print(clsRole.query.all())
        print('Valores de Usuario:')
        print(clsUser.query.all())

        newName     = params['nombre']
        newUser     = params['usuario']
        newPassword = params['clave']
        newEmail    = params['correo']

        login = clsLogin()
        # Instancia de usuario.
        oUser = user()

        checkNewUser      = oUser.isFound(newUser)
        checkNewEmail     = oUser.findEmail(newEmail)
        checkNewPassword  = login.validPassword(newPassword)
        encriptPassword   = login.encript(newPassword)

        print ("usuario: " + str(checkNewUser))
        print ("password: " +  str(checkNewPassword))
        print ("email: " + str(checkNewEmail))
        
        if (not checkNewUser) and checkNewPassword and (not checkNewEmail):
            result = oUser.insertUser(newName,newUser,encriptPassword,newEmail,1)
            if result: 
                print('Se registro satisfactoriamente el Usuario')
            res = results[0]
        else:
            res = results[1]
    else:
        res = results[1]
    #Action code ends here

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    

    #Action code ends here
    return json.dumps(res)



@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
