# Python Banking Program

def show_blc():
    print(f"YOur balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount <= 0:
        print("You cannot deposit 0! ")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount you want to withdraw: "))

    if amount > balance:
        print("Insufficient funds ")
        return 0
    elif amount <= 0:
        print("Amount must be greater than 0 ")
        return 0
    else:
        print(f"The amount ${amount} has been withdrawn.")
        return amount


balance = 0
is_running = True

while is_running:
    print("\nWelcome to the Banking Program.")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_blc()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice.")

print("\nThank you for using Banking Program.")