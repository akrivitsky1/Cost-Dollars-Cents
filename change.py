### Asks for change in coins less then 100
change = int(input("Enter change:"))

###Takes the total amount of quarters from the user inputed coin amount
quarters = (change // 25)
### finds the remainder after quarters are taken from the total amount
change = (change % 25)
dimes = (change // 10)
### finds the remainder after dimes are taken from the total left amount
change = (change % 10)
nickels = (change // 5)
### finds the remainder after nickels are taken from the total left amount
change= (change % 5)
pennies = (change // 1)
### finds the remainder after pennies are taken from the last amount
change = (change % 1)

### Displays the converted change
print("Quarters:",quarters)
print("Dimes:", dimes)
print("Nickels:",nickels)
print("Pennies:",pennies)



