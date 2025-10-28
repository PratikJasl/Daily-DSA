# Bubble Sort
# Swap and move largest to the end.
# Pointer i, swapped.

def BubbleSort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(n-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        n -= 1
    print("Sorted Array :", arr)
    return arr

BubbleSort([2,5,1,4])
            
