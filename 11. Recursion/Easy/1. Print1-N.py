#Q2: Print numbers from 1 to N without using loops.
def Print1N(n):
    if(n <= 1):
        print(n)
        return
    Print1N(n-1)
    print(n)

Print1N(10)