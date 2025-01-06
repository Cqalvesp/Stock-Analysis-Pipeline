import stockClass as stck
import cleaner as cl

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

# Function to move tranformed data to database
def data_transfer():
    pass

# Run functions and print statements
if __name__ == "__main__":
    # Terminal prompts for program backend
    for item in stck.Stock_List:
        print(f"fetching {item} data...")
        stock_data = fetch_data(stck.Stock_Tickers[item])
        
        print(F"Cleaning and preprocessing {item} data...")
        stockHist = cl.clean_hist(stock_data[0])
        stockActs = cl.clean_acts(stock_data[1])
        stockFins = cl.clean_fins(stock_data[2])
        
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
        
    print("The database can now be inspected.")
        
        
        
    