# Personal Expense Tracker

A simple command-line based Personal Expense Tracker developed using Python.

The application allows users to add, view, search, summarize, and delete their expenses. The expense data is stored permanently in a JSON file so that the data is available even after the program is closed.

## Project Overview

Managing daily expenses manually can be difficult. This project provides a simple command-line solution for recording and managing personal expenses.

The application stores each expense with:

- Amount
- Category
- Description

The data is stored in a JSON file using Python's built-in `json` module.

The project was developed to practice Python programming concepts such as:

- Variables
- Data types
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling
- JSON data storage

## Objectives

The main objectives of this project are:

1. Create a simple expense management application.
2. Allow users to add and store expenses.
3. Display all recorded expenses.
4. Calculate total spending.
5. Calculate category-wise spending.
6. Search expenses by category.
7. Delete unwanted expenses.
8. Store data permanently using JSON.
9. Handle invalid user input using exception handling.
10. Build a practical Python project using core programming concepts.

## Features

### 1. Add Expense

Users can enter:

- Amount
- Category
- Description

Example:

```text
Enter amount: 500
Enter category: Food
Enter description: Lunch
```

The expense is added to the list and saved to the JSON file.

### 2. View Expenses

Users can view all recorded expenses.

Example:

```text
----- EXPENSES -----

ID: 1
Amount: 500.0
Category: Food
Description: Lunch
--------------------

ID: 2
Amount: 1000.0
Category: Travel
Description: Petrol
--------------------
```

The application generates an ID dynamically while displaying the expenses.

### 3. Total Spending

The application calculates the total amount spent across all recorded expenses.

Example:

```text
Total Spending: 1500.0
```

---

### 4. Category-wise Spending

The application calculates how much money was spent in each category.

Example:

```text
----- CATEGORY SUMMARY -----

Food : 500.0
Travel : 1000.0
```

### 5. Search Expense

Users can search for expenses based on category.

Example:

```text
Enter category to search: food
```

The application displays matching expenses.

The search is case-insensitive, so `Food`, `food`, and `FOOD` are treated as the same category.

### 6. Delete Expense

Users can delete an expense using its displayed ID.

Example:

```text
Enter expense ID to delete: 2
```

The selected expense is removed from the list and the updated data is saved to the JSON file.

### 7. Data Persistence

Expense data is stored in:

```text
expenses.json
```

This means the data is not lost when the program is closed.

When the application starts again, it loads the existing expenses from the JSON file.

## Technologies Used

- **Python 3**
- **JSON**
- **File Handling**
- **VS Code**

The project uses only Python's built-in `json` module and does not require external Python libraries.


## Project Structure

```text
ExpenseTracker/
│
├── main.py
├── expenses.json
└── README.md
```

### main.py

Contains the complete Python application including:

- Loading expenses
- Saving expenses
- Adding expenses
- Viewing expenses
- Calculating summaries
- Searching expenses
- Deleting expenses
- Main menu

### expenses.json

Stores the expense data permanently in JSON format.

### README.md

Contains project documentation, setup instructions, features, and technical information.

## Data Structure

The application uses a **list of dictionaries** to store expenses.

Example:

```python
expenses = [
    {
        "amount": 500.0,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 1000.0,
        "category": "Travel",
        "description": "Petrol"
    }
]
```

Each dictionary represents one expense.

## Application Workflow

The application follows this basic workflow:

```text
Start
  |
  v
Load expenses from JSON
  |
  v
Display Main Menu
  |
  +----> Add Expense
  |
  +----> View Expenses
  |
  +----> Total Spending
  |
  +----> Search Expense
  |
  +----> Delete Expense
  |
  +----> Exit
```

When the user exits the program, the stored data remains inside `expenses.json`.

## How the Application Works

### Loading Data

When the application starts, the `load_expenses()` function reads the JSON file.

```python
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
```

If the file exists, the stored expenses are loaded.

If the file does not exist, an empty list is returned.

### Saving Data

