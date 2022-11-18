def anss(arr) :
    ran = 0
    ans = 0
    # print(len(arr))
    print(arr)
    while ans < sum:
        ans = ans + arr[ran]
        ran = ran + 1
        # if ans > sum :
        #     print("Break")
    return ans, arr[0], ran

sum = int(input("Enter the sum"))
# arr = []
# arrRange = int(input("enter the range of the array"))
# for i in range(0, arrRange) :
#     getIn = int(input("Enter elements in an array"))
#     arr.append(getIn)
arr = [1,2,3,7,5,6,7,8,9,10]
cop = arr.copy()

nav = 0
fis = 0
checkValue = 0
for i in arr :
    checkValue = checkValue + i
print(checkValue)
if sum <= checkValue :
    while nav < sum:
        nav = nav + arr[fis]
        fis = fis + 1

    name = anss(arr)

    if nav == sum:
        print(1, fis)
    else:
        count = 0
        while name[0] != sum:
            count = count + 1
            arr.pop(0)
            name = anss(arr)
        print(name[0])

        if name[0] == sum:
            value = cop.index(name[1])
            print(value + 1, value + name[2])
        else:
            print("The sum is not present in the range of numbers given")
            # if count > len(cop) :
            #     print(cop.index(name[1]) + 1, count + 2)
            # else :
            #     print(cop.index(name[1]) + 1, count + 1)
else:
    print("The sum is not present in the range of numbers given")
