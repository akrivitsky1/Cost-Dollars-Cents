###prints Cash Register
print("Cash register")
### constants to use in the loop
running_count = 0
running_sum = 0
###While input = a #
while True:
    price_ask = input("Enter the price of an item:")
    ### if input is equal to a enter key/no input put in, leave loop
    if price_ask == "":
        break
    ##converts input to a float
    num = float(price_ask)
    ###adds to counter of how many items were inputed
    running_count += 1
    ### adds up inputs
    running_sum +=num
##formats the sum to a string to the 2nd decimal 
formatted_str = "${:.2f}".format(running_sum)
##3prints final result of all inputs
print("You entered",running_count,"items totaling",formatted_str)
