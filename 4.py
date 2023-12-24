from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

# Replace YOUR_API_KEY with your actual Alpha Vantage API key
api_key = 'YOUR_API_KEY'

# Initialize the TimeSeries object
ts = TimeSeries(key=api_key, output_format='pandas')

# List of stock symbols
stocks = ['AAPL', 'GOOGL', 'MSFT']  # Add more stock symbols as needed

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate through the list of stocks and get their data
for symbol in stocks:
    # Make an API call to get the stock data
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    
    # Add a new column with the stock symbol
    data['Company'] = symbol
    
    # Concatenate the data with the combined_data DataFrame
    combined_data = pd.concat([combined_data, data])
    
    # Pause for a few seconds to avoid hitting API rate limits
    time.sleep(5)

# Print the combined data with stock symbols
print(combined_data)
