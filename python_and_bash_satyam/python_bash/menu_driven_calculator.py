
# Menu-Driven Calculator
# Supports addition, subtraction, multiplication, and division


# 1. Function for addition
def add(a, b):
    return a + b


# 2. Function for subtraction
def subtract(a, b):
    return a - b


# 3. Function for multiplication
def multiply(a, b):
    return a * b


# 4. Function for division
def divide(a, b):
    # Check whether the second number is zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")

    return a / b


# Main program: keep displaying the menu until the user exits
while True:

    # Display calculator menu
    print("\n===== MENU-DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-5): ").strip()

    # Exit the program
    if choice == "5":
        print("Thank you for using the calculator!")
        break

    # Check whether the choice is valid
    elif choice in ("1", "2", "3", "4"):

        # Get two numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == "1":
                result = add(num1, num2)
                print("Result:", result)

            elif choice == "2":
                result = subtract(num1, num2)
                print("Result:", result)

            elif choice == "3":
                result = multiply(num1, num2)
                print("Result:", result)

            elif choice == "4":
                result = divide(num1, num2)
                print("Result:", result)

        # Handle division by zero
        except ZeroDivisionError as error:
            print("Error:", error)

        # Handle non-numeric input
        except ValueError:
            print("Error: Please enter valid numbers.")

    # Handle an invalid menu choice
    else:
        print("Invalid choice! Please select an option from 1 to 5.")