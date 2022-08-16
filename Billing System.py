#© 2022 NaveenKumar MuraliTharan. All Rights Reserved.
#Structured And Functional Code
def itemsAtShopFunc(itemsAtShop) :
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
def customerPurchase(purchasedByCustomer, ans1, itemsAtShop) :
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


def denomination(possibleNotesDeno) :
    possibleNotesDenoArray = []
    for i in range(0, possibleNotesDeno, 1):
        rupees = int(input("Enter the rupee : "))
        rupeeCount = int(input("Enter the rupee count : "))
        possibleNotesDenoArray.append([rupees, rupeeCount])
    return possibleNotesDenoArray
def purchasedByCus(purchasedByCustomer, name, ans1, ans2) :
    billingArray = []
    customerPurchase = ans2
    for i in range(0, purchasedByCustomer, 1):
        for j in range(0, name , 1):
            if customerPurchase[i][0] == ans1[j][0]:
                logic = ans1[j][1] * customerPurchase[i][1]
                logicTax = logic / 100
                logicTax = logicTax * ans1[j][2]
                total = logic + logicTax
                billingArray.append([customerPurchase[i][0], ans1[j][1], customerPurchase[i][1],
                                     ans1[j][1] * customerPurchase[i][1], ans1[j][2], logicTax,
                                     total])


    return billingArray


def tax(ans3) :
    taxArray = []
    totalWithoutTax = 0
    taxAlone = 0

    for i in range(0, len(ans3), 1):
        totalWithoutTax = totalWithoutTax + ans3[i][3]
        taxAlone = taxAlone + ans3[i][5]
        totalWithTax = totalWithoutTax + taxAlone
        taxArray.append([totalWithoutTax,taxAlone,totalWithTax])
    return taxArray
def premiumTax(premium, ans4, purchasedByCustomer) :

    if premium == "Y":
        discount = ans4[purchasedByCustomer - 1][2] - (ans4[purchasedByCustomer - 1][2] / 10)
        return discount
    elif premium == "N":
        discount = ans4[purchasedByCustomer - 1][2]
        return discount
    else:
        discount = "Invalid character"
        return discount

def denominationOutput(cashPaidByCus, ans5, ans6) :

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

itemsAtShop = int(input("No. Of Items Available In The Shop : "))

ans1 = itemsAtShopFunc(itemsAtShop)
print(ans1)

premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()

purchasedByCustomer = int(input("No. of items purchased by customer : "))
ans2 = []
if premium == "Y" or premium == "N" :
    ans2 = customerPurchase(purchasedByCustomer, ans1, itemsAtShop)
    print(ans2)
else :
    print("Entered Charecter Does not exist")


possibleNotesDeno = int(input("Enter possible denominations : "))

ans6 = denomination(possibleNotesDeno)

cashPaidByCus = int(input("Cash paid by Customer : "))

print("==START_BILLING==")
name = purchasedByCustomer
ans3 = []
if purchasedByCustomer == 1 :
    name = name + 1
    ans3 = purchasedByCus(purchasedByCustomer, name, ans1, ans2)
else :
    ans3 = purchasedByCus(purchasedByCustomer, name, ans1, ans2)

# ans3 = billingArray(purchasedByCustomer, ans1, ans2)

for i in range(0, purchasedByCustomer, 1) :
    print(ans3[i][0],"|",ans3[i][1],"|",ans3[i][2],"|",ans3[i][3],"|",ans3[i][4],"|",ans3[i][5], ans3[i][6])

ans4 = tax(ans3)

print(ans4[purchasedByCustomer - 1][0])
print(ans4[purchasedByCustomer - 1][1])
print(ans4[purchasedByCustomer - 1][2])
ans5 = premiumTax(premium, ans4, purchasedByCustomer)
print(ans5)

print(round(ans5))
print(cashPaidByCus - round(ans5))
remainingMoney = 0

