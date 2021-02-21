"""
Calculations Module
-------------------------------

Financial calculations module which acts upon a Pandas DataFrame object containing information about assets. A set of 
various computations for this data is defined here.

NOTE: All functions within this module will operate under the assumption that the DataFrame instance indicates closing
        prices of assets.
"""

def calculate_daily_returns(df):
    """
    Calculates the daily returns on closing prices.

    :param df: Closing prices.
    :type df: Pandas DataFrame.
    """
    daily_returns_df = df.pct_change().dropna()
    return daily_returns_df

def calculate_average_annual_returns(daily_return_df):
    """
    Calculates the annual returns on daily returns.
    Must only be ran after calculate_daily_returns() method has been called.

    :param df: Daily returns.
    :type df: Pandas DataFrame.
    """
    average_annual_returns_df = (daily_return_df.mean() * 252)
    return average_annual_returns_df

def calculate_average_annual_volatility(daily_return_df):
    """
    Calculates the annual volatility on daily returns. 
    Must only be ran after calculate_daily_returns() method has been called.

    :param df: Daily returns.
    :type df: Pandas DataFrame. 
    """
    average_annual_volatility_df = (daily_return_df.std() * 252**(1/2))
    return average_annual_volatility_df
