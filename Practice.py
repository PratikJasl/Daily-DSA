nums = [4,1,2,3]
output = [2,3,4,1]

#Step1: Store all odd indexs value in an array and sort them in descreaing order.
#Step2: Store all even indexes value in an array and sort them in ascending order.
#Step3: Iterate through the original array and replace even indexes with elements of 

def sort_even_odd(nums: list[int]):
    n = len(nums)
    even_indexs = []
    odd_indexs = []
    j = 0
    k = 0

    for i in range(n):
        if (i % 2 == 0):
            even_indexs.append(nums[i])
        else:
            odd_indexs.append(nums[i])
    
    even_indexs.sort()
    odd_indexs.sort(reverse=True)
    print(even_indexs, odd_indexs)

    for i in range(n):
        if(i % 2 == 0 and j < len(even_indexs)):
            nums[i] = even_indexs[j]
            j += 1
        elif(i % 2 != 0 and k < len(odd_indexs)):
            nums[i] = odd_indexs[k]
            k += 1
    
    print(nums)

sort_even_odd([2,1])