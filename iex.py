import pandas as pd

import requests

import yfinance as yf



def get_prices(symbol,start,end):
    return yf.download(symbol,start,end)

def get_company(symbol):
    return yf.Ticker(symbol).info

r = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=bp498tfrh5rfu45ksgqg')

companies = [{"label": i["description"], "value": i["symbol"]} for i in r.json()]
