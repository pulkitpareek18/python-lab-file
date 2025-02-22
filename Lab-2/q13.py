# Write a python program that displays options for inserting or deleting elements in a list. If user choses a deletion option, display a submenu and ask if element is to be deleted by value or by position or a list slice is to be deleted.

lst = [1,2,3]

def insert():
    n = int(input("Enter the number of elements to insert: "))
    for i in range(n):
        ele = int(input("Enter element: "))
        lst.append(ele)
    
def delete_at_index():
    n = int(input("Enter the index to delete: "))
    lst.pop(n)    
        
def delete_by_value():
    n = int(input("Enter the element to delete: "))
    lst.remove(n)
    
def delete_by_slice():
    n = int(input("Enter the start index of slice: "))
    m = int(input("Enter the end index of slice: "))
    del lst[n:m+1]   
     
def delete():
    print("Enter 1 to delete by value.")
    print("Enter 2 to delete by index.")
    print("Enter 3 to delete by slice.")
    choice = int(input())
    
    if choice == 1:
        delete_by_value()
    elif choice == 2:
        delete_at_index()
    elif choice == 3:
        delete_by_slice()
    
    print(lst)
    

print(lst)

choice = 0

while choice != -1:
    print("Enter 1 to insert element.")
    print("Enter 2 to delete element.")
    print("Enter 3 to display list.")
    print("Enter -1 to exit.")
    choice = int(input())
    
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        print(lst)
    elif choice == -1:
        print("Exiting...")
        break