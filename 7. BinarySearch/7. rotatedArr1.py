#Leet code: 33
#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

#Brute Force: O(n)
#Step1: Iterte through the array.
#Step2: Return the index if target is found else -1.

#Less Optimal: Binary Search O(logN) : Fails in some Edge cases
#Step1: Create low, high and mid indexes
#Step2: Check is target is greater than low or less then high to determine which side is valid.
#Step3: perform Binary Search on that side.
#Step4: If element is not found perfom BS on other side

def binarySearch(low, high, arr, target):
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == target):
            return mid
        elif(target > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

def findTargetInRotatedArray(arr, target):
    n = len(arr)
    high = n - 1
    low = 0
    ans = -1
    mid = (low + high) // 2

    if(arr(mid) == target):
        return mid
    
    ans = binarySearch(low, mid, arr, target)

    if(ans == -1):
        ans = binarySearch(mid+1, high, arr, target)

    print('target found on :', ans)
    return ans

arr = [3,1]
findTargetInRotatedArray(arr, 1)

#Optimal Solution: BS O(LogN)
#Step1: Create low, high and mid Index
#Step2: Check which part of the array is sorted
#Step3: On the sorted part search of the element
#Step4: if not found on sorted part find on non-sorted part

def search(arr, n, k):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
                
        # if right part is sorted
        else:  
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1