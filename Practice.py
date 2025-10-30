#Rotate array by k
arr  = [1,2,3,4,5,6]
k = 6

def rotateArray(arr, k):
    n = len(arr)
    k = k%n
    rotated = arr[n-k:]
    notRotated = arr[:n-k]
    arr[:] = rotated + notRotated
    print(arr)

rotateArray(arr, k)