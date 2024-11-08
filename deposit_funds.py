def deposit_funds(balance):
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful. New balance:", balance)
    else:
        print("Invalid amount.")
    return balance
