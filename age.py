#Question - Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Algorithm -
#->Get user age
#->set n = 100 - age;
#->Get current year from user store it in now;
#->set ressult = now + n;

#Mayur Sunil Kakade.


age = int(input("Enter Your age :"))
n = 100 - age;
now = int(input("Enter current year :"))
result = now + n
print("You will become 100 years old in ", result)
