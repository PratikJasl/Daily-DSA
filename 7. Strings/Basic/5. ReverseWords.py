# Given an input string s, reverse the order of the words.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

#Approach:
#Step1: Slpit the string into an array where-ever there is a space. Doing this we identfy today words.
#Step2: Reverse the array.
#Step3: Join the array back with spaces.


def ReverseWords(str):
    words = str.split()
    words.reverse()
    result = " ".join(words)
    return result



    


print(ReverseWords(" the sky is    blue "))