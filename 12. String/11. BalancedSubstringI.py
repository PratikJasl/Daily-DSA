# 3713: Longest Balanced Substring I

# Approach: Two Points: T: O(n^2) | S:O(26) -> O(1)
# Step1: Find all possible substrings.
# Step2: Create seen map with all substrings.
# Step3: The challenge here is seperating balanced substrings from the map.
# Step4: Create a set with all values of substring. (This is create a set with count of strings)
# Step5: Whenever the count of set is 1 meaninig only count of strings with same values. Update max_len

def longestBalanced(s: str) -> int:
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = {}
        for j in range(i, n):
            if s[j] not in seen:
                seen[s[j]] = 1
            else:
                seen[s[j]] += 1
            
            distinct_frequencies = set(seen.values())
            if len(distinct_frequencies) == 1:
                current_len = j - i + 1
                max_len = max(max_len, current_len)
                
    return max_len