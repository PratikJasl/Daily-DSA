#Extract digits from a number.
num = 2598

def extractdigit(N):
    while(N > 0):
        lastDigit = N % 10
        print(lastDigit)
        N = int(N/10)

#Reverse a number: 2598
def reverseNum(N):
    sum = 0
    while(N > 0):
        lastDigit = N % 10
        sum = (sum * 10) + lastDigit
        N = int(N/10)
    print(sum)

#Armstrong number: 371
def armstrongNum(N):
    n = N
    sum = 0
    while(N > 0):
        lastDigit = N % 10
        sum += (lastDigit*lastDigit*lastDigit)
        N = int(N/10)
    return (sum == n)

print(armstrongNum(375))