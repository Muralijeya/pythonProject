class Input:

    itemsAtShop = int(input("No. Of Items Available In The Shop : "))
    premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()
    purchasedByCustomer = int(input("No. of items purchased by customer : "))
    possibleNotesDeno = int(input("Enter possible denominations : "))
    cashPaidByCus = int(input("Cash paid by Customer : "))

class AllFunctions:

    def itemsAtShopFunc(itemsAtShop):
        codePriceTax = []
        if itemsAtShop > 0:
            for i in range(0, itemsAtShop, 1):
                itemCode = int(input("Enter the Code"))
                itemPrice = int(input("Enter the Price"))
                itemTax = int(input("Enter the Tax"))
                codePriceTax.append([itemCode, itemPrice, itemTax])
            return codePriceTax
        else:
            codePriceTax = "Items at the shop is 0"
            return codePriceTax

    #
    def customerPurchase(purchasedByCustomer, ans1, itemsAtShop):
        customerPurchase = []
        if purchasedByCustomer <= itemsAtShop:
            for i in range(0, purchasedByCustomer, 1):
                itemCode = int(input("Enter the Code"))
                itemCount = int(input("Enter the Count"))
                for j in range(0, itemsAtShop, 1):
                    if itemCode == ans1[i][0]:
                        customerPurchase.append([itemCode, itemCount])
                        break
        else:
            val = "The items are greater than present in the shop"
            return val
        if customerPurchase == []:
            return "Items not available at the shop"
        else:
            return customerPurchase

    def denomination(possibleNotesDeno):
        possibleNotesDenoArray = []
        for i in range(0, possibleNotesDeno, 1):
            rupees = int(input("Enter the rupee : "))
            rupeeCount = int(input("Enter the rupee count : "))
            possibleNotesDenoArray.append([rupees, rupeeCount])
        return possibleNotesDenoArray

    def purchasedByCus(purchasedByCustomer, name, ans1, ans2):
        billingArray = []
        customerPurchase = ans2
        for i in range(0, purchasedByCustomer, 1):
            for j in range(0, name, 1):
                if customerPurchase[i][0] == ans1[j][0]:
                    logic = ans1[j][1] * customerPurchase[i][1]
                    logicTax = logic / 100
                    logicTax = logicTax * ans1[j][2]
                    total = logic + logicTax
                    billingArray.append([customerPurchase[i][0], ans1[j][1], customerPurchase[i][1],
                                         ans1[j][1] * customerPurchase[i][1], ans1[j][2], logicTax,
                                         total])

        return billingArray

    def tax(ans3):
        taxArray = []
        totalWithoutTax = 0
        taxAlone = 0

        for i in range(0, len(ans3), 1):
            totalWithoutTax = totalWithoutTax + ans3[i][3]
            taxAlone = taxAlone + ans3[i][5]
            totalWithTax = totalWithoutTax + taxAlone
            taxArray.append([totalWithoutTax, taxAlone, totalWithTax])
        return taxArray

    def premiumTax(premium, ans4, purchasedByCustomer):

        if premium == "Y":
            discount = ans4[purchasedByCustomer - 1][2] - (ans4[purchasedByCustomer - 1][2] / 10)
            return discount
        elif premium == "N":
            discount = ans4[purchasedByCustomer - 1][2]
            return discount
        else:
            discount = "Invalid character"
            return discount

    def denominationOutput(cashPaidByCus, ans5, ans6):

        arrat = []
        remainingMoney = cashPaidByCus - round(ans5)
        if remainingMoney != 0:
            for i in range(0, len(ans6), 1):
                cou = ans6[i][1]
                route = 0
                while cou > 0:
                    remainingMoney = remainingMoney - ans6[i][0]
                    if remainingMoney < 0:
                        remainingMoney = remainingMoney + ans6[i][0]
                        break
                    else:
                        route = route + 1
                        cou = cou - 1
                if route > 0:
                    arrat.append([ans6[i][0], route])
            for i in range(0, len(arrat), 1):
                print(arrat[i][0], "|", arrat[i][1])
            out = "==End_Bill=="
            return out
        else:
            out = "==End_Bill=="
            return out


class Output :
    ans1 = AllFunctions.itemsAtShopFunc(Input.itemsAtShop)
    ans2 = AllFunctions.customerPurchase(Input.purchasedByCustomer, ans1, Input.itemsAtShop)
    possibleNotesDenoArray = AllFunctions.denomination(Input.possibleNotesDeno)
    print("==START_BILLING==")
    name = Input.purchasedByCustomer
    ans3 = []
    if Input.purchasedByCustomer == 1:
        name = name + 1
        ans3 = AllFunctions.purchasedByCus(Input.purchasedByCustomer, name, ans1, ans2)
    else:
        ans3 = AllFunctions.purchasedByCus(Input.purchasedByCustomer, name, ans1, ans2)
    ans4 = AllFunctions.tax(ans3)
    anss4 = ans4[Input.purchasedByCustomer - 1]
    print(ans1)
    print(ans2)
    print(ans3)
    print(anss4[0])
    print(anss4[1])
    print(anss4[2])
    ans5 = AllFunctions.premiumTax(Input.premium, ans4, Input.purchasedByCustomer)
    print(ans5)

    print(round(ans5))
    print(Input.cashPaidByCus - round(ans5))
    remainingMoney = 0
    ans6 = AllFunctions.denomination(Input.possibleNotesDeno)
    AllFunctions.denominationOutput(Input.cashPaidByCus, ans5, ans6)

