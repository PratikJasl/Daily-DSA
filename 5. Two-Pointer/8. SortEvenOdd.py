# Given an array of int, make sure the even numbers appear first and then the Odd numbers.
# Keep the relative order same and return the same array.

# Example:
# nums = [1,2,3,4,6,7]
# result = [2,4,6,1,3,7]
nums = [4, 7, 8, 10]

#Approch: 
# Step1: Sort the Array to ensure odd elements are present first.
# Step2: Whenever right pointer is even swap left and right and increment both.
# Step3: Else just increment left

def SortEvenOdd(nums: list[int]):
    n = len(nums)
    nums.sort()
    left = 0
    right = left + 1

    while(left < right and right < n):
        if(nums[right] % 2 == 0):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        else:
            right += 1

    print("Sorted Nums:", nums)

SortEvenOdd(nums)