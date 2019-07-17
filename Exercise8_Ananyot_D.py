username = input("Username : ")
password = input("Password : ")
if username == "Ananyot" and password == "1234" :
    print("Welcome to my shop!!!")
    print("---Please selecting product---")
    print("1.chair 50 THB")
    print("2.table 100 THB")
    selected = int(input("Select number : "))
    if selected == 1:
        print("How many do you want?")
        chair = 50
        amount = int(input("I want : "))
        total = chair*amount
        print("Total price :",total,"THB")
    elif selected == 2:
        print("How many do you want?")
        table = 100
        amount = int(input("I want : "))
        total = table*amount
        print("Total price :",total,"THB")
    else :
        print("ERROR")
else :
    print("Username or Password incorrect")