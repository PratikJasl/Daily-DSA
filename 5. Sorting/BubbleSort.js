
function BubbleSort(arr){
    let n = arr.length;
    let swapped;
    do {
        swapped = false
        for(let i = 0; i < n; i++){
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

BubbleSort([9,2,7,1,8,5,8]);