# -*- coding: utf-8 -*-. 

# Se importan las librerias necesarias.
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
    A_idActor           = db.Column(db.Integer, primary_key = True)
    A_nameActor         = db.Column(db.String(50))
    A_actorDescription  = db.Column(db.String(140))
    A_idBacklog         = db.Column(db.Integer,db.ForeignKey('backlog.BL_idBacklog'))
    A_refUser           = db.relationship('clsUser', backref = 'actors',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    A_refActorsUserHist = db.relationship('clsActorsUserHistory', backref = 'actors',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
      
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
    O_descObjective  = db.Column(db.String(140))
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
        return '<IdObjetivo %r, Descripcion %r, IdBacklog %r>' %(self.O_idObjective, self.O_descObjective, self.O_idBacklog)
 
 
 	
class clsAccion(db.Model):
    '''Clase que define el modelo Accion'''
 
    __tablename__  = 'accions'
    AC_idAccion          = db.Column(db.Integer, primary_key = True)
    AC_accionDescription = db.Column(db.String(140))
    AC_idBacklog         = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))    
    AC_refUserHistory    = db.relationship('clsUserHistory', backref = 'accions', lazy = 'dynamic',cascade = "all, delete, delete-orphan")
     
    def __init__(self, accionDescription,idBacklog):
        '''Constructor del modelo Accion'''
        self.AC_accionDescription = accionDescription
        self.AC_idBacklog         = idBacklog
 
    def __repr__(self):
        '''Respresentación en string del modelo accion'''
        return '<IdAccion %r, Descripcion %r, IdBacklog %r>' %(self.AC_idAccion, self.AC_accionDescription, self.AC_idBacklog)
        
    
        
class clsUserHistory(db.Model):
	'''Clase que define el modelo de tabla userHistory'''
 	
	__tablename__ = 'userHistory'
	UH_idUserHistory     = db.Column(db.Integer, primary_key = True, index = True)
	UH_codeUserHistory   = db.Column(db.String(11), index = True) 
	UH_idSuperHistory    = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'),nullable = True) 
	UH_accionType        = db.Column(db.Integer)
	UH_idAccion	         = db.Column(db.Integer, db.ForeignKey('accions.AC_idAccion'))
	UH_idBacklog         = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
	UH_scale             = db.Column(db.Integer, index = True)
	UH_refActorsUserHist = db.relationship('clsActorsUserHistory', backref = 'userHistory',lazy = 'dynamic', cascade = "all, delete, delete-orphan")
	UH_refTareaUserHist  = db.relationship('clsTask', backref = 'userHistory',lazy = 'dynamic', cascade = "all, delete, delete-orphan")
	UH_refObjUserHist    = db.relationship('clsObjectivesUserHistory', backref = 'userHistory',lazy = 'dynamic', cascade = "all, delete, delete-orphan")

	def __init__(self,codeUserHistory,idSuperHistory,accionType,idAccion,idBacklog,scale):
		self.UH_codeUserHistory = codeUserHistory
		self.UH_idSuperHistory  = idSuperHistory 
		self.UH_accionType      = accionType
		self.UH_idAccion        = idAccion
		self.UH_idBacklog       = idBacklog
		self.UH_scale		    = scale

	def __repr__(self):
		'''Representacion en string de la Historia de Usuario'''
		return '<idUserHistory %r, codeUserHistory %r, idSuperHistory %r, scale %r>' % (self.UH_idUserHistory ,self.UH_codeUserHistory,self.UH_idSuperHistory,self.UH_scale)
 	

	
class clsActorsUserHistory(db.Model):
	'''Clase que define el modelo de tabla actorsUserHistory'''
 	
	__tablename__ = 'actorsUserHistory'
	AUH_idActorsUserHist = db.Column(db.Integer, primary_key = True, index = True) 
	AUH_idActor          = db.Column(db.Integer, db.ForeignKey('actors.A_idActor'))
	AUH_idUserHistory    = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))
 	
	def __init__(self, idActor, idUserHistory):
		self.AUH_idActor       = idActor
		self.AUH_idUserHistory = idUserHistory

	def __repr__(self):
		'''Representacion en string de los id's a los actores y sus historias'''
		return '<idActor %r, idUserHistory %r>' % (self.AUH_idActor, self.AUH_idUserHistory)
 
 
 
class clsObjectivesUserHistory(db.Model):
	'''Clase que define el modelo de tabla ObjectivesUserHistory'''
 	
	__tablename__ = 'objectivesUserHistory'
	OUH_idObjectivesUserHist = db.Column(db.Integer, primary_key = True, index = True)
	OUH_idObjective          = db.Column(db.Integer, db.ForeignKey('objectives.O_idObjective'))
	OUH_idUserHistory        = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))	
 	
	def __init__(self,idObjective,idUserHistory):
		self.OUH_idObjective   = idObjective
		self.OUH_idUserHistory = idUserHistory
 		
	def __repr__(self):
		'''Representacion en string de los id's a los roles y sus historias'''
		return '<idObjective %r, idUserHistory %r>' % (self.OUH_idObjective, self.OUH_idUserHistory)
		
class clsTask(db.Model):
	'''Clase que define el modelo de la tabla Task'''
	
	__tablename__ = 'task'
	HW_idTask        = db.Column(db.Integer, primary_key = True, index = True)
	HW_description 	 = db.Column(db.String(140),unique = True , index = True) 
	HW_weight        = db.Column(db.Integer)
	HW_idCategory    = db.Column(db.Integer, db.ForeignKey('category.C_idCategory'))
	HW_idUserHistory = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))
	
	def __init__(self,description,idCategory,weight,idUserHistory):
		self.HW_description	  = description
		self.HW_idCategory    = idCategory
		self.HW_weight        = weight
		self.HW_idUserHistory = idUserHistory 

	def __repr__(self):
		'''Representacion en string de la Tarea'''
		return '<HW_ idTask  %r,HW_idCategory %r, HW_weight %r ,HW_idUserHistory %r>' % (self.HW_idTask,self.HW_idCategory,self.HW_weight,self.HW_idUserHistory)		
		
class clsCategory(db.Model):
	'''Clase que define el modelo de la tabla Category'''
	
	__tablename__ = 'category'
	C_idCategory      = db.Column(db.Integer, primary_key = True, index = True)
	C_nameCate     	  = db.Column(db.String(50),unique = True , index = True)
	C_weight          = db.Column(db.Integer, index = True) 
	C_refTaskCategory = db.relationship('clsTask', backref = 'category',lazy = 'dynamic', cascade = "all, delete, delete-orphan")

	def __init__(self,nameCate,weight):
		self.C_nameCate	  = nameCate
		self.C_weight     = weight 

	def __repr__(self):
		'''Representacion en string de la Categoria'''
		return '<C_idCategory  %r, C_nameCate %r, C_weight %r>' % (self.C_idCategory,self.C_nameCate,self.C_weight)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
db.create_all() # Creamos la base de datos
