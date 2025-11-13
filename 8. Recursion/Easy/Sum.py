#Q: Write a program to find the sum of first N natural numbers.

#Parameterised resurssion
sum = 0
def SumN(n):
    global sum
    if(n == 0):
        return
    sum += n
    SumN(n-1)

SumN(6)
print('Sum of N natural no is:', sum)

#Functional Recursion
sum2 = 0
def sumN2(n):
    global sum2
    if(n == 0):
        return 'Sum of N natural no is', sum
    sum2 += n
    return sumN2(n-1)

result = sumN2(6)
print(result)