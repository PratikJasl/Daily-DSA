array = [64, 25, 12, 22, 11]

def insertionSort(arr): # T:O(n^2) | S: O(n)
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > current):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

print(insertionSort(array))
