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

# Definicion de la Base de Datos.

class clsBacklog(db.Model):
	'''Clase que define el modelo Backlog'''
 	
	__tablename__ =  'backlog'
	BL_idBacklog    = db.Column(db.Integer,primary_key = True, index = True)
	BL_name         = db.Column(db.String(50),unique = True)	
	BL_description  = db.Column(db.String(140))
	BL_scaleType    = db.Column(db.Integer)
	BL_refObjective = db.relationship('clsObjective',backref = 'backlog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
	BL_refActor     = db.relationship('clsActor',backref = 'backlog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
	BL_refAccion    = db.relationship('clsAccion',backref = 'backlog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")	
	BL_refUserHist  = db.relationship('clsUserHistory',backref = 'backlog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
 
	def __init__(self,name,description,scaleType):
		'''Constructor del modelo Backlog'''
		self.BL_name 		= name
		self.BL_description = description
		self.BL_scaleType	= scaleType
 		
	def __repr__(self):
		'''Representacion en string del modelo Bakclog'''
		return '<idBacklog %r, name %r, scaleType %r>' % (self.BL_idBacklog, self.BL_name, self.BL_scaleType)
 	
 	
	
class clsActor(db.Model):
    '''Clase que define el modelo Actor'''

    __tablename__ = 'actors'
    A_idActor          = db.Column(db.Integer, primary_key = True)
    A_nameActor        = db.Column(db.String(50), unique = True)
    A_actorDescription = db.Column(db.String(140))
    A_idBacklog        = db.Column(db.Integer,db.ForeignKey('backlog.BL_idBacklog'))
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
    O_idObjective    = db.Column(db.Integer, primary_key = True)
    O_descObjective  = db.Column(db.String(140), unique = True)
    O_idBacklog      = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    O_objType	     = db.Column(db.String(5)) 
    O_refObjUserHist = db.relationship('clsObjectivesUserHistory', backref = 'objectives',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    
    def __init__(self,descObjective,idBacklog,objType):
        '''Constructor del modelo Objective'''
        self.O_descObjective = descObjective
        self.O_idBacklog     = idBacklog
        self.O_objType	     = objType
 
    def __repr__(self):
        '''Respresentación en string del modelo Objective'''
        return '<IdObjetivo %r>, <Descripcion %r>, <IdBacklog %r>' %(self.O_idObjective, self.O_descObjective, self.O_idBacklog)
 
 
 	
class clsAccion(db.Model):
    '''Clase que define el modelo Accion'''
 
    __tablename__  = 'accions'
    AC_idAccion          = db.Column(db.Integer, primary_key = True)
    AC_accionDescription = db.Column(db.String(140), unique = True)
    AC_idBacklog         = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))    
    AC_UserHistory       = db.relationship('clsUserHistory', backref = 'accions', lazy = 'dynamic',cascade = "all, delete, delete-orphan")
     
    def __init__(self, accionDescription,idBacklog):
        '''Constructor del modelo Accion'''
        self.AC_accionDescription = accionDescription
        self.AC_idBacklog         = idBacklog
 
    def __repr__(self):
        '''Respresentación en string del modelo accion'''
        return '<IdAccion %r>, <Descripcion %r>, <IdBacklog %r>' %(self.AC_idAccion, self.AC_accionDescription, self.AC_idBacklog)
        
        
        
class clsUserHistory(db.Model):
	'''Clase que define el modelo de tabla userHistory'''
 	
	__tablename__ = 'userHistory'
	id_userHistory  = db.Column(db.Integer, primary_key = True, index = True)
	cod_userHistory = db.Column(db.String(11),unique = True , index = True) 
	id_History      = db.Column(db.Integer, db.ForeignKey('userHistory.id_userHistory'),nullable = True) 
	type_accion     = db.Column(db.Integer)
	ref_idaccion	= db.Column(db.Integer, db.ForeignKey('accions.AC_idAccion'))
	id_backLog      = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
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
	ref_idrole         = db.Column(db.Integer, db.ForeignKey('actors.A_idActor'))
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
	ref_idobjective         = db.Column(db.Integer, db.ForeignKey('objectives.O_idObjective'))
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

db.create_all() # Creamos la base de datos