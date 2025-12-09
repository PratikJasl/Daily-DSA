#Objective: Find all the divisors of a number.
# Input: 36 
# Output: divisors--> 1,2,3,4,6,9,12,18,36

def AllDivisors(N):
    divisors = []
    for i in range(1, N+1):
        if(N % i == 0):
            divisors.append(i)
    print(divisors)
    return divisors

AllDivisors(52)