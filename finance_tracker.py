# Personal Finance Tracker - Step 6: Using Dictionaries

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
    """Add a new transaction using a dictionary"""
    global transactions
    
    print("--- Add Transaction ---")
    trans_type = input("Type (income/expense): ")
    amount = input("Amount: $")
    description = input("Description: ")
    
    # Create a DICTIONARY to store the transaction
    transaction = {
        "type": trans_type,
        "amount": amount,
        "description": description
    }
    
    # Add the dictionary to our list
    transactions.append(transaction)
    
    print()
    print("✓ Transaction added!")
    print()


def view_transactions():
    """Display all transactions"""
    global transactions
    
    print("--- All Transactions ---")
    
    if len(transactions) == 0:
        print("No transactions yet. Add some first!")
    else:
        for t in transactions:
            print("- " + t["type"] + ": $" + t["amount"] + " - " + t["description"])
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
    
    # Get user's name
    name = input("What's your name? ")
    print()
    print("Hello " + name + "! Let's track your finances.")
    print()
    
    # Main loop
    while True:
        show_menu()
        
        choice = input("Choose an option (1-3): ")
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
            print("Invalid choice! Please enter 1, 2, or 3.")
            print()


# This line starts the program - MUST be at the very end!
if __name__ == "__main__":
    main() #agatin