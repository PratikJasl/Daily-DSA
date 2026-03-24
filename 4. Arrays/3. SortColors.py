# leetcode: 75: Sort Colors

# Using the Dutch National Flag algorithm.
# Step1: Create three pointers: low, mid = 0 and high = n-1
# Step2: If mid is 0, swap low and mid and increment both.
# Step3: elif mid is 1, just increment mid
# Step4: else mid is 2, swap mid and high and decrement high.

def sortColors(nums: list[int]) -> None:
    low = 0
    mid = 0
    high = len(nums) - 1

    while(mid <= high):
        if(nums[mid] == 0):
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif(nums[mid] == 1):
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1