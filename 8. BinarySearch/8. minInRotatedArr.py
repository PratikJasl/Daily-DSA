# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

#BruteForce: Linear Search: O(n)
#Step1: Iterate through the loop
#Step2: Do a minimum between the current element and minimum.

def LinearSearch(nums):
    minimum = nums[0]
    for i in range(len(nums)):
        minimum = min(nums[i], minimum)
    return minimum

# Optimal Solution: BS : O(logN)
# Step1: assign the high, low and mid index
# Step2: Find the sorted side, and store the minimum
# Step3: Run LS on non sorted side

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        mid = (low + high) // 2

        if(nums[mid] > nums[high]):
            minimum = self.LinearSearch(nums, mid, high+1)
        else:
            minimum = self.LinearSearch(nums, low, mid+1)
        
        return minimum
    
    def LinearSearch(self, nums, start, end):
        minimum = nums[start]
        for i in range(start, end):
            minimum = min(nums[i], minimum)
        return minimum