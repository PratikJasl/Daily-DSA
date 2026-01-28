#26. Remove Duplicates

#Given: Sorted Array with integers
#To Do: Remove duplicate elements, and keep array in same order
#Return: number of unique elements and updated array.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Brute Force:
# Step1: Create a list of unique element
# Step2: Overwrite the array with that unique list.
def RemoveDuplicates(nums: list[int]):
    n = len(nums)
    unique = []

    for i in nums: #Fill list with unique
        if i not in unique:
            unique.append(i)
    
    for i in range(len(unique)): #Overwrite list
        nums[i] = unique[i]
    
    return len(unique)

RemoveDuplicates([1,1,2])

# Optimal Solution: Using Two Pointers
# Step1: Maintain two pointer left and right
# Steo2: If left and right are same increament right
# Step3: If left and right are not same increment left and nums[left] = nums[right]
def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    left = 0
    for right in range(1, n):
        if(nums[left] != nums[right]):
            left += 1
            nums[left] = nums[right]

    return left + 1
