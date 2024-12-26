# File to pull data from Yahoo Finance API
# Retrieves data based on given financial metrics
# Pulled data: Current stock price, number of splits, dividend rates, company valuation, etc.
import yfinance as yf

# Stock object
class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
     
    # Method to fetch stock's financials   
    def financials(self):
        return self.ticker.financials
    
    # Method to fetch stock's historical data
    def historical_data(self):
        return self.ticker.history(period="1mo")
    
    # Method to fetch stock's actions like dividends and splits
    def actions(self):
        return self.ticker.actions
   

    
    
    