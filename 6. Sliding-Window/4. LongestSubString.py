# 3. Longest Substring without Repeating Characters

#Brute Force: O(n^2)
# Step1: Find all subarrays.
        # Step2: for every subarray maintain a set.
        # Step3: If element is new add it and update max lenght.
        # Step4: Else, clear the set.
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    maxlen = 0
    
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] not in seen:
                seen.add(s[j])
                maxlen = max(maxlen, len(seen))
            else:
                seen.clear()
    
    return maxlen


6 #Approach: O(n) Variable Size Window
7 #Step1: Create a Set, a maxCount and a left and right pointer variable.
8 #Step2: Iterate through the string till right is less than length.
9 #Step3: If element does not exist in set add it to set and increment right and count.
10 #Step4: If element does not exist delete the first element, and increment
def longestSubstring(s: str) -> int:
    if not s:
        return 0
    
    seen = set()
    max_count = 0
    left = 0 
    
    for right in range(len(s)):
        
        # Shrink the window from the left until the duplicate is gone.
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        seen.add(s[right])
        
        max_count = max(max_count, right - left + 1)
        
    return max_count

print(longestSubstring('pwwkew'))