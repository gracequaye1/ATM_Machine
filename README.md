# ATM Machine

## Authors
- [Naomi](https://github.com/naomikortey75)
- [Grace](https://github.com/gracequaye1)

## Project Overview
This repository contains an interactive command-line project:

1. **ATM Machine**: A simple ATM simulator that allows users to check balance, deposit, withdraw, and change their PIN.

## ![Image](https://www.idfcfirstbank.com/content/dam/idfcfirstbank/images/blog/finance/what-is-atm-717x404.jpg)

## How to Use This Repository
1. Clone the repository to your local machine.
2. Navigate to the directory where you cloned it.
3. Run the provided Python scripts in your terminal.
4. Follow the prompts in each script to interact with the programs.

## Project Structure
- `control_flow_atm.py`: Contains the ATM Machine simulation.

## Tech Stack
- Python

## Contribution
If you find this project interesting and want to add new features, improve existing functionality, or fix any issues, your contributions are more than welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, concise messages.
4. Push your branch and create a pull request for review.

You can contact us on [Naomi](https://github.com/naomikortey75) or [Grace](www.linkedin.com/in/grace-okailey-quaye-286b52287)

## Objectives:

- Strengthen control flow through nested conditions.
- Practice variable manipulation, loops, and functions.
- Implement enhanced user security and transaction tracking.

## Project Specifications

### 1. Initial Setup
- Create a variable `balance` to hold the user’s account balance (e.g., 5000).
- Set up a `pin` variable (e.g., 1234) for the user’s ATM PIN.

### 2. User Authentication
- Prompt the user to enter their PIN.
- Allow only three attempts if the PIN does not match; if all attempts are incorrect, exit with the message: "Too many incorrect attempts. Access blocked."
- If the PIN matches, proceed to the main menu.

### 3. Main Menu
After successful PIN entry, display a menu with options:
1. Check Balance
2. Deposit Funds
3. Withdraw Funds
4. Change PIN
5. Exit

- Use a loop to allow the user to return to the main menu until they choose to exit.

### 4. Functionality
- **Check Balance**: Display the current balance.
- **Deposit Funds**: Prompt the user to enter a deposit amount.
    - Allow only positive numbers; update and display the new balance.
- **Withdraw Funds**: Prompt the user to enter a withdrawal amount.
    - Ensure the amount is positive and doesn’t exceed the balance.
    - Display an error if the balance is insufficient; otherwise, update and display the new balance.
- **Change PIN**:
    - Prompt the user to enter the current PIN.
    - If it matches, allow them to set a new 4-digit PIN.
    - Confirm the new PIN by asking them to enter it again.

### 5. Error Handling
- Ensure all user inputs (amounts and PINs) are valid integers.
- Include error messages and re-prompts for invalid entries.

### 6. Exiting the ATM
- Thank the user upon exit and display a summary of the total deposits and withdrawals during the session.
