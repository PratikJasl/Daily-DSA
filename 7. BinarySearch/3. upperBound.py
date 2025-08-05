# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.
#find the first element which is >x.
# Example 1:
# Input Format: arr[] = {1,2,2,3}, x = 2
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] > x.

#Approach:
# Step1: implement BS
# Step2: if we find an element >x at mid. decrement high to mid-1 and check no other element before satify the condition.

def upperBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    output = n

    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] > target):
            output = mid
            high = mid - 1
        else:
            low = mid + 1
    return output

print(upperBound([1,2,2,3], 2))