from flask import render_template, request, flash, redirect, url_for
from app import app
from game import parseUserInput
from classes import Room, Person, Item, GameState, directions
from map import startRoom


def formatText(text):
    text = text.split('\n')
    ret = ''
    for t in text:
        ret += '<p>%s</p>\n' % t
    return str(ret)

@app.route('/')
@app.route('/index')
def index():
    G = app.config['Game']
    return render_template('index.html', G=G)

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def my_form_post():
    userInput = request.form['text'].lower().split()
    G = app.config['Game']
    parseUserInput(G, userInput)
    if len(app.config['stdout'].getvalue()) != app.config['stdoutLength']:
        flash(app.config['stdout'].getvalue()[app.config['stdoutLength']:])
    app.config['stdoutLength'] = len(app.config['stdout'].getvalue())
    return render_template('index.html', G=G)

@app.route('/newgame')
def newGame():
    P = Person()
    G = GameState(P, startRoom)
    app.config['Game'] = G
    return redirect(url_for('index'))