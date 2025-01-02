import stockClass
import cleaner

# Define stock tickers to track and create ticker object for each
Stock_List = ["AAPl", "TSLA", "F", "VOO", "INTL", "NVDA", "CMG", "AMZN", "MSFT", "JPM", "PLTR", "GOOGL", "META", "T", "VZ", "GOLD", "COP", "EOG", "CNQ"]
Stock_Tickers = {x : stockClass.Stock(x) for x in Stock_List}

# Define global CSV files to write data in and wipe after data is sent to database
historyFile = 'history.csv'
actionsFile = 'actions.csv'
financialsFile = 'financials.csv'

# Use stockClass to pull each attribute from given stock
def fetch_data(stock):
    # Save historical data to the history csv file
    history = stock.get_history()
    # Save action data to the actions csv file
    actions = stock.get_actions()         
    # Save financial data to the financials csv file
    financials = stock.get_financials()
    
    # Return important stock data
    return history, actions, financials

# Function that uses cleaner module on fetched data to have it preprocessed and transformed
def transformer(data):
    pass

# Function to move tranformed data to database

# Run functions and print statements
if __name__ == "__main__":
    # Terminal prompts for program backend
    for item in Stock_List:
        print(f"fetching {item} data...")
        stock_data = fetch_data(item)
        
        print(F"Cleaning and preprocessing {item} data...")
        stockHist = transformer(stock_data[0])
        stockActs = transformer(stock_data[1])
        stockFins = transformer(stock_data[2])
        
        stockHist.to_csv()
        stockActs.to_csv()
        stockFins.to_csv()
        print(f"Sending {item} data to database...")
        # Run function to send csv files to SQL database
        
        # Wipe the csv files
        with open(historyFile, 'w', newline='') as history:
            pass
        with open(actionsFile, 'w', newline='') as actions:
            pass
        with open(financialsFile, 'w', newline='') as financials:
            pass
        
        
        
    