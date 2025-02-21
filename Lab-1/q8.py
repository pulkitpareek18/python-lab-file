# Write a python program to merge two tuples and remove duplicates.

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
t3 = t1 + t2
t4 = tuple(set(t3))
print("Merged tuple after removing duplicates is:", t4)

# Output:
# Merged tuple after removing duplicates is: (1, 2, 3, 4, 5, 6, 7, 8)