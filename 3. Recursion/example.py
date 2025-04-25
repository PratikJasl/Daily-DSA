# Example1: Print Names Five Times.
def Names(count):
    if count > 5:
        return
    print("Pratik \^^/ Pratiksha")
    Names(count+1)
Names(1)

# Example2: Print Linearly from 1 to N.
def Linear(M):
    global count1
    if(count1 > M):
        return
    print(count1)
    count1 += 1
    Linear(M)
Linear(10)

#Example3: Print from N to 1.
def Decrement(N):
    if(N < 1):
        return
    print(N)
    N -= 1
    Decrement(N)
Decrement(10)

