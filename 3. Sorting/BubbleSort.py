# //Approach: compare adjust and swap the largerst to right, after one iteration largest is to the right reduce array size. 

# function BubbleSort(arr){
#     let n = arr.length;
#     let swapped;
#     do {
#         swapped = false
#         for(let i = 0; i < n-1; i++){
#             if(arr[i] > arr[i+1]){
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp;
#                 swapped = true;
#             }
#         }
#         n--; 
#     } while (swapped);
#     console.log(arr)
# }

#In Python:
def BubbleSort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            
        if not swapped:
            break
        n -= 1
    
    print('sorted array:', arr)
    return(arr)

BubbleSort([12,14,14,7,67,27])