The `save_expenses()` function saves the current expense list into the JSON file.

```python
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
```

The `json.dump()` function converts the Python data into JSON format.

### Adding an Expense

The application collects the amount, category, and description from the user.

The information is stored inside a dictionary.

```python
expense = {
    "amount": amount,
    "category": category,
    "description": description
}
```

The dictionary is then added to the expense list using:

```python
expenses.append(expense)
```

Finally, the updated list is saved to the JSON file.

### Viewing Expenses

The application uses a `for` loop to go through every expense.

```python
for i, expense in enumerate(expenses, start=1):
```

The `enumerate()` function provides a number for each expense.

The displayed ID starts from 1 to make it easier for the user to select an expense.

### Calculating Total Spending

The application starts with:

```python
total = 0
```

Then it loops through all expenses and adds each amount:

```python
total = total + expense["amount"]
```

This produces the total amount spent.

### Category-wise Summary

A dictionary is used to calculate spending for each category.

Example:

```python
category_total = {}
```

If the category already exists, the new amount is added to the existing total.

Otherwise, a new category is created.

This allows the application to produce a summary such as:

```text
Food : 1500
Travel : 3000
Shopping : 1000
```

### Searching Expenses

The application asks the user for a category.

The `.lower()` method is used so that the search is case-insensitive.

```python
if expense["category"].lower() == search_category.lower():
```

A Boolean variable called `found` is used to determine whether a matching expense exists.


### Deleting Expenses

The user selects an expense using its displayed ID.

Because Python list indexes start from `0`, while the displayed IDs start from `1`, the application converts the ID into an index:

```python
expense_id - 1
```

The selected expense is then removed using:

```python
expenses.pop(expense_id - 1)
```

The updated list is saved back to the JSON file.

## JSON Data Storage

JSON stands for **JavaScript Object Notation**.

It is a lightweight format commonly used for storing and exchanging structured data.

Example:

```json
[
    {
        "amount": 500.0,
        "category": "Food",
        "description": "Lunch"
    }
]
```

JSON was selected for this project because:

- It is lightweight.
- It is human-readable.
- It is easy to use with Python.
- Python provides built-in JSON support.
- It is suitable for a small personal application.
- It allows structured data to be stored easily.

## File Handling

The project uses Python file handling to read and write expense data.

### Read Mode

```python
open("expenses.json", "r")
```

`r` means read.

### Write Mode

```python
open("expenses.json", "w")
```

`w` means write.

The current expense list is written to the file, keeping all existing records unless an expense has been deleted.

### Using `with`

The project uses:

```python
with open(...) as file:
```

This automatically handles closing the file after the operation is completed.


## Error Handling

The application uses `try` and `except` to handle invalid input and missing files.

### Handling Missing JSON File

```python
except FileNotFoundError:
    return []
```

If `expenses.json` does not exist, the application starts with an empty list instead of crashing.

### Handling Invalid Menu Input

```python
try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("Please enter a valid number.")
```

This prevents the application from crashing if the user enters text instead of a number.

### Handling Invalid Expense ID

The delete operation also uses exception handling to ensure the user enters a valid number.

## Python Concepts Used

This project demonstrates several important Python concepts.

### Variables

```python
amount = 500
category = "Food"
```

### Lists

```python
expenses = []
```

A list stores multiple expense records.

### Dictionaries

```python
expense = {
    "amount": amount,
    "category": category,
    "description": description
}
```

A dictionary stores related information using key-value pairs.

### Functions

The project is divided into functions such as:

```python
add_expense()
view_expenses()
show_summary()
search_expense()
delete_expense()
```

Functions make the code organized and reusable.

### Loops

The project uses `for` loops to process expenses and a `while` loop to keep the menu running.

### Conditional Statements

The project uses:

```python
if
elif
else
```

to make decisions.

### Exception Handling

The project uses:

```python
try
except
```

to handle errors safely.

### JSON

The built-in `json` module is used for data storage.

---

## Installation and Setup

### Step 1: Install Python

Install Python 3 on your computer.

