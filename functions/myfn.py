import yfinance as yf
from datetime import datetime
def downloader(ticker,interval):
  period = None
  short = ["5m","15m","30m","1h"]
  period = "1mo" if interval in short else "max"
  df =  yf.download(
    # tickers list or string as well
    tickers = ticker,

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period = period,

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals:5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval = interval
  )
  return df.reset_index()

def converter(df):
  data = []
  for index, row in df.iterrows():
    candle = {}
    unix = int(
        datetime.timestamp(
        row["Datetime"]
    ) + 19800
    )
    candle.update({
        "time": unix,
        "open": row["Open"],
        "high": row["High"],
        "low": row["Low"],
        "close": row["Close"]
    })
    data.append(
        candle
    )
  return data
