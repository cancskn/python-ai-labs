# deposit
# check balance
# withdraw

# if user input deposit, deposit() will be executed...
# if balance < 0, then withdraw will raise error 'your balance 0'

def bank_app():
    print("Menu \nCheck balance (1): \nDeposit money (2): \nWithdraw money (3): \nExit (0)\n")


    balance = 0
    while True:
        operation = int(input("Please choose an operation: "))

        if operation == 1 :
            print("Your have " + str(balance) + " zt" + " in your account." )
        elif operation == 2 :
            money = int(input("Enter the amount of money you want to deposit: "))
            balance += money
            print("Operation is confirmed.")
        elif operation == 3 :
            if balance > 0:
                money = int(input("Enter the amount of money you want to withdraw: "))
                balance -= money
                print("Operation is confirmed.")
            else:
                print("Your balance is 0 or less")
        elif operation == 0 :
            print("Goodbye!")
            break
        else:
            print("Wrong input, please try again.")

bank_app()


