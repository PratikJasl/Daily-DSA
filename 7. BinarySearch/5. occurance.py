#leetcode: 34

# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

def LastOccurance(nums, target):
    n = len(nums)
    low = 0
    high = n - 1 
    ans = -1

    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            ans = mid
            low = mid + 1
        elif(target < nums[mid]):
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
    return ans

print(LastOccurance([5,7,7,8,8,10], 8))