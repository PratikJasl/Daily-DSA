# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

# Example 2:
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

def minimumDifference(self, nums: list[int], k: int) -> int:
    if k == 1:
        return 0
        
    nums.sort()
    
    # 2. Initialize min_diff to infinity (or a very large number)
    min_diff = float('inf')
    
    for i in range(len(nums) - k + 1):
        
        current_diff = nums[i + k - 1] - nums[i]
        
        min_diff = min(min_diff, current_diff)
        
    return min_diff