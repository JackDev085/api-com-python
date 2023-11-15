import requests
import json

req = requests.get('https://python--computadordb.repl.co/pegarvendas')
total= req.json()
dicionario= req.json()
print(dicionario["Vendas totais"])