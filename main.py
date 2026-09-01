import json
# Load expenses 
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save expenses 
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- EXPENSES -----")

    for i, expense in enumerate(expenses, start=1):
        print("ID:", i)
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("--------------------")


# Show total and category-wise spending
def show_summary(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0
    category_total = {}

    for expense in expenses:
        total = total + expense["amount"]

        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    print("\nTotal Spending:", total)

    print("\n----- CATEGORY SUMMARY -----")

    for category in category_total:
        print(category, ":", category_total[category])


# Search expenses by category
def search_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    search_category = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("\nAmount:", expense["amount"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("--------------------")
            found = True

    if not found:
        print("No expenses found for this category.")


# Delete an expense
def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    view_expenses(expenses)

    try:
        expense_id = int(input("Enter expense ID to delete: "))

        if 1 <= expense_id <= len(expenses):
            deleted_expense = expenses.pop(expense_id - 1)
            save_expenses(expenses)

            print("Deleted:", deleted_expense["description"])
            print("Expense deleted successfully!")
        else:
            print("Invalid expense ID.")

    except ValueError:
        print("Please enter a valid number.")


# Load data
expenses = load_expenses()


# Main program
while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense(expenses)

        elif choice == 2:
            view_expenses(expenses)

        elif choice == 3:
            show_summary(expenses)

        elif choice == 4:
            search_expense(expenses)

        elif choice == 5:
            delete_expense(expenses)

        elif choice == 6:
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again")

    except ValueError:
        print("Please enter a valid number")