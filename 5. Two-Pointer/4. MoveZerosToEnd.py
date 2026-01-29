#283. Move Zeros
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n <= 1:
        return nums

    left = 0
    for i in range(n):
        if nums[i] == 0:
            left = i
            break
    
    right = left+1
    print(left, right)
    while(right < n):
        if(nums[left] == 0 and nums[right] != 0):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        else:
            right +=1