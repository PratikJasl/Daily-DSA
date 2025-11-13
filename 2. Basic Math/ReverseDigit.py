#Objective: Reverse a digit, if it has 0's in trailing digits those will not be included.
#Input: 1400 
#Output: 1400--> 0041 --> 41

#Concept: The extraction of digits concept extracts the digit in reverse order. We use it to extract digits 
# then multiple it with a base of 10 and add the next digits.


def ReverseNumber(N):
    Sum = 0
    while(N > 0):
        lastDigit = N % 10 
        N = int(N / 10)
        Sum = (Sum * 10) + lastDigit
    
    print(Sum)
    return Sum

ReverseNumber(1400)