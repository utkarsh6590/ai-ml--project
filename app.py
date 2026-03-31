import argparse
import matplotlib.pyplot as plt

from src.data import data_load
from src.features import add_features
from src.train import train_models
from src.backtest import backtest

def main():

    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=["train","run"],required=True)
    args=parser.parse_args()

    data=data_load()
    data=add_features(data)

    train=data[data.index<"2023-01-01"]
    test=data[data.index>="2023-01-01"]

    features=["Prev_Return","MA5","MA10","Volatility","Momentum","RSI"]

    log_model,rf_model,scaler=train_models(train,test,features)

    if args.mode=="run":

        cum_log,cum_rf,market=backtest(test,features,log_model,rf_model,scaler)

        print("\nFinal Returns:")
        print("Logisticc:",cum_log.iloc[-1]-1)
        print("RF:",cum_rf.iloc[-1]-1)
        print("Market:",market.iloc[-1]-1)

        plt.plot(cum_log,label="Logistic")
        plt.plot(cum_rf,label="RF")
        plt.plot(market,label="Market")
        plt.legend()
        plt.title("Strategy Comparison")
        plt.show()

if __name__=="__main__":
    main()




