#Direction problem of mallow


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