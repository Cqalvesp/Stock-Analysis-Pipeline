import stockClass
import csv

# Define stock tickers to track and create ticker object for each
Stock_List = ["AAPl", "TSLA", "F", "VOO", "INTL", "NVDA", "CMG", "AMZN", "MSFT", "JPM", "PLTR", "GOOGL", "META", "T", "VZ", "GOLD", "COP", "EOG", "CNQ"]
Stock_Tickers = {x : stockClass.Stock(x) for x in Stock_List}

# Use stockClass to pull each attribute from every ticker in list
def write_to_csv():
    # CSV file path for function to write data
    csv_file = 'stockdata.csv'
    # Open CSV file in write mode
    with open(csv_file, mode = 'w', newline = '') as file:
        # Create object to write to CSV file
        pencil = csv.writer(file)
        
    # For loop to iterate over every stock ticker and write data for each into CSV file
    for stock in Stock_Tickers:
        pencil.writerows(stock.historical_data)

# Run data from each ticker separately through the cleaner module

# Send tranformed data to database