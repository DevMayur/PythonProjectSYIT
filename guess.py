#Question ->Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

from random import randint


def play():
	a=randint(0,9)
	b = int(input("Enter a number in 0 to 9"))
	if a==b:
		print("You gussed correctly :")
	elif a < b:
		print("You guessed too high")
		start()
	elif a > b:
		print("You guessed too low")
		start()
def start ():
	ask = input("Do you want to Play")
	if ask == "y" or ask == "Y" or ask == "yes" or ask == "Yes" or ask == "YES":
		play()
start()
