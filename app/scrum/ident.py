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
    oCate    = category()
    oTask    = task()
    oHistory = userHistory()

    isEmpty  = oActor.emptyTable()
    
    if isEmpty:
        print('Cargando datos de prueba...')
        
        # Se crean las categorías por defecto
        resu1  = oCate.insertCategory('Implementar una acción',2)
        resu2  = oCate.insertCategory('Implementar una vista',2)
        resu3  = oCate.insertCategory('Implementar una regla de negocio on un método de una clase',2)
        resu4  = oCate.insertCategory('Migrar la base de datos',2)
        resu5  = oCate.insertCategory('Crear un diagrama UML',1)
        resu6  = oCate.insertCategory('Crear datos iniciales',1)
        resu7  = oCate.insertCategory('Crear un criterio de aceptación',1)
        resu8  = oCate.insertCategory('Crear una prueba de aceptación',2)
        resu9  = oCate.insertCategory('Actualizar en elemento implementado en otra tarea',1)
        resu10 = oCate.insertCategory('Escribir el manual en línea de una página',2)    
        resu11 = oCate.insertCategory('Ordenar las placas',5)
        resu12 = oCate.insertCategory('Mirar colores llamativos',3)
        resu13 = oCate.insertCategory('Crear aplicación de WitSoft',7)
        resu14 = oCate.insertCategory('Reutilizar herramientas de trabajo',4)

        # Creamos el primer producto
        resu15 = oBacklog.insertBacklog('Taxi Seguro','Mejor forma de operar un taxi',1)
    
        # Insertamos los actores asociados
        resu16 = oActor.insertActor('Conductor','Encargado de manejar un automovil',1)
        resu17 = oActor.insertActor('Mecánico','Encargado de reparar automóviles',1)
        resu18 = oActor.insertActor('Supervisor','Persona involucrada en el desarrollo del producto',1)
    
        # Insertamos las acciones asociadas
        resu19 = oAccion.insertAccion('Enseñar el uso de la aplicación',1)
        resu20 = oAccion.insertAccion('Registrar vehiculos',1)
    
        # Se crean objetivos no transversales
        resu21 = oObj.insertObjective('Verificar fallas existentes y solucionarlas',1,False)
        resu22 = oObj.insertObjective('Facilitar la deteccion de defectos',1,False)
    
        # Se crean objetivos transversales
        resu23 = oObj.insertObjective('Incrementar la produccion',1,True)
            
        # Creamos el segundo producto
        resu24 = oBacklog.insertBacklog('WitGrafies','Herramienta graficadora',2)
    
        # Insertamos los actores asociados
        resu25 = oActor.insertActor('Diseñador Gráfico','Decide como se ve la aplicación',2)
        resu26 = oActor.insertActor('Diseñador de Experiencias de Usuario','Decide como se siente usar la aplicación',2)
    
        # Insertamos las acciones asociadas
        resu27 = oAccion.insertAccion('Elegir elementos gráficos',2)
        resu28 = oAccion.insertAccion('Elegir mecanismos de interacción',2)
    
        # Se crean objetivos no transversales
        resu29 = oObj.insertObjective('Presentar correctamente la información',2,False)
        resu30 = oObj.insertObjective('Presentar pasos lógicos de la interacción',2,False)
    
        # Se crean objetivos transversales
        resu31 = oObj.insertObjective('Ofrecer seguridad a los datos del usuario',2,True)

        oLogin = login()
        oUser  = user()     
        #Creamos usuarios con los tres posibles roles
        password         = 'Sabeys.2008'
        encriptPassword  = oLogin.encript(password)
         
        result = oUser.insertUser('Dueno','admin',encriptPassword,'productOwner@gmail.com',1) 
        result = oUser.insertUser('Maestro Scrum','scrum',encriptPassword,'scrumMaster@gmail.com',2) 
        result = oUser.insertUser('Equipo de Trabajo','team',encriptPassword,'teamMember@gmail.com',3) 

        print('Se cargaron los datos.')
        
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
