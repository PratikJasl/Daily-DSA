# Given an integer array nums and an integer k, return true if there are two distinct indices 
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Brute Force: Nested Loops
# Complexity: T: O(n^2) | S: O(1)
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i] == nums[j]):
                    if(abs(i - j) <= k):
                        return True
        
        return False

# Optimal Solution: T:O(n) | S: O(n)
# Step1: Create a Dictionary for seen.
# Step2: Iterate through the array.
# Step3: If element in seen, check if i-j <= K return true
# Step4: If element not in seen add it to seen with index.
def containsDuplicateII(nums: list[int], k: int) -> bool:
    n = len(nums)
    seen = {} 

    for i in range(n):
        if nums[i] in seen:
            if(abs(i - seen[nums[i]]) <= k):
                return True

        seen[nums[i]] = i
    
    return False

