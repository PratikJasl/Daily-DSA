#Q: Write a function to reverse a string using recursion.

#Approach1: Two pointer with recursion
#Step1: Create two pointers left and right
#Step2: While left < right
#Step3: Swap left and right in the list
#Step4: Decrement left, increment right and call function
#Step5: In python string is immutable so we will convert it into a list and then back to string
def ReverseString(str, left, right):
    if(left < right):
        str[left], str[right] = str[right], str[left]
        ReverseString(str, left + 1, right - 1)
    else:
        return

str = "Geeks for Geeks"
str_list = list(str)  # Convert string to list
ReverseString(str_list, 0, len(str_list) - 1)
result = ''.join(str_list)  # Convert list back to string
print(result)


#Approach2:
#Step1: Slice from the 1st index and add last to front.
#Step2: keep doing this 
def ReverseStr(str):
    if(len(str) == 0):
        return str
    return ReverseStr(str[1:]) + str[0]

print(ReverseStr("Hello"))