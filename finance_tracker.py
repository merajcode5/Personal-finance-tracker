# Personal Finance Tracker - Learning Python Step by Step

# STEP 3: Getting User Input for Transactions
# Now we let the USER add their own transactions!

# Personal Finance Tracker - Step 4: Menu with Loop


# Create empty list to store transactions
transactions = []


print("=" * 40)
print("  WELCOME TO FINANCE TRACKER")
print("=" * 40)
print()

# Get user's name
name = input("What's your name? ")
print()
print("Hello " + name + "! Let's track your finances.")
print()

# This is the MAIN LOOP - it keeps the program running
while True:
    # Display the menu
    print("-" * 40)
    print("MENU")
    print("-" * 40)
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Exit")
    print("-" * 40)

    # Get user's choice
    choice = input("Choose an option (1-3): ")
    print()

    # CHeck what the user chose
    if choice == "1":
        # ADD TRANSACTION
        print("--- Add Transaction ---")
        trans_Type = input("Type (income/expense): ")
        amount = input("Amount: $")
        description = input("Description: ")

        # Create the transaction and add to list
        transaction = trans_Type + ": $" + amount + " - " + description
        transactions.append(transaction)

        print()
        print("✓ Transaction added!")
        print()

    elif choice == "2":
        # VIEW ALL TRANSACTIONS
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

    elif choice == "3":
        #Exit
        print("Thanks for using Finance Tracker. " + name + "!")
        print("Goodbye!")
        break # This EXITS the loop and ends the program

    else:
        # invalid choice
        print("invalid choice! Please enter 1, 2, or 3.")
        print()