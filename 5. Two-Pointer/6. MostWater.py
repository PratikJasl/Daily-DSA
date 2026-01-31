#Leet Code: 11 : 
# Container with Most Water: https://leetcode.com/problems/container-with-most-water/description/

# Approach: Two Pointer: T: O(n) | O(1)
# Step 1: Use left and right pointer 
# Step 2: Compute Volume and Max Volume
# Step 3: Decrease left and right based on height

class Solution:
    def maxArea(height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        volume = 0
        max_volume = 0

        while(left < right):
            d = right - left
            h = min(height[left], height[right])
            volume = d * h

            if(volume > max_volume):
                max_volume = volume
            
            if(height[left] == height[right]):
                left += 1
                right -= 1
            elif(height[left] > height[right]):
                right -= 1
            else: 
                left += 1
        print(max_volume)
        return max_volume


result = Solution()

result1 = Solution.maxArea([1,8,6,2,5,4,8,3,7])


