print("Pocket change calculator")

###Asks users for inputs for each prompt and converts it to a integer
quarters = int(input("How many quarters?"))
dimes = int(input("How many dimes?"))
nickels = int(input("How many nickels?"))
pennies = int(input("How many pennies?"))

#### converts total of all user inputed coins
total_coin = (quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)

#### converts the total amount of coins to dollars
total_dollar = (total_coin / 100)

### formating statement
formatted_str = "${:.2f}".format(total_dollar)

##prints total amount of money
print("You have",formatted_str)
