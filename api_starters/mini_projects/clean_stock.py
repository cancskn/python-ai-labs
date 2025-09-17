import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_KEY")


class StockMarket:
    url = "https://www.alphavantage.co/query"

    def __init__(self, stock_name="", api_key="demo", function="TIME_SERIES_DAILY"):
        self.stock_name = stock_name
        self.api_key = api_key
        self.function = function

    def get_data(self):
        self.stock_name = input("Stock Name :")
        response = requests.get(
            f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock_name}&apikey=API_KEY")
        data = response.json()["Time Series (Daily)"]
        data_list = [value for key, value in data.items()]
        yesterday = data_list[0]['4. close']
        the_day_before = data_list[1]['4. close']
        # print(f"yesterday stock price was {yesterday}\nthe day before yesterday stock price was {the_day_before}")

        for value in data.values():
            print(value['4. close'])


IBM_data = StockMarket()
IBM_data.get_data()