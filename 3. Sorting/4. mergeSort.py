arr = [64, 25, 12, 22, 11, 10]

def mergeSort(arr): #T: O(n log n) | S: O(n)
    if len(arr) <= 1: #Base Condition
        return arr
    mid = len(arr) // 2 #Floor Division
    left_part = mergeSort(arr[:mid])
    right_part = mergeSort(arr[mid:])

    return merge(left_part, right_part)

def merge(left, right):
    temp = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    
    temp.extend(left[i:]) #inserts the remaining elements inside
    temp.extend(right[j:])
    return temp


print(mergeSort(arr))