denominationOutput(cashPaidByCus, ans5, ans6)
#---------------------------Raw And Unstructured Code
# itemsAtShop = int(input("No. Of Items Available In The Shop : "))
# codePriceTax = []
# if itemsAtShop > 0 :
#     for i in range(0, itemsAtShop, 1) :
#         itemCode = int(input("Enter the Code"))
#         itemPrice = int(input("Enter the Price"))
#         itemTax = int(input("Enter the Tax"))
#         codePriceTax.append([itemCode,itemPrice,itemTax])
# else :
#     print("Items at the shop is 0")
#
# print(codePriceTax)
#
# premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()
# customerPurchase = []
# purchasedByCustomer = int(input("No. of items purchased by customer : "))
# if premium == "Y" :
#     if purchasedByCustomer <= itemsAtShop :
#         for i in range(0, purchasedByCustomer, 1):
#             itemCode = int(input("Enter the Code"))
#             itemCount = int(input("Enter the Count"))
#             for j in range(0, itemsAtShop, 1):
#                 if itemCode == codePriceTax[i][0]:
#                     customerPurchase.append([itemCode, itemCount])
#                     break
#     else :
#         print("The items are greater than present in the shop")
#     if customerPurchase == []:
#         print("Items not available at the shop")
#     else:
#         print(customerPurchase)
#
# elif premium == "N" :
#     if purchasedByCustomer <= itemsAtShop:
#         for i in range(0, purchasedByCustomer, 1):
#             itemCode = int(input("Enter the Code"))
#             itemCount = int(input("Enter the Count"))
#             for j in range(0, itemsAtShop, 1):
#                 if itemCode == codePriceTax[i][0]:
#                     customerPurchase.append([itemCode, itemCount])
#             if customerPurchase == []:
#                 print("Items not available at the shop")
#             else:
#                 print(customerPurchase)
#     else:
#         print("The items are greater than present in the shop")
# else :
#     print("Entered Charecter Does not exist")
#
# possibleNotesDeno = int(input("Enter possible denominations : "))
# possibleNotesDenoArray = []
# for i in range(0, possibleNotesDeno, 1) :
#     rupees = int(input("Enter the rupee : "))
#     rupeeCount = int(input("Enter the rupee count : "))
#     possibleNotesDenoArray.append([rupees, rupeeCount])
# print(possibleNotesDenoArray)
#
# cashPaidByCus = int(input("Cash paid by Customer : "))
#
# print("==START_BILLING==")
# billingArray = []
# if purchasedByCustomer == 1 :
#     for i in range(0, purchasedByCustomer, 1):
#         for j in range(0, purchasedByCustomer + 1, 1):
#             if customerPurchase[i][0] == codePriceTax[j][0]:
#                 logic = codePriceTax[j][1] * customerPurchase[i][1]
#                 logicTax = logic / 100
#                 logicTax = logicTax * codePriceTax[j][2]
#                 total = logic + logicTax
#                 billingArray.append([customerPurchase[i][0], codePriceTax[j][1], customerPurchase[i][1],
#                                      codePriceTax[j][1] * customerPurchase[i][1], codePriceTax[j][2], logicTax, total])
# else :
#     for i in range(0, purchasedByCustomer, 1):
#         for j in range(0, purchasedByCustomer, 1):
#             if customerPurchase[i][0] == codePriceTax[j][0]:
#                 logic = codePriceTax[j][1] * customerPurchase[i][1]
#                 logicTax = logic / 100
#                 logicTax = logicTax * codePriceTax[j][2]
#                 total = logic + logicTax
#                 billingArray.append([customerPurchase[i][0], codePriceTax[j][1], customerPurchase[i][1],
#                                      codePriceTax[j][1] * customerPurchase[i][1], codePriceTax[j][2], logicTax, total])
#
# for i in range(0, len(billingArray), 1) :
#     print(billingArray[i])
# totalWithoutTax = 0
# taxAlone = 0
# totalWithTax = 0
# for i in range(0, len(billingArray), 1) :
#     totalWithoutTax = totalWithoutTax + billingArray[i][3]
#     taxAlone = taxAlone + billingArray[i][5]
#     totalWithTax = totalWithoutTax + taxAlone
# discount = 0
# if premium == "Y" :
#     discount = totalWithTax - (totalWithTax / 10)
# elif premium == "N":
#     discount = totalWithTax
# else :
#     print("Invalid character")
# print(totalWithoutTax)
# print(taxAlone)
# print(totalWithTax)
# print(discount)
# print(round(discount))
#
# print(cashPaidByCus - round(discount))
# remainingMoney = 0
#
# arrat = []
# remainingMoney = cashPaidByCus - round(discount)
# if remainingMoney != 0 :
#     for i in range(0, len(possibleNotesDenoArray), 1):
#         cou = possibleNotesDenoArray[i][1]
#         route = 0
#         while cou > 0:
#             remainingMoney = remainingMoney - possibleNotesDenoArray[i][0]
#             if remainingMoney < 0:
#                 remainingMoney = remainingMoney + possibleNotesDenoArray[i][0]
#                 break
#             else:
#                 route = route + 1
#                 cou = cou - 1
#         if route > 0 :
#             arrat.append([possibleNotesDenoArray[i][0], route])
#     for i in range(0, len(arrat), 1):
#         print(arrat[i][0],"|",arrat[i][1])
#     print("==End_Bill==")
# else :
#     print("==End_Bill==")
#---------------------Billing Array Full-----------------------------
    #
    #
    # def itemsAtShopFunc(itemsAtShop):
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
    #
    #
    # def customerPurchase(purchasedByCustomer, ans1, itemsAtShop):
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
    #
    # def denomination(possibleNotesDeno):
    #     possibleNotesDenoArray = []
    #     for i in range(0, possibleNotesDeno, 1):
    #         rupees = int(input("Enter the rupee : "))
    #         rupeeCount = int(input("Enter the rupee count : "))
    #         possibleNotesDenoArray.append([rupees, rupeeCount])
    #     return possibleNotesDenoArray
    #
    #
    # def billingArray(purchasedByCustomer, ans1, ans2):
    #     billingArray = []
    #     customerPurchase = ans2
    #     if purchasedByCustomer == 1:
    #         for i in range(0, purchasedByCustomer, 1):
    #             for j in range(0, purchasedByCustomer + 1, 1):
    #                 if customerPurchase[i][0] == ans1[j][0]:
    #                     logic = ans1[j][1] * customerPurchase[i][1]
    #                     logicTax = logic / 100
    #                     logicTax = logicTax * ans1[j][2]
    #                     total = logic + logicTax
    #                     billingArray.append([customerPurchase[i][0], ans1[j][1], customerPurchase[i][1],
    #                                          ans1[j][1] * customerPurchase[i][1], ans1[j][2], logicTax,
    #                                          total])
    #         return billingArray
    #     else:
    #         for i in range(0, purchasedByCustomer, 1):
    #             for j in range(0, purchasedByCustomer, 1):
    #                 if customerPurchase[i][0] == ans1[j][0]:
    #                     logic = ans1[j][1] * customerPurchase[i][1]
    #                     logicTax = logic / 100
    #                     logicTax = logicTax * ans1[j][2]
    #                     total = logic + logicTax
    #                     billingArray.append([customerPurchase[i][0], ans1[j][1], customerPurchase[i][1],
    #                                          ans1[j][1] * customerPurchase[i][1], ans1[j][2], logicTax,
    #                                          total])
    #         return billingArray
    #
    #
    # def tax(ans3):
    #     taxArray = []
    #     totalWithoutTax = 0
    #     taxAlone = 0
    #
    #     for i in range(0, len(ans3), 1):
    #         totalWithoutTax = totalWithoutTax + ans3[i][3]
    #         taxAlone = taxAlone + ans3[i][5]
    #         totalWithTax = totalWithoutTax + taxAlone
    #         taxArray.append([totalWithoutTax, taxAlone, totalWithTax])
    #     return taxArray
    #
    #
    # def premiumTax(premium, ans4, purchasedByCustomer):
    #
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
    #
    # def denominationOutput(cashPaidByCus, ans5, ans6):
    #
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
    #
    # itemsAtShop = int(input("No. Of Items Available In The Shop : "))
    #
    # ans1 = itemsAtShopFunc(itemsAtShop)
    # print(ans1)
    #
    # premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()
    #
    # purchasedByCustomer = int(input("No. of items purchased by customer : "))
    # ans2 = []
    # if premium == "Y" or premium == "N":
    #     ans2 = customerPurchase(purchasedByCustomer, ans1, itemsAtShop)
    #     print(ans2)
    # else:
    #     print("Entered Charecter Does not exist")
    #
    # possibleNotesDeno = int(input("Enter possible denominations : "))
    #
    # ans6 = denomination(possibleNotesDeno)
    #
    # cashPaidByCus = int(input("Cash paid by Customer : "))
    #
    # print("==START_BILLING==")
    # ans3 = billingArray(purchasedByCustomer, ans1, ans2)
    #
    # for i in range(0, purchasedByCustomer, 1):
    #     print(ans3[i][0], "|", ans3[i][1], "|", ans3[i][2], "|", ans3[i][3], "|", ans3[i][4], "|", ans3[i][5])
    #
    # ans4 = tax(ans3)
    #
    # print(ans4[purchasedByCustomer - 1][0])
    # print(ans4[purchasedByCustomer - 1][1])
    # print(ans4[purchasedByCustomer - 1][2])
    # ans5 = premiumTax(premium, ans4, purchasedByCustomer)
    # print(ans5)
    #
    # print(round(ans5))
    # print(cashPaidByCus - round(ans5))
    # remainingMoney = 0
    #
    # denominationOutput(cashPaidByCus, ans5, ans6)