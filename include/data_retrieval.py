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

def import_stock_data(start, end, tickers, timeframe):
    """
    Import stock data via Alpaca API.

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
    load_dotenv("API_KEYS.env")

    # Retrieve ALPACA_API_KEY and ALPACA_SECRET_KEY.
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create Alpaca API object.
    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version = "v2"
    )

    # Format dates as ISO.
    start_date = pd.Timestamp(start, tz="America/New_York").isoformat()
    end_date = pd.Timestamp(end, tz="America/New_York").isoformat()

    # Retrieve and return data frame of stock data.
    stock_df = alpaca.get_barset(
        tickers,
        timeframe,
        start = start_date,
        end = end_date
    ).df

    return stock_df

