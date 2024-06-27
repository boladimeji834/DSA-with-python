# this program prints the fibonacci sequence of n numbers to the terminal
prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fibo in range(4):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 0
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# fibonacci(4)