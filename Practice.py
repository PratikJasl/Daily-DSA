#given an array of ‘N’ integers. Find the length of the longest sequence which contains the consecutive elements.

# Example 1:
# Input: [100, 200, 1, 3, 2, 4]
# Output: 4
# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4

#Approach 1: Sorting T:O(NlogN) S:O(1)
#step1: Sort the array.
#Step2: Loop through the array, till n-1
#Step3: Compare adjusent element and count the length of consecutive sequence.

#[1,2,3,4,100,200] c =3, m=3
def longest_consecutive_sorting(arr):
    n = len(arr)
    count = 0
    maxCount = 0
    arr.sort()
    for i in range(n-1):
        if(arr[i] == (arr[i+1]-1)):
            count += 1
            maxCount = max(count, maxCount)
    print("MaxCount:", maxCount+1)
    return maxCount + 1

longest_consecutive_sorting([100,101,200,102])

#Approach 2: Hashing T:O(n) S:O(n) 
#Note: Using a Set might be better if there are duplicates.
#step1: Create an hash map from the array.
#step2: loop through the array and check if element +1 exist's in the map.
#step3: Increment count if it does.

def longest_sequence(arr: list[int]) -> int:
    n = len(arr)
    count = 0
    maxCount = 0
    Map = {}

    for i in range(n):
        if(arr[i] not in Map):
            Map[arr[i]] = i
    print("Map Created:", map)

    for i in range(n):
        if((arr[i]+1) in Map):
            count += 1
            maxCount = max(count, maxCount)

    print("MaxCount:", maxCount+1)          

longest_sequence([3, 8, 5, 7, 6]) #c=3