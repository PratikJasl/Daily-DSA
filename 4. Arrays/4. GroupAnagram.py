# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs: list[str]) -> list[str]:
    seen = {}

    for s in strs:
        final_key= "".join(sorted(s))

        if final_key in seen:
            seen[final_key].append(s)
        else:
            seen[final_key] = [s]
    
    print("Group Anagram:", list(seen.values()))
    return(list(seen.values()))


groupAnagrams(["eat","tea","tan","ate","nat","bat"])