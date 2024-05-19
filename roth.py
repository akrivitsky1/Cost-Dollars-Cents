### counter for amount of months
month = 0
##asks user for initial deposit amount
roth_ira = float(input("Enter an initial Roth IRA deposit amount:"))
### asks user for anual percent of return
APR  = int(input("Enter an annual percent rate of return:"))
##converts current value as the starting value of initial deposit
current_value = roth_ira
##Loop runs only while the amount is less then double the initial amount
while current_value < 2 * roth_ira:
    ### formula for interest
    added_interest = current_value * (APR / 100) / 12
    ###stacking sum
    current_value += added_interest
    ###adds a month to the counter every time its looped
    month += 1
    ##formats value to 2nd decimal for money
    format_value = "${:.2f}".format(current_value)
    ###prints each month value in money and what month it is
    print("Value after month",str(month)+":",format_value) 
##formates the input of return to include a percent
formatted_return = "{:.0f}%".format(APR)
##prints final result of the loop
print("It will take",month,"months to double your investment with a",formatted_return,"return.")
