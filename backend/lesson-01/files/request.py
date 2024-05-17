import requests

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
data = response.json()

tax_dollar = float(data['USDBRL']['bid'])
print(f'A taxa do dolar é R$ {tax_dollar:.2f}')