# Selection Sort
# Select the minimum and move it to the start.
# 2 Points, 1 minIndex

def selectionSort(arr):
    n = len(arr)
    for i in range (n):
        minIndex = i
        for j in range(i+1, n):
            if(arr[j] < arr[minIndex]):
                minIndex = j
        if(minIndex != i):
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print("Sorted Array:", arr)
    return arr

selectionSort([1,5,7,3,2,4,8,6,9])