import sys
from pathlib import Path
import fire
import questionary

def get_info():
    """Prompt dialog to retrieve investor's financial information to determine risk profile.

    Returns:
        Returns the investor's initial investment amount or insufficient funds
    """
    
    print('Welcome. In order to determine your initial investment, please answer the following questions. If none, please enter 0!')
    
    cash = questionary.text("What is your cash savings?").ask()
    assets = questionary.text("What is the value of your total investments (ie. stocks, bonds, real estate, cryptoassets)?").ask()
    income = questionary.text("What is your total annual income?").ask()
    liquidity = questionary.text("What is your average annual spending needs (ie. rent/mortgage, credit card, loan payments)?").ask()

    cash = float(cash)
    assets = float(assets)
    income = float(income)
    liquidity = float(liquidity)
    
    return cash, assets, income, liquidity

def qualification(cash, assets, income, liquidity):
    net_worth = (cash + assets + income - liquidity)
    if net_worth > 0:
        print(f"You are able to invest: {net_worth}")
        risk_profile()
    else:
        print(f"You do not have sufficient funds to invest")
       
        
def risk_profile():
    score = 0
    # Assess investor's ability to take risk - determined by investment time horizon (65 - "age"). Ask investor's age and assume end of investment time horizon is at age 65 (retirement age). Longer the investment time horizon, the more ability to take risk. If 5yrs or less, the investor will be considered "conservative". If 6-10yrs investor will be considered "moderate". If 10 or more years invester will be considered "aggressive". 
    age = questionary.text("What is your age?").ask()
    time_horizon = (65 - int(age))
    
    if time_horizon <= 5:
        score =+ 1   
    elif (5 < time_horizon) and (time_horizon <=10):
        score =+ 2    
    elif time_horizon < 10:
        score =+ 3
    
    # Assess investor's willingness to take risk - determined by level of comfort with loss. If investor is comfortable with less than 10% loss, considered "conservative". If comfortable with 10%-50% loss, considered "moderate". If comfortable with greater than 50% loss, considered "aggressive".
    willingness = questionary.select("Which best defines your comfort level of loss?", choices=["Less than 10% loss", "10%-50% loss", "Greater than 50% loss"]).ask()
    if willingness == "Less than 10% loss":
        score =+1
    elif willingness == "10%-50% loss":
        score =+2
    elif willingness == "Greater than 50% loss":
        score =+3

    avg_score = score / 2
    if avg_score < 2:
        print(f"Your Risk Profile is: Conservative")
        return "conservative"

    elif avg_score == 2:
        print(f"Your Risk Profile is: Moderate")
        return "moderate"

    elif avg_score > 2:
        print(f"Your Risk Profile is: Aggressive")
        return "aggressive"
                  
def run():
    """The main function for running the script."""

    # Get investor's financial information
    cash, assets, income, liquidity = get_info()

    # Determine qualifying investable amount
    net_worth = qualification(cash, assets, income, liquidity)
                  
    # Get investor's risk profile
    risk_profile()
    
    sys.exit()

if __name__ == "__main__":
    fire.Fire(run)