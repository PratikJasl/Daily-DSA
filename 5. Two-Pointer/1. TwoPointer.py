#Two pointers
nums = [1,2,4,5,6]
nums2 = [5,7,2,8,9,0]

#Approach 1: Left and Right pointer oppsoite directions.
# Used when the array is Sorted.
def OppositePointers(nums: list[int]) -> str:
    n = len(nums)
    left = 0
    right = n-1

    while(left < right):
        pass
        #move in when both are equal

        #move left if sum/comparison is to small, to increase the value.

        #move right if sum/comparison is to large, to decrease the value.

    return "Left & Right Pointer"

#Approach 2: Fast and slow pointer same start.
def SlowFast(nums2: list[int]) -> bool:
    n = len(nums2)
    slow = 0
    fast = 0

    while(fast < n and slow < n):
        pass
        #move fast and iterate through all
        #move slow when a condition is met.
    return "Fast & Slow Pointer"