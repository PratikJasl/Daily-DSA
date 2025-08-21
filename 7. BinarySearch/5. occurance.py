#leetcode: 34
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

#BruteForce: O(n)
#Step1: Iterate through the loop
#Step2: If num is equal to target update start and end.
# def LastOccurance(nums, target):
#     n = len(nums)
#     start = n+1
#     end = 0

#     for i in range(n):
#         if nums[i] == target:
#             start = min(start, i)
#             end = max(end, i)
#     if end == 0:
#         return [-1,-1]
#     else:
#         return [start, end]

# print(LastOccurance([5,7,7,8,8,10], 8))

#Binary Search Approach: O(logN)
#Step1: Use lower bound to find the start index
#Step2: Use Upper bound -1 to find end index
#Step3: handle edge cases where it did not find the target and it returns a value not equal to target.

def lowerBound(nums, x):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low+high) // 2
        if(nums[mid] >= x):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upperBound(nums, x):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low+high) // 2
        if(nums[mid] > x):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def LastOccurance(nums, target):
        start = lowerBound(nums, target)
        if start == -1 or nums[start] != target:
            return [-1,-1]
        else:
            return[start, upperBound(nums, target)-1]

print(LastOccurance([5,7,7,8,8,10], 8))