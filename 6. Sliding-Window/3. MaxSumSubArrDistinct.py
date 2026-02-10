
# Brute Force
# Step1: Loop through all possible windows.
# Step2: If elements are unique compute sum and update max.

def maximumSubarraySum(nums: list[int], k: int) -> int:
        n = len(nums)
        max_sum = 0
        
        for i in range(n - k+1):
            current_sum = 0
            seen = set()
            is_valid_window = True
            for j in range(i, i + k):
                if nums[j] in seen:
                    is_valid_window = False
                    break
                
                seen.add(nums[j])
                current_sum += nums[j]
            
            if is_valid_window:
                max_sum = max(max_sum, current_sum)
                 
        return max_sum


# Optimal Solution: Sliding Window
# Step1: If element not in seen, Add element to seen and increment sum.
# Step2: If window size is incresed remove left element from seen and decrement left from sum.
# Step3: If window size is valid update max sum.
# Step4: If element in seen, keep removing left, and decrementing sum till element is removed.

def max_Subarray_sum_dis(nums:list[int], k: int) -> int:
    n = len(nums)
    seen = set()
    current_sum = 0
    max_sum = 0
    left = 0

    for right in range(n):
        while(nums[right] in seen):
            current_sum -= nums[left]
            seen.remove(nums(left))
            left+=1

        seen.add(nums[right])
        current_sum += nums[right]
        
        if(right - left + 1 > k):
            current_sum -= nums[left]
            seen.remove[nums(left)]
            left += 1
        
        if(right - left +1) == k:
            max_sum = max(max_sum, current_sum)
    print("Max Sum:", max_sum)
    return max_sum

max_Subarray_sum_dis(nums=[1,5,4,2,9,9,9], k=3)