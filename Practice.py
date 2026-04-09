def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    if(len(nums) < 2):
        return nums

    l = 0
    r = k-1
    output = []

    while(r < len(nums)):
        Sum = 0
        for i in range(l, r+1):
            Sum += nums[i]
        
        output.append(Sum)
        l += 1
        r = k-1
        
    return output

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], k=3 ))