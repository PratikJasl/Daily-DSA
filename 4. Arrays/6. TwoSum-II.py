# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing 
# order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Brute Force: Nested Loops
# Complexity: T:O(n^2) | S:O(1)
def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if(nums[i] + nums[j] == target):
                return [i,j]
            

# Optimal Solution: Two Pointers
# Complexity: T:O(n) | S:O(1)
# Since the array is sorted, we no longer have to check all possible pairs.
# We use opposite ends Two Pointers
def twoSum(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    left = 0
    right = n - 1

    while (left < right):
        sum = numbers[left] + numbers[right]

        if( sum > target ):
            right -= 1
        elif( sum < target ):
            left += 1
        else:
            return [left+1, right+1]