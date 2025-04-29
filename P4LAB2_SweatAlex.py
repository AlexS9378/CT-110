def show_multiplication_table(number):
    for i in range(1, 13): 
        print(f"{number} x {i} = {number * i}")
    print()


run_again = "yes"
while run_again.lower() == "yes":
    try:
        user_input = int(input("Enter an integer: "))
        if user_input >= 0:
            show_multiplication_table(user_input)
        else:
            print("This program cannot handle negative numbers.\n")
    except ValueError:
        print("Enter a valid integer.\n")
    
    run_again = input("Do you want to run the program again?: ")

print("Exiting program...")
