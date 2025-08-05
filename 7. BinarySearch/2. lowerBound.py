# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
#find the first element which is >=x.
# Example 1:
# Input Format: arr[] = {1,2,2,3}, x = 2
# Result: 1
# Explanation: Index 1 is the smallest index such that arr[1] >= x.

#Approach:
# Step1: implement BS
# Step2: if we find an element >=x at mid. decrement high to mid-1 and check no other element before satify the condition.
def lowerBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    output = n

    while(low <= high):
        mid = (low + high) // 2

        if(nums[mid] >= target):
            output = mid
            high = mid - 1
        else:
            low = mid + 1
    return output


nums = [3,5,8,15,19]
target = 9
print(lowerBound(nums, target))