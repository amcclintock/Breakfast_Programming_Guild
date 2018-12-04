#Grab a year, check if it's a leap year, if not find the next closest ones

#   on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#   unless the year is also evenly divisible by 400
#
import random


# Get a year
user_input = input('Enter a year to check:')

# Sometimes I don't want to guess
if str.upper(user_input) == "NO":
    user_input = random.randint(1,4000)

if int(user_input) % 4 == 0:
    if int(user_input) % 100 == 0:
        if int(user_input) % 400 == 0:
            print (user_input, " is a leap year")
        else:
            print (user_input, " is not a leap year")
    else:
        print(user_input, " is a leap year")
else:
    print (user_input, " is not a leap year")


#Challenge:  If not a leap year, be creative and find a leap year...loop, function, random, find the next one?