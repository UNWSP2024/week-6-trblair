# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def taxcalculation():
    print("What was the value of all combined sales this month?\n$")
    totalsales=float(input())
    countytax=totalsales*0.025
    statetax=totalsales*0.05
    totaltax=statetax+countytax
    print("The state tax is equal to $",statetax)
    print("The county tax is equal to $",countytax)
    print("The total tax is equal to $",totaltax)
taxcalculation()
