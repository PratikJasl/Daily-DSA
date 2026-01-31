#Two Sum Problem
nums = [3,3] 
target = 6

def Two_Sum(nums, target):
    n = len(nums)
    hash_map = {}

    for i in range(n):
        compliment = target - nums[i]
        if(compliment in hash_map):
            print( hash_map[compliment], i)
            return [i, hash_map[compliment]]
        elif(nums[i] not in hash_map):
            hash_map[nums[i]] = i
    
Two_Sum(nums, target)