# // Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# // Example 1:

# // Input: nums = [2,7,11,15], target = 9
# // Output: [0,1]
# // Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def TwoSum(nums, target):
    if(len(nums) < 1): return 0
    map = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if(compliment in map):
            return([map[compliment], i])
        else:
            map[nums[i]] = i
    return "Target not in given array"

print(TwoSum([2,7,11,15], 9))