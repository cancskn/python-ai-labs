import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_KEY")

class StockMarket:
    def get_price(self):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        price = data["Global Quote"]["05. price"]
        return price

stock = StockMarket()
print("Tesla stock price:", stock.get_price())
