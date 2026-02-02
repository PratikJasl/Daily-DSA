#2461: Maximum Sum of Distinct Subarrays with Length K.
nums = [1,5,4,2,9,9,9]
k = 3

# Using Nested Loops:
# Step1: Iterate i till n-k
# Step2: Iterate j from i to i+K
# Step3: compute sum and maxsum
def BruteForce(nums: list[int], k: int) -> int:
    n = len(nums)
    maxSum = 0
    
    for i in range(n-k):
        sum = 0
        for j in range(i, i+k):
            sum += nums[j]
            if(sum > maxSum):
                maxSum = sum
    print("Max Sum:", maxSum)
    return maxSum

BruteForce(nums, k)

# Optimal Solution: Sliding Window

def Max_sum_subarray(nums: list[int], k: int)-> int:
    n = len(nums)
    sum = 0
    Maxsum = 0
    i = 0
    j = k - 1

    for i in range(k):
        sum += nums[i]

    while(j < n-1):
        sum -= nums[i]
        i += 1
        j += 1
        sum += nums[j]

        if sum > Maxsum:
            Maxsum = sum
    
    print("Max Sum:", Maxsum)
    return Maxsum

Max_sum_subarray(nums, k)