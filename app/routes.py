
from app import app
from flask import render_template
from tap import PeixeStock
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify

@app.route('/')
@app.route('/index')




def index():
    nome=PeixeStock#aqui é o tap rolando.
    return render_template('index.html',n=nome)















