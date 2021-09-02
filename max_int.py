#Print out the maximum positive integer input by the user
#Ask the user to input a number
#create a while loop that is True as long as the users' input is a positive number
#Store the maximumum number in the while loop
#if num_int is larger then max_int
#max_int becomes num_int
#Once the loop becomes False, print out the maximum number

num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int >= max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line
