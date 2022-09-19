# def monday():
#     return "monday"
# def tuesday():
#     return "tuesday"
# def wednesday():
#     return "wednesday"
# def thursday():
#     return "thursday"
# def friday():
#     return "friday"
# def saturday():
#     return "saturday"
# def sunday():
#     return "sunday"
# def default():
#     return "Invalid day"
# switcher = {
#     1: monday,
#     2: tuesday,
#     3: wednesday,
#     4: thursday,
#     5: friday,
#     6: saturday,
#     7: sunday
# }
# def switch(dayOfWeek):
#     return switcher.get(dayOfWeek, default)()
# print(switch(1))
# print(switch(0))


# def vowel(num):
#     switch={
#       1:'a',
#       2:'e',
#       3:'i',
#       4:'o',
#       5:'u'
#       }
#     return switch.get(num,"Invalid input")
# a = int(input("Enter a value: "))
# print(vowel(a))
# print(vowel(3))
# print(vowel(0))
#
# #
# def add(n,m):
#     return n+m
#
# def subs(n,m):
#     return n-m
#
# def prod(n,m):
#     return n*m
#
# def div(n,m):
#     return m/n
#
# def rem(n,m):
#     return m%n
#
# def operations(op,n,m):
#     switch={
#        '+': add(n,m),
#        '-': subs(n,m),
#        '*': prod(n,m),
#        '/': div(n,m),
#        '%': rem(n,m),
#        }
#     return switch.get(op,'Choose one of the following operator:+,-,*,/,%')
# a = input("enter the string")
# b = int(input("Enter the number"))
# c = int(input("Enter the number"))
# print(operations(a,b,c))
#
# # operations('^')
#
#
# def common(res) :
#     if res < 0:
#         d = res * (-1)
#         return d
#     else :
#         return res
# def calc(a,b,c) :
#     if c == '+':
#         res = int(a) + int(b)
#         return common(res)
#     elif c == '-':
#         res = int(a) - int(b)
#         return common(res)
#     elif c == '*':
#         res = int(a) * int(b)
#         return common(res)
#     elif c == '/':
#         res = int(a) / int(b)
#         return common(res)
#     elif c == '%':
#         res = int(a) % int(b)
#         return common(res)
#     else:
#         return "Invalid Symbol"
#
#
# a = input("Enter the value")
# b = input("Enter the value")
# c = input("Enter the math function")
# ans = calc(a, b, c)
# # print(ans)
# arr = [1,2,3,4,5]#changbel and only Same datatype and repeatable
# list1 = ["NAveen", 1, 1.0]#changbel and only diff datatype and repeatable
# tuple = ("NAveen", 1, 1.0)#unChangable and only diff datatype
# set = {"NAveen", 1, 1.0}#unChangable and only diff datatype and unrepeatable

# list1 = ["Naveen",2,3,"Sabari",5]
#
# for name in range(0, len(list1), 1) :
#     print(list1[name])
# num1 = int(input("enter"))#2
# num2 = int(input("enter"))#10
#
# for i in range(1,num2+1,1):
#     print(i,"*",num1,"=",i*num1)
list1 = []
len1 = int(input("enter length"))
for i in range(0,len1,1):
    a = int(input("Enter Number"))
    list1.append(a)
odd = []
even = []
for i in range(0,len(list1),1) :
    if list1[i] % 2 == 0:
        even.append(list1[i])
    else:
        odd.append(list1[i])
print(odd)
print(even)


ans1 = sorted(odd)
ans2 = []
for i in range(len(ans1)-1,-1,-1) :
    ans2.append(ans1[i])
print(ans2)

