
itemsAtShop = int(input("No. Of Items Available In The Shop : "))
codePriceTax = []
if itemsAtShop > 0 :
    for i in range(0, itemsAtShop, 1) :
        itemCode = int(input("Enter the Code"))
        itemPrice = int(input("Enter the Price"))
        itemTax = int(input("Enter the Tax"))
        codePriceTax.append([itemCode,itemPrice,itemTax])
else :
    print("Items at the shop is 0")

print(codePriceTax)

premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()
customerPurchase = []
purchasedByCustomer = int(input("No. of items purchased by customer : "))
if premium == "Y" :
    if purchasedByCustomer <= itemsAtShop :
        for i in range(0, purchasedByCustomer, 1):
            itemCode = int(input("Enter the Code"))
            itemCount = int(input("Enter the Count"))
            for i in range(0, itemsAtShop, 1):
                if itemCode == codePriceTax[i][0]:
                    customerPurchase.append([itemCode, itemCount])
            if customerPurchase == []:
                print("Items not available at the shop")
            else:
                print(customerPurchase)
    else :
        print("The items are greater than present in the shop")

elif premium == "N" :
    if purchasedByCustomer <= itemsAtShop:
        for i in range(0, purchasedByCustomer, 1):
            itemCode = int(input("Enter the Code"))
            itemCount = int(input("Enter the Count"))
            for i in range(0, itemsAtShop, 1):
                if itemCode == codePriceTax[i][0]:
                    customerPurchase.append([itemCode, itemCount])
            if customerPurchase == []:
                print("Items not available at the shop")
            else:
                print(customerPurchase)
    else:
        print("The items are greater than present in the shop")
else :
    print("Entered Charecter Does not exist")

possibleNotesDeno = int(input("Enter possible denominations : "))
possibleNotesDenoArray = []
for i in range(0, possibleNotesDeno, 1) :
    rupees = int(input("Enter the rupee : "))
    rupeeCount = int(input("Enter the rupee count : "))
    possibleNotesDenoArray.append([rupees, rupeeCount])
print(possibleNotesDenoArray)

cashPaidByCus = int(input("Cash paid by Customer : "))

print("==START_BILLING==")
billingArray = []
if purchasedByCustomer == 1 :
    for i in range(0, purchasedByCustomer, 1):
        for j in range(0, purchasedByCustomer + 1, 1):
            if customerPurchase[i][0] == codePriceTax[j][0]:
                logic = codePriceTax[j][1] * customerPurchase[i][1]
                logicTax = logic / 100
                logicTax = logicTax * codePriceTax[j][2]
                total = logic + logicTax
                billingArray.append([customerPurchase[i][0], codePriceTax[j][1], customerPurchase[i][1],
                                     codePriceTax[j][1] * customerPurchase[i][1], codePriceTax[j][2], logicTax, total])
else :
    for i in range(0, purchasedByCustomer, 1):
        for j in range(0, purchasedByCustomer, 1):
            if customerPurchase[i][0] == codePriceTax[j][0]:
                logic = codePriceTax[j][1] * customerPurchase[i][1]
                logicTax = logic / 100
                logicTax = logicTax * codePriceTax[j][2]
                total = logic + logicTax
                billingArray.append([customerPurchase[i][0], codePriceTax[j][1], customerPurchase[i][1],
                                     codePriceTax[j][1] * customerPurchase[i][1], codePriceTax[j][2], logicTax, total])

for i in range(0, len(billingArray), 1) :
    print(billingArray[i])
totalWithoutTax = 0
taxAlone = 0
totalWithTax = 0
for i in range(0, len(billingArray), 1) :
    totalWithoutTax = totalWithoutTax + billingArray[i][3]
    taxAlone = taxAlone + billingArray[i][5]
    totalWithTax = totalWithoutTax + taxAlone
discount = 0
if premium == "Y" :
    discount = totalWithTax - (totalWithTax / 10)
elif premium == "N":
    discount = totalWithTax
else :
    print("Invalid character")
print(totalWithoutTax)
print(taxAlone)
print(totalWithTax)
print(discount)
print(round(discount))

print(cashPaidByCus - round(discount))
