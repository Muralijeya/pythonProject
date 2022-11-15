import sys
# # # # #1.Print elements one by one present in a list
# # # # #2.Print a range with given a and b
# # # # #3.Print 13 table with 10
# # # # #4.append empty list with given range with getting input
# # # # #5.break and continue(create a list with fruits, if "" == list in fruit break, continue
# # # #
# # # # # #1
# # # # # newList = ["app","Web","0",1,4]
# # # # # for l in range(0, len(newList), 1):
# # # # #     print(newList[l])
# # # #
# # # #
# # # # # 1 Print elements one by one present in a list
# # # # # a = [1,2,3,4,5]
# # # # # for i in range(0, len(a), 1):
# # # # #     print(a[i])
# # # #
# # # # # a = int(input("Enter a number"))
# # # # # b = int(input("Enter a range"))
# # # # # for i in range(1, b+1, 1) :
# # # # #     print(i,"*",a,"=",i*a)
# # # #
# # # # # a = int(input("Enter value"))
# # # # # b = int(input("Enter range"))
# # # # # for mul in range(1, b+1, 1) :
# # # # #     print(mul,"*",a,"=",mul*a)
# # # # # a = int(input("Enter Starting Range"))
# # # # # b = int(input("Enter Ending Range"))
# # # # # for i in range(a,b,1) :
# # # # #     print(i)
# # # #
# # # # #Break & Continue
# # # # # a = ["dragonfrt","Kiwi","banana","apple","jackfrt"]
# # # # # for x in a :
# # # # # #     if x == "Kiwi":
# # # # # #         break
# # # # # #     print(x)
# # # # # def linearSearch(b) :
# # # # #     a = ["dragonfrt", "Kiwi", "banana", "apple", "jackfrt"]
# # # # #
# # # # #
# # # # # b = "Kiwi"
# # # # # ans = linearSearch(b)
# # # # # print(b,"with its index number is",ans)
# # # #
# # # #
# # # # a = 10
# # # # b = []
# # # # c = []
# # # # for i in range(0, a, 1) :
# # # #     num = input("enter fruit names")
# # # #     b.append(num)
# # # # print(b)
# # # # for i in range(2, 8, 1) :
# # # #     print(b[i])
# # # #     c.append(b[i])
# # # # print(c)
# # # # d = input("enter elment tobe searchrd")
# # # #
# # # # for i in range(0, len(c), 1):
# # # #     if d == c[i] :
# # # #         print(i)
# # # # else:
# # # #     print(i)
# # # #
# # # # x = input("enter name")
# # # # for i in range(0, len(x),1) :
# # # #     if i != 0 :
# # # #         if i % 2 == 0 :
# # # #             print(x[i])
# # #
# # # # n = int(input("enter the upto number"))
# # # # x = input("enter the string")
# # # # print(x[2:4])
# # # # rang = int(input("Enter the range"))
# # # # y = []
# # # # for i in range(0,rang,1) :
# # # #     n = int(input("Enter the number"))
# # # #     y.append(n)
# # # # print(y)
# # # # # val = [l,b,c,d,e,f,g,h,t,a]y
# # # # # g = len(val) - 1
# # # # if y[0] == y[len(y)-1] :
# # # #     print("True")
# # # # else :
# # # #     print("False")
# # #
# # # # Madam Maden is an art. She is from England
# # # # x = input("enter a sentence")
# # # # y = input("enter a substring")
# # # # z = x.split(" ")
# # # # print(z)
# # # # count = 0
# # # # for i in range(0,len(z),1) :
# # # #     if z[i] == y :
# # # #         count = count + 1
# # # # print(count)
# # # # i = 1
# # # # x = 13
# # # # while i <= 13 :
# # # #     if i != 13 :
# # # #         print("Enable")
# # # #         i = i + 1
# # # #     else :
# # # #         print("Disable")
# # # #         i = i + 1
# # # # x = input("enter the string")
# # # # for i in range(len(x)-1, -1, -1) :
# # # #     print(x[i], end=" ")
# # # j = 0
# # # k = 0
# # # num1 = [1,2,3,4,5,6,7,8,9,10]
# # # for i in num1 :
# # #     # print(i)
# # #     # # break
# # #     # continue
# # #     # if 4 == i :
# # #     #     # print(i)
# # #     #     continue
# # #     # print(i)
# # #     j = j + 1
# # #     # continue
# # #     continue
# # #     k = k + 1
# # #     print(i)
# # # print(j)
# # # print(k)
# # # a = [] #[1,2,3,4]
# # # b = [] #[10,20,30,40]
# # # c = [] #[40,30,20,10]
# # # [[],[],[]]
# # # emp = []
# # # user = int(input("Enter Range"))
# # # for i in range(0,user,1) :
# # #     emp.append([])
# # # print(emp)
# # # for i in range(0,len(emp),1) :
# # #     for j in range(0,4,1) :
# # #         a = int(input("enter value"))
# # #         emp[i].append(a)
# # #     # a = int(input())
# # #     # emp[i].append(a)
# # #     # b = int(input())
# # #     # emp[i].append(b)
# # #     # c = int(input())
# # #     # emp[i].append(c)
# # #     # d = int(input())
# # #     # emp[i].append(d)
# # # print(emp)
# # # s = ["1,2,3,4","10,20,30,40"]
# # # emp = []
# # # for i in range(0, len(s), 1 ) :
# # #     d = s[i].split(",")
# # #     emp.append(d)
# # # print(emp)
# # # emp1 = [[],[]]
# # # for i in range(0,len(emp),1) :
# # #     f = emp[i]
# # #     for j in range(0,len(f),1) :
# # #         emp1[i].append(int(f[j]))
# # # print(emp1)
# # # print([emp1[0][3],emp1[1][3]])
# #
# # sam = [40,20,30,10]
# # sam.sort()
# # print(sam)
# # # val = sam[::-1]
# # # print(sam[len(sam)-1])
# # # print(sam)
# # # print(val)
# # emm = []
# # # n = "Naveen"
# # # print(n[::-1])
# # for i in range(len(sam)-1, -1, -1) :
# #     emm.append(sam[i])
# # print(emm)
# a = 1234
# print(type(a))
# b = str(a)
# print(b)
# print(type(b))

