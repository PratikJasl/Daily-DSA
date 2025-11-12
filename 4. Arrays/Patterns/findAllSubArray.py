#Find all possible subarrays of a given array.

arr = [1, 2, 3]

# Using two pointers: T: O(N) | S: O(1)
# For listing out all the possible subarrays this is the best solution.
def find_all_subarrays(arr: [int]) -> [int]:
    n = len(arr)
    subarrays = []
    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    
    print("Total subarrays:", subarrays)
    return subarrays

find_all_subarrays(arr)
