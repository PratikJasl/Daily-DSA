# //Approach: Find the minimum value and swap it.

# //Time Complexity: O(n^2)
#In JavaScript:
# // function selectionSort(arr){
# //     let n = arr.length;
# //     for(let i = 0; i < n; i++){
# //         let minIndex = i;
# //         //@dev: Iterate the whole loop and find minimum.
# //         for(let j = i+1; j < n; j++){
# //             if(arr[j] < arr[minIndex]){
# //                 minIndex = j
# //             }
# //         }
# //         //@dev: Swap the minimum and ith element.
# //         if(minIndex !== i){
# //             let temp = arr[i]
# //             arr[i] = arr[minIndex]
# //             arr[minIndex] = temp
# //         }
# //     }
# //     console.log(arr);
# // }

#In python:
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
    
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print('Sorted array:', arr)
    return arr


selectionSort([8,4,6,7,1,5,3,2])
