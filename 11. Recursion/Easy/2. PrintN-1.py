#Print N to 1 using resursion

def PrintN1(n):
    if(n == 1):
        print(n)
        return

    print(n)
    PrintN1(n-1)


PrintN1(10)