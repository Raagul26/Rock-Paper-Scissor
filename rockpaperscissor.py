import random
import time
# Games starts here
print("^__^~~~~~~~~~~~~~~~~~~~~ Rock Paper Scissor ~~~~~~~~~~~~~~~~~~~~^__^")
user = input("Enter player name: ")
print("Let's start the game....")

# Get target score
try:
    n = input("Enter your target score: ")
    n = int(n)
except:
    print("Use only numbers")
    while not n.isnumeric():
        n = input("Enter your target score: ")
    n = int(n)

userscore = 0
compscore = 0

# Compares rock , paper and scissor
while True:
    if ((userscore >= n) and (compscore <= n)) or ((userscore <= n) and (compscore >= n)):
        break
    print("\n Rock => 1\t Paper => 2\t Scissor => 3")
    try:
        choice1 = input("\n" + user + "'s Turn: ")
        choice1 = int(choice1)
    except:
        print("Use only numbers")
        while not choice1.isnumeric():
            print("\n___Enter 1 or 2 or 3___")
            choice1 = input(user + "'s Turn: ")
        choice1 = int(choice1)
    choice2 = random.choice((1, 2, 3))
    if choice1 == choice2:
        print("Draw!!!")
    elif choice1 == 1:  # rock
        if choice2 == 2:
            print("Computer Wins!!!")
            compscore += 1
        if choice2 == 3:
            print(user, "Wins!!!")
            userscore += 1
    elif choice1 == 2:  # paper
        if choice2 == 3:
            print("Computer Wins!!!")
            compscore += 1
        if choice2 == 1:
            print(user, "Wins!!!")
            userscore += 1
    elif choice1 == 3:  # scissor
        if choice2 == 2:
            print(user, "Wins!!!")
            userscore += 1
        if choice2 == 1:
            print("Computer Wins!!!")
            compscore += 1
    else:
        print("Use only (1 or 2 or 3) to beat the computer")
# Compares two scores
if userscore == compscore:
    r = "\nYou and computer gets draw!!!"
elif userscore > compscore:
    r = user + " smashed the computer"
elif userscore < compscore:
    r = "Computer beats you"
print("""\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
/                                                                 /
                 """ + r + """                               
/                                                                 /
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/""")
print("""\n        Score Board           
    """+f"{user}'s score: {userscore}"+"""
    """+f"Computer's score: {compscore}")

# some conversation
if r == "Computer beats you":
    time.sleep(0.5)
    print("\nHa ha ha ha ha.....")
    time.sleep(2)
    print("Don't try to beat me")
    time.sleep(2)
    print("Humans are not more powerful than me ^_^")
    time.sleep(1)
elif r == user + " smashed the computer":
    time.sleep(1)
    print("\nComputer >> Not all time like this")
    time.sleep(2)
    print("\tI'm just kidding")
ex = input("\nPress Enter to exit")
exit(1)
