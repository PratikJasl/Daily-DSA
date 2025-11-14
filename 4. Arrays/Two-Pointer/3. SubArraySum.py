#Find the longest subarry with sum k.

#Brute Force Approach: T: O(n^3)
#Step1: Find all possible subarrays.
#Step2: Calculate sum of each subarray.
#Step3: Keep track of maximum length subarray.

arr = [2,3,5,1,9]
k = 5

def Longest_Subarray_Sum(a: list[int], k: int) -> int:
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
Longest_Subarray_Sum(arr, k)

#Better Solution: T : O(n^2) | S : O(1)
#Reduce one loop.
#arr = [2,3,5,1,9]
def longest_subarray_sum(a: list[int], k: int) -> int:
    n = len(arr)
    maxLength = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            
            if(sum == k):
                maxLength = max(maxLength, j-i+1)
    
    print("MaxLength:", maxLength)
longest_subarray_sum(arr, k)