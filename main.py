#© 2022 NaveenKumar MuraliTharan. All Rights Reserved.
# 8072120536
# num = int(input("enter the capacity of the array: "))
# arrSet = []
# positive = 1
# findNum = int(input("enter the num to be found: "))
# for i in range(0,num,1) :
#     numGet = int(input("enter the num to array"))
#     arrSet.append(numGet)
# print(arrSet)
# for i in range(0,num,1) :
#     if findNum == arrSet[i] :
#         print(i)
#         positive = 0
#         break
# if positive == 1 :
#     print("the number is not in the array")
# arrSet.sort()
# print(arrSet)
# list=[10,1,5,0,6,8,7,3,11,4]
#
# i=1
# while(i<10):# 2 < 10
#   element=list[i]# ele = list[2] = 1
#   j=i# j = 2
#   i=i+1 # i = 1 + 1 = 3
#
#   while(j>0 and list[j-1]>element): # check 2 > 0 and list[ 2-1 = 1 ] > 10
#     list[j]=list[j-1]
#     j=j-1
#
#   list[j]=element
#
# i=0
# while(i<10):
#   print (list[i])
#   i=i+1
# attempt = 1
# while attempt < 3:
#     if attempt == 0:
#         print("Total Players should be less than 5 or greater than 1(More Than 2 attempt will EXIT the game): ",
#               attempt, "st attempt")
#         attempt = attempt + 1
#         countCheck(totalPeople)
#     elif attempt == 1:
#         print("Total Players should be less than 5 or greater than 1(More Than 2 attempt will EXIT the game): ",
#               attempt, "nd attempt")
#         attempt = attempt + 1
#         countCheck(totalPeople)
#     else:
#         sys.exit("More than two attempts have arrised : GAME OVER")

# #Direction problem of mallow
# import sys
# numOfLaps = int(input("Enter the Number of laps: "))
# distance = []
# speed = []
# direction = []
# time = 0
# xAxis = 0
# yAxis = 0
#
# for i in range(0, numOfLaps, 1):
#     dis = int(input("Enter distance: "))
#     spd = int(input("Enter speed: "))
#     direc = input("Enter direction: ").upper()
#     distance.append(dis)
#     speed.append(spd)
#
#     if direc == "N" or direc == "S" or direc == "E" or direc == "W":
#         direction.append(direc)
#     else :
#         sys.exit("Invlid direction")#exit() or quit()
#
#     time = time + distance[i] / speed[i]  # 1/5 + 1/3 + 1/20
#
#     if direction[i] == "N":
#         yAxis = yAxis + distance[i]
#     elif direction[i] == "S":
#         yAxis = yAxis - distance[i]
#     elif direction[i] == "E":
#         xAxis = xAxis + distance[i]
#     elif direction[i] == "W":
#         xAxis = xAxis - distance[i]
#     else :
#         break
#
#
# # for i in range(0, numOfLaps, 1):
# #     print(distance[i], speed[i], direction[i])
# mins = time * 60
# print(round(mins), "Mins")
# if xAxis > 0 and yAxis > 0:
#     print(direction[0] + "E")
# else:
#     print(direction[0] + "W")
# #------------------------------------------------------------------------
import sys

def timeInterval(distance, speed) :
    time = 0
    for i in range(0, numOfLaps, 1):
        time = time + distance[i] / speed[i]  # 1/5 + 1/3 + 1/20
    mins = time * 60
    return mins


def directionEnd(distance, direction) :
    xAxis = 0
    yAxis = 0
    for i in range(0, numOfLaps, 1):
        if direction[i] == "N":
            yAxis = yAxis + distance[i]
        elif direction[i] == "S":
            yAxis = yAxis - distance[i]
        elif direction[i] == "E":
            xAxis = xAxis + distance[i]
        elif direction[i] == "W":
            xAxis = xAxis - distance[i]
        else:
            break

    if xAxis > 0 and yAxis > 0:
        return direction[0] + "E"
    else:
        return direction[0] + "W"


numOfLaps = int(input("Enter the Number of laps: "))
distance = []
speed = []
direction = []

for i in range(0, numOfLaps, 1):
    dis = int(input("Enter distance: "))
    spd = int(input("Enter speed: "))
    direc = input("Enter direction: ").upper()
    distance.append(dis)
    speed.append(spd)

    if direc == "N" or direc == "S" or direc == "E" or direc == "W":
        direction.append(direc)
    else :
        sys.exit("Invlid direction")#exit() or quit()

for i in range(0, numOfLaps, 1):
    print(distance[i], speed[i], direction[i])
output1 = timeInterval(distance, speed)
output2 = directionEnd(distance, direction)
print("The time taken : " , round(output1))
print("The direction reached : " , output2)
# change = [[2000, 10],[500,10],[100,10],[50,10],[20,10],[10,10],[5,10],[2,10],[1,10]]
# given = 100
# bill = 100
# arrat = []
# amount = given - bill
# rupee = []
# count = []
# ans = []
# for i in range(0 ,len(change), 1) :
#     cou = change[i][1]
#     route = 0
#     while cou > 0 :
#         amount = amount - change[i][0]
#         if amount < 0 :
#             amount = amount + change[i][0]
#             break
#         else :
#             route = route + 1
#             cou = cou - 1
#     arrat.append([change[i][0],route])
# print(arrat)
