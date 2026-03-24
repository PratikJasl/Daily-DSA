# Leetcode: 169. Majority Element

#Brute Force: Using hashmap
# T: O(n) | S: O(n)
# Step1: Count freq of elements
# Step2: Return the elements who's freq is greater than n/2
def majorityElement(nums: list[int]) -> int:
    n = len(nums)
    freq = {}
    for item in nums:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        if(value > n/2):
            return key
        
#Optimal: Using Voting Algorithm
# T: O(n) | S:O(1)
# Step1: create two variables candidate and count.
# Step2: iterate through the loop, and if count is zero assign new candidate.
# Step3: Every time we encounter candidate increase count, if not reduce count.

def majorityElement(nums: list[int]) -> int:
    candidate = None
    count = 0

    for item in nums:
        if(count == 0):
            candidate = item
        
        if(item == candidate):
            count += 1
        else:
            count -= 1
    
    return candidate