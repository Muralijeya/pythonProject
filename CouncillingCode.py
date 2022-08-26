noOfClg = int(input("Enter clg numbers :"))
# clgDetailArr = [["2021/08/18", 1001, 2],["2021/08/19", 1002, 2],["2021/08/20", 1003, 2],["2021/08/21", 1004, 2],["2021/08/22", 1005, 2]]
clgDetailArr = []
for i in range(0, noOfClg, 1) :
    year = input("year")
    slot = int(input("Enter slot numbers :"))
    slotCount = int(input("Enter slot count :"))
    clgDetailArr.append([year, slot, slotCount])
noOfApply = int(input("apply"))
# tuArray = [[101, 99, 20, 95, 90], [102, 93, 21, 95, 90], [103, 93, 22, 95, 90], [104, 92, 23, 95, 90], [105, 92, 23, 96, 90], [106, 91, 24, 97, 90], [107, 91, 24, 99, 91], [108, 90, 25, 98, 92], [109, 90, 25, 98, 92]]
stuArray = []
for i in range(0, noOfApply, 1) :
    stdID = int(input("id"))
    cutOff = int(input("cutoff:"))
    age = int(input("Age"))
    hsc = int(input("hsc:"))
    sslc = int(input("sslc:"))

    stuArray.append([stdID, cutOff, age, hsc, sslc])
# print(clgDetailArr)
# print(stuArray)
for i in range(0, noOfApply, 1):
    for j in range(0, noOfApply-i-1):
        if (stuArray[j][1] < stuArray[j+1][1])  :
            temp = stuArray[j]
            stuArray[j] = stuArray[j + 1]
            stuArray[j + 1] = temp

# stuArray = stuArray
# print(cutOffArray)
for i in range(0, noOfApply, 1):
    for j in range(0, noOfApply-i-1):
        if stuArray[j][1] == stuArray[j + 1][1]:
            if (stuArray[j][2] < stuArray[j + 1][2]):
                temp = stuArray[j]
                stuArray[j] = stuArray[j + 1]
                stuArray[j + 1] = temp

# stuArray = stuArray
# print(ageArray)
for i in range(0, noOfApply, 1):
    for j in range(0, noOfApply-i-1):
        if stuArray[j][2] == stuArray[j + 1][2] and stuArray[j][1] == stuArray[j + 1][1]:
            if (stuArray[j][3] < stuArray[j + 1][3]):
                temp = stuArray[j]
                stuArray[j] = stuArray[j + 1]
                stuArray[j + 1] = temp

# stuArray = stuArray
# print(hscArray)
for i in range(0, noOfApply, 1):
    for j in range(0, noOfApply-i-1):
        if stuArray[j][3] == stuArray[j + 1][3] and stuArray[j][2] == stuArray[j + 1][2] and stuArray[j][1] == stuArray[j + 1][1]:
            if (stuArray[j][4] < stuArray[j + 1][4]):
                temp = stuArray[j]
                stuArray[j] = stuArray[j + 1]
                stuArray[j + 1] = temp

# stuArray = stuArray
# print(stuArray)
for i in range(0, noOfApply, 1):
    for j in range(0, noOfApply-i-1):
        if stuArray[j][4] == stuArray[j + 1][4] and stuArray[j][3] == stuArray[j + 1][3] and stuArray[j][2] == stuArray[j + 1][2] and stuArray[j][1] == stuArray[j + 1][1]:
            if (stuArray[j][0] > stuArray[j + 1][0]):
                temp = stuArray[j]
                stuArray[j] = stuArray[j + 1]
                stuArray[j + 1] = temp

finalArray = stuArray
print(finalArray)

outputArray = []
for i in range(0, noOfClg, 1):
    outputArray.append([[clgDetailArr[i][1]], clgDetailArr[i][0]])
print(outputArray)
slotsApp = []
count = 0
for i in range(0, noOfClg, 1):
    slot = clgDetailArr[i][2]
    while slot > 0:
        if count >= len(stuArray):
            count = count - 1
            slotsApp.pop(len(stuArray) - 1)
        else :
            slotsApp.append(stuArray[count][0])
            count = count + 1
            slot = slot - 1

finalOutput = []
countAgain = 0
for i in range(0, noOfClg, 1):
    slot = clgDetailArr[i][2]
    while slot > 0:
        if countAgain >= len(stuArray):
            countAgain = countAgain - 1
            finalOutput.pop(len(stuArray) - 1)
        else:
            finalOutput.append([outputArray[i], slotsApp[countAgain]])
            countAgain = countAgain + 1
            slot = slot - 1


for i in range(0, len(finalOutput), 1):
    print(finalOutput[i])
newArray = []
for i in range(0, len(finalOutput), 1):
    for j in range(0, len(finalOutput)-i-1):
        if finalOutput[j][0][0] == finalOutput[j + 1][0][0]:
            newArray.append([finalOutput[j][0], finalOutput[j][1], finalOutput[j + 1][1]])
    else:
        newArray.append([finalOutput[len(finalOutput) - 1][0], finalOutput[len(finalOutput) - 1][1]])

    break

for i in range(0, len(newArray), 1):
    print(newArray[i])


dateInput = "2021/08/22"
for i in range(0,len(newArray), 1):
    if dateInput == newArray[i][0][1]:
        # print(len(newArray[i][1]))
        if len(newArray[i]) == 2:
            print("SlotNo: {0} -> SeatNo: {1} -> {2}".format(i+1 , 1, newArray[i][1]))
        else :
            count = 1
            val = len(newArray[i]) - 1
            while val > 0 :
                print("SlotNo: {0} -> SeatNo: {1} -> {2}".format(i + 1, count,newArray[i][count]))
                count = count + 1
                val = val -1
