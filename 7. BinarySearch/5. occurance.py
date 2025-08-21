#leetcode: 34
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

#BruteForce:
#Step1: Iterate through the loop
#Step2: If num is equal to target update start and end.
def LastOccurance(nums, target):
    n = len(nums)
    start = n+1
    end = 0

    for i in range(n):
        if nums[i] == target:
            start = min(start, i)
            end = max(end, i)
    if end == 0:
        return [-1,-1]
    else:
        return [start, end]

print(LastOccurance([5,7,7,8,8,10], 8))