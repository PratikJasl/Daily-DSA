#Given an integer array nums and an interger "K", return the "K" most frequent elements.

# Example:
# nums = [4,1,-1,2,-1,2,3]
# k = 2
# output = [1,2]

def top_k_frequent_element(nums, k):
    count = {}
    freq = []
    res = []
    for i in range(len(nums)+1):
        freq.append([])

    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    for value, count in count.items():
        freq[count].append(value)
    
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if(len(res) == k):
                return res











    
    # sorted_map = sorted(hash_map.items(), key=lambda x:x[1] , reverse=True)
    # print("Sorted Map:", sorted_map)

    # frequent_element = sorted_map[:k]
    # temp = [item[0] for item in frequent_element[:k]]
    # print("Frequent Element:", frequent_element, temp)
    
