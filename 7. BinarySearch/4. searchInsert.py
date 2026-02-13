# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Brute Force: Linear Check O(n)
def searchInsert(nums: list[int], target: int) -> int:
    n = len(nums)
    for i in range(n):
        if(nums[i] > target):
            return i
        elif(nums[i] == target):
            return i 

    return n

# Optimal Approach: BS O(log n)
def searchInsert(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    ans = n

    while (low <= high):
        mid = (low + high) // 2

        if(nums[mid] >= target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans