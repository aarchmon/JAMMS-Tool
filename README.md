# SAM Tool
# TEST


![SAM Tool](./Images/main_image.jpg)

---

## Description
The tool will create a customized asset allocation for an investor to use a reference for an optimal portfolio based on their ability and willingness to take risk. 

---
## Usage
This can be a useful tool for first time investors to assess their investments using a benchmark based on client specific situation. 

---
## Systems Diagram
![Systems_Diagram]("./Systems_Diagrams/Pipelines/main_pipeline.png")

---
## Installation Guidecs
    * Python
    * Pandas
    * Matplotlib
    * NumPy
    * SciPy
    * Monte Carlo
    * Alpaca API
    * Quandl
    * SQL Alchemy
    * OS
    * Questionary
    * Fire
    * Doxygen
    * Kivy
    * Seaborn
    * Scikit

---
## User Profile
This is will collect financial information to categorize investor into a risk profile. Initial screen will prompt dialog to retrieve investor's financial information to determine risk profile. Based on information provided, user will be promted to next steps or give an output of "insufficient funds" if investor does not have sufficient funds to invest. 

### Determine Investor's Net Worth
Investor's net worth is defined by sum of cash, assets, and annual income minus annual spending needs

    * Cash
    * Assets (i.e. stocks, bonds, real estate, cryptoasset)
    * Annual Income
    * Annual Spending Needs (ie. rent/mortgage, credit card, loan payments)

### Determine Investor's Risk Ability
Investor's ability to take risk is determined by their investment time horizon which is the number of years they can invest. We assume an average investor's retirement age will be 65. Investment time horizon will be determined by 65 minus age of investor.

    * If less than 5 years to invest, assign a value of 1
    * If between 6 and 10 years to invest, assign a value of 2
    * If more than 10 years to invest, assign a value of 3

### Determine Investor's Risk Willingness
Investor's willingness to take risk is a preference and determined by their level of comfort with loss.  

    * If investor is comfortable with losing at most 10%, assign a value of 1
    * If investor is comfortable with losing 10% to 50%, assign a value of 2
    * If investor is comfortable with losing more than 50%, assign a value of 3

### Score Questionnaire
Average the score from ability and willingness to risk. Assign each score as a risk profile:

    * 1 = Conservative
    * 1.5 = Moderately Conservative
    * 2 = Moderate
    * 2.5 = Moderately Aggressive
    * 3 = Aggressive

---
## Calculations
Based on investor's profile, we will assume the following asset allocation for each profile:

![Risk Profiles](./Images/risk_score.jpg)


---
## Output / Visualizations

---
## Contributors

_Sarah Kang_ 

_Might Lee_  

_Aaron Montano_

---

## License

