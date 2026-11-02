import sqlite3
from datetime import datetime
from database import create_database
create_database()
def add_expense():
    try:
        amount = float(input("Enter amount:"))
        category = input("Enter category:")
        date = input("Enter date (YYYY-MM-DD):")
        description = input("Enter description:")

        datetime.strptime(date, '%Y-%m-%d')
        conn = sqlite3.connect('expense.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO expense (amount, category, date, description)
        values (?, ?, ?, ?)""", (amount, category, date, description))
        conn.commit()
        conn.close()
        print("Expense added successfully!")

    except ValueError:
        print("invalid input!")

def view_expense():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expense")
    expense = cursor.fetchall()
    conn.close()
    if not expense:
        print("No expense found.")
    else:
        for expense in expense:
            print(expense)

def search_expense():
    category = input("Enter category to search:")
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expense WHERE category = ?", (category,))
    expense = cursor.fetchall()
    conn.close()
    if not expense:
        print("No expense found.")
    else:
        for expense in expense:
            print(expense)

def update_expense():
    try:
        expense_id = int(input("Enter expense id:"))
        amount = float(input("Enter new amount:"))
        category = input("Enter new category:")
        date = input("Enter new date (YYYY-MM-DD):")
        description = input("Enter new description:")

        datetime.strptime(date, '%Y-%m-%d')
        conn = sqlite3.connect('expense.db')
        cursor = conn.cursor()

        cursor.execute("""UPDATE expense SET amount = ?, category = ?, date = ?, description = ?
        where id = ?""", (amount, category, date, description, expense_id))
        conn.commit()
        conn.close()

        print("Expense updated successfully!")
    except ValueError:
        print("invalid input!")

def delete_expense():
    try:
        expense_id = int(input("Enter expense id to delete:"))
        conn = sqlite3.connect('expense.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expense WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()
        print("Expense deleted successfully!")
    except ValueError:
        print("Please Enter a valid ID.")

def monthly_summary():
    month = input("Enter month (YYYY-MM):")
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expense WHERE date Like ?", (month + "%",))

    result = cursor.fetchone()
    conn.close()

    total = result[0]

    if total is None:
        total = 0

        print(f"Total expense for {month}: ₹{total:.2f}")

def category_summary():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()

    cursor.execute("SELECT category, SUM(amount) FROM expense GROUP BY category")
    result = cursor.fetchall()
    conn.close()

    if not result:
        print("No expense found.")
        return
    print("\nCategory-wise expense Summary")
    for category, total in result:
        print(f"{category}: ₹{total:.2f}")

def highest_expense():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expense ORDER BY amount DESC LIMIT 1")
    expense = cursor.fetchone()
    conn.close()

    if expense:
        print("\nHighest expense!")
        print(expense)
    else:
        print("No expense found.")



def main():
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expense")
        print("3. Search expense")
        print("4. Update expense")
        print("5. Delete expense")
        print("6. Monthly summary")
        print("7. category-wise summary")
        print("8. Highest expense")
        print("9. Exit")

        choice = (input("Enter your choice:"))
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            category_summary()
        elif choice == "8":
            highest_expense()

        elif choice == "9":
            print("Thank You for using EXPENSE TRACKER!")
            break

        else:
            print("Invalid choice.Please try again.")

if __name__ == "__main__":
 main()



