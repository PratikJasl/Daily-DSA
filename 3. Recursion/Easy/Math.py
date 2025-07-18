#Q: Write a function to find the factorial of a number.

#Approach: Parameterized Recursion
#Step1: Take an input N.
#Step2: Base condition-> Check N == 0
#Step3: Multiply and reduce n.
result = 1
def Fact(N):
    global result
    if(N == 0):
        return 1
    result *= N
    Fact(N-1)

Fact(5)
print(result)

#Approach: Functional Recursion
def Factorial(N):
    if(N == 0):
        return 1
    return N * Factorial(N-1)

print(Factorial(5))