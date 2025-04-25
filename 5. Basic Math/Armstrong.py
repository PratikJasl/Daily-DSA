# Armstrong Number: Any number whose individual digits square adds up to that number.
# Objective: To check if a number is armstrong or not.

# Input: 371 = 3^3 + 7^3 + 1^3 == 371
# Output: true

def CheckArmstrong(N):
    n = N
    sum = 0
    while(N > 0):
        lastDigit = N % 10
        sum += lastDigit*lastDigit*lastDigit
        N = int(N/10)
        
    print(sum == n)
    return sum == n

CheckArmstrong(371)