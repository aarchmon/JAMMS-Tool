# Creating a table for visualising average annualized returns, volatility, and Sharpe Ratio of each asset (SPY, AGG, BTC)
consolidated_table = pd.concat([avg_annual_returns_df, avg_annual_volatility_df, avg_annual_sharpe_ratio_df], axis=1) 
consolidated_table.columns = ['Returns', 'Volatility', 'Sharpe Ratio']
consolidated_table

# Define an empty array for portfolio returns
p_ret = [] 

# Define an empty array for portfolio volatility
p_vol = [] 

# Define an empty array for asset weights
p_weights = [] 

num_assets = len(df.columns)
num_portfolios = 10000

for portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights = weights/np.sum(weights)
    p_weights.append(weights)
 
 #break

# Returns are the product of individual expected returns of asset and its weights
    returns = np.dot(weights, ind_er)
    p_ret.append(returns)
    
# Portfolio Variance
    var = cov_matrix.mul(weights, axis=0).mul(weights, axis=1).sum().sum()
    sd = np.sqrt(var) # Daily standard deviation
    ann_sd = sd*np.sqrt(250) # Annual standard deviation = volatility
    p_vol.append(ann_sd)

    data = {'Returns':p_ret, 'Volatility':p_vol}

for counter, symbol in enumerate(df.columns.tolist()):
    #print(counter, symbol)
    data[symbol+' weight'] = [w[counter] for w in p_weights]

    portfolios  = pd.DataFrame(data)
    
# Dataframe of the 10000 portfolios created
    portfolios.head() 
    
# Plot efficient frontier
portfolios.plot.scatter(x='Volatility', y='Returns', marker='o', s=10, alpha=0.3, grid=True, figsize=[10,10])