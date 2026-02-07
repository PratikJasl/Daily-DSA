# Given an array of int, make sure the even numbers appear first and then the Odd numbers.
# Keep the relative order same and return the same array.

# Example:
# nums = [1,2,3,4,6,7]
# result = [2,4,6,1,3,7]

nums = [1,2,3,4,6,7]

def SortEvenOdd(nums: list[int]):
    n = len(nums)
    left = 0

    for i in range(n):
        if(nums[i] % 2 != 0):
            right = i
            print(nums[i], right)
            break

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