# 15. 3 SUM
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Brute Force:
# Step1: Use three nested loops to find all possibel triplets.
# Step2: To avoid Duplicate thriplet sort them and store in result.
# Step3: Before storgin check if sorted triplet present in result or not.
def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(nums[i]+ nums[j]+ nums[k] == 0):
                        if(sorted([nums[i], nums[j], nums[k]])) not in result:
                            result.append(sorted([nums[i], nums[j], nums[k]]))
    print('Result:', result)
    return result

threeSum([1,-1,-1,0])

def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()  # 1. Sort the array (Essential for Two Pointers)

    for i, a in enumerate(nums):
        # 2. Skip positive integers immediately (Optimization)
        # If the current number 'a' is > 0, we can never sum to 0
        # because the array is sorted (all remaining numbers are also > 0).
        if a > 0:
            break

        # 3. Avoid Duplicates for the FIRST number
        # We already processed this number in the previous iteration
        if i > 0 and a == nums[i - 1]:
            continue

        # 4. Standard Two Sum II logic
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                # Found a triplet!
                res.append([a, nums[l], nums[r]])
                
                # 5. Update pointers AND avoid duplicates for the SECOND number
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res