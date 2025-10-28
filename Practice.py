# Insertion Sort
# pointer: i, j Variable: Current

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        current = arr[i]
        while(j>=0 and arr[j] > current):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    print("Sorted Array:", arr)
    return arr 

insertionSort([5,1,4,3,2])   