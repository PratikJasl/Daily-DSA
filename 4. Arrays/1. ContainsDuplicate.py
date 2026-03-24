# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Using set
def containsDuplicate(nums):
    unique = set(nums)
    if(len(unique) != len(nums)):
        return True
    else:
        return False