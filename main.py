# Python Banking Program

def show_blc():
    pass

def deposit():
    pass

def withdraw():
    pass

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
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice.")

print("\nThank you for using Banking Program.")