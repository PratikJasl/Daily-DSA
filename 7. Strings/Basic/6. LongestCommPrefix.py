# Write a function to find the longest common prefix string amongst an array of strings.

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#Brute Force: O(n^2)
#  step1: Loop thourgh the first string.
#  Step2: comapre the first letter of the first string with all other strings.
#  Step3: if all the first letters are equal add it to prefix.
#  step4: else check the next letter.
#  Step5: return the prefix at end.


#Optimal Solution: O(n)
#Step1: Sort the string and find the smallest and largest strings
#Step2: Loop through the length of smallest among the two strings.
#Step3: Compare the two string, if characters are equal add to answer.
#Step4: Return if characters are not equal
def LongestCommPrefix(strs):
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        
        # Store the common prefix characters
        ans = []
        
        # Compare characters of first and last string
        for i in range(min(len(first), len(last))):
            # Stop if characters differ
            if first[i] != last[i]:
                return ''.join(ans)
            # Add matching character to result
            ans.append(first[i])
        
        # Return the longest common prefix
        return ''.join(ans)