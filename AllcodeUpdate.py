# # # # # year = 2024
# # # #
# # year = int(input("Enter a year: "))
# #
# # if (year % 400 == 0) and (year % 100 == 0):
# #     print("{0} is a leap year".format(year))
# #
# # elif (year % 4 == 0) and (year % 100 != 0):
# #     print("{0} is a leap year.".format(year))
# #
# # else:
# #     print("{0} is not a leap year.".format(year))
# # n = int(input("Enter"))
# # for i in range(n-1):
# #     for j in range(i,n):
# #         print(" ", end = " ")
# #     for j in range(i+1):
# #         print("*", end = " ")
# #     for j in range(i):
# #         print("*", end = " ")
# #     print()
# #
# # for i in range(n):
# #     for j in range(i+1):
# #         print(" ", end = " ")
# #     for j in range(i,n-1):
# #         print("*", end = " ")
# #     for j in range(i,n):
# #         print("*", end = " ")
# #     print()
# # for i in range(n):
# #     for j in range(0,n) :
# #         if ((j == 0 or j == 4) and i >=0) or ((j == 1 or j == 3) and i == 1) or (j == 2 and i == 2) :
# #            print("*", end = " ")
# #         else :
# #             print(" ", end = " ")
# #     print()
# # for i in range(n):
# #     for j in range(0,n) :
# #         if (i == 0 and j == 2) or (i == 1 and (j == 1 or j == 3)) or (i == 2 and (j >= 1 or j <= 3)) or (i == 3 and (j == 0 or j == 4)) or (i == 4 and (j == 0 or j == 4)):
# #             print("*", end=" ")
# #         else:
# #             print(" ", end=" ")
# #     print()
# # lower = int(input("enter lower"))
# # upper = int(input("enter upper"))
# #
# # print("Prime numbers between", lower, "and", upper, "are:")
# #
# # for num in range(lower, upper + 1):
# #    if num > 1:
# #        for i in range(2, num):
# #            if (num % i) == 0:
# #                break
# #        else:
# #            print(num)
# # # ------------------------------------------------------------------------------------------------------------------------
# # n = int(input("enter a number"))
# # temp = n
# # sum = 0
# # while n > 0 :
# #     r = n % 10
# #     sum = sum * 10 + r
# #     n = n // 10
# # if temp == sum :
# #     print("palindrome")
# # else :
# #     print("not a palindrome")
# #
# # nap = input("Enter the string").upper()
# # nap_array = []
# # nap_array_rev = []
# # print(nap[1])
# # for i in range(len(nap)-1,-1,-1) :
# #     nap_array_rev.append(nap[i].upper())
# #
# # for i in range(0,len(nap),1) :
# #     nap_array.append(nap[i].upper())
# # if nap_array == nap_array_rev :
# #     print("Palindrome")
# # else :
# #     print("not a palindrome")
# # # n = input()
# # # temp = n
# # # val = n[::-1]
# # # if  ==
# # #
# # # prime
# # num = 11
# # # If given number is greater than 1
# # if num > 1:
# #     # Iterate from 2 to n / 2
# #     for i in range(2, int(num/2)+1):
# #         # If num is divisible by any number between
# #         # 2 and n / 2, it is not prime
# #         if (num % i) == 0:
# #             print(num, "is not a prime number")
# #             break
# #     else:
# #         print(num, "is a prime number")
# # else:
# #     print(num, "is not a prime number")
# # # ----------------------------------------------------------------------------------
# # lower = int(input("enter lower"))
# # upper = int(input("enter upper"))
# #
# # print("Prime numbers between", lower, "and", upper, "are:")
# #
# # for num in range(lower, upper + 1):
# #    if num > 1:
# #        for i in range(2, num):
# #            if (num % i) == 0:
# #                break
# #        else:
# #            print(num)
# # # -----------------------------------------------------
# # n = int(input("Enter the number"))
# # sum = 0
# # tem = n
# #
# # for i in range(1, n):
# #     r = n % 10
# #     sum = sum + r * r * r
# #     n = n // 10
# # if (tem == sum):
# #     print(1)
# # else:
# #     print(0)
# # # ---------------------------------------------------------------------------
# # a=0
# # b=1
# # n=int(input("enter the number"))
# # # temp=n
# # count=0
# # while(count<=n):
# #     print(a)
# #     c=a+b
# #     a=b
# #     b=c
# #     count+=1
# # # ------------------------------------------------------------------
# # f=1
# # n=int(input("enter the number"))
# # for i in range(1,n+1):
# #     f=f*i
# #     print(f)
# # # ----------------------------------------------------------
# # num = int(input("enter the capacity of the array: "))
# # arrSet = []
# # positive = 1
# # findNum = int(input("enter the num to be found: "))
# # for i in range(0,num,1) :
# #     numGet = int(input("enter the num to array"))
# #     arrSet.append(numGet)
# # print(arrSet)
# # for i in range(0,num,1) :
# #     if findNum == arrSet[i] :
# #         print(i)
# #         positive = 0
# #         break
# # if positive == 1 :
# #     print("the number is not in the array")
# # # -----------------------------------------------------
# # num = int(input("enter the capacity of the array: "))
# # arrSet = []
# # for i in range(0,num,1) :
# #     numGet = int(input("enter the num to array"))
# #     arrSet.append(numGet)
# # print(arrSet)
# # for i in range(0, num, 1) :
# #     for j in range(0, num-i-1, 1) :
# #         if arrSet[j] > arrSet[j+1] :
# #             arrSet[j], arrSet[j+1] = arrSet[j+1], arrSet[j]
# # print(arrSet)
# # #---------------------------------------------------------------------------
#
# noOfClg = int(input("Enter clg numbers :"))
# clgDetailArr = [["2021/08/18", 1001, 2],["2021/08/19", 1002, 2],["2021/08/20", 1003, 2],["2021/08/21", 1004, 2],["2021/08/22", 1005, 2]]
# # clgDetailArr = []
# # for i in range(0, noOfClg, 1) :
# #     year = input("year")
# #     slot = int(input("Enter slot numbers :"))
# #     slotCount = int(input("Enter slot count :"))
# #     clgDetailArr.append([year, slot, slotCount])
# noOfApply = int(input("apply"))
# stuArray = [[101, 99, 20, 95, 90], [102, 93, 21, 95, 90], [103, 93, 22, 95, 90], [104, 92, 23, 95, 90], [105, 92, 23, 96, 90], [106, 91, 24, 97, 90], [107, 91, 24, 99, 91], [108, 90, 25, 98, 92], [109, 90, 25, 98, 92]]
# # stuArray = []
# # for i in range(0, noOfApply, 1) :
# #     stdID = int(input("id"))
# #     cutOff = int(input("cutoff:"))
# #     age = int(input("Age"))
# #     hsc = int(input("hsc:"))
# #     sslc = int(input("sslc:"))
# #
# #     stuArray.append([stdID, cutOff, age, hsc, sslc])
# # print(clgDetailArr)
# print(stuArray)
# sorrtedArray = []
# for i in range(0, noOfApply, 1):
#     for j in range(0, noOfApply-i-1):
#         if (stuArray[j][1] < stuArray[j+1][1])  :
#             temp = stuArray[j]
#             stuArray[j] = stuArray[j + 1]
#             stuArray[j + 1] = temp
#         # if stuArray[j][1] == stuArray[j+1][1]:
#         #     if (stuArray[j][2] < stuArray[j + 1][2]):
#         #         temp = stuArray[j]
#         #         stuArray[j] = stuArray[j + 1]
#         #         stuArray[j + 1] = temp
#         # if stuArray[j][2] == stuArray[j + 1][2]:
#         #     if (stuArray[j][3] < stuArray[j + 1][3]):
#         #         temp = stuArray[j]
#         #         stuArray[j] = stuArray[j + 1]
#         #         stuArray[j + 1] = temp
#         # if stuArray[j][3] == stuArray[j + 1][3]:
#         #     if (stuArray[j][4] < stuArray[j + 1][4]):
#         #         temp = stuArray[j]
#         #         stuArray[j] = stuArray[j + 1]
#         #         stuArray[j + 1] = temp
#         # if stuArray[j][4] == stuArray[j + 1][4]:
#         #     if (stuArray[j][0] > stuArray[j + 1][0]):
#         #         temp = stuArray[j]
#         #         stuArray[j] = stuArray[j + 1]
#         #         stuArray[j + 1] = temp
# # print(stuArray)
# cutOffArray = stuArray
# # print(cutOffArray)
# for i in range(0, noOfApply, 1):
#     for j in range(0, noOfApply-i-1):
#         if cutOffArray[j][1] == cutOffArray[j+1][1]:
#             if (cutOffArray[j][2] < cutOffArray[j + 1][2]):
#                 temp = cutOffArray[j]
#                 cutOffArray[j] = cutOffArray[j + 1]
#                 cutOffArray[j + 1] = temp
#
# ageArray = cutOffArray
# # print(ageArray)
# for i in range(0, noOfApply, 1):
#     for j in range(0, noOfApply-i-1):
#         if ageArray[j][2] == ageArray[j+1][2] and cutOffArray[j][1] == cutOffArray[j+1][1]:
#             if (ageArray[j][3] < ageArray[j + 1][3]):
#                 temp = ageArray[j]
#                 ageArray[j] = ageArray[j + 1]
#                 ageArray[j + 1] = temp
#
# hscArray = ageArray
# # print(hscArray)
# for i in range(0, noOfApply, 1):
#     for j in range(0, noOfApply-i-1):
#         if hscArray[j][3] == hscArray[j+1][3] and ageArray[j][2] == ageArray[j+1][2] and cutOffArray[j][1] == cutOffArray[j+1][1]:
#             if (hscArray[j][4] < hscArray[j + 1][4]):
#                 temp = hscArray[j]
#                 hscArray[j] = hscArray[j + 1]
#                 hscArray[j + 1] = temp
#
# sslcArray = hscArray
# print(sslcArray)
# for i in range(0, noOfApply, 1):
#     for j in range(0, noOfApply-i-1):
#         if sslcArray[j][4] == sslcArray[j+1][4] and hscArray[j][3] == hscArray[j+1][3] and ageArray[j][2] == ageArray[j+1][2] and cutOffArray[j][1] == cutOffArray[j+1][1]:
#             if (sslcArray[j][0] > sslcArray[j + 1][0]):
#                 temp = sslcArray[j]
#                 sslcArray[j] = sslcArray[j + 1]
#                 sslcArray[j + 1] = temp
# #
# finalArray = sslcArray
# print(finalArray)
#
# # print(ageArray)
#
# # for i in range(0, noOfApply, 1):
# #     for j in range(0, noOfApply-i-1):
# #         if (stuArray[j][1] < stuArray[j+1][1]) :
# #             temp = stuArray[j]
# #             stuArray[j] = stuArray[j + 1]
# #             stuArray[j + 1] = temp
# #         elif stuArray[j][1] == stuArray[j+1][1] :
# #             if (stuArray[j][2] < stuArray[j + 1][2]):
# #                 temp = stuArray[j]
# #                 stuArray[j] = stuArray[j + 1]
# #                 stuArray[j + 1] = temp
# #             elif stuArray[j][2] == stuArray[j + 1][2] :
# #                 if (stuArray[j][3] < stuArray[j + 1][3]):
# #                     temp = stuArray[j]
# #                     stuArray[j] = stuArray[j + 1]
# #                     stuArray[j + 1] = temp
# #                 elif stuArray[j][3] == stuArray[j + 1][3] :
# #                     if (stuArray[j][4] < stuArray[j + 1][4]):
# #                         temp = stuArray[j]
# #                         stuArray[j] = stuArray[j + 1]
# #                         stuArray[j + 1] = temp
# #                     elif stuArray[j][4] == stuArray[j + 1][4]:
# #                         if (stuArray[j][0] < stuArray[j + 1][0]):
# #                             # print(stuArray[j][2])
# #                             # print(stuArray[j+1][2])
# #                             temp = stuArray[j]
# #                             stuArray[j] = stuArray[j + 1]
# #                             stuArray[j + 1] = temp
# #
# # for i in range(0, noOfApply, 1):
# #     for j in range(0, noOfApply - i - 1):
# #         if (stuArray[j][1] == stuArray[j + 1][1]):
# #             if (stuArray[j][2] < stuArray[j + 1][2]):
# #                 temp = stuArray[j]
# #                 stuArray[j] = stuArray[j + 1]
# #                 stuArray[j + 1] = temp
# # for i in range(0, noOfApply, 1):
# #     for j in range(0, noOfApply - i - 1):
# #         if (stuArray[j][2] == stuArray[j + 1][2]):
# #             if (stuArray[j][3] < stuArray[j + 1][3]):
# #                 temp = stuArray[j]
# #                 stuArray[j] = stuArray[j + 1]
# #                 stuArray[j + 1] = temp
# # for i in range(0, noOfApply, 1):
# #     for j in range(0, noOfApply - i - 1):
# #         if (stuArray[j][3] == stuArray[j+1][3]) :
# #             if (stuArray[j][4] < stuArray[j + 1][4]):
# #                 temp = stuArray[j]
# #                 stuArray[j] = stuArray[j + 1]
# #                 stuArray[j + 1] = temp
# # for i in range(0, noOfApply, 1):
# #     for j in range(0, noOfApply - i - 1):
# #         if (stuArray[j][4] == stuArray[j+1][4]):
# #             if (stuArray[j][0] < stuArray[j + 1][0]):
# #                 # print(stuArray[j][2])
# #                 # print(stuArray[j+1][2])
# #                 temp = stuArray[j]
# #                 stuArray[j] = stuArray[j + 1]
# #                 stuArray[j + 1] = temp
# #
# # print(stuArray)
#
# # for i in range(0, noOfClg, 1) :
# #     slots = clgDetailArr[i][1]
# #     for j in range(0, slots, 1):
# #         seats = clgDetailArr[i][2]
# #         for k in range(0, seats, 1):
# #             for l in range(0, len(stuArray),1):
# #                 if j == 0 and k == 0:
# #                     print("1st slot -> 1st seat -> {0}".format(stuArray[i][0]))
# #                 elif j == 0 and k == 1:
# #                     print("1st slot -> 2nd seat -> {0}".format(stuArray[i][0]))
# #                 elif j == 1 and k == 0:
# #                     print("2nd slot -> 1st seat -> {0}".format(stuArray[i][0]))
# #                 elif j == 1 and k == 1:
# #                     print("2nd slot -> 2nd seat -> {0}".format(stuArray[i][0]))
#
# # z = noOfApply
# # for i in range(0, noOfClg, 1) :
# #     seat = clgDetailArr[i][2]
# #     for j in range(0,seat,1):
# #         for k in range(0, z, 1):
# #             if stuArray[z][2] == stuArray[z + 1][2]:
# #                 if stuArray[z][1] == stuArray[z + 1][1]:
# #                     if stuArray[z][3] == stuArray[z + 1][3]:
# #                         if stuArray[z][4] == stuArray[z + 1][4]:
# #                             if stuArray[z][0] > stuArray[z + 1][0]:
# #                                 print(i,"clg-->",j,"seat-->",stuArray[z][0])
# #                             else:
# #                                 print(i, "clg -->", j, "seat-->", stuArray[z+1][0])
# #                         else:
# #                             print("Ex")
# #                     else:
# #                         print("Ex")
# #                 else :
# #                     print("Ex")
# #             else :
# #                 print("Ex")
#
# # [[slotid[stuids]]]
# outputArray = []
# for i in range(0, noOfClg, 1):
#     outputArray.append([[clgDetailArr[i][1]], clgDetailArr[i][0]])
# print(outputArray)
# slotsApp = []
# count = 0
# for i in range(0, noOfClg, 1):
#     slot = clgDetailArr[i][2]
#
#
#     while slot > 0:
#         if count >= len(sslcArray):
#             count = count - 1
#             slotsApp.pop(len(sslcArray) - 1)
#         else :
#             slotsApp.append(sslcArray[count][0])
#             count = count + 1
#             slot = slot - 1
#
# finalOutput = []
# countAgain = 0
# for i in range(0, noOfClg, 1):
#     slot = clgDetailArr[i][2]
#
#     while slot > 0:
#         if countAgain >= len(sslcArray):
#             countAgain = countAgain - 1
#             finalOutput.pop(len(sslcArray) - 1)
#         else:
#             finalOutput.append([outputArray[i], slotsApp[countAgain]])
#             countAgain = countAgain + 1
#             slot = slot - 1
#
# for i in range(0, len(finalOutput), 1):
#     print(finalOutput[i])
# dateInput = "2021/08/20"
# dateArray = []
# for i in range(0, len(finalOutput), 1):
#     if dateInput == finalOutput[i][0][1]:
#         dateArray.append(finalOutput[i])
#
#
#
# for i in range(0, len(dateArray), 1):
#     print(dateArray[i])
val = "59.98"
arra = []
arra.extend(val)
print(arra)