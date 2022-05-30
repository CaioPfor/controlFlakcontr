#!C:\Users\caio\AppData\Local\Programs\Python\Python38\python.exe
from re import T
import pandas as pd
import os
from flask import Flask, request, jsonify, send_from_directory

print("content-type: text/html\n\n" )



entrada =pd.read_excel("entrada.xlsx")
entrada.to_html("entrada.html")
arq= open("entrada.html","w")
#print(tabela.to_html())

arq.write(entrada.to_html())

##########################################3

saida =pd.read_excel("saida.xlsx")
saida.to_html("saida.html")
arq= open("saida.html","w")
#print(tabela.to_html())

arq.write(saida.to_html())







print(entrada.to_html())
print(saida.to_html())



PeixeStock=(entrada['quantidade'].values[0]-saida['quantidade'].values[0])

CarneStock=(entrada['quantidade'].values[1]-saida['quantidade'].values[1])

LegumesStock=(entrada['quantidade'].values[2]-saida['quantidade'].values[2])



print(PeixeStock)
print(CarneStock)
print(LegumesStock)

#OBJETIVO 1- DIMINUIR VALORES DE PRODUTO DA ENTRADA POR SAIDA(Eprodutos-Sproduto) NA TABELA,
#produto nomeId = produto, valor


DIRETORIO = "C:\\xampp\\htdocs\\controlFlak"

api = Flask(__name__)


@api.route("/arquivos", methods=["GET"])
def lista_arquivos():
    arquivos = []

    for nome_do_arquivo in os.listdir(DIRETORIO):
        endereco_do_arquivo = os.path.join(DIRETORIO, nome_do_arquivo)

        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)

    return jsonify(arquivos)


@api.route("/arquivos/<nome_do_arquivo>",  methods=["GET"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(DIRETORIO, nome_do_arquivo, as_attachment=True)


@api.route("/arquivos", methods=["POST"])
def post_arquivo():
    arquivo = request.files.get("meuArquivo")

    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))

    return '', 201


if __name__ == "__main__":
    api.run(debug=True, port=5000)