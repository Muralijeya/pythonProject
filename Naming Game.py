#© 2022 NaveenKumar MuraliTharan. All Rights Reserved.
#Words naming Game
#Problem Statement
#1.In this game we can have maximum of four players and minimum of two(1 vs com will be updated)
#2.The Game should start with player 1 spelling a meaningfull word and the last letter of the word will
#be used by the player 2 to spell the next meaningfull word.
#3.The words which are already used should not be used again.
#4.Timing for a word will be used in development progress.
#5.if word is not guessed then the game will be end.
import  sys

def totalPlayers() :
    totalPlayers = int(input("Please Enter Total Number of Players(min 2 : max4) : "))
    return totalPlayers

def totalWords() :
    totalPlayers = int(input("Please Enter Total Number of words to play this game : "))
    return totalPlayers

def outputPlayer(totalPeople) :
    playerArr = []
    playerNameArr = []
    # wordArray = []
    startingLetter = ""
    totalWord = totalWords()

    for i in range (1, totalPeople + 1, 1) :
        player = input("Enter player name :" )
        playerNameArr.append(player)

    for word in range(1, totalWord + 1 , 1) :

        for i in range(len(playerNameArr)) :
            print(playerNameArr[i], "Its Your turn : ")
            getWord = input().upper()
            # playerArr.append(getWord)

            if len(playerArr) == 0 :
                playerArr.append(getWord)
                startingLetter = getWord[::-1]
                startingLetter = startingLetter[0]
                print("Please Enter the word starts with : ", startingLetter)


            else :
                startingLetter = getWord[::-1]
                startingLetter = startingLetter[0]
                for findWord in range(len(playerArr)) :

                    # if getWord[0] == startingLetter :
                    #     if playerArr[findWord] == getWord:
                    #         print("Same Word repeated Again")
                    #         return playerArr
                    #
                    #     playerArr.append(getWord)
                    # else :
                    #     print("")
                    print("Please Enter the word starts with : ", startingLetter)

                    if playerArr[findWord] == getWord:
                        print("Same Word repeated Again")
                        return playerArr

                    elif getWord[0] == startingLetter :
                        playerArr.append(getWord)
                        startingLetter = getWord[::-1]
                        startingLetter = startingLetter[0]
                    else :
                        print("First letter nt same")
                        print(playerNameArr[i], "Lost the game")
                        return playerNameArr

    print("Game Over")
    return playerArr

# def countCheck(totalPeople):
#     if totalPeople > 1 and totalPeople < 5:
#         return outputPlayer()


print("Naming Gaming")
print("Let's Start")
#totalPlayers()
attempt = 1
#totalWords()
totalPeople = totalPlayers()

if totalPeople > 1 and totalPeople < 5 :
    print(outputPlayer(totalPeople))

elif totalPeople < 2 or totalPeople > 4  :
    print("Total Players should be less than 5 or greater than 1(More Than 1 attempt will EXIT the game): ",   attempt,"st attempt")
    totalPeople = totalPlayers()

    if totalPeople > 1 and totalPeople < 5 :
        print(outputPlayer(totalPeople))

    else:
        print("Total Players should be less than 5 or greater than 1(More Than 1 attempt will EXIT the game): ", attempt + 1 ,"nd attempt")
        print("More than one attempthas been reached")
        sys.exit("GAME OVER . Reason: Imapporiate Number Of Players In Game As Per Rule")


