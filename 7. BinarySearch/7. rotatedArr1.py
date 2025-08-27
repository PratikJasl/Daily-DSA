#Leet code: 33
#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

#Brute Force: O(n)
#Step1: Iterte through the array.
#Step2: Return the index if target is found else -1.

#Optimal: Binary Search O(logN)
#Step1: Create low, high and mid indexes
#Step2: Check is target is greater than low or less then high to determine which side is valid.
#Step3: Check edge cases