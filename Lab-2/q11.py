# Write a python program to check whether a number is present in the list or not. If number is present print the position of that number.

lst = [1, 2, 3, 4, 5]
num = 4

if num in lst:
    print(f"{num} is present at position {lst.index(num)}.")
else:
    print(f"{num} is not present in the list.")
    
# Output:
# 4 is present at position 3.