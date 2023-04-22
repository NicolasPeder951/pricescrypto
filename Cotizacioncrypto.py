import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY': apikey.key,
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    coins = data['data']
    for x in coins:
        symbol = x['symbol']
        price = x['quote']['USD']['price']
        print(symbol, price)
else:
    print('Error getting data from CoinMarketCap,Status Code HTTP:', response.status_code)
