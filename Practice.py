def longestSubarray(nums, k):
    n = len(nums)
    sum = nums[0]
    maxLen = 0
    left = 0
    right = 0
    print("Initial SUM:", sum)
    print("Array length", n)
    while(right < n-1):
        print("Inside While Loop")
        print("SUM:", sum)
        if(sum < k):
            right += 1
            sum += nums[right]
        elif(sum > k):
            left += 1
            sum -= nums[left]
        elif(sum == k):
            maxLen = max(maxLen, (right - left) + 1)
            print("MaxLen:", maxLen)
            sum -= nums[left]
            right += 1
            left += 1
            sum += nums[right]
    print(maxLen)
    return maxLen


arr = [1, -1, 5, -2, 3]
k=3

longestSubarray(arr, k)