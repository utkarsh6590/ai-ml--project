import pandas as pd

def backtest(test,features,log_model,rf_model,scaler):

    X=test[features]
    X_scaled=scaler.transform(X)

    log_probs=log_model.predict_proba(X_scaled)[:,1]
    log_signal=(log_probs>0.60).astype(int)
    log_returns=test["Return"]*pd.Series(log_signal,index=test.index).shift(1)
    log_returns.fillna(0,inplace=True)
    cum_log=(1+log_returns).cumprod()

    rf_probs=rf_model.predict_proba(X)[:,1]
    rf_signal=(rf_probs>0.60).astype(int)
    rf_returns=test["Return"]*pd.Series(rf_signal,index=test.index).shift(1)
    rf_returns.fillna(0,inplace=True)
    cum_rf=(1+rf_returns).cumprod()

    market=(1+test["Return"]).cumprod()

    return cum_log,cum_rf,market