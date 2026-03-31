import yfinance as yf

def data_load(ticker="TCS.NS",start="2020-01-01",end="2026-03-25"):
 data=yf.download("TCS.NS",start=start,end=end)

 if data.empty:
  raise ValueError(f"No data found for{ticker}")
 
 return data
