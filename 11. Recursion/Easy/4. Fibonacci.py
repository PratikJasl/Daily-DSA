# Write a recursive function to return Fibonacci of n.
# A Fibonacci number is the sum of preceeding two numbers.
# F(n) = F(n-1) + F(n-2)
# F(2) = F(1) + F(0) = 1 + 1
# F(0) is 1 and F(1) is 1

def fibonacci(n):
    if(n == 1):
        return 1
    if(n <= 0):
        return 0
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))