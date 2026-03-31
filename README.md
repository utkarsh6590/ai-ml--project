# AI-Based Stock Trading Strategy using Machine Learning

## Overview
This project builds a machine learning–based system to predict stock price movement (up or down) and generate trading signals accordingly. It uses historical market data, derives technical indicators, trains predictive models, and evaluates performance through backtesting.

The goal is to explore how well simple ML models can support trading decisions when combined with standard financial indicators.

---

## Objectives
- Predict next-day stock price direction  
- Develop a rule-based trading strategy using model predictions  
- Evaluate performance against a basic market benchmark  

---

## Features
- **Machine Learning Models**
  - Logistic Regression  
  - Random Forest  

- **Technical Indicators**
  - Moving Averages (MA5, MA10)  
  - Relative Strength Index (RSI)  
  - Volatility  
  - Momentum  

- **Backtesting**
  - Simulates trading strategy on historical data  
  - Tracks returns over time  

- **Visualization**
  - Plots cumulative returns and performance trends  

- **CLI Support**
  - Run training and testing from the command line  

---

## Project Structure
stock-ml-project/
│
├── src/
│   ├── data_loader.py      # Load and preprocess stock data
│   ├── features.py         # Feature engineering and indicators
│   ├── train.py            # Model training and evaluation
│   ├── backtest.py         # Strategy backtesting
│
├── models/                 # Saved trained models
├── app.py                  # Entry point for running the project
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── report.pdf              # Detailed analysis (optional)

---

## Installation
Clone the repository and install dependencies:

git clone <your-repo-link>
cd stock-ml-project
pip install -r requirements.txt

---

## Usage

### 1. Train the Model
python src/train.py

### 2. Run Backtesting
python src/backtest.py

### 3. Run the Application
python app.py

---

## How It Works
1. Data Loading  
   Historical stock data is loaded and cleaned.

2. Feature Engineering  
   Technical indicators such as moving averages, RSI, and momentum are computed.

3. Model Training  
   Machine learning models are trained to classify whether the next day’s price will go up or down.

4. Prediction & Signals  
   Predictions are converted into buy/sell signals.

5. Backtesting  
   The strategy is tested on past data to evaluate performance.

---

## Results
Results may vary depending on:
- Stock dataset used  
- Time period  
- Model parameters  

Performance can be improved by tuning hyperparameters, adding new features, or using more advanced models.

---

## Future Improvements
- Add advanced models (XGBoost, LSTM)  
- Include transaction costs and slippage in backtesting  
- Improve feature engineering with additional indicators  
- Deploy as a web-based dashboard  

---

## Disclaimer
This project is for educational purposes only. It does not constitute financial advice or guarantee profits in real-world trading.
