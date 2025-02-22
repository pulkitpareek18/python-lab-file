# Write a python program to check whether a number is even or odd.

# Function to check whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Input
num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}")

# Output
# Enter a number: 5
# 5 is Odd