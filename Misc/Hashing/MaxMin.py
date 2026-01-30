#Write a function to find the highest occuring element in an array.

#Approach: Using Hash: Time: O(N) Space: O(N)
#Step1: Create a frequency map.
#Step2: iterate over the map.
#Step3: compare value with maxFrequency
#Step3: if more push value inside array.

arr = [1,2,1,3,3,4,4,5,2,2,2]
def countFrequency(arr):
    map = {}
    maxFrequency = 0
    leastFrequency = 1
    mostFrequent = []
    leastFrequent = []

    for item in arr: #Build the map.
        if item not in map:
            map[item] = 1
        else:
            map[item] += 1
    print(map)

    for value, count in map.items():   #iterate over the map and find most frequent.
        if count > maxFrequency:
            maxFrequency = count
            mostFrequent = [value]
        elif count == maxFrequency:
            mostFrequent.append(value)
    print('most frequent:',mostFrequent)

    for value, count in map.items():   #iterate over the map and find least frequent.
        if count <= leastFrequency:
            leastFrequency = count
            leastFrequent = [value]
        elif count == leastFrequency:
            leastFrequent.append(value)
    print('Least Frequent:', leastFrequent)
    
countFrequency(arr)
