balance = 5000  # Initial balance
pin = 1234  # Default PIN

attempts = 3
while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        break
    else:
        attempts -= 1
        print("Incorrect PIN. Attempts remaining:", attempts)

if attempts == 0:
    print("Too many incorrect attempts. Access blocked.")
    exit()


while True:
    print("\n1. Check Balance\n2. Deposit Funds\n3. Withdraw Funds\n4. Change PIN\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposit successful. New balance:", balance)
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print("Withdrawal successful. New balance:", balance)
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount.")

    elif choice == "4":
        current_pin = int(input("Enter current PIN: "))
        if current_pin == pin:
            new_pin = int(input("Enter new 4-digit PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))
            if new_pin == confirm_pin and 1000 <= new_pin <= 9999:
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PINs did not match or invalid PIN format.")
        else:
            print("Incorrect current PIN.")

    elif choice == "5":
        print("Thank you for using the ATM. Have a great day!")
        break

    else:
        print("Invalid choice. Please try again.")
