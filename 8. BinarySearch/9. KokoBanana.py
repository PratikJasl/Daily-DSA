
# Approach: Binary Search
# Step1: Write a function to check the hours of eating in a given speed.
# Step2: Use binary search on all possible speeds ranges.
# Step3: Pass speed to check, if speed is too slow increase low pointer.
# Step4: If speed can be reduced decrease high pointer.
def minEatingSpeed(piles: list[int], h: int) -> int:
    low = 1
    high = max(piles)
    ans = high

    while(low <= high):
        mid = (low + high) // 2
        hours = check(piles, mid)
        print(hours, piles[mid])
        if(hours > h):
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    return ans
    

def check(piles , k):
    hours = 0
    for i in range(len(piles)):
        diff = piles[i]
        while(diff > 0):
            hours += 1
            diff -= k
    
    return hours
    


# Optimal Solution: Replacing the While loop with math operator ceil.
# Will allow us to pass time limit exceed test cases.
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # FIX 1: The search space is the range of speeds, NOT the array indices.
        low = 1
        high = max(piles) 
        ans = high # Initialize with the max possible valid speed

        while low <= high:
            mid = (low + high) // 2  # 'mid' is now the SPEED (k), not an index
            
            hours = self.check(piles, mid)
            
            if hours <= h: # If we can eat all piles within 'h' hours
                ans = mid   # This speed works! Let's try to find a slower one.
                high = mid - 1
            else:           # Too slow! We need to eat faster.
                low = mid + 1

        return ans

    def check(self, piles, k):
        hours = 0
        for pile in piles:
            # FIX 2: Optimization
            # Instead of a while loop (simulation), use math to calculate hours instantly.
            # math.ceil(pile / k) is equivalent to (pile + k - 1) // k
            hours += math.ceil(pile / k) 
        
        return hours