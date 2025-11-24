import os
import csv
from datetime import datetime

FILE = "expenses.csv"

# This function is defined to create the file to if not created 
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "amount", "category"])


# Function to add an expense to the file
def add_expense():
    amount = float(input("Enter amount spent: "))
    category = input("Enter category (food/travel/shopping/etc): ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), amount, category])

    print("Expense added successfully.\n")


# Function to display all stored expenses
def view_expenses():
    print("\n--- ALL EXPENSES ---")
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            print(", ".join(row))
    print()


# Function to calculate the total expenses
def total_expenses():
    total = 0
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # here the next fuction is used to skip the header
        for row in reader:
            total += float(row[1])
        print(total)


# Function to check the budget status
def check_budget():
    budget = float(input("Set your monthly budget = "))
    spent = total_expenses()

    print(f"\nTotal spent : Rs{spent}")
    print(f"Your budget: Rs{budget}")

    if spent > budget:
        print(" You have exceeded your budget!")
    else:
        print("You are within your budget.")
    print()


# input reciver from user
while True:
    print("----- SMART EXPENSE TRACKER -----")
    print("1. Add Expense \n2. View Expenses \n3. Show Total Expenses \n4. Check Budget\n5. Exit")

    choice = input("Enter your choice = ")

    if (choice == "1"):
        add_expense()

    elif (choice == "2"):
        view_expenses()

    elif (choice == "3"):
        print(f"\nTotal Expenses: Rs{total_expenses()}\n")

    elif (choice == "4"):
        check_budget()

    elif (choice == "5"):
        print("Exit")
        break

    else:
        print("Invalid choice! \n Try again.\n")
