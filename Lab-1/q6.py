# Write a python program to find common element between two tuples.

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
common = tuple(set(t1) & set(t2))
print("Common elements between two tuples are:", common)

# Output:
# Common elements between two tuples are: (4, 5)