total_mile = 0
total_gallon = 0
print("Your Personal Fuel Economy")

while True:
    miles = input("Number of miles traveled (or enter to exit):")
    if miles == "":
        break
    gallons = float(input("Number of gallons needed:"))
    miles = float(miles)
    mpg = miles/gallons

    total_gallon += gallons
    total_mile += miles
    print("Mileage this tank:{: .1f}".format(mpg))
print("Average mileage:{: .1f}".format(total_mile/total_gallon))

    
    
    
    
    

