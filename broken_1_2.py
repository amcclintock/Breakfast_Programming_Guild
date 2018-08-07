#Leap year at some point
feb_days = 28

#Start by collecting a month
month_info = input('Enter a month:')

if month_info == "feb":
    year_info = input('Enter the year:')

    #To determine whether a year is a leap year, follow these steps:
        #1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
        #2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
        #3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
        #4. The year is a leap year (it has 366 days).
        #5. The year is not a leap year (it has 365 days).


    #Define date numbers after leap year calc
    cal_dict = {'jan':31, 'feb':feb_days, 'mar':31, 'smarch':30, 'APR':30, "may":31, 'jun':30, 'July':   31, 'aug': 30,
            'sep':30, 'oct':31, 'NOV':30, 'dec':31}

#Print the total number of days in the month
print ("The number of days in ", month_info, " is ", cal_dict[month_info])

