from flask import render_template, request, flash, redirect, url_for
from flask import current_app as app
from flask import session
from game import parseUserInput
from classes import Room, Person, Item, GameState, directions
from map import startRoom
from io import StringIO
import sys


def formatText(text):
    text = text.split('\n')
    ret = ''
    for t in text:
        ret += '<p>%s</p>\n' % t
    return str(ret)

@app.route('/')
@app.route('/index')
def index():
    if 'Game' not in session.keys():
        return redirect(url_for('newGame'))
    G = session['Game']
    return render_template('index.html', G=G)

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def my_form_post():
    if 'Game' not in session.keys():
        return redirect(url_for('newGame'))
    userInput = request.form['text'].lower().split()
    G = session['Game']
    parseUserInput(G, userInput)
    if len(session['stdout'].getvalue()) != session['stdoutLength']:
        flash(session['stdout'].getvalue()[session['stdoutLength']:])
    session['stdoutLength'] = len(session['stdout'].getvalue())
    return render_template('index.html', G=G)

@app.route('/newgame')
def newGame():
    print(app.secret_key)
    print(session)
    P = Person()
    G = GameState(P, startRoom)
    session['Game'] = G
    session['Directions'] = directions
    sys.stdout = session['stdout'] = StringIO()
    session['stdoutLength'] = len(session['stdout'].getvalue())
    return redirect(url_for('index'))