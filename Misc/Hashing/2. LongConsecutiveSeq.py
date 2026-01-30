# Given an Unsorted array of integers. 
# Find the length of the longest sequence which contains the consecutive elements.

# Exampl1e 1:
nums = [100, 200, 1, 3, 2, 4] # Input: [100, 200, 1, 3, 2, 4] 
# Output: 4
# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4

# Brute Force: Sorting
# T: O(nlogn) S: O(1)
# Step1: Sort the array.
# Step2: Iterate through the array from 1.
# Step3: check if nums[i] != nums[i-1] for duplicates, skip duplicates.
# step4: check if nums[i] == nums[i-1] + 1
# Step5: If yes increment count and update max.
# Step6: else reset count to 1.

def brute_force(nums):
    if not nums:
        return 0
    n = len(nums)
    nums.sort()
    count = 1
    max_count = 1
    for i in range(1, n):
        if(nums[i] != nums[i-1]): #Skip Duplicates
            if(nums[i] == nums[i-1] + 1):
                count += 1 
                max_count = max(count, max_count)
            else:
                count = 1
    return max_count

#print(brute_force(nums))

# Optimal Solution: Hashing
# T:O(n) | S: O(n)
# Step1: create a set from the array.
# Step2: Loop through set.
# Step3: We have to find the starting point, so check item-1 not in set.
#(If we don't start from starting point, we will not get correct count)
#(Example: [9,5,8,6,7] if we start from 9 and check if 9+1 exists it dosen't so we find the starting point)
# Step4: If we find starting point set count to 1.
# Step5: Run a while loop till we have starting point + 1 and update count.
# Step6: Update longest.

def optimal_solution(nums):
    if not nums:
        return 0
    #create a set
    nums_set = set(nums)
    longest = 0

    for item in nums_set:
        if(item - 1 not in nums_set): #Starting element
            count = 1
            current_item = item
            while (current_item + 1) in nums_set:
                current_item += 1
                count += 1
            longest = max(longest, count)
    
    return longest
    

print(optimal_solution(nums))









































