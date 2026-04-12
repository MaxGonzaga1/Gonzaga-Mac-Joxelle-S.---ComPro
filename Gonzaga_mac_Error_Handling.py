balance = 0

print("Welcome to Simple Money Withdrawal System")

def withdraw():
    global balance
    try:
        withd = int(input("Enter amount of money: "))
        if balance <= withd:
            print("insufficient funds.")
            print("do you want to do other operation instead?")
        else:
            balance -= withd
            print(f"Your new Balance: {balance}")
    except ValueError:
        print("invalid input.")
        print("do you want to do other operation instead?")
def deposit():
    global balance
    try:
        depo = int(input("Enter amount of money: "))
        balance += depo
        print(f"Your new Balance: {balance}")
    except ValueError:
        print("invalid input.")
        print("do you want to do other operation instead?")
def checkBalance():
    print(f"Your current balance: {balance}")
def exit():
    print("Thank you and goodbye!")
    
while True:
    print("")
    print("""These are the operations:
        1. Withdraw
        2. Deposit
        3. Check Balance
        4. Exit""")
    operation = input("Enter operation: ")
    try:
        if operation == "1":
            print("")
            withdraw()
        elif operation == "2":
            print("")
            deposit()
        elif operation == "3":
            print("")
            checkBalance()
        elif operation == "4":
            print("")
            exit()
            break
        else:
            print("")
            print("invalid input.")
    except ValueError:
        print("")
