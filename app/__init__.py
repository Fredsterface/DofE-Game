import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from flask import Flask
from classes import Room, Person, Item, GameState, directions
from map import startRoom
from io import StringIO

app = Flask(__name__)
app.secret_key = 'Prince Philip is my hero'

P = Person()
G = GameState(P, startRoom)
app.config['Game'] = G
app.config['Directions'] = directions
sys.stdout = app.config['stdout'] = StringIO()
app.config['stdoutLength'] = len(app.config['stdout'].getvalue())
from app import routes
