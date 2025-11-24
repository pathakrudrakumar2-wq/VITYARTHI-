# VITYARTHI-
Smart Expense Tracker — Money Management System
A simple Python-based command-line application that helps users record expenses, track spending habits, and compare total expenses against a monthly budget.
This tool stores expense data in a CSV file, making it lightweight, portable, and easy to analyze later.
________________________________________
 Features
•	 Add expenses with amount and category
•	 Automatically timestamps each entry
•	 View all stored expenses
•	 Calculate total spending
•	 Check whether spending exceeds a set monthly budget
•	 Data stored locally in expenses.csv
•	 Runs entirely in the terminal—no external database needed
________________________________________
 Technologies Used
•	Python
•	csv module (data storage)
•	datetime module (date handling)
•	os module (file checking)
________________________________________
 Installation & Setup
1.	Clone or download the project
2.	git clone <repository-url>
3.	Navigate to the project folder
4.	cd money-management-system
5.	Run the script
6.	python MONEY MANAGEMENT SYSTEM.py
 If expenses.csv doesn’t exist, the program automatically creates it.
________________________________________
 How to Use
When the script runs, you’ll see a menu:
----- SMART EXPENSE TRACKER -----
1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Check Budget
5. Exit
1.  Add Expense
•	Enter amount spent
•	Enter category (ex: food, travel, shopping, etc.)
 2. View Expenses
Displays all past expenses saved in the CSV file
 3. Show Total Expenses
Calculates and prints total spending
 4. Check Budget
•	Enter your monthly budget
•	Compares total expenses with the budget
•	Warns if you've exceeded your limit
 5. Exit
Closes the application
________________________________________
 File Structure
 Project Folder
│
├── MONEY MANAGEMENT SYSTEM.py
└── expenses.csv   # auto-generated
________________________________________
 Notes & Limitations
•	No editing or deleting previous expenses
•	User input must be numeric for amounts and budget
•	No category validation—free text allowed
________________________________________
 Future Enhancements (Optional Ideas)
•	Monthly expense reports
•	Category-wise spending summary
•	Data visualization with charts
•	GUI or web interface
•	Export to PDF or Excel


