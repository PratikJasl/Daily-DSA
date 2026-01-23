#Given an integer array nums and an interger "K", return the "K" most frequent elements.

# Example:
# nums = [4,1,-1,2,-1,2,3]
# k = 2
# output = [1,2]

def top_k_frequent_element(nums, k):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    print("Frequency Map:", freq)











    
    # sorted_map = sorted(hash_map.items(), key=lambda x:x[1] , reverse=True)
    # print("Sorted Map:", sorted_map)

    # frequent_element = sorted_map[:k]
    # temp = [item[0] for item in frequent_element[:k]]
    # print("Frequent Element:", frequent_element, temp)
    
