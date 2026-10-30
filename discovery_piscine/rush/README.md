# Expense Tracker

## Purpose
A terminal app that helps you record daily spending, see where your money goes, and stay within a monthly budget.

## Main features
- Add, view, update and delete expenses (item, category, amount)
- Set a monthly budget (default 5,000 THB)
- Summary: total and % per category, biggest expense, total vs budget, budget status

## Business rules
1. Amount must be a number more than 0 and at most 1,000,000 THB (letters, zero and negatives are rejected)
2. Category must be one of: food, transport, shopping, bills, other
3. If adding or updating an expense pushes the total over budget, the app warns you and only saves it if you type `y` or `yes`

## Data processing
1. Total spent per category, with its % of total spending
2. Biggest single expense

---

# User Manual

## 1. Requirements
- Python 3 (the version announced for the Discovery Piscine)
- A terminal
- No extra libraries are needed

## 2. Starting the program

### Step 1: Check that Python 3 is installed
Open a terminal and type:

```
python3 --version
```

You should see something like `Python 3.x.x`. If you see `command not found`, install Python 3 first.

### Step 2: Get the project (skip if you already have it)

```
git clone <repository-url>
```

This creates a folder named `DPPy-pohongth` in the folder your terminal is currently in.

### Step 3: Go to the `rush` folder
The program is inside `DPPy-pohongth/discovery_piscine/rush`. First, check where you are:

```
pwd
```

`pwd` prints the folder your terminal is currently in. Then use the matching command:

| `pwd` ends with... | Command to type |
|---|---|
| `/rush` | Nothing, you are already in the right folder |
| `/discovery_piscine` | `cd rush` |
| `/DPPy-pohongth` | `cd discovery_piscine/rush` |
| Anything else (e.g. your home folder or Desktop) | `cd <path-to>/DPPy-pohongth/discovery_piscine/rush`, replacing `<path-to>` with where you saved the project |

For example, if you cloned the project onto your Desktop:

```
cd ~/Desktop/DPPy-pohongth/discovery_piscine/rush
```

Tip: if you are unsure, type `cd ` (with a space), then drag the `rush` folder from Finder or File Explorer into the terminal window and press **Enter**. The full path is filled in for you.

### Step 4: Check that you are in the right folder

```
ls
```

You should see these three files:

```
README.md  auteur  expense_tracker.py
```

If you do not see `expense_tracker.py`, you are in the wrong folder; go back to Step 3.

### Step 5: Run the program

```
python3 expense_tracker.py
```

If you see `No such file or directory`, the terminal is not in the `rush` folder; go back to Step 3.

The main menu appears:

```
======================================

\( ^o^)/   Hi! What can I do for you?

-------------------------------------
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Summary
6. Set Budget
7. Exit
Pick your number:
```

Type the number of an option and press **Enter**. After each action, the menu comes back until you choose **7. Exit**.

## 3. Menu options

### 1. Add Expense
Records a new expense. The program asks for three things:

| Question | What to type | Example |
|---|---|---|
| `Item name:` | Any text, cannot be empty | `Pad thai` |
| `Category:` | One of: food, transport, shopping, bills, other (capital letters are OK) | `food` |
| `Amount (THB):` | A number more than 0 and at most 1,000,000. Decimals are allowed | `60` or `45.50` |

If you type something invalid, the program shows an error and asks the same question again.

If this expense would push your total over the budget, you will see:

```
Warning: this puts you 90.00 THB over your budget!
Save anyway? (y/n):
```

Type `y` to save it anyway, or anything else to cancel.

### 2. View Expenses
Shows all expenses in a numbered table:

```
#   Item                 Category         Amount
1   Pad thai             food              60.00
2   Taxi                 transport        150.00
```

The number in the `#` column is the one you use to update or delete an expense.

### 3. Update Expense
Changes an existing expense.
1. The table of expenses is shown.
2. At `Expense number:`, type the `#` of the expense you want to change.
3. Type the new item name, category and amount (same rules as Add Expense).

The over-budget warning also applies here, based on the difference between the old and new amount.

### 4. Delete Expense
Removes an expense.
1. The table of expenses is shown.
2. At `Expense number:`, type the `#` of the expense you want to delete.

The program confirms with `Deleted: <item name>`.

### 5. Summary
Shows an overview of your spending:

```
--- Spending by category ---
food: 60.00 THB (29% of total)
transport: 150.00 THB (71% of total)
Biggest expense: Taxi (150.00 THB)
Total spent: 210.00 / 5000.00 THB
Status: OK, 4790.00 THB left
```

Only categories you have spent money in are listed. The status can be:

| Status | Meaning |
|---|---|
| `OK, ... THB left` | You have used less than 80% of your budget |
| `Careful, you have used 80% or more of your budget` | You are close to the limit |
| `OVER BUDGET` | You have spent more than your budget |

### 6. Set Budget
Shows your current budget and asks for a new one (same number rules as the amount). The default budget is **5,000 THB**.

### 7. Exit
Prints `Goodbye!` and closes the program. You can also press **Ctrl+C** or **Ctrl+D** at any time to exit safely.

## 4. Example session

```
Pick your number: 1
Item name: Pad thai
Categories: food, transport, shopping, bills, other
Category: food
Amount (THB): 60
Expense added!

Pick your number: 5
--- Spending by category ---
food: 60.00 THB (100% of total)
Biggest expense: Pad thai (60.00 THB)
Total spent: 60.00 / 5000.00 THB
Status: OK, 4940.00 THB left

Pick your number: 7
Goodbye!
```

(The menu is printed again between actions; it is left out here to keep the example short.)

## 5. Error messages

The program never crashes on bad input. It shows a message and lets you try again.

| Message | When it appears |
|---|---|
| `Invalid choice :( Please type a number from 1 to 7.` | The menu choice is not 1–7 |
| `Error: item name cannot be empty.` | You pressed Enter without typing a name |
| `Error: '...' is not a valid category.` | The category is not in the list |
| `Error: please type a number, e.g. 120 or 45.50` | The amount contains letters or symbols |
| `Error: amount must be more than 0 and at most 1,000,000.` | The amount is 0, negative, or too large |
| `No expenses yet.` | You chose View, Update, Delete or Summary before adding any expense |
| `Error: please type a number from the list.` | The expense number is not a number |
| `Error: expense #... does not exist.` | The expense number is not in the table |
| `Cancelled. Nothing was saved.` | You did not type `y` at the over-budget warning |

## 6. Good to know
- Data is kept only while the program is running. When you exit, all expenses are cleared.
- All amounts are in Thai Baht (THB) and shown with 2 decimal places.