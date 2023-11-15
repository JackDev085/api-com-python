import pandas as pd
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello world"

@app.route("/pegarvendas")
def pegarvendas():
  tabela = pd.read_csv('db.csv')
  total_vendas = tabela['Vendas'].sum()
  total = {'Vendas totais' : total_vendas}
  return jsonify(total)


app.run(host = '0.0.0.0')
#tabela = pd.read_csv('db.csv')
#total_vendas = tabela['Vendas'].sum()
#print(int(total_vendas))