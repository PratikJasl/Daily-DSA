#Binary Search Algorithm

def BinarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            return mid
        elif(target > nums[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(BinarySearch([3, 4, 6, 7, 9, 12, 16, 17], 16))