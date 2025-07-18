# #Q: Write a function to find the factorial of a number.

# #Approach: Parameterized Recursion
# #Step1: Take an input N.
# #Step2: Base condition-> Check N == 0
# #Step3: Multiply and reduce n.
# result = 1
# def Fact(N):
#     global result
#     if(N == 0):
#         return 1
#     result *= N
#     Fact(N-1)

# Fact(5)
# print(result)

# #Approach: Functional Recursion
# def Factorial(N):
#     if(N == 0):
#         return 1
#     return N * Factorial(N-1)

# print(Factorial(5))

#Example8: Fibonnaci Number: Its the sum of i + (1+1)
# 0,1 --> 1 --> 2 --> 3 --> 5 --> 8
# F(5) --> F(4) + F(3) --> F(3) + F(2) + F(2) + F(1) --> F(2) + F(1) + F(1) + F(0)
# --> F(1) + F(0) + F(0) + F(0) --> F(0) + F(0) + F(0) + F(0)
# --> F(0) + F(0) + F(0) + F(0) --> 0+1+1+2+3+5 = 8
def Fibonacci(N):
    if(N <= 1):
        return N
    return Fibonacci(N-1) + Fibonacci(N-2)
print("Fibonacci Number is:", Fibonacci(5))

##Fibonacci without recursion.
