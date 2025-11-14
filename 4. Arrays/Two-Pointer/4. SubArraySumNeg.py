# Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
arr = [1,-1,1] 
k = 1
#Output: 3

#Approach 1: Find all subarrays | T:O(n^2) | S:O(1)
#Step1: Find all subarrays.
#Step2: Compute sum of the subarray.
#Step3: Update maxLen when sum is equal to k.

#Best Apporach for this question is using Prefix Sum: T: O(n) | S: O(n)

def sub_array_sum(arr: list[int], k: int) -> int:
    n = len(arr)
    maxLength = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            
            if(sum == k):
                maxLength = max(maxLength, j-i+1)
    
    print("MaxLength:", maxLength)
    