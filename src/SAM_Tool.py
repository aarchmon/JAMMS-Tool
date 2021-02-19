import sys
from pathlib import Path
import fire

# Import profiler functions.
from profiler import get_info
from profiler import qualification
from profiler import risk_profile
                  
def run():
    """The main function for running the script."""

    # Get investor's information
    cash, assets, income, liquidity = get_info()

    # Determine qualifying investable amount
    net_worth = qualification(cash, assets, income, liquidity)
                  
    # Determine investor's risk profile by determining ability to take risk defined by investment time horizon (age) and willingness to risk defined by comfort level with loss
    risk_profile()
    
    sys.exit()

if __name__ == "__main__":
    fire.Fire(run)