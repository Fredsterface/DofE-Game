from flask import Flask
from classes import Room, Person, Item, GameState, directions
from map import rooms
P = Person()
G = GameState(P, rooms[1])

app = Flask(__name__)
app.config['Game'] = G
app.config['Directions'] = directions
from app import routes
