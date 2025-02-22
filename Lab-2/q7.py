# Write a python program to check whether a number is palindrome or not.

num = int(input("Enter a number: "))
num_copy = num
reverse = 0

while num_copy > 0:
    remainder = num_copy % 10
    reverse = reverse * 10 + remainder
    num_copy = num_copy // 10

if num == reverse:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
    
# Output:
# Enter a number: 121
# 121 is a palindrome number.