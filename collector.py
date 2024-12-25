# File to pull data from Yahoo Finance API
# Retrieves data based on given financial metrics
# Pulled data: Current stock price, number of splits, dividend rates, company valuation, etc.
import yfinance as yf

# Stock object
class Stock:
    def __init__(self, sym: str):
        pass
     
    # Method to fetch stock's financials   
    def financials(self):
        pass
    
    # Method to fetch stock's historical data
    def historical_data(self):
        pass
    
    # Method to fetch stock's actions like dividends and splits
    def actions(self):
        pass
    
aapl = Stock("AAPL")
print(aapl.financials)
    
    
    