Verify the installation using:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Open the Project

Open the project folder in VS Code.

---

## How to Run

Open the VS Code terminal inside the project folder.

Run:

```bash
python main.py
```

The application will display:

```text
===== PERSONAL EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Total Spending
4. Search Expense
5. Delete Expense
6. Exit

Enter your choice:
```

---

## Usage

### Add an Expense

Select:

```text
1
```

Then enter:

```text
Amount
Category
Description
```

---

### View Expenses

Select:

```text
2
```

The application displays all stored expenses.

---

### View Total and Category Summary

Select:

```text
3
```

The application displays:

- Total spending
- Category-wise spending

---

### Search an Expense

Select:

```text
4
```

Enter a category such as:

```text
Food
```

The application displays all expenses belonging to that category.

---

### Delete an Expense

Select:

```text
5
```

Enter the ID of the expense you want to delete.

---

### Exit

Select:

```text
6
```

The program exits while the saved expenses remain in `expenses.json`.

---

## Testing

The application was tested using different scenarios.

### Test Case 1: Add Expense

Input:

```text
Amount: 500
Category: Food
Description: Lunch
```

Expected result:

```text
Expense added successfully!
```

### Test Case 2: View Expenses

Expected result:

The application displays all saved expenses with their amount, category, and description.


### Test Case 3: Total Spending

Expected result:

The application calculates and displays the sum of all expense amounts.


### Test Case 4: Search Category

Input:

```text
Food
```

Expected result:

All expenses belonging to the Food category are displayed.

### Test Case 5: Delete Expense

Input:

```text
Expense ID: 1
```

Expected result:

The selected expense is removed and the JSON file is updated.


### Test Case 6: Invalid Input

Input:

```text
abc
```

Expected result:

```text
Please enter a valid number.
```

The program should continue running instead of crashing.

## CRUD Operations

The project demonstrates the basic CRUD concept.

| Operation | Implementation |
|---|---|
| Create | Add a new expense |
| Read | View and search expenses |
| Update | Not currently implemented |
| Delete | Delete an expense |

The current version focuses on creating, reading, and deleting expense records.

## Design Approach

The application follows a simple modular approach.

Instead of putting all the code inside one large block, separate functions are used for different operations.

For example:

```text
load_expenses()
        |
        v
add_expense()
        |
        v
view_expenses()
        |
        v
show_summary()
        |
        v
search_expense()
        |
        v
delete_expense()
```

This makes the program easier to understand, test, and maintain.

## Advantages

- Simple command-line interface
- Easy to understand
- Lightweight
- No external libraries required
- Persistent data storage
- Modular Python functions
- Basic error handling
- Category-wise expense analysis
- Easy to extend

## Limitations

The current version has some limitations:

- It is command-line based.
- There is no graphical user interface.
- There is no user authentication.
- There is no budget management.
- There is no income tracking.
- There are no charts or visual reports.
- It uses JSON instead of a database.
- It does not store date and time for expenses.

These limitations can be addressed in future versions.

## Future Enhancements

Possible future improvements include:

1. Add date and time to every expense.
2. Add an update/edit expense feature.
3. Add monthly and yearly reports.
4. Add budget management.
5. Add income tracking.
6. Add data visualization using charts.
7. Create a graphical user interface.
8. Move from JSON to SQLite or another database.

## Scalability

The current JSON-based approach is suitable for a small personal application.

If the project needs to support:

- Multiple users
- Large amounts of data
- Concurrent access
- Advanced searching
- Complex reporting

then the storage system can be upgraded to a database such as SQLite, MySQL, or PostgreSQL.

The application functions can also be connected to a web framework such as Flask or Django to create a web-based version.


## Conclusion

The Personal Expense Tracker is a beginner-friendly Python project designed to demonstrate practical programming concepts.

It provides essential expense management functionality while maintaining data persistence through JSON storage.

The project can be further extended with databases, graphical interfaces, authentication, reporting, and data visualization to make it suitable for a more advanced application.