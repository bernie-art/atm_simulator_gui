import datetime

# Show Welcome message
print("WELCOME TO MEST ATM")
print("Please insert your atm card")

# Ask user to insert the card
user_card_name = input("Enter your name>> ") 
user_card_number = int(input("Enter your serial number>> "))

# User details
user_pin = 4190
current_balance = 10000.00
# To store transactions
transaction_history = [] 
# Example daily limit
daily_withdrawal_limit = 3000 
withdrawn_today = 0

# --- Helper Functions ---
# Add transaction history
def add_transaction(transaction_type, amount, balance_after):
    """Adds a new transaction to the history list."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_history.append({
        "type": transaction_type,
        "amount": amount,
        "balance": balance_after,
        "date": timestamp
    })

# Print receipt
def print_receipt(transaction_type, amount):
    """Prints a formatted receipt for a transaction."""
    print("\n--------------------------")
    print("      ATM RECEIPT")
    print("--------------------------")
    print(f"Transaction: {transaction_type}")
    print(f"Amount: GHS {amount:.2f}")
    print(f"Balance: GHS {current_balance:.2f}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("--------------------------\n")

# --- Main Functions ---

# PIN Authentication with limited attempts
def pin_authentication():
    """Authenticates the user with a 4-digit PIN, with a limit of 3 attempts."""
    global user_pin
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            pin = int(input("Enter your pin>> "))
            if pin == user_pin:
                print("Login Successful")
                return True
            else:
                attempts += 1
                print(f"Authentication Failed - Try again! You have {max_attempts - attempts} attempt(s) remaining.")
        except ValueError:
            attempts += 1
            print(f"Invalid input - Numbers only! You have {max_attempts - attempts} attempt(s) remaining.")
    
    print("\nToo many incorrect attempts. Exiting.")
    return False

# Deposit Function
def deposit():
    """Handles the deposit process and updates the balance."""
    global current_balance
    try:
        amount = float(input("Enter deposit amount>> "))
        if amount <= 0:
            print("Invalid amount. Must be greater than 0.")
        else:
            current_balance += amount
            add_transaction("Deposit", amount, current_balance)
            print(f"Deposit Successful! New Balance: Ghs {current_balance:.2f}")
            print_receipt("Deposit", amount)
    except ValueError:
        print("Invalid input. Please enter a number.")


# Withdrawal Function
def withdrawal():
    """Handles the withdrawal process, checking for balance and daily limits."""
    global current_balance, withdrawn_today
    try:
        amount = float(input("Enter the amount>> "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > current_balance:
            print("Insufficient balance.")
        elif withdrawn_today + amount > daily_withdrawal_limit:
            print("Daily withdrawal limit reached.")
        else:
            current_balance -= amount
            withdrawn_today += amount
            print("Withdrawal successful, please take your cash.")
            add_transaction("Withdrawal", amount, current_balance)
            print_receipt("Withdrawal", amount)
    except ValueError:
        print("Invalid input. Please enter a number.")


# Check Balance
def check_balance():
    """Displays the user's current account balance."""
    print(f"Your current balance is: Ghs {current_balance:.2f}")


# Show transaction history
def show_history():
    """Displays a list of all transactions."""
    if not transaction_history:
        print("No transactions yet.")
    else:
        print("\n--- Transaction History ---")
        for t in transaction_history:
            print(f"Date: {t['date']} - {t['type']}: GHS{t['amount']:.2f} | Balance: GHS{t['balance']:.2f}")
        print("--------------------------\n")
        
# Change PIN Function
def change_pin():
    """Allows the user to change their PIN."""
    global user_pin
    new_pin_1 = input("Enter your new 4-digit PIN: ")
    new_pin_2 = input("Confirm your new 4-digit PIN: ")

    if len(new_pin_1) != 4 or not new_pin_1.isdigit():
        print("Invalid PIN format. PIN must be a 4-digit number.")
    elif new_pin_1 != new_pin_2:
        print("PINs do not match. Please try again.")
    else:
        user_pin = int(new_pin_1)
        print("Your PIN has been successfully changed!")


# Menu Choices (Loop)
def choices():
    """Displays the main menu and handles user choices in a loop."""
    if not pin_authentication():
        return # Exit the program if authentication fails
        
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Exit")

        options = input("Choose an option>> ")
        if options == "1":
            check_balance()
        elif options == "2":
            deposit()
        elif options == "3":
            withdrawal()
        elif options == "4":
            show_history()
        elif options == "5":
            change_pin()
        elif options == "6":
            print("Thank you for using MEST ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main program execution
if __name__ == "__main__":
    choices()
