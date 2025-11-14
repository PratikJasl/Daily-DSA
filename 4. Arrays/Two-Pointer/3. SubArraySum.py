#Find the longest subarry with sum k.

#Brute Force Approach: T: O(n^3)
#Step1: Find all possible subarrays.
#Step2: Calculate sum of each subarray.
#Step3: Keep track of maximum length subarray.

##NOTE: The Brute Force can be optimized to T:O(n^2)
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

#Optimal Solution: T: O(2n) | S: O(1)
#Step1: Create a Left and Right pointer starting at 0.
#Step2: Compute sum.
#Step3: If sum is greater than K, reduce left.
#Step4: If sum is less than k, increment right.
#Step5: Update maxLength when sum is equal to K.
#arr = [2,3,5,1,9]
def longest_subarray_sum(a: list[int], k: int) -> int:
    n = len(a)
    left = 0
    right = 0
    sum = a[0]
    maxLength = 0

    while(right < n):
        while(left <= right and sum > k):
            sum -= a[left]
            left += 1
        
        if(sum == k):
            maxLength = max(maxLength, right-left+1)

        right += 1
        if(right < n):
            sum += a[right]
    print("MaxLength:", maxLength)
    return maxLength

longest_subarray_sum(arr, k)