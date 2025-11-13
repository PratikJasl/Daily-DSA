#Given: array(nums, unsorted, integer)
#ToFind: Length of longest consecutive sequence

#Approach:
#step1: Sort the array
#step2: Maintain a last smallest, count and maxCount variable
#step3: If there is sequence we increment the count and update lastsmallest
#step4: else we reset the count and update lastsmallest


def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0

    # sort the array
    nums.sort()
    lastSmaller = -1000
    cnt = 0
    longest = 1

    for i in range(n):
        if nums[i] - 1 == lastSmaller:
            cnt += 1
            lastSmaller = nums[i]
        elif nums[i] != lastSmaller:
            cnt = 1
            lastSmaller = nums[i]
        longest = max(longest, cnt)
    return longest