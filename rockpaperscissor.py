from random import choice
from time import sleep


#Games starts here
print("Rock Paper Scissor".center(50, "~"))
user = input("Enter player name: ")
print("Let's start the game....")


def game():				
	#Get target score
	while(True):
	    try:
                n = int(input("Enter target score : "))
                break
	    except ValueError:
	        print("Enter numbers only")
	userscore = 0
	compscore = 0
	#Compares rock , paper and scissor
	while True:
 	    if userscore == n or compscore == n:
                break
 	    print("\n Rock => 1\t Paper => 2\t Scissor => 3")
 	    choice_list = [1, 2, 3]
 	    while(True):
                try:
                    choice1 = int(input(f"{user} turn : "))
                    if choice1 in choice_list:
                    	break
                    else:
                    	print("Enter 1 or 2 or 3 only")
                except ValueError:
                	print("Enter 1 or 2 or 3 only")
 	    
 	    choice2 = choice(choice_list)
 	    if choice1 == choice2:
 	    	print("Draw!!!")
 	    elif choice1 == 1:
 	              		if choice2 == 2:
 	              			print("Paper beats rock\nComputer Wins!!!")
 	              			compscore += 1
 	              		else:
 	              			print(f"Rock beats scissor\n{user} Wins!!!")
 	              			userscore += 1
 	    elif choice1 == 2:  
                	if choice2 == 3:
                		print("Scissor beats paper\nComputer Wins!!!")
                		compscore += 1
                	else:
                		print(f"Rock beats scissor\n{user} Wins!!!")
                		userscore += 1
 	    else:
		              		if choice2 == 2:
		              			print("Scissor beats paper\n{user} Wins!!!")
		              			userscore += 1
		              		else:
		              			print("Rock beats scissor\nComputer Wins!!!")
		              			compscore += 1
                          
	# Compares two scores
	if userscore == compscore:
 	   r = "You and computer gets draw!!!"
 	   result = 0
	elif userscore > compscore:
 	   r = f"{user} smashed the computer"
 	   result = 1
	else:
 	   r = "Computer beats you"
 	   result = -1

	print(f"""\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
/                                                                 /
{r.center(67)}                               
/                                                                 /
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/""")
	print(f"Score Board\n{user}'s score: {userscore}\nComputer's score: {compscore}")

	# some conversation
	if result == -1:
 	    sleep(.5)
 	    print("\nHa ha ha ha ha.....")
 	    sleep(.5)
 	    print("Don't try to beat me")
 	    sleep(.5)
 	    print("Humans are not more powerful than me ^_^")
	elif result == 1:
 	   sleep(.5)
 	   print("\nComputer >> Not all time like this")
 	   sleep(.5)
 	   print("\tI'm just kidding")
	else:
	    sleep(.5)
	    print("\nYou have enough power to fight with me")

def main():
    while(True):
     game()
     if not input("Want to play again (y or n) : ") == "y":
     	break
			
if __name__ == "__main__":
    main()