#
# a = 121
# rev = 0
# temp = a
# while a > 0 :
#     r = a % 10
#     rev = (rev * 10) + r#121
#     a = a // 10#1
# if temp == rev :
#     print("Palindrom")
# else :
#     print("Not Palindrome")
def loginFunc(list1, password) :
    print("Login")
    name = input("Enter the user name").upper()
    count1 = 0
    count2 = 0
    namesave = 0
    for i in range(0, len(list1), 1):
        if list1[i].upper() == name:
            count1 = count1 + 1
            namesave = i
    if count1 == 0:
        print("entered user name is wrong")
    else:
        passwordEnter = input("Enter password")
        if password[namesave] == passwordEnter:
            count2 = count2 + 1
        if count2 == 0:
            print("Entered Password is wrong")
        else:
            print("Login SuccessFully")

def userNameCheck(a,list1) :
    for name in list1 :
        while name.upper() == a :
            return 0



list1 = ["Naveen", "Sandy"]
password = ["1234", "5678"]
user = int(input("enter 0 to create new account or 1 to existing account"))
if user == 0 :
    a = input("Enter name").upper()
    # print(userNameCheck(a,list1))
    amm = userNameCheck(a,list1)
    while amm == 0 :
        print("User Name Already Exist")
        a = input("Enter name").upper()
        amm = userNameCheck(a,list1)

    list1.append(a)
    b = input("Enter password")
    c = input("Reenter password")
    # list1.append(a)

    while b != c:
        print("entered Password does not conform password")
        b = input("Enter password")
        c = input("Reenter password")
    password.append(b)
        # print("entered Password does not conform password")
        # b = input("Enter password")
        # c = input("Reenter password")
        # if b == c :
        #     password.append(b)
        # else :
        #     # print("Please try again after some time")
        #     sys.exit("Please try again after some time")
    loginFunc(list1,password)
else :
    loginFunc(list1,password)

    # Unwanted code
    count = 1
    imp = 0
    while count != 0:
        while a == list1[count - 1].upper():
            # imp = imp + 1
            print("User Name Already Exist")
            a = input("Enter name").upper()
            count = count + imp
        else:
            imp = imp + 1
            count = count - imp

    # for name in list1 :
    #     while name.upper() == a :
    #         list1.append(a)
    #         break

    # userNameCheck(a,list1)
    # for a in list1 :
    #     # while name.upper() == a:
    #     #     # print(name)
    #     print("User Name Already Exist")
    #     a = input("Enter name").upper()
    # # for name in list1 :
    # #     while name.upper() == a:
    #         # print(name)
    #         # print("User Name Already Exist")
    #         # a = input("Enter name").upper()
    # else :
    #     list1.append(a)

    # for name in list1 :
    #     if name.upper() == a :
    #         while name.upper() == a :
    #             print("User Name Already Exist")
    #             a = input("Enter name")
    #     list1.append(a)
    #     break