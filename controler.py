from app import app
import os
from flask import Flask, request, jsonify, send_from_directory
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = '/controlFlak'

ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        # verifique se a solicitacao de postagem tem a parte do arquivo
        if 'file' not in request.files:
            flash('Nao tem a parte do arquivo')
            return redirect(request.url)
        file = request.files['file']
        
        # Se o usuario nao selecionar um arquivo, o navegador envia um
        # arquivo vazio sem um nome de arquivo.
        
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))

    @app.route('/uploads/<name>')
    def download_file(name):
                 return send_from_directory(app.config["UPLOAD_FOLDER"], name)

    if __name__ == '__main__':
                app.run(debug = True)