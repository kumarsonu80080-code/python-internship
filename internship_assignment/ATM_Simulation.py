def atm():
    balance = 10000
    print("*** MENU ***")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. Exit")
    # print(balance)
    check = int(input("FOR AXIS MENU ITEMS ENTER HER NO : "))
    # for i in range(5):
    i = 0
    while True:

        if check == 1:
            print("your balance is :₹ ",balance)
        elif check == 2:
            print("enter your amount")
            amount = int(input(":)"))
            balance = balance + amount
            print("your balance is : ₹ ",balance)
        elif check == 3:
            print("enter your amount")
            amount = int(input(":)"))
            if amount <= balance:
                balance = balance - amount
                print("your balance is :₹ ",balance)
            else:
                print("Insufficient Balance")
        elif check == 4:
            print("*** THANK YOU ***\n")
            

            print("\n*** MENU ***")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. withdraw")
            print("4. Exit")

        else:
            print("----SOMTHING RONG----")
        check = int(input("YOU WANT TO CHECK SOMTHING AGAIN : "))




ATM = atm()
print(ATM)