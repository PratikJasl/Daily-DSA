# Sliding Window Technique

# Fixed Window:
# Question: Find the maximum sum, in the given array and window size. 
nums = [2,3,5,7,9,1]
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

