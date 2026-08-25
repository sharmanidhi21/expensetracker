expense={
    "date": 25-8-26,
    "category": "food",
    "amount": 2100,
    "description" : "dinner"

}

print(expense["amount"])



expenses = []

def add_expense():
    "date"== input("enter a date:")
    "category"== input ("enter a category:")
    "amount" == input ("enter a amount:")
    "description" == input("enter a description:")

    expense = { 
    "date": 25-8-26,
    "category": "trip",
    "amount": 500,
    "description" : "mahabaleshwar"
    
    }
    expenses.append(expense)

print("expenses add successfully")

def view_expenses():
    if len(expenses)== 0:
        print ("no expenses found")
        return

    print("\n expenses")

    for expense in expenses:
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Amount: ₹", expense["amount"])
        print("Description:", expense["description"])
        print("-----------------------------")

def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense: ₹", total)

total_expense()

while True:

    print("\n expenses")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")




