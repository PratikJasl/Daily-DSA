#Remove Duplicates from a sorted array.
arr = [1,1,2]

#Brute Force using a set: T: O(n) | S: O(n)
def removeDublicates(arr):
    unique = set()
    index = 0
    for i in range(len(arr)):
        if(arr[i] not in unique):
            unique.add(arr[i])
            arr[index] = arr[i]
            index += 1
    print(arr, unique)
removeDublicates(arr)

#Optimal solution: T:O(N) | S:O(1)
def removeDublicatesO(arr):
    n = len(arr)
    j = 0
    for i in range(n-1):
        if(arr[i] != arr[j]):
            j+=1
            arr[i] = arr[j]
    print(arr)

removeDublicatesO(arr)
