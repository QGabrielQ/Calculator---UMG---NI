def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def show_menu():
    print("\nAdvanced Python Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show calculation history")
    print("0. Exit")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose operation: ")

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "5":
            print("\nCalculation history:")
            if not history:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)
                operation = f"{a} + {b} = {result}"
            elif choice == "2":
                result = subtract(a, b)
                operation = f"{a} - {b} = {result}"
            elif choice == "3":
                result = multiply(a, b)
                operation = f"{a} * {b} = {result}"
            elif choice == "4":
                result = divide(a, b)
                operation = f"{a} / {b} = {result}"
            else:
                print("Invalid option.")
                continue

            history.append(operation)
            print("Result:", result)

        except ValueError:
            print("Error: please enter valid numbers.")
        except ZeroDivisionError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
