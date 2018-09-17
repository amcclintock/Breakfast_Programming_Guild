#Number half pyramid
#Makes a half pyramid of numbers up to 9
#1
#22
#333
#4444
#55555


outer_loop = 0

while outer_loop <= 10:
    inner_loop = 1
    #print ("Outer Loop is:", outer_loop)
    while inner_loop < outer_loop + 4:
        #print ("Inner Loop is:", inner_loop)
        print (outer_loop),
        inner_loop = inner_loop + 1


    print
    outer_loop = outer_loop + 2

