# Personal Finance Tracker - Step 7: Input Validation

# Global list to store all transactions
transactions = []


def show_menu():
    """Display the menu options"""
    print("-" * 40)
    print("MENU")
    print("-" * 40)
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Exit")
    print("-" * 40)


def add_transaction():
    """Add a new transaction with validation"""
    global transactions
    
    print("--- Add Transaction ---")
    
    # VALIDATION 1: Check transaction type
    while True:
        trans_type = input("Type (income/expense): ").lower()
        if trans_type == "income" or trans_type == "expense":
            break  # Valid input, exit the loop
        else:
            print("❌ Invalid! Please enter 'income' or 'expense'.")
    
    # VALIDATION 2: Check amount is a number
    while True:
        amount = input("Amount: $")
        try:
            # Try to convert to float (decimal number)
            amount_float = float(amount)
            if amount_float > 0:
                break  # Valid positive number, exit the loop
            else:
                print("❌ Amount must be positive!")
        except ValueError:
            # This runs if conversion to float fails
            print("❌ Invalid! Please enter a valid number.")
    
    # VALIDATION 3: Description (can't be empty)
    while True:
        description = input("Description: ").strip()
        if len(description) > 0:
            break  # Not empty, exit the loop
        else:
            print("❌ Description cannot be empty!")
    
    # Create a DICTIONARY to store the transaction
    transaction = {
        "type": trans_type,
        "amount": amount,
        "description": description
    }
    
    # Add the dictionary to our list
    transactions.append(transaction)
    
    print()
    print("✓ Transaction added successfully!")
    print()


def view_transactions():
    """Display all transactions"""
    global transactions
    
    print("--- All Transactions ---")
    
    if len(transactions) == 0:
        print("No transactions yet. Add some first!")
    else:
        for t in transactions:
            print("- " + t["type"].capitalize() + ": $" + t["amount"] + " - " + t["description"])
        print()
        print("Total:", len(transactions), "transactions")
    print()


def main():
    """Main function that runs everything"""
    # Welcome message
    print("=" * 40)
    print("  WELCOME TO FINANCE TRACKER")
    print("=" * 40)
    print()
    
    # Get user's name (with validation!)
    while True:
        name = input("What's your name? ").strip()
        if len(name) > 0:
            break
        else:
            print("❌ Name cannot be empty!")
    
    print()
    print("Hello " + name + "! Let's track your finances.")
    print()
    
    # Main loop
    while True:
        show_menu()
        
        choice = input("Choose an option (1-3): ").strip()
        print()
        
        if choice == "1":
            add_transaction()
        
        elif choice == "2":
            view_transactions()
        
        elif choice == "3":
            print("Thanks for using Finance Tracker, " + name + "!")
            print("Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")
            print()


# Start the program
if __name__ == "__main__":
    main()