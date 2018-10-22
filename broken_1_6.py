Take user input, and tell me stuff about the data


user_input = input('Enter something:')


#Check if the data contains alpha
if (user_input.isalpha()):
    print (user_input, " contains alpha characters")

    #Do some math on characters
    three_user_input = user_input * 3
    print (user_input, " three times is: ", three_user_input) # End of code comment

    #Is it upper case?
    if (user_input.isupper()):
            print (user_input, " is all uppercase")
    elif (user_input.islower()):
        print (user_input, " is all lowercase")
else:
    print (user_input, " is a mix of upper and lowercase")


#Check if the data is a whole number
if (user_input.isdigit()):
    print (user_input, " is a whole numbers")

    #Only if a whole number, dig deeper
    three_user_value = int(user_input) * 3
    print (user_input, " times 3 =", three_user_value)

    #is it an even number?
    if (int(user_input) % 2 == 0):
        print (user_input, " is an even number")
    else:
        print ("Checking to see if it's odd")
    elif:
        print (user_input, " is an odd number")




#No good guess for the data
print ("I don't know what ", user_input, " is!")
