# Python CLI Calculator

A command-line calculator built with Python that performs basic and advanced arithmetic operations, saves calculation history, and allows users to view or clear previous results.

## Features

- Perform calculations directly in the terminal
- Support for addition, subtraction, multiplication, and division
- Modulus, exponentiation, and floor division operations
- Save calculations automatically to a history file
- View previous calculations in reverse chronological order
- Clear saved calculation history
- Exit the application using a simple command
- Handle invalid input and division by zero

## Supported Operations

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | `10 + 2` |
| `-` | Subtraction | `10 - 2` |
| `*` | Multiplication | `10 * 2` |
| `/` | Division | `10 / 2` |
| `%` | Modulus | `10 % 3` |
| `**` | Exponentiation | `2 ** 3` |
| `//` | Floor Division | `10 // 3` |

## Technologies Used

- Python
- File Handling
- Functions
- Conditional Statements
- Loops
- Exception Handling

## Project Structure

```text
calculator-app/
├── main.py
├── history.txt
└── README.md
```

`history.txt` is created automatically when the first successful calculation is saved.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/codebyimran-projects/calculator-app.git
```

### 2. Navigate to the Project Folder

```bash
cd calculator-app
```

### 3. Run the Calculator

```bash
python main.py
```

## Example Usage

```text
Enter calculation or command (history, clear, exit): 10 + 2
Result: 12.0

Enter calculation or command (history, clear, exit): 5 * 4
Result: 20.0

Enter calculation or command (history, clear, exit): history
5 * 4 = 20.0
10 + 2 = 12.0

Enter calculation or command (history, clear, exit): exit
Goodbye!
```

## Available Commands

| Command | Description |
|---|---|
| `history` | Display previous calculations |
| `clear` | Clear saved calculation history |
| `exit` | Close the calculator |

## Learning Objectives

This project demonstrates practical use of Python fundamentals, including functions, loops, conditional logic, exception handling, user input, and file operations.

## Author

**Muhammad Imran**

- Website: [codebyimran.com](https://codebyimran.com)
