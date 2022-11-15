#© 2022 NaveenKumar MuraliTharan. All Rights Reserved.
#Words naming Game
#Problem Statement
#1.In this game we can have maximum of four players and minimum of two(1 vs com will be updated)
#2.The Game should start with player 1 spelling a meaningfull word and the last letter of the word will
#be used by the player 2 to spell the next meaningfull word.
#3.The words which are already used should not be used again.
#4.Timing for a word will be used in development progress.
#5.if word is not guessed then the game will be end.
import sys

def totalPlayers() :
    totalPlayers = int(input("Please Enter Total Number of Players(min 2 : max4) : "))

    return totalPlayers

def playersCountLogic(totalPeople) :
    if totalPeople > 1 and totalPeople < 5 :
        return outputPlayer(totalPeople)

    elif totalPeople < 2 or totalPeople > 4:
        print("Total Players should be less than 5 or greater than 1(More Than 1 attempt will EXIT the game): 1st Attempt")
        totalPeople = totalPlayers()

        if totalPeople > 1 and totalPeople < 5:
            return outputPlayer(totalPeople)

        else:
            print("Total Players should be less than 5 or greater than 1(More Than 1 attempt will EXIT the game): 2nd attempt")
            print("More than one attempts been reached")
            sys.exit("GAME OVER . Reason: Imapporiate Number Of Players In Game As Per Rule")


def totalWords() :
    totalPlayers = int(input("Please Enter Total Number of words to play this game : "))
    if totalPlayers == 0 :
        print("Word count should be greater than or equal to 1")
        totalPlayers = int(input("Please Enter Total Number of words to play this game : "))
        if totalPlayers == 0 :
            sys.exit("Words Cannot be 0")
        return totalPlayers
    else :
        return totalPlayers

# def startLetterLogic(startingLetter, getWord) -> bool:
#     if startingLetter == getWord[0]:
#         return 0
#     else:
#         return 1

# def startingLetterLogic() :
#     startingLetter = getWord[::-1]
#     startingLetter = startingLetter[0]
#
#     print("Please Enter the word starts with : ", startingLetter)


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
                if startingLetter == getWord[0] :
                    startingLetter = getWord[::-1]
                    startingLetter = startingLetter[0]
                    print("Please Enter the word starts with : ", startingLetter)
                    for findWord in range(len(playerArr)):
                        if playerArr[findWord] == getWord:
                            print("Same Word repeated Again")
                            return playerArr
                    playerArr.append(getWord)
                    # returnElement = startLetterLogic(startingLetter, getWord)
                    # print(returnElement)

                else :
                    print(playerNameArr[i],"Lost the Game. The word does not have the starting letter as expected")
                    print("Game Over")
                    sys.exit()
    print("Game Over")
    return playerArr

# def countCheck(totalPeople):
#     if totalPeople > 1 and totalPeople < 5:
#         return outputPlayer()


print("Naming Gaming")
print("Let's Start")
#totalPlayers()
#totalWords()
totalPeople = totalPlayers()
print(playersCountLogic(totalPeople))
