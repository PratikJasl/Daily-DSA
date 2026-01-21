# Given an array of integers nums and an integer target, return indices of the two 
# numbers such that they add up to target.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Brute Force: Nested Loops
# Complexity: T:O(n^2) | S:O(1)
def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if(nums[i] + nums[j] == target):
                return [i,j]

# Optimal Solution: Hashing
# Complexity: T:O(n) | S:O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    freq = {}

    for i in range(n):
        compliment = target - nums[i]
        if compliment in freq:
            return [ i, freq[compliment] ]
        else:
            freq[nums[i]] = i  