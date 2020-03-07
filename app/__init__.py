from flask import Flask, session, flash, redirect, url_for, render_template, request
from classes import Room, Person, Item, GameState, directions
from flask_session import Session
from game import parseUserInput
from map import startRoom
import os
import random
import string
from io import StringIO
import sys


def formatText(text):
    text = text.split('\n')
    ret = ''
    for t in text:
        ret += '<p>%s</p>\n' % t
    return str(ret)

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

app = Flask(__name__)
app.secret_key = os.urandom(25)
#sess = Session()
#sess.init_app(app)
DATA = {}

@app.route('/')
def index():
    if 'user' not in session.keys():
        return redirect(url_for('newGame'))
    G = DATA[session['user']]['Game']
    return render_template('index.html', G=G, Directions=DATA[session['user']]['directions'])

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def my_form_post():
    if 'user' not in session.keys():
        return redirect(url_for('newGame'))
    userInput = request.form['text'].lower().split()
    G = DATA[session['user']]['Game']
    parseUserInput(G, userInput)
    if len(DATA[session['user']]['stdout'].getvalue()) != DATA[session['user']]['stdoutLength']:
        flash(DATA[session['user']]['stdout'].getvalue()[DATA[session['user']]['stdoutLength']:])
    DATA[session['user']]['stdoutLength'] = len(DATA[session['user']]['stdout'].getvalue())
    return render_template('index.html', G=G, Directions=DATA[session['user']]['directions'])

@app.route('/newGame')
def newGame():
    session['user'] = randomString()
    P = Person()
    G = GameState(P, startRoom)
    DATA[session['user']] = { 'Game' : G, 'directions' : directions}
    sys.stdout = DATA[session['user']]['stdout'] = StringIO()
    DATA[session['user']]['stdoutLength'] = len(DATA[session['user']]['stdout'].getvalue())
    return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)