"""
Calculations Module
-------------------------------

Financial calculations module which acts upon a Pandas DataFrame object containing information about assets. A set of 
various computations for this data is defined here.

NOTE: All functions within this module will operate under the assumption that the DataFrame instance indicates closing
        prices of assets.
"""

def calculate_daily_returns(closing_prices_df):
    """
    Calculates the daily returns on closing prices.

    :param df: Closing prices.
    :type df: Pandas DataFrame.
    """
    daily_returns_df = closing_prices_df.pct_change().dropna()
    return daily_returns_df
    

def calculate_average_annual_returns(daily_returns_df):
    """
    Calculates the annual returns on daily returns.
    Must only be ran after calculate_daily_returns() method has been called.

    :param daily_returns_df: Daily returns.
    :type daily_returns_df: Pandas DataFrame.
    """
    avg_annual_returns_df = (daily_returns_df.mean() * 252)
    return avg_annual_returns_df

def calculate_average_annual_volatility(daily_returns_df):
    """
    Calculates the annual volatility on daily returns. 
    Must only be ran after calculate_daily_returns() method has been called.

    :param daily_returns_df: Daily returns.
    :type daily_returns_df: Pandas DataFrame. 
    """
    avg_annual_volatility_df = daily_returns_df.std() * 252**(1/2)
    return avg_annual_volatility_df

def calculate_sharpe_ratio(avg_annual_returns_df, avg_annual_volatility_df):
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

def calculate_portfolio_return(average_annual_returns_df, weight):
    """
    Calculate the portfolio return per a given weight based off of client risk profile.

    :param average_annual_returns_df: Average annual returns of asset data.
    :param weight: Portfolio weight per client risk profile.
    :type average_annual_returns_df: Pandas DataFrame.
    :type weight: float list
    """
    portfolio_return_df = average_annual_returns_df.mul(weight).sum()
    return portfolio_return_df


def calculate_portfolio_std(risk_prof):
<<<<<<< HEAD
    """
    Calculate the colatility on the portfolio.
    Must be ran after calculate_daily_returns()
    
    :param weights: 
    """
=======
>>>>>>> 22eb0ef6bf96fe9ab43897e99023f134dbf04031
    weights=np.array(risk_profile_weights[risk_prof])
    portfolio__annual_cov_df=daily_returns_df.cov()*252
    portfolio_variance=np.dot(weights.T, np.dot(portfolio__annual_cov_df, weights))
    portfolio_vol=np.sqrt(portfolio_variance)
    return portfolio_vol

def calculate_portfolio_sharpe_ratio(portfolio_vol,portfolio_return_df):
    portfolio_sharpe_ratio=portfolio_return_df/portfolio_vol
    return portfolio_sharpe_ratio