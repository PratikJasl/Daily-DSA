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

# Better Solution: Two Pointer
# Complexity: T:O(nlogn) | S:O(n)
# We sort the array, so that we do not have to check all possible pairs.
# But since the indexes are changed we store the indexes in a DS.

def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 1. Store pairs of (value, index) so we don't lose track
    # Input: [3, 2, 4] -> [(3,0), (2,1), (4,2)]
    nums_with_index = []
    for i, num in enumerate(nums):
        nums_with_index.append((num, i))
    # 2. Sort based on the values (O(N log N))
    # Becomes: [(2,1), (3,0), (4,2)]
    nums_with_index.sort()
    left, right = 0, len(nums) - 1
    
    while left < right:
        curr_sum = nums_with_index[left][0] + nums_with_index[right][0]
        
        if curr_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        
        elif curr_sum < target:
            left += 1
        else:
            right -= 1


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