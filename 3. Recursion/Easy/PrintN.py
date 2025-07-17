#Q1: Print numbers from 1 to N without using loops.
def Print_1_N(n, count = 1):
    if(count > n):
        return
    print('1_N:',count)
    Print_1_N(n, count + 1)

Print_1_N(5)


#Q2: Print numbers from N to 1 without using loops.
def Print_N_1(n):
    if(n == 0):
        return
    print('N_1:',n)
    Print_N_1(n-1)

Print_N_1(5)