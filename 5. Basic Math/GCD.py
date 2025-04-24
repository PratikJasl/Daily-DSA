# Gretest Common Divisor

# Objective: find the GCD for 2 numbers.
# Input: N1 = 9 N2 = 12
# Output: 3

def GCD(n1, n2):
    output = 0
    if (n1 > n2): len = n1 
    else: len = n2
    for i in range (1, len+1):
        if(n1 % i ==0 and n2 % i == 0):
            output = i
    print(output)
    return output


GCD(20, 40)