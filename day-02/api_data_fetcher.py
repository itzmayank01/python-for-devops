import requests
api_key="825VJ0X6POTC4O0G"

api_url="https://www.alphavantage.co/"

symbol=input("Enter the ccompany symbol")

interval="5min"
query= f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

print(api_url+query)

def get_stock_market_data():
    
    response= requests.get(url=api_url+query)
    print(response.json())
    
get_stock_market_data()