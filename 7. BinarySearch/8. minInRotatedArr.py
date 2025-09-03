# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

#BruteForce: O(n)
#Step1: Iterate through the loop
#Step2: Do a minimum between the current element and minimum.

# Optimal Solution: BS : O(logN)
# Step1: assign the high low and mid index
# Step2: Find the sorted side, and store the minimum
# Step3: Run LS on non sorted side

def Search(low, high, nums, minimum):
    while(low <= high):
        minimum = min(nums[low], nums[high], minimum)
        low = low+1
    return minimum


def FindMinimum(nums):
    if len(nums) < 1: 
        return 0
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    minimum = 1000000

    if(nums[low] <= nums[mid]):
        minimum = min(nums[low], minimum)
        minimum = Search(mid, high, nums, minimum)
    else:
        minimum = min(nums[mid], minimum)
        minimum = Search(low, mid, nums, minimum)
    
    print(minimum)

FindMinimum([])