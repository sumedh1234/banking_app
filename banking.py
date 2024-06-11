def show_balance(balance):
    print(f"Your Balance is ₹{balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("This is not valid amount!\n")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficiant balance\n")
        return 0
    elif amount < 0:
        print("The amount should be more than 0\n")
        return 0
    else:
        return amount


if __name__ == '__main__':
    balance = 0
    is_running = True

    while is_running:
        print("Banking program\n------------------------------------------")
        print("1.Show the balance\n2.Deposit\n3.Withdraw\n4.Exit\n------------------------------------------")

        choice = input("Enter your choice(1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
            print("Thank you for using me!")
        else:
            print("Enter appropriate choice")
        
