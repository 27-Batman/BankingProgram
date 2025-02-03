# Python Banking Program

def show_blc(balance):
    print("************************")
    print(f"YOur balance is ${balance:.2f}")
    print("************************")

def deposit():
    print("************************")
    amount = float(input("Enter the amount you want to deposit: "))
    print("************************")

    if amount <= 0:
        print("************************")
        print("You cannot deposit 0! ")
        print("************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("************************")
    amount = float(input("Enter the amount you want to withdraw: "))
    print("************************")

    if amount > balance:
        print("*******************")
        print("Insufficient funds ")
        print("*******************")
        return 0
    elif amount <= 0:
        print("************************")
        print("Amount must be greater than 0 ")
        print("************************")
        return 0
    else:
        print("*****************************************")
        print(f"The amount ${amount} has been withdrawn.")
        print("*****************************************")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("    Banking Program    .")
        print("************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_blc(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("************************")
            print("Invalid choice.")
            print("************************")
    print("**************************************************")
    print("Thank you for choosing our bank. Have a nice day!.")
    print("**************************************************")

if __name__ == "__main__":
    main()