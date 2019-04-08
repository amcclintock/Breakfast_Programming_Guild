#Calculator function chosen by option 1
def calculator():
    # 3 errors in this section

    #clear the screen a little
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print ("This calculator only works with the number 3\n") #challenge, can you make it work with 2 user inputs
    print ("1. Add")
    print (2. Subtract)
    print ("3. Multiply")
    print ("4. Divide")

    user_input = input("\nChoose one:")
    user_number = input("\nEnter a number for mathing:")

    if (user_number == "1"):
        print ("\nThe sum of 3 and ", user_number, " is: ", 3 + int(user_number))
    elif (user_input == "2"):
        print ("\nThe difference of 3 from ", user_number, " is: ", float(user_number) - 3)
    elif (user_input == "3"):
        print ("\nThe product of 3 and ", user_number, " is: ", int(user_number) * 3)
    elif (user_input == "3"):
        print ("\nThe quotient of 3 from ", user_number, " is: ", float(user_number) / 3) #what happens if int is used instead of float?
    else:
        print ("\n\nFail\n\n")




#Check if a string is a Palindrome
def palindrome_checker():
    # 3 errors in this section

    clear the screen a little
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


    #Challenge - how to make this case insensitive
    user_input = input("Enter a word or phrase to check: ")
    reveresed_user_input = reversed(reveresed_user_input) #find the reverse user_input of the string

    elif (list(user_input) == list(reveresed_user_input)):
    print ("\n", user_input, " is a palindrome")
else:
print ("\n", user_input, " is not a palindrome")



#Check the days in a month
def days_in_month():
    #3 errors here too

    cal_dict = {'jan':31, 'feb':28, 'mar':31, 'smarch':30, 'APR':30, "may":31, 'jun':30, 'July':   31, 'aug': 30,
                'sep':30, 'oct':31, 'NOV':30, 'dec':31}

    user_input = input("\nEnter the 3 character abbreviation for the month: ")
    #Challenge, make this case insensitive


    print ("\n\nThe number of days in ", user_input, " is ", cal_dict[user_input])




#Performs different functions based on user input
only this one error here



print ("\n\n")
print ("1. Simple Calculator (integer and floats")
print ("2. Calendar days in month")
print ("3. Palindrome checker (string and list)")
user_input = input("\n Choose one: ")

#Condition based on user selection
if (user_input == "1"):
    calculator()
elif (user_input == "2"):
    days_in_month()
elif (user_input == "3"):
    palindrome_checker()
else:
    print ("\n\nDo better\n\n")