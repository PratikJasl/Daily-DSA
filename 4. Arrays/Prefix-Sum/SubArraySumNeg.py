#Find long subarray with sum K.
arr = [2,3,5,6]
k = 5
#-----------------------------------------------------------------------------
#NOTE: This approach 2 the best solution with an array has both positives and negative
#-----------------------------------------------------------------------------

#Approach 1: Find all subarrays | T:O(n^2) | S:O(1)
#Step1: Find all subarrays.
#Step2: Compute sum of the subarray.
#Step3: Update maxLen when sum is equal to k.
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

#Approach 2: Using prefix-sum and hash-map.
# T: O(nlogn) | S: O(n)
#Step1: Loop through the array.
#Step2: Add current element to sum.
#Step3: Check is sum is equal to k, if yes update maxLength.
#step4: Add the sum in map with index, if it does not exist.
#step5: Calculate reminder of sum - k.
#Step6: Check if reminder is present in the map, and update maxLength.

def find_subarray_sum(arr: list[int], k : int) -> int:
    n = len(arr)
    sum = 0
    prefix_sum = {}
    maxLength = 0

    for i in range(n):
        sum += arr[i]

        if(sum == k):
            maxLength = max(maxLength, i+1)

        rem = sum - k
        if(rem in prefix_sum):
            length = i - prefix_sum[rem]
            maxLength = max(maxLength, length)

        if(sum not in prefix_sum):
            prefix_sum[sum] = i
    print("maxLength:", maxLength)
    return maxLength

find_subarray_sum(arr, k)


        
