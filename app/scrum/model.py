# -*- coding: utf-8 -*-. 

import os
import sys
from flask                 import Flask
from flask.ext.migrate     import Migrate, MigrateCommand
from flask.ext.sqlalchemy  import SQLAlchemy
from flask.ext.script      import Manager
from sqlalchemy.sql.schema import PrimaryKeyConstraint
 
# Conexion con la base de datos.
basedir                 = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# Instancia de la aplicacion.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Instancia de la base de datos. 
db = SQLAlchemy(app)

# Descripcion de la Base de Datos.


class clsBackLog(db.Model):
	'''Clase que define el modelo BackLog'''
 	
	__tablename__ =  'backLog'
	id_backLog     = db.Column(db.Integer,primary_key = True, index = True)
	BL_name        = db.Column(db.String(50),unique = True)	
	BL_description = db.Column(db.String(140))
	BL_scaleType   = db.Column(db.Integer)
	#obj_backLog    = db.relationship('clsObjective',backref='objective',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
	act_backLog    = db.relationship('clsActor',backref='backLog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
	#acc_backLog    = db.relationship('clsAccions',backref='backLog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")	
	#usrHis_backLog = db.relationship('clsUserHistory',backref='backLog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
 
	def __init__(self, BL_name,BL_description,BL_scaleType):
		'''Constructor del modelo BackLog'''
		self.BL_name 		= BL_name
		self.BL_description = BL_description
		self.BL_scaleType	= BL_scaleType
 		
	def __repr__(self):
		'''Representacion en string del nombre del BakcLog'''
		return '<id_backLog %r, BL_name %r, BL_scaleType %r>' % (self.id_backLog, self.BL_name,self.BL_scaleType)
 	
 	
	
class clsActor(db.Model):
    '''Clase que define el modelo Actor'''

    __tablename__ = 'actors'
    A_idActor          = db.Column(db.Integer, primary_key=True)
    A_nameActor        = db.Column(db.String(50), unique=True)
    A_actorDescription = db.Column(db.String(140))
    A_idBacklog        = db.Column(db.Integer,db.ForeignKey('backLog.id_backLog'))
    A_refUser          = db.relationship('clsUser', backref = 'actors',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    #sUserHistory_role = db.relationship('clsRolesUserHistory', backref = 'roles',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
      
    def __init__(self, nameActor,actorDescription,idBacklog):
        '''Constructor del modelo Actor'''
        self.A_nameActor        = nameActor
        self.A_actorDescription = actorDescription
        self.A_idBacklog        = idBacklog

    def __repr__(self):
        '''Respresentacion en string del modelo Actor'''
        return '<IdActor %r, Nombre %r, Descripcion %r, IdBacklog %r>' %(self.A_idActor, self.A_nameActor , self.A_actorDescription, self.A_idBacklog)
  


class clsUser(db.Model):
    '''Clase que define el modelo Usuario'''
 
    __tablename__ = 'user'
    U_fullname = db.Column(db.String(50))
    U_username = db.Column(db.String(16), primary_key = True, index = True)
    U_password = db.Column(db.String(200))
    U_email    = db.Column(db.String(30), unique = True)
    U_idActor  = db.Column(db.Integer, db.ForeignKey('actors.A_idActor'))

    def __init__(self, fullname, username, password, email, idActor):
        '''Constructor del modelo usuario'''
        self.U_fullname = fullname
        self.U_username = username
        self.U_password = password
        self.U_email    = email
        self.U_idActor  = idActor
   
    def __repr__(self):
        '''Representacion en string del modelo Usuario'''
        return '<fullname %r, username %r, email %r>' % (self.U_fullname, self.U_username, self.U_email)
       
 	
 	
class clsObjective(db.Model):
    '''Clase que define el modelo Objective'''
 
    __tablename__  = 'objectives'
    idobjective    = db.Column(db.Integer, primary_key=True)
    descObjective  = db.Column(db.String(140), unique=True)
    id_backlog     = db.Column(db.Integer, db.ForeignKey('backLog.id_backLog'))
    obj_type	   = db.Column(db.String(5)) 
    objectiveUserHistory_role = db.relationship('clsObjectivesUserHistory', backref = 'objectives',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    
    def __init__(self, descObjective, id_backLog, objType):
        '''Constructor del modelo Objective'''
        self.descObjective  = descObjective
        self.id_backlog     = id_backLog
        self.obj_type	    = objType
 
    def __repr__(self):
        '''Respresentación en string de la descripción del Objective'''
        return '<Id_Objetivo %r>, <Descripcion %r>, <Id_backlog %r>' %(self.idobjective, self.descObjective, self.id_backlog)
 
 
 	
class clsAccions(db.Model):
    '''Clase que define el modelo Accion'''
 
    __tablename__  = 'accions'
    idaccion          = db.Column(db.Integer, primary_key=True)
    acciondescription = db.Column(db.String(140), unique=True)
    id_backLog        = db.Column(db.Integer, db.ForeignKey('backLog.id_backLog'))
    id_userHistory    = db.Column(db.Integer,db.ForeignKey('userHistory.id_userHistory'),nullable = True)    
     
    
    def __init__(self,  acciondescription, id_backLog):
        '''Constructor del modelo Accion'''
        self.acciondescription = acciondescription
        self.id_backLog        = id_backLog
 
    def __repr__(self):
        '''Respresentación en string de la descripción de la accion'''
        return '<Id_Accions %r>, <Descripcion %r>, <Id_backlog %r>' %(self.idaccion, self.acciondescription, self.id_backLog)
        
        
        
class clsUserHistory(db.Model):
	'''Clase que define el modelo de tabla userHistory'''
 	
	__tablename__ = 'userHistory'
	id_userHistory  = db.Column(db.Integer, primary_key = True, index = True)
	cod_userHistory = db.Column(db.String(11),unique = True , index = True) 
	id_History      = db.Column(db.Integer, db.ForeignKey('userHistory.id_userHistory'),nullable = True) 
	type_accion     = db.Column(db.Integer)
	ref_idaccion	= db.Column(db.Integer, db.ForeignKey('accions.idaccion'))
	id_backLog      = db.Column(db.Integer, db.ForeignKey('backLog.id_backLog'))
	UH_scale        = db.Column(db.Integer, index = True)
	roleUserHistory_userHistory = db.relationship('clsRolesUserHistory', backref = 'userHistory',lazy = 'dynamic', cascade = "all, delete, delete-orphan")
	objUserHistory_userHistory  = db.relationship('clsObjectivesUserHistory', backref = 'userHistory',lazy = 'dynamic', cascade = "all, delete, delete-orphan")	
 	
	def __init__(self,cod_userHistory,id_History,type_accion,ref_idaccion,id_backLog,UH_scale):
		self.cod_userHistory = cod_userHistory
		self.id_History      = id_History 
		self.type_accion     = type_accion
		self.ref_idaccion    = ref_idaccion
		self.id_backLog      = id_backLog
		self.UH_scale		 = UH_scale
 		
	def __repr__(self):
		'''Representacion en string de la Historia de Usuario'''
		return '<id_userHistory %r, cod_userHistory %r, Us_scale %r>' % (self.id_userHistory,self.cod_userHistory, self.UH_scale)
 	
 	
 	
class clsRolesUserHistory(db.Model):
	'''Clase que define el modelo de tabla rolesUserHistory'''
 	
	__tablename__ = 'rolesUserHistory'
	id_roleUserHistory = db.Column(db.Integer, primary_key = True, index = True) 
	#ref_idrole         = db.Column(db.Integer, db.ForeignKey('roles.idrole'))
	ref_idUserHistory  = db.Column(db.Integer, db.ForeignKey('userHistory.id_userHistory'))
 	
	def __init__(self, ref_idrole, ref_idUserHistory):
		self.ref_idrole        = ref_idrole
		self.ref_idUserHistory = ref_idUserHistory
 		
	def __repr__(self):
		'''Representacion en string de los id's a los roles y sus historias'''
		return '<ref_idrole %r, ref_idUserHistory %r>' % (self.ref_idrole, self.ref_idUserHistory)
 		
 	
 	
class clsObjectivesUserHistory(db.Model):
	'''Clase que define el modelo de tabla ObjectivesUserHistory'''
 	
	__tablename__ = 'objectivesUserHistory'
	id_objectiveUserHistory = db.Column(db.Integer, primary_key = True, index = True)
	ref_idobjective         = db.Column(db.Integer, db.ForeignKey('objectives.idobjective'))
	ref_idUserHistory       = db.Column(db.Integer, db.ForeignKey('userHistory.id_userHistory'))	
 	
	def __init__(self, ref_idobjective, ref_idUserHistory):
		self.ref_idobjective   = ref_idobjective
		self.ref_idUserHistory = ref_idUserHistory
 		
	def __repr__(self):
		'''Representacion en string de los id's a los roles y sus historias'''
		return '<ref_idobjective %r, ref_idUserHistory %r>' % (self.ref_idobjective, self.ref_idUserHistory)
		
		
	
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

#db.drop_all()  # Borramos la base de datos
db.create_all() # Creamos la base de datos