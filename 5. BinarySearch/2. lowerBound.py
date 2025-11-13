# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
#find the first element which is >= x.
# Example 1:
# Input Format: arr[] = {1,2,2,3}, x = 2
# Result: 1
# Explanation: Index 1 is the smallest index such that arr[1] >= x.

#Approach:
# Step1: implement BS but do not return at mid.
# Step2: if we find an element >= x at mid update output and decrement high to mid-1
# Step3: if element is not >=x increment low to mid+1

def lowerBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    output = -1

    while(low <= high):
        mid = (low + high) // 2

        if(nums[mid] >= target):
            output = mid
            high = mid - 1
        else:
            low = mid + 1
    return output

nums = [3,5,8,15,19]
target = 1
print(lowerBound(nums, target))