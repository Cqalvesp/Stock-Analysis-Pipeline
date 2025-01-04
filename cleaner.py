# Necessary library imports
import numpy as np
import pandas as pd

# Function to preprocess and transform historical data
def clean_hist(history):
    # Place fetched data into dataframe
    df = pd.DataFrame(history)
    
    # Remove 'Dividends' and 'Stock Splits' columns because they are always empty
    del df['Dividends']
    del df['Stock Splits']
    return df

def clean_acts(actions):
    # Place fetched data into dataframe
    df = pd.DataFrame(actions)
    return df

def clean_fins(financials):
    # List of prefixes for rows to drop
    dropped_rows = ['Tax Effect Of Unusual Items', 'Tax Rate For Calcs', 'Normalized EBITDA', 
                    'Reconciled Depreciation', 'Reconciled Cost Of Revenue', 'Net Interest Income', 'Interest Expense', 
                    'Interest Income', 'Normalized Income', 'Total Operating Income As Reported', 'Diluted Average Shares',
                    'Basic Average Shares', 'Diluted EPS', 'Basic EPS', 'Diluted NI Availto Com Stockholders', 'Net Income Common Stockholders',
                    'Selling General And Administration', 'Interest Income Non Operating', 'Interest Expense Non Operating', 
                    'Net Non Operating Interest Income Expense', 'Other Non Operating Income Expenses', 'Net Income Including Noncontrolling Interests',
                    'Net Income Continuous Operations']
    
    # Place fetched financials into data frame
    df = pd.DataFrame(financials)
    # Remove rows from the data frame that won't be used in analysis
    for item in dropped_rows:
        df = df[~df.index.str.startswith(item)]
    return df
