"""
Visualizer Module
---------------------------------
Visualizer module is responsible for outputting user-friendly 
"""
# Configure a Monte Carlo simulation to forecast 10 years cumulative returns of conservative portfolio
    MC_conservative = MCSimulation(
        conservative_portfolio_df = close_df,
        weights = [.1,.9,0],
        num_simulation = 1000,
        num_trading_days = 252*10
    )
    
    # Run a Monte Carlo simulation to forecast 10 years cumulative returns
    MC_conservative.calc_cumulative_return()
    
    # Save the summary statistics information in a variable for conservative portfolio
    conservative_table = MC_conservative.summarize_cumulative_return()

# Configure a Monte Carlo simulation to forecast 10 years cumulative returns of moderately conservative portfolio
    MC_moderately_conservative = MCSimulation(
        moderately_conservative_portfolio_df = close_df,
        weights = [.25, .7, .05],
        num_simulation = 1000,
        num_trading_days = 252*10
    )
    
    # Run a Monte Carlo simulation to forecast 10 years cumulative returns
    MC_moderately_conservative.calc_cumulative_return()
    
    # Save the summary statistics information in a variable for conservative portfolio
    moderately_conservative_table = MC_moderately_conservative.summarize_cumulative_return()

# Configure a Monte Carlo simulation to forecast 10 years cumulative returns of moderate portfolio
    MC_moderate = MCSimulation(
        moderate_portfolio_df = close_df,
        weights = [.6, .3, .1],
        num_simulation = 1000,
        num_trading_days = 252*10
    )
    
    # Run a Monte Carlo simulation to forecast 10 years cumulative returns
    MC_moderate.calc_cumulative_return()

    # Save the summary statistics information in a variable for moderate portfolio
    moderate_table = MC_moderate.summarize_cumulative_return()
    
# Configure a Monte Carlo simulation to forecast 10 years cumulative returns of moderately aggressive portfolio
    MC_moderately_aggressive = MCSimulation(
        moderately_aggressive_portfolio_df = close_df,
        weights = [.75, .1, .15],
        num_simulation = 1000,
        num_trading_days = 252*10
    )
    
    # Run a Monte Carlo simulation to forecast 10 years cumulative returns
    MC_moderately_aggressive.calc_cumulative_return()
    
    # Save the summary statistics information in a variable for moderately aggressive portfolio
    moderately_aggressive_table = MC_moderately_aggressive.summarize_cumulative_return()
    
# Configure a Monte Carlo simulation to forecast 10 years cumulative returns of aggressive portfolio
    MC_aggressive = MCSimulation(
        aggressive_portfolio_df = close_df,
        weights = [.8, 0, .2],
        num_simulation = 1000,
        num_trading_days = 252*10
    )
    
    # Run a Monte Carlo simulation to forecast 10 years cumulative returns
    MC_aggressive.calc_cumulative_return()
    
    # Save the summary statistics information in a variable for aggressive portfolio
    aggressive_table = MC_aggressive.summarize_cumulative_return()