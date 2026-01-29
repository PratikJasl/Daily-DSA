# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def GroupAnagram(strs: str) -> list[list[str]]:
    freq = {}
    for item in strs:
        sor = "".join(sorted(item)) #sorting and joining strings
        if sor in freq:
            freq[sor].append(item)
        else:
            freq[sor] = [item]
    
    print(list(freq.values()))
    return list(freq.values())

GroupAnagram(["eat","tea","tan","ate","nat","bat"])