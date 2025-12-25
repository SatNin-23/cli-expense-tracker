import csv
import os
from tabulate import tabulate

# Check if the CSV file already exists
# If it does NOT exist, create it and add the header row
if not os.path.exists("expenses.csv"):
    with open("expenses.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item', 'Category', 'Price', 'Date'])


# This function takes input from the user for one expense
# and returns it as a list
def get_expense():
    item = input("Enter Item name: ")
    category = input("Enter item Category: ")
    price = float(input("Enter item Price: "))  # converted to float for calculations
    date = input("Enter date: ")

    expense_list = [item, category, price, date]
    return expense_list


# This function writes a single expense row to the CSV file
def write_expense(expense):
    with open("expenses.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)


# This function allows the user to add multiple expenses
# until they choose to stop
def add_expense():
    keep_going = True

    while keep_going:
        expense = get_expense()     # get expense details from user
        write_expense(expense)     # save expense to CSV file

        more = input("Do you want to keep adding? Y/N ")

        # Continue only if user enters Y or Yes
        if more == "Yes" or more == "Y":
            continue
        else:
            break


# This function reads all expenses from the CSV file
# and displays them in a formatted table using tabulate
def show_expenses():
    with open("expenses.csv", "r", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        table = list(reader)  # convert CSV data into a list

        # table[0] contains headers
        # table[1:] contains the actual expense data
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


# Main function that displays the menu and controls program flow
def main():
    while True:
        print("Expense Tracker Menu")
        print("1. Add Expenses")
        print("2. Show Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            print("Menu Exited")
            break

        else:
            print("Invalid choice. Try again.")


# Start the program
main()
