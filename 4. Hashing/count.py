#Write a function to count frequency of elements in an array.
arr = [1,2,1,3,3,4,4,5,2,2]
map = {}

def countFrequency(arr):
    for item in arr:
        if item not in map:
            map[item] = 1
        else:
            map[item] += 1
    print(map)
    return map

countFrequency(arr)
