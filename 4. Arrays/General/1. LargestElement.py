#Q: Given an array of integers nums, return the value of the largest element in the array
#Input: array of integers
#Output: largest integer in the array

#Approach: T: O(n) | S: O(1)

nums = [10,12,34,55]

def findLargest(nums: list) -> int:
    n = len(nums)
    if n <= 1: return nums
    largest = nums[0]

    for i in range(1, n):
        if(nums[i] > largest):
            largest = nums[i]
    
    return largest

print(findLargest(nums))
