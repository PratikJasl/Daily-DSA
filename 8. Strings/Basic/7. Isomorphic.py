# Given two strings s and t, determine if they are isomorphic.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

#Approach: Using Hash Maps: O(n)
#Step1: Check the length of two strings if not equal return false
#Step2: Loop through both the strings.
#Step3: If element not present in the map add it with count.
#Step4: Check count of appearnce of both character if equal return true, else false.

# def checkIsomorphic(str1, str2):
#     if (len(str1) != len(str2)):
#         return False
    
#     hashMap1 = {}
#     hashMap2 = {}
#     count = 0

#     #Create Hash Map.
#     for i in range(len(str1)):
#         if str1[i] not in hashMap1:
#             hashMap1[str1[i]] = count+1
#         else:
#             hashMap1[str1[i]] = hashMap1[str1[i]] + 1

#         if str2[i] not in hashMap2:
#             hashMap2[str2[i]] = count+1
#         else:
#             hashMap2[str2[i]] = hashMap2[str2[i]] + 1
#     print(hashMap1, hashMap2)
#     #Check if count is eqaul for both strings.
#     for i in range(len(str1)):
#         print(hashMap1[str1[i]] , hashMap2[str2[i]])
#         if hashMap1[str1[i]] != hashMap2[str2[i]]:
#             return False
        
#     return True


#Optimal: Time: O(n) Space: O(n)
#Step1: Check the length of two strings if not equal return false
#Step2: Loop through one string.
#Step3: If element and value is not present in the map, add them. Ex: a -> e
#Step4: If either the element or value is already mapped, return false.

def CheckIsomorphic(s, t):
    if (len(s) != len(t)):
            return False

    hashMap = {}

    #Create Hash Map.
    for i in range(len(s)):
        if s[i] not in hashMap:
            if t[i] in hashMap.values():
                return False
            hashMap[s[i]] = t[i]
        elif(hashMap[s[i]] != t[i]):
            return False
    
    return True

print(CheckIsomorphic("foo", "bar"))