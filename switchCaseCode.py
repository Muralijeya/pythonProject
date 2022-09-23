#1.Print elements one by one present in a list
#2.Print a range with given a and b
#3.Print 13 table with 10
#4.append empty list with given range with getting input
#5.break and continue(create a list with fruits, if "" == list in fruit break, continue

# #1
# newList = ["app","Web","0",1,4]
# for l in range(0, len(newList), 1):
#     print(newList[l])


# 1 Print elements one by one present in a list
# a = [1,2,3,4,5]
# for i in range(0, len(a), 1):
#     print(a[i])

# a = int(input("Enter a number"))
# b = int(input("Enter a range"))
# for i in range(1, b+1, 1) :
#     print(i,"*",a,"=",i*a)

# a = int(input("Enter value"))
# b = int(input("Enter range"))
# for mul in range(1, b+1, 1) :
#     print(mul,"*",a,"=",mul*a)
# a = int(input("Enter Starting Range"))
# b = int(input("Enter Ending Range"))
# for i in range(a,b,1) :
#     print(i)

#Break & Continue
# a = ["dragonfrt","Kiwi","banana","apple","jackfrt"]
# for x in a :
# #     if x == "Kiwi":
# #         break
# #     print(x)
# def linearSearch(b) :
#     a = ["dragonfrt", "Kiwi", "banana", "apple", "jackfrt"]
#
#
# b = "Kiwi"
# ans = linearSearch(b)
# print(b,"with its index number is",ans)


a = 10
b = []
c = []
for i in range(0, a, 1) :
    num = input("enter fruit names")
    b.append(num)
print(b)
for i in range(2, 8, 1) :
    print(b[i])
    c.append(b[i])
print(c)
d = input("enter elment tobe searchrd")

for i in range(0, len(c), 1):
    if d == c[i] :
        print(i)
else:
    print(i)

