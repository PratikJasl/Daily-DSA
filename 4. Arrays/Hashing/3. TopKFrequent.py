#Given an integer array nums and an interger "K", return the "K" most frequent elements.

# Example:
nums = [4,1,-1,2,-1,2,3]
k = 2
# output = [1,2]

#map = { 1: 4, 2: 2, 3: 1}


def top_k_frequent_element(nums, k):
    n = len(nums)
    hash_map = {}

    for i in range(n):
        if nums[i] not in hash_map:
            hash_map[nums[i]] = 1
        else:
            hash_map[nums[i]] += 1
    
    print("Original Map:", hash_map)

    sorted_map = sorted(hash_map.items(), key=lambda x:x[1] , reverse=True)
    print("Sorted Map:", sorted_map)

    frequent_element = sorted_map[:k]
    temp = [item[0] for item in frequent_element[:k]]
    print("Frequent Element:", frequent_element, temp)
    
    
    

top_k_frequent_element(nums, k)