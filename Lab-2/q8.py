# Write a python program to move all the duplicate values to the end of the list.

lst = [1, 1, 2, 3, 4, 3, 5]
unique = []
duplicate = []
for i in lst:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)

lst = unique + duplicate
print(lst)

# Output:
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]    