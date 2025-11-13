# Backtracking: When we write the execution logic after the function call, 
# the lines are executes after all the functions have returned.

# Function Tree: f(0,3) --> f(1,3) --> f(2,3) --> f(3,3) --> f(4, 3)
# f(5) --> f(4) --> f(3) --> f(2) --> f(1) --> f(0)

# Print from N to 1 using backtracking.
def PrintNto1(i, n):
    if(i > n):
        return 
    PrintNto1(i+1, n)
    print(i)

PrintNto1(1, 3)

def Print1ToN(i):
    if(i <= 0):
        return
    Print1ToN(i-1)
    print(i)

Print1ToN(5)
