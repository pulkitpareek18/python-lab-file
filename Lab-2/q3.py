# Write a python program to print all the prime numbers between 1 and 100.

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True


for i in range(1, 101):
    if check_prime(i):
        print(i)
        
# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97