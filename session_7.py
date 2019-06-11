#Parse file
file = open ("C:\\temp\\maps.csv", "r")

#Loop through all the lines
for line in file:

    #Things to find
    line_counter = 0
    count_formats = 0
    count_retailer_maps = 0
    count_standards = 0
    oh_really_map = 0
    stool_map = 0


    #is it a retailer map (starts with H)
    if line.startswith("H"):
        print ("yep, retailer like")

    #is it a formats map (starts with formats) solve this


    #is it a standards map (contains standard) solve this

    # Oh Really?
    if "_Orly_" in line:
        oh_really_location = line

    # Stool location, search for poop


line_counter+= 1


print ("Total Lines in File:")
print ("Total Formats:")
print ("Total Retailers:")
Print ("Total Standards:")
print ("Oh Really Map:")
print ("Stool Map:")