# -*- coding: utf-8 -*-. 

# Se importan las librerias necesarias.
import os
import sys
from flask                 import Flask
from flask.ext.migrate     import Migrate, MigrateCommand
from flask.ext.sqlalchemy  import SQLAlchemy
from flask.ext.script      import Manager
#from sqlalchemy.sql.schema import CheckConstraint


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

# Declaracion del modelo Role
class clsRole(db.Model):
    '''Clase que define el modelo Role'''

    __tablename__ = 'roles'
    idrole    = db.Column(db.Integer, primary_key=True)
    namerole  = db.Column(db.String(50), unique=True)
    user_role = db.relationship('clsUser',backref='role',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    #CheckConstraint(namerole in ('Product Owner','Scrum Master', 'Team member'), name='check_namerole')
      
   
    def __init__(self, idrole, namerole):
        '''Constructor del modelo Role'''
        self.idrole   = idrole
        self.namerole = namerole

    def __repr__(self):
        '''Respresentacion en string del nombre del Role'''
        return '<Role %r>' % self.namerole


class clsUser(db.Model):
    '''Clase que define el modelo Usuario'''
 
    __tablename__ = 'user'
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(16), primary_key = True, index = True)
    password = db.Column(db.String(200))
    email    = db.Column(db.String(30), unique = True)
    id_role  = db.Column(db.Integer, db.ForeignKey('roles.idrole'))

    def __init__(self, fullname, username, password, email, idrole):
        '''Constructor del modelo usuario'''
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email    = email
        self.idrole   = idrole
   
    def __repr__(self):
        '''Representacion en string del nombre de Usuario'''
        return '<username %r, email %r>' % (self.username, self.email)
       
# Declaracion del modelo Objective
class clsObjective(db.Model):
    '''Clase que define el modelo Objective'''

    __tablename__  = 'objectives'
    idobjective    = db.Column(db.Integer, primary_key=True)
    descObjective  = db.Column(db.String(140), unique=True)
    id_backlog     = db.Column(db.Integer, db.ForeignKey('backLog.id_backLog'))
    
   
    def __init__(self, descObjective, id_backlog):
        '''Constructor del modelo Objective'''
        self.descObjective = descObjective
        self.id_backlog    = id_backlog

    def __repr__(self):
        '''Respresentación en string de la descripción del Objective'''
        return '<Id %r>, <Descripcion %r>' %(self.idobjective, self.descObjective)


class clsBackLog(db.Model):
	'''Clase que define el modelo BackLog'''
	
	__tablename__ =  'backLog'
	id_backLog = db.Column(db.Integer,primary_key = True, index = True)	
	BL_name = db.Column(db.String(140), unique = True)
	obj_backLog = db.relationship('clsObjective',backref='objective',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
	#act_backLog = db.relationship('clsActor',backref='actors',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
	
	def __init__(self, BL_name):
		'''Constructor del modelo BackLog'''
		self.BL_name = BL_name
		
	def __repr__(self):
		'''Representacion en string del nombre del BakcLog'''
		return '<id_backLog %r, BL_nombre %r>' % (self.id_backLog, self.BL_name)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

#db.drop_all()   # Borramos la base de datos
db.create_all() # Creamos la base de datos

