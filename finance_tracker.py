# Personal Finance Tracker - Step 10: Complete Version!

import json

# Global list to store all transactions
transactions = []


def load_data():
    """Load transactions from file when program starts"""
    global transactions
    
    try:
        with open("finance_data.json", "r") as file:
            transactions = json.load(file)
            print("✓ Loaded", len(transactions), "transactions from file.")
    except FileNotFoundError:
        print("No previous data found. Starting fresh!")
        transactions = []
    except json.JSONDecodeError:
        print("⚠ Data file is corrupted. Starting fresh!")
        transactions = []


def save_data():
    """Save transactions to file"""
    global transactions
    
    try:
        with open("finance_data.json", "w") as file:
            json.dump(transactions, file, indent=2)
        print("✓ Data saved successfully!")
    except Exception as e:
        print("❌ Error saving data:", str(e))


def show_menu():
    """Display the menu options"""
    print("-" * 40)
    print("MENU")
    print("-" * 40)
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View Summary")
    print("4. Delete Transaction")
    print("5. Exit")
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
    save_data()
    
    print()
    print("✓ Transaction added successfully!")
    print()


def view_transactions():
    """Display all transactions with numbering"""
    global transactions
    
    print("--- All Transactions ---")
    
    if len(transactions) == 0:
        print("No transactions yet. Add some first!")
    else:
        for i, t in enumerate(transactions, 1):
            print(str(i) + ". " + t["type"].capitalize() + ": $" + t["amount"] + " - " + t["description"])
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
    
    # Calculate totals
    for t in transactions:
        amount = float(t["amount"])
        
        if t["type"] == "income":
            total_income += amount
        elif t["type"] == "expense":
            total_expense += amount
    
    # Calculate balance
    balance = total_income - total_expense
    
    # Display summary
    print()
    print("Total Income:  $" + str(total_income))
    print("Total Expense: $" + str(total_expense))
    print("=" * 40)
    print("Balance:       $" + str(balance))
    print()
    
    # Feedback
    if balance > 0:
        print("✓ Great! You're saving money! 💰")
    elif balance == 0:
        print("⚠ You're breaking even. Try to save more!")
    else:
        print("⚠ Warning! You're spending more than you earn! 📉")
    
    print()


def delete_transaction():
    """Delete a transaction by number"""
    global transactions
    
    print("--- Delete Transaction ---")
    
    # Check if list is empty
    if len(transactions) == 0:
        print("No transactions to delete!")
        print()
        return
    
    # Show all transactions first
    print("Current transactions:")
    for i, t in enumerate(transactions, 1):
        print(str(i) + ". " + t["type"].capitalize() + ": $" + t["amount"] + " - " + t["description"])
    print()
    
    # Get transaction number to delete
    while True:
        choice = input("Enter transaction number to delete (or 0 to cancel): ").strip()
        
        try:
            # Convert to integer
            num = int(choice)
            
            # Check if user wants to cancel
            if num == 0:
                print("Delete cancelled.")
                print()
                return
            
            # Check if number is valid (1 to length of list)
            if 1 <= num <= len(transactions):
                # Convert to list index (subtract 1)
                index = num - 1
                
                # Get the transaction we're about to delete
                deleted = transactions[index]
                
                # Delete it using pop()
                transactions.pop(index)
                
                # Save the changes
                save_data()
                
                print()
                print("✓ Deleted:", deleted["type"].capitalize(), "$" + deleted["amount"], "-", deleted["description"])
                print()
                break
            else:
                print("❌ Invalid number! Choose between 1 and", len(transactions))
        
        except ValueError:
            print("❌ Please enter a valid number!")


def main():
    """Main function that runs everything"""
    print("=" * 40)
    print("  WELCOME TO FINANCE TRACKER")
    print("=" * 40)
    print()
    
    # Load data when program starts
    load_data()
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
        
        choice = input("Choose an option (1-5): ").strip()
        print()
        
        if choice == "1":
            add_transaction()
        
        elif choice == "2":
            view_transactions()
        
        elif choice == "3":
            view_summary()
        
        elif choice == "4":
            delete_transaction()
        
        elif choice == "5":
            print("Thanks for using Finance Tracker, " + name + "!")
            print("Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, 4, or 5.")
            print()


# Start the program
if __name__ == "__main__":
    main()