# Given an input string s, reverse the order of the words.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

#Approach:
#Step1: Slpit the string into an array where-ever there is a space. Doing this we identfy today words.
#Step2: Reverse the array.
#Step3: Join the array back with spaces.


def ReverseWords(str):
    temp = str.strip(" ")
    string = ""
    count = 0
    for i in temp:
        if temp[i] != " ":
            string = string + temp[i]
            count = 0
        elif temp[i] == " " & count < 2:
            count += 1
            string = string + temp[i]
    print(string)



    


print(ReverseWords(" the sky is blue "))