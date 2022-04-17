import uvicorn
from fastapi import FastAPI
from functions.myfn import downloader,converter
import yfinance as yf

description = """
    # valid ticker:https://yfinanceapi.hasindusithmin.repl.co
    # valid intervals:5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
"""

app = FastAPI(
    title="yfinance API",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "hasindu sithmin",
        "email": "hasindusithmin64@gmail.com",
        "linkedin":"https://www.linkedin.com/in/hasindu-sithmin-9a1a12209/",
        "github":"https://github.com/hasindusithmin/"
    },
)

names = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'NZD/USD', 'EUR/JPY', 'GBP/JPY', 'EUR/GBP', 'EUR/CAD', 'EUR/SEK', 'EUR/CHF', 'EUR/HUF', 'EUR/JPY', 'USD/CNY', 'USD/HKD', 'USD/SGD', 'USD/INR', 'USD/MXN', 'USD/PHP', 'USD/IDR', 'USD/THB', 'USD/MYR', 'USD/ZAR', 'USD/RUB']
symbol= ['EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'NZDUSD=X', 'EURJPY=X', 'GBPJPY=X', 'EURGBP=X', 'EURCAD=X', 'EURSEK=X', 'EURCHF=X', 'EURHUF=X', 'EURJPY=X', 'CNY=X', 'HKD=X', 'SGD=X', 'INR=X', 'MXN=X', 'PHP=X', 'IDR=X', 'THB=X', 'MYR=X', 'ZAR=X', 'RUB=X']

@app.get("/")
def root():
    return list(
        zip(
            names,symbol
        )
    )

@app.get("/data/{currency}/{interval}")
def forex(currency:str,interval:str):
    return converter(
        downloader(
            ticker=currency, 
            interval=interval
        )
    )

@app.get("/news/{currency}")
def get_news(currency:str):
    return yf.Ticker(currency).news

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000
    )
