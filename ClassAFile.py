# from public import public as Public
class ProductInShop:
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

    itemsAtShop = int(input("No. Of Items Available In The Shop : "))

    ans1 = itemsAtShopFunc(itemsAtShop)

class CustomerPurchase :
    def customerPurchase(purchasedByCustomer, ans1, itemsAtShop):
        customerPurchase = []
        customerPurchase = []
        if purchasedByCustomer == 1:
            itemCode = int(input("Enter the Code"))
            itemCount = int(input("Enter the Count"))
            customerPurchase.append([itemCode, itemCount])
        elif purchasedByCustomer <= itemsAtShop:
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


    ans2 = []
    premium = input("Enter the Customer is premium or not (Y - Premium or N - NonPremium) : ").upper()
    # purchasedByCustomerUpdated = 0
    if premium == "Y" or premium == "N":
        purchasedByCustomer = int(input("No. of items purchased by customer : "))
        # purchasedByCustomerUpdated = purchasedByCustomer
        ans2 = customerPurchase(purchasedByCustomer, ProductInShop.ans1, ProductInShop.itemsAtShop)
    else:
        val = "Entered Charecter Does not exist"
        ans2 = val


class Denominations :
    def denomination(possibleNotesDeno):
        possibleNotesDenoArray = []
        for i in range(0, possibleNotesDeno, 1):
            rupees = int(input("Enter the rupee : "))
            rupeeCount = int(input("Enter the rupee count : "))
            possibleNotesDenoArray.append([rupees, rupeeCount])
        return possibleNotesDenoArray

    def denominationOutput(cashPaidByCus, ans5, ans6):
        arrat = []
        remainingMoney = Denominations.cashPaidByCus - round(ans5)
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

    possibleNotesDeno = int(input("Enter possible denominations : "))
    ans6 = denomination(possibleNotesDeno)
    cashPaidByCus = int(input("Cash paid by Customer : "))


class Billing :
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

    name = CustomerPurchase.purchasedByCustomer
    ans3 = []
    if CustomerPurchase.purchasedByCustomer == 1:
        name = name + 1
        ans3 = purchasedByCus(CustomerPurchase.purchasedByCustomer, name, ProductInShop.ans1, CustomerPurchase.ans2)
    else:
        ans3 = purchasedByCus(CustomerPurchase.purchasedByCustomer, name, ProductInShop.ans1, CustomerPurchase.ans2)

    # ans3 = billingArray(purchasedByCustomer, ans1, ans2)
class TaxAndPremium :
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

    ans4 = tax(Billing.ans3)
    ans5 = premiumTax(CustomerPurchase.premium, ans4, CustomerPurchase.purchasedByCustomer)


class Output:
    val1 = ProductInShop.ans1
    val2 = CustomerPurchase.ans2
    print(val1)
    print(val2)
    for i in range(0, CustomerPurchase.purchasedByCustomer, 1):
        ans3 = Billing.ans3
        print(ans3[i][0], "|", ans3[i][1], "|", ans3[i][2], "|", ans3[i][3], "|", ans3[i][4], "|", ans3[i][5],
              ans3[i][6])
    change1 = CustomerPurchase.purchasedByCustomer
    change2 = TaxAndPremium.ans4
    print(change2[change1 - 1][0])
    print(change2[change1 - 1][1])
    print(change2[change1 - 1][2])
    print(TaxAndPremium.ans5)

    print(round(TaxAndPremium.ans5))
    print(Denominations.cashPaidByCus - round(TaxAndPremium.ans5))
    ans7 = Denominations.denominationOutput(Denominations.cashPaidByCus, TaxAndPremium.ans5, Denominations.ans6)