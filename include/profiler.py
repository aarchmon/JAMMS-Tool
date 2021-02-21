"""
Profiler Module
---------------------------------
Profiler module incorporates methods which retrieve a client's personal financial information.
This information will be used to etermine overall strategic asset allocation blend based on this profile. 
"""

import questionary

def get_info():
    """
    Prompt dialog to retrieve investor's financial information.

    :param name: None
    :param type: None
    :rtype cash, assets, income, liquidity: float
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
    """
    Determine whether or not Client holds sufficient net worth to invest.

    :param cash: Total cash on-hand.
    :param assets: Net assets.
    :param income: Annual gross income.
    :param liquidity: Liquidity of Client. 
    :type cash: float
    :type assets: float
    :type income: float
    :type liquidity: float
    """
    net_worth = (cash + assets + income - liquidity)
    if net_worth > 0:
        print(f"You are able to invest: {net_worth}")
    else:
        print(f"You do not have sufficient funds to invest")
       
        
def risk_profile():
    """
    Determine risk profile of Client.

    :param None:
    :rtype profile: str
    """
    score = 0
    
    age = questionary.text("What is your age?").ask()
    time_horizon = (65 - int(age))
    
    if time_horizon <= 5:
        score =+ 1   
    elif (5 < time_horizon) and (time_horizon <=10):
        score =+ 2    
    elif time_horizon < 10:
        score =+ 3
            
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