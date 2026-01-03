arr = [64, 25, 12, 22, 11]

def quickSort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex+1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Put pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return pivot index
    return i + 1

print(quickSort(arr, 0 , len(arr)-1))