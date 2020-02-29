import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from flask import Flask
from classes import Room, Person, Item, GameState, directions
from map import startRoom
P = Person()
G = GameState(P, startRoom)

app = Flask(__name__)
app.config['Game'] = G
app.config['Directions'] = directions
from app import routes
