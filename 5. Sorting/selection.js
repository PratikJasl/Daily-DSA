function selectionSort(arr){
    let n = arr.length;
    for(let i = 0; i < n; i++){
        let minIndex = i;

        //@dev: Iterate the whole loop and find minimum.
        for(let j = i+1; j < n; j++){
            if(arr[j] < arr[minIndex]){
                minIndex = j
            }
        }
        //@dev: Swap the minimum and ith element.
        if(minIndex !== i){
            let temp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = temp
        }
    }
    console.log(arr);
}

selectionSort([8,4,6,7,1,5,3,2]);
