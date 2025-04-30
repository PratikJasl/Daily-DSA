
function InsertionSort(arr){
    let n = arr.length;
    for(let i = 1; i < n; i++){
        let j = i-1;
        let current = arr[i]
        //@dev: Shift the element to the right.
        while(j>=0 && arr[j] > current){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = current;
    }
    console.log(arr);
}

InsertionSort([8,3,1,9,7,2,4,5,6])