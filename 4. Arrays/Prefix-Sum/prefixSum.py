#Prefix Sum is the sum of all the prefixes and the current index.
#Example:
arr = [1,2,3,4,5]
prefix_sum = [1,3,6,10,15]

def find_prefix_sum(arr: list[int]) -> list[int]:
    n = len(arr)
    prefix_sum = arr[:]
    for i in range(1, n):
        prefix_sum[i] = arr[i] + prefix_sum[i-1]
    
    print("Prefix Sum:", prefix_sum)

find_prefix_sum(arr)

