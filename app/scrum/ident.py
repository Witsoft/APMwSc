# -*- coding: utf-8 -*-

from flask           import request, session, Blueprint, json
from app.scrum.role  import *
from app.scrum.user  import *
from app.scrum.login import *

ident = Blueprint('ident', __name__)

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters.
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño de producto'], "actor":"duenoProducto"}, {'label':'/VMaestroScrum', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"}, {'label':'/VDesarrollador', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"}, {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    
    if request.method == 'POST':
        userName     = params['usuario']
        userPassword = params['clave']
        
        # Buscamos el usuario en la base de datos.
        oUser     = user()
        userLogin = oUser.searchUser(userName)

        if userLogin:
            encriptPassword = userLogin[0].U_password
            # Chequeamos el password.
            oLogin  = login();
            isValid = oLogin.check_password(encriptPassword, userPassword)

            if isValid:
                session['usuario'] = {'nombre':userLogin[0].U_fullname.title()}
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
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, ]

    if request.method == 'POST':
        # Se precargan valores en la base de datos.
        oActor   = actor()
        oBackLog = backLog()

        isEmpty  = oActor.emptyTable()
        if isEmpty:
            result1 = oBackLog.insertBackLog('Taxi Seguro','Mejor forma de operar un taxi',1)
            result2 = oActor.insertActor('Product Owner','Encargado de las decisiones de diseno del producto.',1)
            result3 = oActor.insertActor('Scrum Master','Encargado de orientar y ayudar al equipo desarrollador del producto.',1)
            result  = oActor.insertActor('Team Member','Equipo encargado del desarrollo del producto.',1)

        # Extraemos los datos.
        newName     = params['nombre']
        newUser     = params['usuario']
        newPassword = params['clave']
        newEmail    = params['correo']

        oLogin = login()
        oUser  = user()

        checkNewUser     = oUser.isFound(newUser)
        checkNewEmail    = oUser.findEmail(newEmail)
        checkNewPassword = oLogin.validPassword(newPassword)
        encriptPassword  = oLogin.encript(newPassword)
        
        res = results[1]
        
        if (not checkNewUser) and checkNewPassword and (not checkNewEmail):
            result = oUser.insertUser(newName,newUser,encriptPassword,newEmail,1)  
            
            print('Valores de BackLog:')
            print(clsBackLog.query.all())
            print('Valores de Actor:')
            print(clsActor.query.all())
            print('Valores de Usuario:')
            print(clsUser.query.all()) 
             
            if result: 
                res = results[0]

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