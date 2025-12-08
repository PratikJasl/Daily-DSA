# A number that has exactly 2 factors 1 and itself is called a Prime.
# Objective: check if a number is prime or not.
# input: 2 
# Output: True

def CheckPrime(N):
    count = 0
    for i in range (1, N+1):
        if(N % i == 0):
            count += 1
    if(count > 2):
        return False
    else:
        return True
    
print(CheckPrime(10))