# answer = Output
# print(answer)
#
#
#
#
# def itemsAtShopFunc(itemsAtShop) :
#     codePriceTax = []
#     if itemsAtShop > 0:
#         for i in range(0, itemsAtShop, 1):
#             itemCode = int(input("Enter the Code"))
#             itemPrice = int(input("Enter the Price"))
#             itemTax = int(input("Enter the Tax"))
#             codePriceTax.append([itemCode, itemPrice, itemTax])
#         return codePriceTax
#     else:
#         codePriceTax = "Items at the shop is 0"
#         return codePriceTax
#
# def customerPurchase(purchasedByCustomer, ans1, itemsAtShop) :
#     customerPurchase = []
#     if purchasedByCustomer <= itemsAtShop:
#         for i in range(0, purchasedByCustomer, 1):
#             itemCode = int(input("Enter the Code"))
#             itemCount = int(input("Enter the Count"))
#             for j in range(0, itemsAtShop, 1):
#                 if itemCode == ans1[i][0]:
#                     customerPurchase.append([itemCode, itemCount])
#                     break
#     else:
#         val = "The items are greater than present in the shop"
#         return val
#     if customerPurchase == []:
#         return "Items not available at the shop"
#     else:
#         return customerPurchase
#
# def denomination(possibleNotesDeno) :
#     possibleNotesDenoArray = []
#     for i in range(0, possibleNotesDeno, 1):
#         rupees = int(input("Enter the rupee : "))
#         rupeeCount = int(input("Enter the rupee count : "))
#         possibleNotesDenoArray.append([rupees, rupeeCount])
#     return possibleNotesDenoArray
#
# def purchasedByCus(purchasedByCustomer, name, ans1, ans2) :
#     billingArray = []
#     customerPurchase = ans2
#     for i in range(0, purchasedByCustomer, 1):
#         for j in range(0, name , 1):
#             if customerPurchase[i][0] == ans1[j][0]:
#                 logic = ans1[j][1] * customerPurchase[i][1]
#                 logicTax = logic / 100
#                 logicTax = logicTax * ans1[j][2]
#                 total = logic + logicTax
#                 billingArray.append([customerPurchase[i][0], ans1[j][1], customerPurchase[i][1],
#                                      ans1[j][1] * customerPurchase[i][1], ans1[j][2], logicTax,
#                                      total])
#     return billingArray
#
#
# def tax(ans3) :
#     taxArray = []
#     totalWithoutTax = 0
#     taxAlone = 0
#     for i in range(0, len(ans3), 1):
#         totalWithoutTax = totalWithoutTax + ans3[i][3]
#         taxAlone = taxAlone + ans3[i][5]
#         totalWithTax = totalWithoutTax + taxAlone
#         taxArray.append([totalWithoutTax,taxAlone,totalWithTax])
#     return taxArray
#
# def premiumTax(premium, ans4, purchasedByCustomer) :
#     if premium == "Y":
#         discount = ans4[purchasedByCustomer - 1][2] - (ans4[purchasedByCustomer - 1][2] / 10)
#         return discount
#     elif premium == "N":
#         discount = ans4[purchasedByCustomer - 1][2]
#         return discount
#     else:
#         discount = "Invalid character"
#         return discount
#
# def denominationOutput(cashPaidByCus, ans5, ans6) :
#     arrat = []
#     remainingMoney = cashPaidByCus - round(ans5)
#     if remainingMoney != 0:
#         for i in range(0, len(ans6), 1):
#             cou = ans6[i][1]
#             route = 0
#             while cou > 0:
#                 remainingMoney = remainingMoney - ans6[i][0]
#                 if remainingMoney < 0:
#                     remainingMoney = remainingMoney + ans6[i][0]
#                     break
#                 else:
#                     route = route + 1
#                     cou = cou - 1
#             if route > 0:
#                 arrat.append([ans6[i][0], route])
#         for i in range(0, len(arrat), 1):
#             print(arrat[i][0], "|", arrat[i][1])
#         out = "==End_Bill=="
#         return out
#     else:
#         out = "==End_Bill=="
#         return out
#
# itemsAtShop = int(input("No. Of Items Available In The Shop : "))
# ans1 = itemsAtShopFunc(itemsAtShop)
# print(ans1)
# premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()
# purchasedByCustomer = int(input("No. of items purchased by customer : "))
# ans2 = []
# if premium == "Y" or premium == "N" :
#     ans2 = customerPurchase(purchasedByCustomer, ans1, itemsAtShop)
#     print(ans2)
# else :
#     print("Entered Charecter Does not exist")
# possibleNotesDeno = int(input("Enter possible denominations : "))
# ans6 = denomination(possibleNotesDeno)
# cashPaidByCus = int(input("Cash paid by Customer : "))
# print("==START_BILLING==")
# name = purchasedByCustomer
# ans3 = []
# if purchasedByCustomer == 1 :
#     name = name + 1
#     ans3 = purchasedByCus(purchasedByCustomer, name, ans1, ans2)
# else :
#     ans3 = purchasedByCus(purchasedByCustomer, name, ans1, ans2)
# for i in range(0, purchasedByCustomer, 1) :
#     print(ans3[i][0],"|",ans3[i][1],"|",ans3[i][2],"|",ans3[i][3],"|",ans3[i][4],"|",ans3[i][5], ans3[i][6])
# ans4 = tax(ans3)
# print(ans4[purchasedByCustomer - 1][0])
# print(ans4[purchasedByCustomer - 1][1])
# print(ans4[purchasedByCustomer - 1][2])
# ans5 = premiumTax(premium, ans4, purchasedByCustomer)
# print(ans5)
# print(round(ans5))
# print(cashPaidByCus - round(ans5))
# remainingMoney = 0
# denominationOutput(cashPaidByCus, ans5, ans6)