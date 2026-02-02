
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Enter a different number than 0."

def power(x, y):
    return x ** y

def mod(x, y):
    if y == 0:
        return ("Error: Enter a different number than 0.")
    return x % y


if __name__ == "__main__":
    print(f"Add: {add(2, 3)}")
    print(f"Subtract: {subtract(5, 2)}")
    print(f"Multiply: {multiply(4, 3)}")
    print(f"Divide: {divide(10, 0)}")
    print(f"Power: {power(2, 3)}")
    print(f"Mod: {mod(10, 0)}")


