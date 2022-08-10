#© 2022 NaveenKumar MuraliTharan. All Rights Reserved.
#Words naming Game
#Problem Statement
#1.In this game we can have maximum of four players and minimum of two(1 vs com will be updated)
#2.The Game should start with player 1 spelling a meaningfull word and the last letter of the word will
#be used by the player 2 to spell the next meaningfull word.
#3.The words which are already used should not be used again.
#4.Timing for a word will be used in development progress.
#5.if word is not guessed then the game will be end.
def totalPlayers() :
    totalPlayers = int(input("Please Enter Total Number of Players(min 2 : max4) : "))
    return totalPlayers
def checkPlayerCount(totalPeople) :
    if totalPeople < 2 or totalPeople > 4:
        print("Please enter the players less han 5 and greater than 1")
        totalPlayers()


print("Naming Gaming")
print("Let's Start")
#totalPlayers()
totalPeople = totalPlayers()
playerCheck = 0
while i == 0 :
