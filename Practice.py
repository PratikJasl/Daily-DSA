# Group Anagram
strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(strs: list[str]) -> list[str]:
    seen = {}

    for s in strs:
        final_key= "".join(sorted(s))

        if final_key in seen:
            seen[final_key].append(s)
        else:
            seen[final_key] = [s]
    
    print("Group Anagram:", list(seen.values()))
    return(list(seen.values()))

groupAnagram(strs)