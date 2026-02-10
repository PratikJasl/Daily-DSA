# 3. Longest Substring without Repeating Characters

6 #Approach: O(n) Variable Size Window
7 #Step1: Create a Set, a maxCount and a left and right pointer variable.
8 #Step2: Iterate through the string till right is less than length.
9 #Step3: If element does not exist in set add it to set and increment right and count.
10 #Step4: If element does not exist delete the first element, and increment

def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    seen = set()
    max_count = 0
    left = 0
    right = 0

    while(right < n):
        if s[right] not in seen:
            seen.add(s[right])
            right += 1
            max_count = max(max_count, len(seen))
        else:
            seen.remove(s[left])
            left += 1
    
    return max_count