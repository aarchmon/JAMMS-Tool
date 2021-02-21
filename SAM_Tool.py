import sys
import fire
import pandas as pd 
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Import profiler functions.
from include.profiler import get_info
from include.profiler import qualification
from include.profiler import risk_profile

# Import data retrieval.
from include.data_retrieval import import_asset_data
from include.data_retrieval import format_close_price

# Import calculation functions.
from include.calculations import calculate_average_annual_returns
from include.calculations import calculate_average_annual_volatility
from include.calculations import calculate_daily_returns
from include.calculations import calculate_sharpe_ratio

# Client information.
cash = 0
assets = 0
income = 0
liquidity = 0
net_worth = 0
risk_prof = ""

# Tickers.
timeframe = "1D"
tickers = ["AGG", "SPY"]
start_date = "2010-06-01"
end_date = "2020-06-01"
                  
def run():
    """The main function for running the script."""

    # Get investor's information
    cash, assets, income, liquidity = get_info()

    # Determine qualifying investable amount
    net_worth = qualification(cash, assets, income, liquidity)
                  
    # Determine investor's risk profile by determining ability to take risk defined by investment time horizon (age) and willingness to risk defined by comfort level with loss
    risk_prof = risk_profile()

    # Import historical financial data and retrieve closing prices.
    raw_data_df = import_asset_data(start_date, end_date, tickers, timeframe)
    raw_data_close_df = format_close_price(raw_data_df, tickers)

    # Retrieve average annual returns and average annual volatility.
    daily_returns_df = calculate_daily_returns(raw_data_close_df)
    average_annual_returns_df = calculate_average_annual_returns(daily_returns_df)
    average_annual_volatility_df = calculate_average_annual_volatility(daily_returns_df)

    # Calculate Sharpe Ratios. 
    print(calculate_sharpe_ratio(average_annual_returns_df, average_annual_volatility_df))

    sys.exit()

if __name__ == "__main__":
    fire.Fire(run)