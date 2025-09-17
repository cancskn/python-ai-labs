import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_KEY")

class StockMarket:
    def get_price(self):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        price = data["Time Series (Daily)"]["2025-09-05"]["4. close"]
        return price

stock = StockMarket()
print("Tesla daily stock price:", stock.get_price())
