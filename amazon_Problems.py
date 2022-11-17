# def anss(ans,arr) :
#     ran = len(arr)
#     while ran > 0:
#         ans = ans + arr[ran - 1]
#         ran = ran - 1
#     return ans, arr[0]
#
# sum = 12
# arr = [1,2,3,7,5]
# ans = 0
# count = 0
# # nav = 0
# # fis = 0
# # while nav < sum:
# #     nav = nav + arr[fis]
# #     fis = fis + 1
# # # print(nav)
# name = anss(ans,arr)
# # # print(name)
# # if nav == sum :
# #     # print(nav)
# #     print(1, fis + 1)
# while name[0] != sum:
#     count = count + 1
#     arr.pop(0)
#     # print(arr)
#     name = anss(ans, arr)
# print(name[0])
#
#
#
# if name[0] == sum:
#     print(arr.index(name[1]) + 2, count + 1)
# #
#
#
# # print(ran)
# # print(ans)
# # print(arr)
# # name = anss(ans,arr)
# # while name[0] != sum :
# #     # name[1].pop(0)
# #     name = anss(ans,name[1])
# #
# # print(ans)
# # print(arr)




def anss(ans,arr) :
    ran = 0
    while ans < sum:
        ans = ans + arr[ran]
        ran = ran + 1
    # print(ans)
    return ans, arr[0], ran

sum = int(input("Enter the sum"))
arr = []
arrRange = int(input("enter the range of the array"))
for i in range(0, arrRange) :
    getIn = int(input("Enter elements in an array"))
    arr.append(getIn)
# arr = [1,2,3,7,5,6,7,8,9,10]
cop = arr.copy()
ans = 0
count = 0
nav = 0
fis = 0
while nav < sum:
    nav = nav + arr[fis]
    fis = fis + 1

name = anss(ans,arr)

if nav == sum :
    print(1, fis)
else :
    while name[0] != sum:
        count = count + 1
        arr.pop(0)
        name = anss(ans, arr)
    print(name[0])

    if name[0] == sum:
        value = cop.index(name[1])
        print(value + 1, value + name[2])
        # if count > len(cop) :
        #     print(cop.index(name[1]) + 1, count + 2)
        # else :
        #     print(cop.index(name[1]) + 1, count + 1)