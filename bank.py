# deposit
# check balance
# withdraw

# if user input deposit, deposit() will be executed...
# if balance < 0, then withdraw will raise error 'your balance 0'

balance = 0
def check_balance():
    print("Your have " + str(balance) + " zt" + " in your account.")

def deposit():
    global balance
    money = int(input("Enter the amount of money you want to deposit: "))
    balance += money
    print("Operation is confirmed.")

def withdraw():
    global balance
    if balance > 0:
        money = int(input("Enter the amount of money you want to withdraw: "))
        balance -= money
        print("Operation is confirmed.")
    else:
        print("Your balance is 0 or less")
def bank_app():
    print("Menu \nCheck balance (1): \nDeposit money (2): \nWithdraw money (3): \nExit (0)\n")

    while True:
        operation = int(input("Please choose an operation: "))

        if operation == 1 :
            check_balance()
        elif operation == 2 :
            deposit()
        elif operation == 3 :
            withdraw()
        elif operation == 0 :
            print("Goodbye!")
            break
        else:
            print("Wrong input, please try again.")

bank_app()


