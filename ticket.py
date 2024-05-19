### Asks user for age
age = int(input("Enter age:"))
####checks to see if the person is a child under 3
if( age > 0 and age <3):
    print("Price: FREE")
####checks to see if the person is a child 
if( age >=3 and age<=12):
    print("Price: %29.95")
####checks to see if the person is a student without ID
if(age >=13 and age<=17):
    print("Price: $39.95")
###checks to see if the person is a senior
if(age >= 65):
    print("Price: $39.95")
###checks to see if the person is student by checking for ID
if(age<65 and age>17):
    id = input("College ID? (y/n)")
    if(id == "y"):
        print("Price: $39.95")
    else:
        print("Price: $49.95")
        
    
