#Q: Convert a given decimal to binary
#Appraoch: 
# step1: Module the decimal by 2
# step2: Add (10 * funCall(d//2))


def dec_to_bin(d):
    if(d == 0):
        return 0
    else:
        return (d % 2 + 10 * dec_to_bin(d//2))


d = 10
print(dec_to_bin(10))