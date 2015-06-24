# -*- coding: utf-8 -*-

from flask                  import request, session, Blueprint, json
from app.scrum.role         import *
from app.scrum.accions      import *
from app.scrum.objective    import *
from app.scrum.user         import *
from app.scrum.login        import *
from app.scrum.category     import *
from app.scrum.task         import *
from app.scrum.userHistory  import *  

ident = Blueprint('ident', __name__)

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters.
    params  = request.get_json()

    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño del producto'], "actor":"duenoProducto"},
               {'label':'/VProductos', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"}, 
               {'label':'/VProductos', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"},
               {'label':'/VLogin',     'msg':['Datos de identificación incorrectos']}]
    res     = results[3]
    
    if request.method == 'POST':
        userName     = params['usuario']
        userPassword = params['clave']

        # Buscamos el usuario en la base de datos
        oUser     = user()
        userLogin = oUser.searchUser(userName)

        if userLogin:
            encriptPassword = userLogin[0].U_password
            # Chequeamos el password
            oLogin  = login();
            isValid = oLogin.check_password(encriptPassword, userPassword)

            if isValid:
                # Mostramos el nombre en la aplicación
                fullname = userLogin[0].U_fullname
                session['usuario'] = {'nombre': fullname.title()}
                
                # Verificamos el rol del usuario
                rolUser = userLogin[0].U_idActor
                
                if rolUser == 1: res = results[0]
                if rolUser == 2: res = results[1]
                if rolUser == 3: res = results[2]            

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


 
@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VLogin'   , 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, 
               {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']} ]
    res     = results[1]

    
    if request.method == 'POST':

        # Extraemos los datos
        newName     = params['nombre']
        newUser     = params['usuario']
        newPassword = params['clave']
        newEmail    = params['correo']
        newActor    = params['actorScrum']

        oLogin = login()
        oUser  = user()
        
        checkNewUser     = oUser.isFound(newUser)
        checkNewEmail    = oUser.findEmail(newEmail)
        checkNewPassword = oLogin.validPassword(newPassword)
        encriptPassword  = oLogin.encript(newPassword)
        
        if (not checkNewUser) and checkNewPassword and (not checkNewEmail):
            result = oUser.insertUser(newName,newUser,encriptPassword,newEmail,newActor)  
             
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

    session.pop('usuario', None)
    
    # Se precargan valores en la base de datos
    oBacklog = backlog() 
    oActor   = role()
    oAccion  = accions()
    oObj     = objective()
    oCat     = category()
    oTask    = task()
    oHistory = userHistory()
    isEmpty  = oActor.emptyTable()
    
    if isEmpty:
        print('Cargando datos de prueba...')
        # Se crea un nuevo producto
        result1  = oBacklog.insertBacklog('Taxi Seguro','Mejor forma de operar un taxi',1)
        # Se crean los roles
        result2  = oActor.insertActor('Dueño del Producto','Encargado de las decisiones de diseño del producto.',0)
        result3  = oActor.insertActor('Maestro Scrum','Encargado de orientar y ayudar al equipo desarrollador del producto.',0)
        result4  = oActor.insertActor('Miembro del Equipo','Pesona involucrada en el desarrollo del producto.',0)
        # Se crean acciones
        result5  = oAccion.insertAccion('Enseñar el uso de la aplicacion',1)
        result6  = oAccion.insertAccion('Registrar vehiculos',1)
        # Se crean objetivos no transversales
        result7  = oObj.insertObjective('Verificar fallas existentes y solucionarlas',1,False)
        result8  = oObj.insertObjective('Facilitar la deteccion de defectos',1,False)
        # Se crean objetivos transversales
        result9  = oObj.insertObjective('Incrementar la produccion',1,True)
        #Se crean categorias para las tareas
        result10 = oCat.insertCategory('Crear una acción',1)
        result11 = oCat.insertCategory('Migrar la base de datos',2)
        result12 = oCat.insertCategory('Escribir el manual en línea de una vista',1)
        result13 = oCat.insertCategory('Crear un criterio de aceptación',1)
        result14 = oCat.insertCategory('Crear una prueba de aceptación',2)
        result15 = oCat.insertCategory('Crear una regla de negocio compleja',3)
         
        oLogin = login()
        oUser  = user()     
        #Creamos usuarios con los tres posibles roles
        password         = 'Sabeys.2008'
        encriptPassword  = oLogin.encript(password)
         
        result = oUser.insertUser('Dueno','admin',encriptPassword,'productOwner@gmail.com',1) 
        result = oUser.insertUser('Maestro Scrum','scrum',encriptPassword,'scrumMaster@gmail.com',2) 
        result = oUser.insertUser('Equipo de Trabajo','team',encriptPassword,'teamMember@gmail.com',3) 
        print('Se cargaron los datos.')
         
    print('Valores de Usuario:')
    print(clsUser.query.all()) 
    
    
        
    return json.dumps(res)



@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor'] = session['actor']

    res['fUsuario_opcionesActorScrum'] = [
      {'key':2,'value':'Maestro Scrum'},
      {'key':1,'value':'Dueño de producto'},
      {'key':3,'value':'Miembro del equipo de desarrollo'},
      {'key':0,'value':'Seleccione un rol'}
    ]

    return json.dumps(res)


#Use case code starts here


#Use case code ends here
