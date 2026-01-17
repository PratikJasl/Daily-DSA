num = [1,-2,5,8,-8]

def kadanesAlgo(num):
    sum = num[0]
    maximum = num[0]

    for i in range(1, len(num)):
        sum = max(sum, sum + num[i])
        maximum = max(sum, maximum)

    print("contigious subarray sum:", maximum)
    return maximum

kadanesAlgo(num)

# Kadane with indexes
def KadanesAlgoWithIndex(nums):
    sum = nums[0]
    maximum = nums[0]
    start = 0
    end = 0
    for i in range(1, len(nums)):
        if(nums[i] > sum + nums[i]):
            sum = nums[i]
            start = i
        else:
            sum += nums[i]

        if(sum > maximum):
            maximum = sum
            end = i
    print(maximum, start, end)

KadanesAlgoWithIndex(num)