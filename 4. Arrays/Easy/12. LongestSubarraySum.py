#Q: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

#Input: arr = [2,3,5] , sum = 5

#Approach: Two Pointers | T:O(2n) | S: O(1)
#Step1: Point the left and right pointer at arr[0], and make sum as arr[0]
#Step2: Check if Sum is equal to K, if yes update MaxLen
#Step3: If Sum is greater than K, substract left from sum and increment it till sum is less than K.
#Step4: if Sum is less than k, increment Right and add right to sum.

def longest_subarray_sum(arr: [int], k: [int]) -> int:
    n = len(arr)
    left = 0
    right = 0
    sum = arr[0]
    maxLength = 0

    while(right < n):
        while(left <= right and sum > k):
            sum -= arr[left]
            left+=1
        
        if(sum == k):
            maxLength = max(maxLength, right-left+1)

        right += 1
        if(right < n):
            sum += arr[right]
    print(maxLength)
    return maxLength

longest_subarray_sum([2,3,5,1,9], 10)