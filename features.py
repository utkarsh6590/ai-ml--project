import numpy as np

def add_features(data):

 data["Return"]=data["Close"].pct_change()
 data["Prev_Return"]=data["Return"].shift(1)
 data["MA5"]=data["Return"].rolling(5).mean()
 data["MA10"]=data["Return"].rolling(10).mean()
 data["Volatility"]=data["Return"].rolling(5).std()
 data["Momentum"]=data["Close"]-data["Close"].shift(5)

 delta=data["Close"].diff()
 gain=(delta.where(delta>0,0)).rolling(14).mean()
 loss=(delta.where(delta<0,0)).rolling(14).mean()
 rs=gain/loss
 data["RSI"]=100-(100/(1+rs))

 data["Direction"]=(data["Return"].shift(-1)>0).astype(int)

 data.dropna(inplace=True)

 return data

  