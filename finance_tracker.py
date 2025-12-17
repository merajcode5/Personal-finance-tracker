# Personal Finance Tracker - Learning Python Step by Step

# STEP 3: Getting User Input for Transactions
# Now we let the USER add their own transactions!

# Personal Finance Tracker - Step 4: Menu with Loop

# Personal Finance Tracker - Step 5: Using Functions

# Global list to store all transactions
transactions = []


# FUNCTION 1: Display the menu
def show_menu():
    """This function shows the menu options"""
    print("-" * 40)
    print("MENU")
    print("-" * 40)
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Exit")
    print("-" * 40)


# FUNCTION 2: Add a transaction
def add_transaction():
    """This function adds a new transaction to the list"""
    global transactions  # Tell Python we're using the global variable
    
    print("--- Add Transaction ---")
    trans_type = input("Type (income/expense): ")
    amount = input("Amount: $")
    description = input("Description: ")
    
    # Create the transaction and add to list
    transaction = trans_type + ": $" + amount + " - " + description
    transactions.append(transaction)
    
    print()
    print("✓ Transaction added!")
    print()


# FUNCTION 3: View all transactions
def view_transactions():
    """This function displays all transactions"""
    global transactions  # Tell Python we're using the global variable
    
    print("--- All Transactions ---")
    
    # Check if list is empty
    if len(transactions) == 0:
        print("No transactions yet. Add some first!")
    else:
        for t in transactions:
            print("- " + t)
        print()
        print("Total:", len(transactions), "transactions")
    print()


# FUNCTION 4: Main program
def main():
    """This is the main function that runs everything"""
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
        show_menu()  # Call the show_menu function
        
        choice = input("Choose an option (1-3): ")
        print()
        
        if choice == "1":
            add_transaction()  # Call the add_transaction function
        
        elif choice == "2":
            view_transactions()  # Call the view_transactions function
        
        elif choice == "3":
            print("Thanks for using Finance Tracker, " + name + "!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            print()


# Start the program by calling main()
main()