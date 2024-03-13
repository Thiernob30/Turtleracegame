# variables to hold the size of the tract and number of acres.
tractSize = 0.0
acres = 0.0

#constant for the number of square feet in an acre.
SQ_FEET_PER_ACRE = 43560

# Get the square feet in the tract.
tractSize = float (input("Enter the number of square feet in the tract."))

#calculate the acreage.
acres = tractSize/ SQ_FEET_PER_ACRE

#print the number of acres.
print ("The size of that tract is", format(acres, '.2f'),"acres.")
