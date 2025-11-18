#Given an array consisting of only 0s, 1s, and 2s. 
#Write a program to in-place sort the array without using inbuilt sort functions.

#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

#Approach: Using Pointers
#Step1: Create 3 pointers, low, mid, high
#Step2: If mid == 0, swap low and mid, and increment both.
#Step3: elif mid == 1, increment mid.
#Step3: else, when mid == 2, swap high and mid, and decrement high.
#[2,0,2,1,1,0]
#[0,0,2,1,1,2]
#[0,0,1,1,2,2]
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
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
        print("Sorted Array:", nums)      


nums = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(nums) 
