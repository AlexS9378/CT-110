# Alex Sweat
# 4/23/2025
# P3LAB
# Tests student's knowledge of how to write code that displays information to users

def calculate_change(amount):
    cents = int(round(amount * 100))

    coins = {
        "dollar": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

    result = []

    for coin_name, coin_value in coins.items():
        count = cents // coin_value
        cents -= count * coin_value

        if count == 1:
            result.append(f"1 {coin_name}")
        elif count > 1:
            result.append(f"{count} {coin_name}s")

    return "\n".join(result)


try:
    user_input = float(input("Enter an amount of money as a float: $"))
    if user_input < 0:
        print("Please enter a non-negative amount.")
    else:
        print(calculate_change(user_input))
    if user_input == 0:
        print("No change")
except ValueError:
    print("Invalid.")

