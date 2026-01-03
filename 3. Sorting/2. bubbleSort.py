array = [64, 25, 12, 22, 11] 

def bubble_sort(arr): #T:O(n^2) | S:O(1)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j] #Swap
    return arr

print(bubble_sort(array))
