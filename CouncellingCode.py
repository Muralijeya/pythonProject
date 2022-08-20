# # # year = 2024
# #
year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year.".format(year))

else:
    print("{0} is not a leap year.".format(year))
n = int(input("Enter"))
for i in range(n-1):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i,n-1):
        print("*", end = " ")
    for j in range(i,n):
        print("*", end = " ")
    print()
for i in range(n):
    for j in range(0,n) :
        if ((j == 0 or j == 4) and i >=0) or ((j == 1 or j == 3) and i == 1) or (j == 2 and i == 2) :
           print("*", end = " ")
        else :
            print(" ", end = " ")
    print()
for i in range(n):
    for j in range(0,n) :
        if (i == 0 and j == 2) or (i == 1 and (j == 1 or j == 3)) or (i == 2 and (j >= 1 or j <= 3)) or (i == 3 and (j == 0 or j == 4)) or (i == 4 and (j == 0 or j == 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
lower = int(input("enter lower"))
upper = int(input("enter upper"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
# ------------------------------------------------------------------------------------------------------------------------
n = int(input("enter a number"))
temp = n
sum = 0
while n > 0 :
    r = n % 10
    sum = sum * 10 + r
    n = n // 10
if temp == sum :
    print("palindrome")
else :
    print("not a palindrome")

nap = input("Enter the string").upper()
nap_array = []
nap_array_rev = []
print(nap[1])
for i in range(len(nap)-1,-1,-1) :
    nap_array_rev.append(nap[i].upper())

for i in range(0,len(nap),1) :
    nap_array.append(nap[i].upper())
if nap_array == nap_array_rev :
    print("Palindrome")
else :
    print("not a palindrome")
# n = input()
# temp = n
# val = n[::-1]
# if  ==
#
# prime
num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
# ----------------------------------------------------------------------------------
lower = int(input("enter lower"))
upper = int(input("enter upper"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
# -----------------------------------------------------
n = int(input("Enter the number"))
sum = 0
tem = n

for i in range(1, n):
    r = n % 10
    sum = sum + r * r * r
    n = n // 10
if (tem == sum):
    print(1)
else:
    print(0)
# ---------------------------------------------------------------------------
a=0
b=1
n=int(input("enter the number"))
# temp=n
count=0
while(count<=n):
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
# ------------------------------------------------------------------
f=1
n=int(input("enter the number"))
for i in range(1,n+1):
    f=f*i
    print(f)
# ----------------------------------------------------------
num = int(input("enter the capacity of the array: "))
arrSet = []
positive = 1
findNum = int(input("enter the num to be found: "))
for i in range(0,num,1) :
    numGet = int(input("enter the num to array"))
    arrSet.append(numGet)
print(arrSet)
for i in range(0,num,1) :
    if findNum == arrSet[i] :
        print(i)
        positive = 0
        break
if positive == 1 :
    print("the number is not in the array")
# -----------------------------------------------------
num = int(input("enter the capacity of the array: "))
arrSet = []
for i in range(0,num,1) :
    numGet = int(input("enter the num to array"))
    arrSet.append(numGet)
print(arrSet)
for i in range(0, num, 1) :
    for j in range(0, num-i-1, 1) :
        if arrSet[j] > arrSet[j+1] :
            arrSet[j], arrSet[j+1] = arrSet[j+1], arrSet[j]
print(arrSet)
#---------------------------------------------------------------------------
noOfClg = int(input("Enter clg numbers :"))
clgDetailArr = []
for i in range(0, noOfClg, 1) :
    year = input("year")
    slot = int(input("Enter slot numbers :"))
    slotCount = int(input("Enter slot count :"))
    clgDetailArr.append([year, slot, slotCount])
noOfApply = int(input("apply"))
stuArray = []
for i in range(0, noOfApply, 1) :
    stdID = int(input("id"))
    age = int(input("Age"))
    cutOff = int(input("cutoff:"))
    hsc = int(input("hsc:"))
    sslc = int(input("sslc:"))

    stuArray.append([stdID, age, cutOff, hsc, sslc])
# print(clgDetailArr)
print(stuArray)
# sorrtedArray = []
for i in range(0,noOfApply, 1):
    for j in range(0,noOfApply-i-1):
        if (stuArray[j][2] < stuArray[j+1][2]) or (stuArray[j][1] > stuArray[j+1][1]) or (stuArray[j][3] > stuArray[j+1][3]) or (stuArray[j][4] > stuArray[j+1][4]) or (stuArray[j][0] > stuArray[j+1][0]):
            # print(stuArray[j][2])
            # print(stuArray[j+1][2])
            temp = stuArray[j]
            stuArray[j] = stuArray[j+1]
            stuArray[j+1] = temp

print(stuArray)
z = noOfApply
# for i in range(0, noOfClg, 1) :
#     seat = clgDetailArr[i][2]
#     for j in range(0,seat,1):
#         for k in range(0, z, 1):
#             if stuArray[z][2] == stuArray[z + 1][2]:
#                 if stuArray[z][1] == stuArray[z + 1][1]:
#                     if stuArray[z][3] == stuArray[z + 1][3]:
#                         if stuArray[z][4] == stuArray[z + 1][4]:
#                             if stuArray[z][0] > stuArray[z + 1][0]:
#                                 print(i,"clg-->",j,"seat-->",stuArray[z][0])
#                             else:
#                                 print(i, "clg -->", j, "seat-->", stuArray[z+1][0])
#                         else:
#                             print("Ex")
#                     else:
#                         print("Ex")
#                 else :
#                     print("Ex")
#             else :
#                 print("Ex")