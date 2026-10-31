# Project: Expense Tracker
# Installment 5: The Menu Comes Alive
# Author: Jeus Leroy L. Armentano
# Description: Displays the banner once, asks for the name, tax rate and
#              budget once, then keeps showing the main menu until the user
#              chooses Exit. Logs expenses with size messages, shows a
#              summary with a budget verdict, and says goodbye.
programmerName = "Jeus Leroy L. Armentano"

print("=" * 40)
print(" " * 12 + "EXPENSE TRACKER")
print(" " * 8 + "Know where your money goes.")
print("=" * 40)

name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate? "))
budget = float(input("Budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print(" " * 2 + "[1] Add an expense")
    print(" " * 2 + "[2] View all expenses".ljust(30) + "(coming soon)")
    print(" " * 2 + "[3] Show total spent")
    print(" " * 2 + "[4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total
        print("-" * 40)
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal:.2f}")
        print(f"Tax ({tax_percent}%):\t${tax:.2f}")
        print(f"Grand total:\t${total:.2f}")
        if over_budget:
            print(f"Over budget by ${total - budget:.2f}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${left:.2f} left.")
        else:
            print(f"Within budget. ${left:.2f} left.")
        print("-" * 40)
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print(f"Made by: {programmerName}  |  Installment 5")