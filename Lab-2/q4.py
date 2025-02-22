# Write a python program to check whether a given number is prime or not.

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if check_prime(num):
    print(f"{num} is a prime number.")
    
# Output:
# Enter a number: 23
# 23 is a prime number.