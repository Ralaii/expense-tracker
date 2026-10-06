# Project: Expense Tracker
# Installment 3: The Tracker Does Math
# Author: Jeus Leroy L. Armentano
# Description: Displays the landing page, greets the user by name, logs two
#              expenses, then computes the subtotal, average, tax, grand
#              total, and budget status, and prints a summary.
programmerName = "Jeus Leroy L. Armentano"

print("=" * 40)
print(" " * 12 + "EXPENSE TRACKER")
print(" " * 8 + "Know where your money goes.")
print("=" * 40)
print("\nMAIN MENU")
print(" " * 2 + "[1] Add an expense".ljust(30) + "(coming soon)")
print(" " * 2 + "[2] View all expenses".ljust(30) + "(coming soon)")
print(" " * 2 + "[3] Show total spent".ljust(30) + "(coming soon)")
print(" " * 2 + "[4] Exit".ljust(30) + "(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1:.2f}")
print(f"  - {item2}:\t${amount2:.2f}")
print(f"Subtotal:\t${subtotal:.2f}")
print(f"Average:\t${average:.2f}")
print(f"Tax ({tax_percent}%):\t${tax:.2f}")
print(f"Grand total:\t${total:.2f}")
print(f"Over budget?:\t{over_budget}")
print(f"Left in budget:\t${left:.2f}")
print("-" * 40)
print(f"Made by: {programmerName}  |  Installment 3")