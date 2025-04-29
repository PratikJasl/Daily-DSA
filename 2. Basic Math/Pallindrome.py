#Objective: Check if a number is pallindrome or not.

#Input: 121
#Output: true

#Concept: We already saw how to reverse a digit, compare the original and reversed digit

def IsPallindrome(N):
    original = N
    revNum = 0
    while(N > 0):
        lastDigit = N % 10
        N = int(N / 10)
        revNum = (revNum * 10) + lastDigit
    print(revNum == original)
    return revNum == original

IsPallindrome(122)