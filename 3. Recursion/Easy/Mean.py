# Calculate the Mean of an array using recursion.

#Approach1: Using parameterised recursion.
sum1 = 0
sum2 = 0
result = 0

def Mean(arr, i = 0):
    global sum1
    if(i >= len(arr)):
        print("The mean of array is:", sum1/len(arr))
        return
    sum1 += arr[i]
    Mean(arr, i+1)

Mean([1,2,3,4,5])


#Approach2: Functional recursion
def Mean2(arr, i=0):
    global sum2
    if( i >= len(arr)):
        return sum2/len(arr)
    sum2 += arr[i]
    return Mean2(arr, i+1)

result = Mean2([1,2,3,4,5])
print("the mean of the array is:", result)