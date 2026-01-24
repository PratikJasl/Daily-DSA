#Given an integer array nums and an interger "K", return the "K" most frequent elements.

# Example:
# nums = [4,1,-1,2,-1,2,3]
# k = 2
# output = [1,2]

#Approach: T:O(n) | S: O(n)
# Step1: Create a frequency map
# Step2: Use bucket sort to create a list of element with freq.
# Step3: Return top k results.

def top_k_frequent_element(nums, k):
    count = {}
    freq = []
    res = []
    for i in range(len(nums)+1): #Fill freq array with [] in each index
        freq.append([])

    for n in nums: #Create count map.
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    for value, count in count.items(): #store value in count index
        freq[count].append(value)
    
    for i in range(len(freq)-1,0,-1): #iterate from end and return res.
        for n in freq[i]:
            res.append(n)
            if(len(res) == k):
                return res











    
    # sorted_map = sorted(hash_map.items(), key=lambda x:x[1] , reverse=True)
    # print("Sorted Map:", sorted_map)

    # frequent_element = sorted_map[:k]
    # temp = [item[0] for item in frequent_element[:k]]
    # print("Frequent Element:", frequent_element, temp)
    
