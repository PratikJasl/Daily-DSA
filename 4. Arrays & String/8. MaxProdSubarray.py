# 152. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Brute Force: O(N^3)
# Find all possible subarray product and return maximum.

def Max_Product_Subarray(nums):
    n = len(nums)
    maximum = nums[0]
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j+1):
                product *= nums[k]
                maximum = max(product, maximum)
    
    return maximum

def MaProductSubarray(nums):
    pass