#!/usr/bin/env python3

expenses = []
settings = {"budget": 5000.0}
CATEGORIES = ["food", "transport", "shopping", "bills", "other"]

# --- Inputs ---

## To get a name of item.

def get_item_name(prompt="Item name: "):
    while True:
        name = input(prompt).strip()
        if name == "":
            print("Error: item name cannot be empty.")
        else:
            return name

## To match and store correct category of item.

def get_category():
    while True:
        options = ", ".join(CATEGORIES)
        print(f"Categories: {options}")
        category = input("Category: ").strip().lower()
        if category in CATEGORIES:
            return category
        else:
            print(f"Error: '{category}' is not a valid category.")

## To get a NUMBER of price, budget.

def get_amount(prompt):
    while True:
        text = input(prompt)
        try:
            amount = float(text)
        except ValueError:
            print("Error: please type a number, e.g. 120 or 45.50")
            continue
        amount = round(amount, 2)
        if amount > 0 and amount <= 1000000:
            return amount
        else:
            print("Error: amount must be more than 0 and at most 1,000,000.")

## To choose expense.

def choose_expense():
    if len(expenses) == 0:
        print("No expenses yet.")
        return -1
    view_expenses()
    text = input("Expense number: ").strip()
    if not text.isdecimal():
        print("Error: please type a number from the list.")
        return -1
    number = int(text)
    if number < 1 or number > len(expenses):
        print(f"Error: expense #{number} does not exist.")
        return -1
    return number - 1

# --- Data Process ---

## To calculate total expense.

def calculate_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return round(total, 2)

## To check if it is still within the budget.

def confirm_if_over_budget(extra):
    new_total = round(calculate_total() + extra, 2)
    if extra > 0 and new_total > settings["budget"]:
        over = new_total - settings["budget"]
        print(f"Warning: this puts you {over:.2f} THB over your budget!")
        answer = input("Save anyway? (y/n): ").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        else:
            print("Cancelled. Nothing was saved.")
            return False
    return True

## To check total expense of each category.

def total_by_category():
    totals = {}
    for category in CATEGORIES:
        totals[category] = 0
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals[category] + expense["amount"]
    return round(total, 2)

## To see what is the biggest expense.

def find_biggest():
    if len(expenses) == 0:
        return None
    biggest = expenses[0]
    for expense in expenses:
        if expense["amount"] > biggest["amount"]:
            biggest = expense
    return biggest

# --- Menu Actions ---

## 1. Add Expense

def add_expense():
    name = get_item_name()
    category = get_category()
    amount = get_amount("Amount (THB): ")
    if confirm_if_over_budget(amount):
        expense = {"item": name, "category": category, "amount": amount}
        expenses.append(expense)
        print("Expense added!")

## 2. View Expense

def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print(f"\n{'#':<3} {'Item':<20} {'Category':<12} {'Amount':>10}")
    number = 1
    for expense in expenses:
        print(f"{number:<3} {expense['item']:<20} {expense['category']:<12} "
              f"{expense['amount']:>10.2f}")
        number += 1

## 3. Update Expense

def update_expense():
    index = choose_expense()
    if index == -1:
        return
    old = expenses[index]
    print(f"Updating: {old['item']} ({old['category']}) {old['amount']:.2f}")
    name = get_item_name("New item name: ")
    category = get_category()
    amount = get_amount("New amount (THB): ")
    if confirm_if_over_budget(amount - old["amount"]):
        expenses[index] = {"item": name, "category": category, "amount": amount}
        print("Expense updated.")

## 4. Delete Expense

def delete_expense():
    index = choose_expense()
    if index == -1:
        return
    removed = expenses.pop(index)
    print(f"Deleted: {removed['item']}")

## 5. Summary

def show_summary():
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    total = calculate_total()
    totals = total_by_category()
    budget = settings["budget"]

    print("--- Spending by category ---")
    for category in CATEGORIES:
        if totals[category] > 0:
            percent = round(totals[category] / total * 100)
            print(f"{category}: {totals[category]:.2f} THB ({percent}% of total)")

    biggest = find_biggest()
    print(f"Biggest expense: {biggest['item']} ({biggest['amount']:.2f} THB)")
    print(f"Total spent: {total:.2f} / {budget:.2f} THB")

    if total > budget:
        print("Status: OVER BUDGET")
    elif total >= budget * 0.8:
        print("Status: Careful, you have used 80% or more of your budget")
    else:
        print(f"Status: OK, {budget - total:.2f} THB left")

## 6. Set Budget

def set_budget():
    print(f"Current budget: {settings['budget']:.2f} THB")
    settings["budget"] = get_amount("New monthly budget (THB): ")
    print("Budget updated.")

# --- Main Menu ---

def show_menu():
    print("\n======================================")
    print("\n\\( ^o^)/   Hi! What can I do for you?")
    print("\n-------------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Summary")
    print("6. Set Budget")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Pick your number: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            set_budget()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice :( Please type a number from 1 to 7.")

try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nGoodbye!")