num = [1,-2,5,8,-8]

def kadanesAlgo(num):
    sum = num[0]
    maximum = num[0]

    for i in range(1, len(num)):
        sum = max(num[i], sum + num[i])
        maximum = max(sum, maximum)

    print("contigious subarray sum:", maximum)
    return maximum

kadanesAlgo(num)

