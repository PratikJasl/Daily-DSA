#Find the longest subarry with sum k.

#Brute Force Approach: T: O(n^3)
#Step1: Find all possible subarrays.
#Step2: Calculate sum of each subarray.
#Step3: Keep track of maximum length subarray.

arr = [2,3,5,1,9]
k = 5

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a)
    maxLength = 0

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for z in range(i, j+1):
                sum += arr[z]

            if(sum == k):
                maxLength = max(maxLength, j-i+1)
    
    print(maxLength)
    return maxLength

getLongestSubarray(arr, k)