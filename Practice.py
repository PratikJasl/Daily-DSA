#Array union

arr1 = [1,2,3,7,4]
arr2 = [2,2,3,5,6]

def arrayUnion(num1, num2):
    combined = num1 + num2
    unique = set(combined)
    return list(unique)

print(arrayUnion(arr1, arr2))