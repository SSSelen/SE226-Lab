import math

#1. Problem
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

x = int(input("Please enter a number: "))


print(f"Answer is ", factorial(x))


#2. Problem
func = lambda n, x: ((-1) ** n) * ((x ** (2 * n + 1)) / factorial(2 * n + 1))
def sine_x(x, n):
    x = math.radians(x)
    sine_sum = 0
    for i in range(n):
        sine_sum += func(i, x)
    return sine_sum

x = float(input("Enter x(angle): "))
n = int(input("Enter n: "))
print(f"Answer is ", sine_x(x, n))

#3. Problem
total = 0
def harmonic_series(k):
    global total
    if k == 1:
        total += 1
    else:
        total += 1 / k
        harmonic_series(k - 1)

k = int(input("Enter k for harmonic: "))
harmonic_series(k)
print(f"Answer is ", total)
