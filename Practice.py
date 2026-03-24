def containerWithMostWater(nums: list[int]) -> int:
    if(not nums):
        return 0
    
    n = len(nums)
    low = 0
    high = n - 1
    max_volume = 0
    
    while(low < high):
        min_element = min(nums[low], nums[high])
        volume = (min_element) * (high - low)
        max_volume = max(volume, max_volume)

        if(nums[low] < nums[high]):
            low += 1
        else:
            high -= 1
    
    return max_volume

print(containerWithMostWater([1, 1]))