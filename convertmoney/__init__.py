import requests

def convert_usd(currentcy,amount):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    currentcy = currentcy.upper()
    return data['rates'][currentcy] * float(amount)