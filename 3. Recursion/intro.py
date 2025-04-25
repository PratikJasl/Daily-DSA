# Recursion: When a function calls itself again and again, until a specified condition is met.

# Base Condition: The condition 



# Example2: Infinite recursion code

def PrintCount():
    print(1)
    PrintCount()

PrintCount()

# Example: Finite recursion code.
global count
count = 0

def Print1():
    global count
    if count == 5 : #Base Condition
        return
    print(1)
    count += 1
    Print1()

Print1()
