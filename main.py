#!/usr/bin/env python3
"""A simple calculator program with fraction support."""

from fractions import Fraction


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def parse_number(input_str):
    """Parse input as either a fraction or float."""
    try:
        if "/" in input_str:
            return Fraction(input_str)
        else:
            return Fraction(float(input_str)).limit_denominator()
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid number format")


def calculator():
    """Main calculator function."""
    print("Simple Calculator with Fraction Support")
    print("-" * 40)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-" * 40)
    print("Enter numbers as decimals (e.g., 2.5) or fractions (e.g., 1/2)")
    print("-" * 40)

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = parse_number(input("Enter first number: "))
                num2 = parse_number(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
            except ValueError as e:
                print(f"Invalid input. {e}")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    calculator()
