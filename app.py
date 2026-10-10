
HISTORY_FILE = "history.txt"


def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No history found!")


def clear_history():
    with open(HISTORY_FILE, "w") as file:
        pass
    print("History cleared!")


def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")


def calculation(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid syntax! Example: 10 + 2")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid number!")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 / num2
    elif op == "%":
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 % num2
    elif op == "**":
        result = num1 ** num2
    elif op == "//":
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 // num2
    else:
        print("Invalid operator!")
        return

    print("Result:", int(result))
    save_to_history(user_input, result)


def main():
    while True:
        user_input = input(
            "Enter calculation or command "
            "(history, clear, exit): "
        ).strip().lower()

        if user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            calculation(user_input)


if __name__ == "__main__":
    main()
