
function BubbleSort(arr){
    let n = arr.length;
    let swapped;
    do {
        swapped = false
        for(let i = 0; i < n-1; i++){
            if(arr[i] > arr[i+1]){
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp;
                swapped = true;
            }
        }
        n--; 
    } while (swapped);
    console.log(arr)
}

BubbleSort([12,14,14,7,67,27]);