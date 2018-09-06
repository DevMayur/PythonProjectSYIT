# Question ->Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user


getnumber = int(input("Enter an number to check whether it is even or odd :"))
if (getnumber % 2) == 0 :
	print("Given number is even ")
else :
	print ("Given number is odd ")
