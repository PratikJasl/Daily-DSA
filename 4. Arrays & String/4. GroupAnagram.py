# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = {}

    for s in strs:
        sorted_key = "".join(sorted(s))

        anagram_map[sorted_key].append(s)
    
    print(anagram_map)
        
    return list(anagram_map.values())

groupAnagrams(["eat","tea","tan","ate","nat","bat"])