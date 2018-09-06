# Question ->    8. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message 
#of congratulations to the winner, and ask if the players want to start a new game)
#    • Remember the rules: Rock beats scissors
#    • Scissors beats paper
#    • Paper beats rock
def play():
	t=["Rock","Paper","Scissor"]
	player1 = input("Player 1 -> Rock,Paper,Scissor?")
	player2 = input("Player 2 -> Rock,Paper,Scissor?")
	if player1 == player2 :
		print("Its tie ")
	elif player1 == "Rock" and player2 =="Scissor":
		print("player 1 is winner ")
	elif player1 == "Scissor" and player2 == "Paper":
		print ("Player 1 is winner ")
	elif player1 == "Paper" and player2 == "Rock":
		print ("Player 1 is Winner")
	
	elif player2 == "Rock" and player1 =="Scissor":
		print("player 2 is winner ")
	elif player2 == "Scissor" and player1 == "Paper":
		print ("Player 2 is winner ")
	elif player2 == "Paper" and player1 == "Rock":
		print ("Player 2 is Winner")
	else:
		print (" Please check your spellings ")
	ask = input("Do you want to play Rock Paper Scissor game ? y/n")
	if ask == "y" or ask == "Y" or ask == "yes":
		play()
	return
ask = input("Do you want to play Rock Paper Scissor game ? y/n")
if ask == "y" or ask == "Y" or ask == "yes":
	play()
