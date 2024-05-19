###total bill inputed by user
total_bill = float(input("Enter total bill:"))
#### loops from 15 to 25 percent
for i in range(15,26):
    ###find discount from i
    discount_price = (total_bill / 100 * i) ###find discount from i
    ## formats percent, and formats bills to the 2nd decimal place
    formatted_str = "{:.0f}% is ${:.2f}".format(i,discount_price)
    ##prints both percent and bill to the 2nd decimal place
    print(formatted_str)

