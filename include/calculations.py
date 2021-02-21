"""
Calculations Module
-------------------------------

Financial calculations module which acts upon a Pandas DataFrame object containing information about assets. A set of 
various computations for this data is defined here.

NOTE: All functions within this module will operate under the assumption that the DataFrame instance indicates closing
        prices of assets.
"""
# tickers = ["SPY", "AGG", "BTC"]
# weights {}        
conservative_weight = [0.1, 0.9, 0]
moderately_conservative_weight = [0.25, 0.7, 0.05]
moderate_weight = [0.6, 0.3, 0.1]
moderately_aggressive_weight = [0.75, 0.2, 0.15]
aggressive_weight = [0.8, 0, 0.2]

def calculate_daily_returns(closing_prices_df):
    """
    Calculates the daily returns on closing prices.

    :param df: Closing prices.
    :type df: Pandas DataFrame.
    """
    daily_returns_df = closing_prices_df.pct_change().dropna()
    return daily_returns_df
    

def calculate_average_annual_returns(avg_annual_returns_df):
    """
    Calculates the annual returns on daily returns.
    Must only be ran after calculate_daily_returns() method has been called.

    :param df: Daily returns.
    :type df: Pandas DataFrame.
    """
    avg_annual_returns_df = (daily_returns_df.mean() * 252)
    return avg_annual_returns_df

def calculate_average_annual_volatility(avg_annual_returns_df_df):
    """
    Calculates the annual volatility on daily returns. 
    Must only be ran after calculate_daily_returns() method has been called.

    :param df: Daily returns.
    :type df: Pandas DataFrame. 
    """
    avg_annual_volatility_df = (avg_annual_returns_df.std() * np.sqrt(250)
    return avg_annual_volatility_df

def calculate_average_sharpe_ratio(avg_annual_returns_df, avg_annual_volatility_df):
    """
    Calculates the Sharpe Ratio of a given portfolio.
    Must only be ran after calculate_daily_returns(), calculate_average_annual_returns()
    calculate_average_annual_volatility() methods have been called. 

    :param avg_annual_returns_df: Average annual returns.
    :param avg_annual_volatility_df: Average annual volatility.
    :type avg_annual_returns_df: Pandas DataFrame.
    :type avg_annual_volatility_df: Pandas DataFrame.
    """
    avg_annual_sharpe_ratio_df = avg_annual_returns_df / avg_annual_volatility_df
    return avg_annual_sharpe_ratio_df


# Creating expected return of portfolio for each risk porfile                          
conservative_portfolio_return = (avg_annual_returns_df * conservative_weight).sum()
moderately_conservative_portfolio_return = (avg_annual_returns_df * moderately_conservative_weight).sum()
moderate_portfolio_return = (avg_annual_returns_df * moderate_weight).sum()
moderately_aggressive_portfolio_return = (avg_annual_returns_df * moderately_aggressive_weight).sum()
aggressive_portfolio_return = (avg_annual_returns_df * aggressive_weight).sum()
                                
# Creating volatility of portfolio for each risk porfile  
conservative_portfolio_vol =
moderately_conservative_portfolio_vol =
moderate_portfolio_vol = 
moderately_aggressive_portfolio_vol = 
aggressive_portfolio_vol =                     
                                
# Creating Sharpe Ratio of portfolio for each risk porfile  
conservative_portfolio_sharpe =
moderately_conservative_portfolio_sharpe =
moderate_portfolio_sharpe = 
moderately_aggressive_portfolio_sharpe = 
aggressive_portfolio_sharpe =   