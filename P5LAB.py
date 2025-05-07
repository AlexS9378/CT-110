# Alex Sweat
# 5/7/2025
# P5LAB
# This program will simulate a customer using a self-checkout machine. A random float value will be generated as the total owed for the purchase. The user should be prompted to enter the amount of money they will put into the self-checkout machine (as a float). The program should then display the amount of dollars, quarters, dimes, nickels, and pennies required to make the change

import random

def disperse_change(amount):
    # Convert dollars to cents
    cents = int(round(amount * 100))

    coins = [
        ("dollar", 100),
        ("quarter", 25),
        ("dime", 10),
        ("nickel", 5),
        ("penny", 1)
    ]

    for coin_name, coin_value in coins:
        count = cents // coin_value
        cents = cents % coin_value

        if count > 0:
            # Handle pluralization and formatting
            if coin_name == "penny":
                name = "penny" if count == 1 else "pennies"
            else:
                name = coin_name if count == 1 else coin_name + "s"
            print(f"{count} {name}")

def main():
    # Generate a random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    try:
        user_input = float(input("How much cash will you put in the self-checkout?: $"))
        if user_input == amount_owed:
            print("No change owed.")
        else:
            change = round(user_input - amount_owed, 2)
            print(f"Change owed: ${change:.2f}")
            print("Change breakdown:")
            disperse_change(change)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
main()
