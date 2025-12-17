# Personal Finance Tracker - Step 8: Financial Summary

# Global list to store all transactions
transactions = []


def show_menu():
    """Display the menu options"""
    print("-" * 40)
    print("MENU")
    print("-" * 40)
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View Summary")
    print("4. Exit")
    print("-" * 40)


def add_transaction():
    """Add a new transaction with validation"""
    global transactions
    
    print("--- Add Transaction ---")
    
    # Validate transaction type
    while True:
        trans_type = input("Type (income/expense): ").lower()
        if trans_type == "income" or trans_type == "expense":
            break
        else:
            print("❌ Invalid! Please enter 'income' or 'expense'.")
    
    # Validate amount
    while True:
        amount = input("Amount: $")
        try:
            amount_float = float(amount)
            if amount_float > 0:
                break
            else:
                print("❌ Amount must be positive!")
        except ValueError:
            print("❌ Invalid! Please enter a valid number.")
    
    # Validate description
    while True:
        description = input("Description: ").strip()
        if len(description) > 0:
            break
        else:
            print("❌ Description cannot be empty!")
    
    # Create transaction dictionary
    transaction = {
        "type": trans_type,
        "amount": amount,
        "description": description
    }
    
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


def view_summary():
    """Calculate and display financial summary"""
    global transactions
    
    print("--- Financial Summary ---")
    
    if len(transactions) == 0:
        print("No transactions yet. Add some to see your summary!")
        print()
        return
    
    # Initialize totals
    total_income = 0
    total_expense = 0
    
    # Loop through all transactions and calculate totals
    for t in transactions:
        amount = float(t["amount"])  # Convert string to number
        
        if t["type"] == "income":
            total_income = total_income + amount
        elif t["type"] == "expense":
            total_expense = total_expense + amount
    
    # Calculate balance
    balance = total_income - total_expense
    
    # Display the summary
    print()
    print("Total Income:  $" + str(total_income))
    print("Total Expense: $" + str(total_expense))
    print("=" * 40)
    print("Balance:       $" + str(balance))
    print()
    
    # Give feedback based on balance
    if balance > 0:
        print("✓ Great! You're saving money! 💰")
    elif balance == 0:
        print("⚠ You're breaking even. Try to save more!")
    else:
        print("⚠ Warning! You're spending more than you earn! 📉")
    
    print()


def main():
    """Main function that runs everything"""
    print("=" * 40)
    print("  WELCOME TO FINANCE TRACKER")
    print("=" * 40)
    print()
    
    # Get user's name with validation
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
        
        choice = input("Choose an option (1-4): ").strip()
        print()
        
        if choice == "1":
            add_transaction()
        
        elif choice == "2":
            view_transactions()
        
        elif choice == "3":
            view_summary()
        
        elif choice == "4":
            print("Thanks for using Finance Tracker, " + name + "!")
            print("Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
            print()


# Start the program
if __name__ == "__main__":
    main()