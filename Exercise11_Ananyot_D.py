number = int(input("Enter number : "))
for x in range(number):
    space = " "*(number-x)
    star = "*"*(x*2+1)
    print(space,star)