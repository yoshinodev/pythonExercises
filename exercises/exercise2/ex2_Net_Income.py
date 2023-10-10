# IEFP - Data analytics - Python 10805
# Autor: Anaïs Gilbert
# Data: 2021/10/05
# Exercise 2: Create a simple app that calculates the net income of a worker
# based on the gross income, the taxes from the Country and the food subsidy given

# Declaring and Initializing variables

gross_income = 1153 # monthly gross income in €
IRS_TAX = 0.165 # constant variable, IRS Rate = Personal Income Tax In Portugal
food_subsidy = 100 # monthly food subsidy in €
SS_TAX = 0.11 # constant variable, SS Rate = Social Security Tax In Portugal

# calculate the net income of the worker, applying the IRS and SS tax rates and adding the food subsidy
# round( ,3) to round the result to 3 decimals

net_income = round(gross_income - (gross_income * IRS_TAX) - (gross_income * SS_TAX) + food_subsidy, 3)


# output the result on the terminal/console
print(f"The net income of the worker it's {net_income} €")
