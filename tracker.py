# Project: Expense Tracker
# Installment 2: Talking to the User
# Author: Jeus Leroy L. Armentano
# Description: Displays the landing page, greets the user by name, logs two
#              expenses, and prints a summary with the total and average.
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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"{f'  - {item1}:':<16}${amount1}")
print(f"{f'  - {item2}:':<16}${amount2}")
print(f"{'Total spent:':<16}${total}")
print(f"{'Average:':<16}${average}")
print("-" * 40)
print(f"Made by: {programmerName}  |  Installment 2")