# STEP 1: Your First Python Program - A Simple Menu

print("Welcome to Finance Tracker")
print("Let's learn Python together")

#Lets get input from the user
name = input("What's your name?: ")

#Now lets use that input
print("Hello " + name + "!")
print("Ready to track your finances?")

# STEP 2: Learning about Lists
# A list is like a container that can hold multiple items

# Create an empty list to store our transactions
transactions = []

print("welcome to Finance Tracker!")
print("Let's learn about lists!")
print()

# Let's add some items to our list
print("Adding transactions to our list...")
transactions.append("Salary: $3000")
transactions.append("Groceries: -$150")
transactions.append("Rent: -$1000")

print("Done adding")
print()

# Let's see what's in our list
print("Here are all transaction:")
print(transactions)
print()

# Let's print each transaction on its own line
print("Let's display them nicely:")
for transaction in transactions:
    print("- " + transaction)

print()
print("Total number of transactions:", len(transactions))