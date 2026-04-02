#Q1: Print numbers from 1 to N without using loops.
def Print_1_N(n):
    count = 1
    if(count == n):
        return

    count += 1
    Print_1_N(count)


#Q2: Print numbers from N to 1 without using loops.
