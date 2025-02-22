# Write a python program to find factorial of a number n.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")

# Output:
# Enter a number: 5
# Factorial of 5 is 120