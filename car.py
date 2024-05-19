#### prints the prompt
print("Guess the price and win the prize!")
####Constants
price = 42500
trys = 0
done = False
### keeps asking until its told to stop
while not done:
    guess = int(input("Enter your guess:"))
    ### counts the amount of guesses
    trys = trys + 1
    ### if gues is correct leavs loop
    if guess == price:
        done = True
    ## else it checks if guess is too high or too low
    elif guess < price:
        print("Too low!")
    elif guess > price:
        print("Too high!")
###take the number of guesses from the loop and compares it

if trys >= 5:
    print("Too many guesses!")
else:
    print("You won the car!")
                  
    
