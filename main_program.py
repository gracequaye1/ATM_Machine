# This is the main file where we run the ATM program.
# We import the functions from other files here.

from check_balance import check_balance
from deposit_funds import deposit_funds

# Example ATM Program logic
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

# Main menu
while True:
    print("\n1. Check Balance\n2. Deposit Funds\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        balance = deposit_funds(balance)

    elif choice == "3":
        print("Thank you for using the ATM. Have a great day!")
        break

    else:
        print("Invalid choice. Please try again.")
