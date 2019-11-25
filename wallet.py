def wallet(initial_amount):
    balance = 0

    def create_wallet(amount):
        print()
        print("-------------------------WALLET CREATED-----------------------")
        nonlocal balance
        balance += amount
        print("Available Balance: Rs. " + str(balance))
        print("------------------------------------------------------------")
        print()

    create_wallet(initial_amount)

    def deposit(amount):
        print()
        print("---------------------------DEPOSIT--------------------------")

        nonlocal balance
        print("Available Balance: Rs. " + str(balance))
        print("Amount Deposited: Rs. " + str(amount))
        balance += amount
        print("Available Balance: Rs. " + str(balance))
        print("------------------------------------------------------------")
        print()

    def spend(amount):
        print()
        print("--------------------------SPENDING--------------------------")
        nonlocal balance
        if balance >= amount:
            print("Available Balance: Rs. " + str(balance))
            balance -= amount
            print("Amount spent: Rs. " + str(amount))
            print("Balance: Rs. " + str(balance))
        else:
            print("No sufficient balance...")
            print("Balance: Rs. " + str(balance))

        print("------------------------------------------------------------")
        print()

    def fund_transfer(amount,Wallet):
        withdraw(amount)
        Wallet['deposit'](amount)


    def print_balance():
        print()
        print("-------------------PRINTING BALANCE-------------------------")
        nonlocal balance
        print("Balance Rs. " + str(balance))
        print("------------------------------------------------------------")
        print()

    def withdraw(amount):
        print()
        print("---------------------WITHDRAWAL----------------------------")
        nonlocal balance
        if balance >= amount:
            print("Available Balance: Rs. " + str(balance))
            balance -= amount
            print("Amount withdrawn: Rs. " + str(amount))
            print("Balance: Rs. " + str(balance))
        else:
            print("No sufficient balance...")
            print("Your balance is Rs. " + str(balance))

        print("------------------------------------------------------------")
        print()

    return {"deposit": deposit, "spend": spend, "printBalance": print_balance, "withdraw": withdraw,
            "fundtransfer": fund_transfer}


myWallet1 = wallet(500)
myWallet2 = wallet(500)
# myWallet1['spend'](300)
# myWallet1['printBalance']()
# myWallet1['deposit'](1000)
# myWallet1['withdraw'](200)
myWallet1['fundtransfer'](200,myWallet2)
myWallet1['printBalance']()
myWallet2['printBalance']()