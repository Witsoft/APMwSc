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
                session['usuario'] = {'nombre':userLogin[0].fullname.title()}
                res = results[0]
            else:
                res = results[3]
        else:
            res = results[3]

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

    if request.method == 'POST':
        # Se precargan valores en la base de datos.
        oRole    = role()
        oBackLog = backLog()

        isEmpty  = oRole.emptyTable()
        if isEmpty:
            result1 = oBackLog.insertBackLog('Taxi Seguro','Mejor forma de operar un taxi',1)
            result2 = oRole.insertRole('Product Owner','Encargado de las decisiones de diseno del producto.',1)
            result3 = oRole.insertRole('Scrum Master','Encargado de orientar y ayudar al equipo desarrollador del producto.',1)
            result  = oRole.insertRole('Team Member','Equipo encargado del desarrollo del producto.',1)
            
        print('Valores de BackLog:')
        print(clsBackLog.query.all())
        print('Valores de Role:')
        print(clsRole.query.all())
        print('Valores de Usuario:')
        print(clsUser.query.all())

        newName     = params['nombre']
        newUser     = params['usuario']
        newPassword = params['clave']
        newEmail    = params['correo']

        login = clsLogin()
        oUser = user()

        checkNewUser      = oUser.isFound(newUser)
        checkNewEmail     = oUser.findEmail(newEmail)
        checkNewPassword  = login.validPassword(newPassword)
        encriptPassword   = login.encript(newPassword)
        
        if (not checkNewUser) and checkNewPassword and (not checkNewEmail):
            result = oUser.insertUser(newName,newUser,encriptPassword,newEmail,1)          
            if result: 
                print('Se registro satisfactoriamente el Usuario')
            res = results[0]
        else:
            res = results[1]
    else:
        res = results[1]

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

    session.pop('usuario', None)
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
