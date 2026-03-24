# 3917: Longest Balanced Subarray.

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        # Step 1: Find all subarrays.
        # Step 2: Store elements inside each subarray.
        # Step 3: Check if the elements are balanced or not.
        n = len(nums)
        result = 0
        for i in range(n):
            seen = {}
            even_unique = 0
            odd_unique = 0
            for j in range(i, n):
                if nums[j] not in seen:
                    seen[nums[j]] = 1
                    if nums[j] % 2 == 0:
                        even_unique += 1
                    else:
                        odd_unique += 1
                else:
                    seen[nums[j]] += 1
        
                if even_unique == odd_unique:
                    result = max(result, j-i+1)

        return result
             

