# Q: Given an array of integers nums, return the second-largest element in the array. 
# If the second-largest element does not exist, return -1.
# Input: array of integers
# Output: Second Largest element, or -1.

# Brute Force: T: O(nlogn) | S: O(1)
nums = [20,7,6,1,9,21]

def findSecondLargest_(nums):
    n = len(nums)
    nums.sort()
    return nums[n-2]

#Optimal Approach:  T: O(n) | S: O(1)
#Step1: Create a variable largest and second largest variable and initialize it -1.
#Step2: Iterate through the array from 0.
#Step3: Compare element with largest, if element is larger than largest, we update the largest and second largest.
#Step4: Else we check if the element is less than largest and greater than second largest, if ues update second largest.

def findSecondLargest(nums: list) -> int:
    n = len(nums)
    largest = -1
    second_largest = -1

    for i in range(n):
        if(nums[i] > largest):
            second_largest = largest
            largest = nums[i]
        elif(nums[i] > second_largest and nums[i] < largest):
            second_largest = nums[i]
    
    return second_largest


print(findSecondLargest(nums))
