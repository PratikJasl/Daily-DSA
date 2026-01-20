# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Brute Force: T: O(nlogn) | S: O(1)
# Step1: Convert string to array of character.
# Step2: Sort the arrays.
# Step3: Check if array elements are same.

def isAnagram(s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    
    sorted_s = list(s)
    sorted_t = list(t)
    sorted_s.sort()
    sorted_t.sort()

    for i in range(len(sorted_s)):
        if(sorted_s[i] != sorted_t[i]):
            return False
    
    return True

# Optimal Approach: T: O(n) | S: O(n)
# Step1: Create frequency map of both strings.
# Step2: Compare both the frequency maps. (The comparison only works for dict and set since they are unordered)
def isAnagram(s: str, t: str) -> bool:
    if(len(s) != len(t)):
        return False
        
    trackS = {}
    trackT = {}

    for i in range(len(s)):
        if s[i] in trackS:
            trackS[s[i]] += 1
        else:
            trackS[s[i]] = 1
    
    for i in range(len(t)):
        if t[i] in trackT:
            trackT[t[i]] += 1
        else:
            trackT[t[i]] = 1

    return trackS == trackT