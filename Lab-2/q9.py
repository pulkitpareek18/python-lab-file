# Write a python program to compare two equal size lists and print the first index where they differ.

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 6]

for i in range(len(list1)):
    if list1[i] != list2[i]:
        print(f"Lists differ at index {i}.")
        break
else:
    print("Lists are equal.")

# Output:
# Lists differ at index 4.