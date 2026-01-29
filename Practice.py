# Given an integer array nums and an interger "K", return the "K" most frequent elements.

# Example:
# nums = [4,1,-1,2,-1,2,3]
# k = 2
# output = [1,2]

# Step1: Find the freq of each element using a map.
# Step2: Create a list and fill it with list 
# Step3: Iterate through the count and create res with top K.
def TopKFrequent(nums: list[int], k:int) -> list[int]:
    freq = {}
    count = []
    result = []

    for item in nums:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    for i in range(len(nums)+1):
        count.append([])
    
    for value, c in freq.items():
        count[c].append(value)

    for i in range(len(count)-1, 0, -1):
        for n in count[i]:
            result.append(n)
            if(len(result) == k):
                print("Result:", result)
                return result

    print(freq, count)

TopKFrequent([1], 2)