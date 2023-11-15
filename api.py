#Lib requests utilizado para fazer requisições http
import requests
#Lib json usada para transformar requisições em json
import json
#Atribuindo a variavel cotação uma requisição a APi do awesome api que no mesmo busca cotações de varias moedas
cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Atribuindo a essa requisição no site um formato json 
cotacao = cotacao.json()
#MOstrando na tela as cotações em formato json
print(cotacao) 
# {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '4.8659', 'low': '4.861', 'varBid': '-0.0044', 'pctChange': '-0.09', 'bid': '4.86', 'ask': '4.862', 'timestamp': '1700047859', 'create_date': '2023-11-15 08:30:59'},
#  'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '5.2937', 'low': '5.2627', 'varBid': '-0.0176', 'pctChange': '-0.33', 'bid': '5.2687', 'ask': '5.2767', 'timestamp': '1700068517', 'create_date': '2023-11-15 14:15:17'}, 
# 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '178949', 'low': '171743', 'varBid': '784', 'pctChange': '0.44', 'bid': '178499', 'ask': '178507', 'timestamp': '1700068531', 'create_date': '2023-11-15 14:15:31'}}


cotacao_dolar =cotacao["USDBRL"]["bid"]
print(cotacao_dolar)


