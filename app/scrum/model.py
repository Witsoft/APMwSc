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

# Declaracion del modelo actor
class clsActors(db.Model):
    '''Clase que define el modelo actor'''

    __tablename__ = 'actors'
    idactor    = db.Column(db.Integer, primary_key=True)
    nameactor  = db.Column(db.String(50), unique=True)
    actordescription = db.Column(db.String(140))
    id_pila = db.Column(db.Integer, db.ForeignKey('backLog.id_backLog'))
    user_actor = db.relationship('clsUser',backref='actor',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    
    #CheckConstraint(nameactor in ('Product Owner','Scrum Master', 'Team member'), name='check_nameactor')
      
   
    def __init__(self, nameactor,actordescription,id_pila):
        '''Constructor del modelo actor'''
        self.nameactor = nameactor
        self.actordescription = actordescription
        self.id_pila = id_pila

    def __repr__(self):
        '''Respresentacion en string del nombre del actor'''
        return '<actor %r>' % self.nameactor


class clsUser(db.Model):
    '''Clase que define el modelo Usuario'''
 
    __tablename__ = 'user'
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(16), primary_key = True, index = True)
    password = db.Column(db.String(200))
    email    = db.Column(db.String(30), unique = True )
    id_actor  = db.Column(db.Integer, db.ForeignKey('actors.idactor'))

    def __init__(self, fullname, username, password, email, idactors):
        '''Constructor del modelo usuario'''
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email    = email
        self.idactors   = idactors
   
    def __repr__(self):
        '''Representacion en string del nombre de Usuario'''
        return '<username %r, email %r>' % (self.username, self.email)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

#db.drop_all()   # Borramos la base de datos
db.create_all() # Creamos la base de datos