
from app import app
from flask import render_template
from tap import PeixeStock


@app.route('/')
@app.route('/index')




def index():
    nome=PeixeStock
    return render_template('index.html',n=nome)















