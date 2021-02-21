"""
Data Retrieval Module
-------------------------------
Data retrieval module which imports up-to-date financial data via Alpaca API. This information will be used to carry out
a series of financial calculations.
"""

import os
import requests
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import numpy as np

def import_asset_data(start, end, tickers, timeframe):
    """
    Import asset data via Alpaca API.

    :param start: Start date of stock data.
    :param end: End date of stock data.
    :param tickers: List of stock tickers.
    :param timeframe: Timeframe of analysis.
    :type start: str as "YYYY-MM-DD" format.
    :type end: str as "YYYY-MM-DD" format.
    :type tickers: List of str values.
    :type timeframe: str of timeframe (i.e., "1D").
    :rtype stock_df: Pandas DataFrame. 
    """

    # Load .env environment variables.
    load_dotenv("./Resources/API_KEYS.env")

    # Retrieve ALPACA_API_KEY and ALPACA_SECRET_KEY.
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create Alpaca API object.
    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version = "v2"
    )

    # Create the list for the required tickers
    tickers = ["SPY", "AGG", "BTC"]
    
    # Format dates as ISO.
    start_date = pd.Timestamp(start, tz="America/New_York").isoformat()
    end_date = pd.Timestamp(end, tz="America/New_York").isoformat()

    # Set timeframe to one day (1D)
    timeframe = "1D"
    
    # Retrieve and closing prices data frame of assets.
    close_df = alpaca.get_barset(
        tickers,
        timeframe,
        start = start_date,
        end = end_date
    ).df

def format_close_price(df, tickers):
    """
    Formats a Pandas DataFrame such that only closing prices of assets are displayed.

    :param df: Numerical asset information.
    :param tickers: Tickers to extract closing price from.
    :type df: Pandas DataFrame.
    :type tickers: List of tickers as str data type.
    :rtype closing_prices_df: Modified Pandas DataFrame.
    """

    # Create an empty DataFrame to hold closing prices.
    closing_prices_df = pd.DataFrame()
    
    # For each ticker, retrieve closing prices and append to closing_prices_df.
    for ticker in tickers:
        closing_prices_df[ticker] = close_df[ticker]["close"]

    # Drop the time component of row date.
    closing_prices_df.index = closing_prices_df.index.date

