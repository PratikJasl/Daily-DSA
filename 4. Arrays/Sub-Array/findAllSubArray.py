#Find all possible subarrays of a given array.

arr = [1, 2, 3]

def find_all_subarrays(arr: list[int]) -> list[int]:
    n = len(arr)
    subarrays = []
    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    
    print("Total subarrays:", subarrays)
    return subarrays

find_all_subarrays(arr)