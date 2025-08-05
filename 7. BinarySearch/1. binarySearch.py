#Binary Search Algorithm
nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 3

#Iterative Approach
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


#Recursive Approach:
def binarySearchRec(nums, target, low, high):
    if(low > high):
        return -1
    
    mid = (low + high) // 2

    if(nums[mid] == target):
        return mid
    elif(target > nums[mid] + 1):
        return binarySearchRec(nums, target, mid+1, high)
    else:
        return binarySearchRec(nums, target, low, mid-1)


print(BinarySearch(nums, target))
print(binarySearchRec(nums,target, 0, 7 ))
