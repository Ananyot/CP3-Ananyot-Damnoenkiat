def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "abc" and password == "123":
        return showMenu()
    else:
        print("Username or Password incorrect")
        return login()
def showMenu():
    print("---KShop---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelected()
def menuSelected():
    userSelected = int(input(">> "))
    if userSelected == 1:
        print(vatCalculate(int(input("Price : "))))
    elif userSelected == 2:
        print(priceCalculate())
    else:
        print("ERROR")
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
def priceCalculate():
    price1 = int(input("First price : "))
    price2 = int(input("Second price : "))
    return vatCalculate(price1 + price2)

login()
