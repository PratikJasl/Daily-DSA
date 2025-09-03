# Given an array of integers nums sorted in non-decreasing order, 
# find the count of a given target value.
# If target is not found in the array, return 0.

#Brute Force: O(n)
#Step1: Iterate through the loop
#Step2: Whenever we encounter a target increment the count

#Binary Search: O(logN)
#Step1: Implement lower bound to find first index
#Step2: Implement Upper bound to find last index
#Step3: Calculate count using fist and last index
#Step4: handle edge cases.

def lowerBound(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] >= target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upperBound(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] > target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def countOccurance(nums, target):
    start = lowerBound(nums, target)
    if start == len(nums) or nums[start] != target:
        return 0
    end = upperBound(nums, target) - 1

    count = (end - start) + 1
    return count

print(countOccurance([1,2,2,5,5,5], 1))