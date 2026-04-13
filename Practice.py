def mergeSort(nums):
    #Base Condition:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_part = mergeSort(nums[:mid])
    right_part = mergeSort(nums[mid:])
    return merge(left_part, right_part)

def merge(left, right):
    temp = []
    i, j = 0, 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    
    temp.extend(left[i:])
    temp.extend(right[j:])

    return temp

print(mergeSort([38,27]))