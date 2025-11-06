#Find the longest subarry with sum k.

#Brute Force Approach
#Step1: Find all possible subarrays.
#Step2: Calculate sum of each subarray.

arr = [2,3,5,1,9]
k = 10

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += a[K]

            if s == k:
                length = max(length, j - i + 1)
    print(length)
    return length
    

getLongestSubarray(arr, k)