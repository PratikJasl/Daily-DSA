# # Example1: Print Names Five Times.
# def Names(count):
#     if count > 5:
#         return
#     print("Pratik \^^/ Pratiksha")
#     Names(count+1)
# Names(1)

# # Example2: Print Linearly from 1 to N.
# def Linear(M):
#     global count1
#     if(count1 > M):
#         return
#     print(count1)
#     count1 += 1
#     Linear(M)
# Linear(10)

# #Example3: Print from N to 1.
# def Decrement(N):
#     if(N < 1):
#         return
#     print(N)
#     N -= 1
#     Decrement(N)
# Decrement(10)

# #Example4: Sum of N Numbers.
# #Add(5) --> 5+Add(4) --> 4+Add(3) --> 3+Add(2) --> 2+Add(1) --> 1+Add(0)                                              
# def Add(N):
#     if(N == 0):
#         return 0
#     return N + Add(N-1)
# print(Add(5))

# #Sum of N Numbers using Backtracking.
# #Sum(5) --> Sum(4) --> Sum(3) --> Sum(2) --> Sum(1)
# #Sum(1, 5) --> Sum(2, 5) --> Sum(3, 5) --> Sum(4, 5) --> Sum(5, 5)
# global sum
# Sum = 0
# def BackAdd(i, N):
#     global Sum
#     if(i > N):
#         return
#     BackAdd(i+1, N)
#     Sum += i 
#     print(Sum)
# BackAdd(1, 5)

# #Example5: Factorial Of N numbers: 5*4*3*2*1
# #Using functional Recursion.
# # 5*Fact(4) --> 4*Fact(3) --> 3*Fact(2) --> 2*Fact(1) -->1*Fact(0)
# def Fact(N):
#     if(N==0):
#         return 1
#     return N * Fact(N-1)
# print('Factorial is:', Fact(5))

# #Factorial of N numbers using While loop.
# global fact
# fact = 1
# def Fact1(N):
#     global fact
#     while(N > 0):
#         fact *= N
#         N -= 1
#     return fact
# print("The factorial is:", Fact1(5))

# #Example6: Reverse an array using recursion.
# # [1,2,3,4,5] --> [5,4,3,2,1]
# global arr
# arr = [1,2,3,4,5]
# def ReverseArr(start, end):
#     if(start == end):
#         return
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp
#     ReverseArr(start+1, end-1)
# ReverseArr(0, len(arr)-1)
# print('reversed array is:', arr)

# #Example7: Check if a string is pallindrome or not.
# # check(0, 3) --> check(1,2) -->check(1,1)
# global str
# str = "MADA"
# def checkPallindrome(start, end):
#     if(start >= end):
#         return True
#     if(str[start] != str[end]):
#         return False
#     return checkPallindrome(start+1, end-1)
# print("Pallindrome Check:", checkPallindrome(0, len(str)-1))

##Example8: Fibonnaci Number: Its the sum of i + (1+1)
#0,1 --> 1 --> 2 --> 3 --> 5 --> 8
# F(5) --> F(4) + F(3) --> F(3) + F(2) + F(2) + F(1) --> F(2) + F(1) + F(1) + F(0)
# --> F(1) + F(0) + F(0) + F(0) --> F(0) + F(0) + F(0) + F(0)
# --> F(0) + F(0) + F(0) + F(0) --> 0+1+1+2+3+5 = 8
# def Fibonacci(N):
#     if(N <= 1):
#         return N
#     return Fibonacci(N-1) + Fibonacci(N-2)
# print("Fibonacci Number is:", Fibonacci(5))

##Fibonacci without recursion.
def Fibonacci(N):
    for i in range(N, -1, -1):
        print((i-1) + (i-2))
        return (i-1) + (i-2)
    
print(Fibonacci(4))