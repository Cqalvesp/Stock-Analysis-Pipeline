import stockClass

# Define stock tickers to track and create ticker object for each
Stock_List = ["AAPl", "TSLA", "F", "VOO", "INTL", "NVDA", "CMG", "AMZN", "MSFT", "JPM", "PLTR", "GOOGL", "META", "T", "VZ", "GOLD", "COP", "EOG", "CNQ"]
Stock_Tickers = {x : stockClass.Stock(x) for x in Stock_List}

# Use stockClass to pull each attribute from every ticker in list

# Run data from each ticker separately through the cleaner module

# Send tranformed data to database