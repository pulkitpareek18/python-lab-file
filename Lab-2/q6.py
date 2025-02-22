# Write a python program to print fibonacci series upto n terms.

def fibonacci(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter no. of fibonacci terms: "))
for i in range(n):
    print(fibonacci(i))

# Output:
# Enter no. of fibonacci terms: 10
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34