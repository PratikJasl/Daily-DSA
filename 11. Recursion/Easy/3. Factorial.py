# Write a recursion function to calculate the factorial

def Factorial(n):
    if(n <= 1):
        return 1
    return n * Factorial(n-1)
   