import math_utils

def main():
    try:
        operator = input("Enter operator (+, -, *, /, **, %): ")
        x = float(input("Enter a number: "))
        y = float(input("Enter a number: "))

        if operator == "+":
            result = math_utils.add(x, y)
        elif operator == "-":
            result = math_utils.subtract(x, y)
        elif operator == "*":
            result = math_utils.multiply(x, y)
        elif operator == "/":
            result = math_utils.divide(x, y)
        elif operator == "**":
            result = math_utils.power(x, y)
        elif operator == "%":
            result = math_utils.mod(x, y)
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
