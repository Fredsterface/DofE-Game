from flask import render_template, request
from app import app
from game import parseUserInput

def formatText(text):
    text = text.split('\n')
    ret = ''
    for t in text:
        ret += '<p>%s</p>\n' % t
    return str(ret)

@app.route('/')
def index():
    print(1)
    G = app.config['Game']
    return render_template('index.html', G=G)

@app.route('/', methods=['POST'])
def my_form_post():
    userInput = request.form['text'].lower().split()
    G = app.config['Game']
    parseUserInput(G, userInput)
    return render_template('index.html', G=G)
