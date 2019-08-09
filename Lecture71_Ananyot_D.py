menuList = []
priceList = []

def showBill():
    total = 0
    print("--- Food ---")
    for food in range(len(menuList)):
        print(menuList[food],":",priceList[food])
    for price in range(len(priceList)):
        total += priceList[price]
    print("Total Price :",total,"THB")

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()