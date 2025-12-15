# Personal Finance Tracker - Learning Python Step by Step

# STEP 3: Getting User Input for Transactions
# Now we let the USER add their own transactions!

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

# Let's add atransaction by asking the user
print("--- Add Your First Transaction ---")
print()

# Ask for Transaction type
trans_type = input("Is this income or expense? ")

# Ask for amount
amount = input("How much? $")

# Ask for description 
description = input("What's it for? ")

# Combine all the information into one string
transaction = trans_type + ": $" + amount + " - " + description

# Add it to your list
transactions.append(transaction)

print()
print("--- All your Transactions ---")
for t in transactions:
    print("- " + t)

print()
print("Total Transactions:", len(transactions))