#Q1: Print numbers from 1 to N without using loops.



#Q2: Print numbers from N to 1 without using loops.
def Print_1_N(n):
    if(n == 1):
        print(1)
        return 1
    print(n)
    Print_1_N(n-1)
    

Print_1_N(11)