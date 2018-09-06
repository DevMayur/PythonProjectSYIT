# Question -> Ask the user for a string and print out whether this string is a palindrome or not.



def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "I am pretty good at programming"

print ("Original string is :", s)
print ("reversed string is :", reverse(s))
