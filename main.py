import uvicorn
from fastapi import FastAPI
from functions.myfn import downloader,converter


description = """
    https://api.domain.com/{ticker}/{interval}
    # valid ticker:EURUSD,AUDUSD,GBPUSD,NZDUSD,EURJPY,GBPJPY,EURGBP,EURCAD,EURSEK...()
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

@app.get("/")
def root():
    return "welcome to finance api"

@app.get("/forex/{currency}/{interval}")
def forex(currency:str,interval:str):
    return converter(
        downloader(
            ticker=currency, 
            interval=interval
        )
    )
    

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000
    )
