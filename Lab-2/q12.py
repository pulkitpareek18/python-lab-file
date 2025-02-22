# Ask the user to enter a list with numbers between 0-9. Then replace all the entries in the list with 10 that are greater than 10.

lst = []
n = int(input("Enter the number of elements in the list: "))
print("Enter the elements of the list:")
for i in range(n):
    lst.append(int(input()))

lst = [10 if i > 7 else i for i in lst]
print(lst)

# Output:
# Enter the number of elements in the list: 5
# Enter the elements of the list:
# 1 5 7 8 9
# [1, 5, 7, 10, 10]
