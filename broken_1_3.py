# Blake's math 'helper'


print ("Blake's homework\n\n\n")

print ("Multiples of 12")
for counter_a in range (12):
    for counter_b in range (12):
        #print ("Counter A:", counter_a, "\t\t Counter B:", counter_b) #uncomment me to see a loop within a loop
        if counter_a * counter_b == 12:
            print ("\t", counter_a, " and ", counter_b)
            #break #what happens with this and without?  Use line 8 and line 8 commented out for a hint



print ("\n\n\nMultiples of 20")
for counter_a in range(1, 20):
        if (counter_a % 20) == 1:
            print ("\t", int(20/counter_a), " and ", counter_a) # What happens without the int(), do we need it to be true?