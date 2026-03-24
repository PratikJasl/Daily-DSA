# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum

#Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Using kadane's algorithm
# Intituion: Will adding make my sum greater or no.

def MaximumSubarray(nums):
    n = len(nums)
    Sum = nums[0]
    maximum = nums[0]
    start = 0
    end = 0
    for i in range(1, n):
        if(Sum + nums[i] > nums[i]):
            Sum += nums[i]
        else:
            Sum = nums[i]
            start = i
        
        if(Sum > maximum):
            maximum = Sum
            end = i
    
    print(start, end , maximum)
    return maximum
