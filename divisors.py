# Question  ->Create a program that asks the user for a number and then prints out a list of all the divisors of that numbers.

def print_factors(x):

	print("The factors of",x,"are :")
	for i in range(1 , x+1):
		if x % i == 0 :
			print (i)

num = int(input("Enter an number :"))

print_factors(num)
