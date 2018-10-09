#Magic 8 ball!

#Need to add informaiton on how to create a random number
import random
random_result = random.randint(1,20)

#Get a question
magic_question = input('Enter a question:')

#Find and print the result

if random_result == 1:
    print ("It is certain.")

if random_result == 2:
    print ("It is decidedly so.")

if random_result == 3:
    print ("Without a doubt.")

if random_result == 4:
    print ("Yes - definitely.")

if random_result == 5 or magic_question == "Will Aaron win the PowerBall":
    print ("You may rely on it.")

if random_result == 6:
    print ("As I see it, yes.")

if random_result == 7:
    print ("Most likely.")

if random_result == 8:
    print ("Outlook good.")

if random_result == 9:
    print ("Yes.")

if random_result == 10:
    print ("Signs point to yes.")

if random_result == 11:
    print ("Reply hazy, try again")

if random_result == 12:
    print ("Ask again later.")

if random_result == 13:
    print ("Better not tell you now.")

if random_result == 14:
    print ("Cannot predict now.")

if random_result == 15:
    print ("Concentrate and ask again.")

if random_result == 16:
    print ("Don't count on it.")

if random_result == 17:
    print ("My reply is no.")

if random_result == 18:
    print ("My sources say no.")

if random_result == 19:
    print ("Outlook not so good.")

if random_result == 20:
    print ("Very doubtful.")



