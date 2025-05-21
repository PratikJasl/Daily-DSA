//Approach: Divide the array into two halves, sort them and merge them back together.

//@dev: Function to divide the array into two halves and sort them.
function mergeSort(arr, low, high){
    if(low < high) return;
    let mid = Math.floor((low + high) / 2);
    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);
    merge(arr, low, mid, high);
}

//@Dev: Function to merge and sort the two halves.
function merge(arr, low, mid, high){
    let left = low;
    let right = mid+1;
    temp = [];
    //@dev: We take the two halves and compare them, and merge them into a single sorted array.
    while(left <= mid && right <= high){
        if(arr[left] < arr[right]){
            temp.push(arr[left]);
            left++;
        } else {
            temp.push(arr[right]);
            right++;
        }
    }

    //@dev: If there are any elements left in the left half, add them to the temp array.
    while(left <= mid){
        temp.push(arr[left]);
        left++;
    }

    //@dev: If there are any elements left in the right half, add them to the temp array.
    while(right <= high){
        temp.push(arr[right]);
        right++;
    }

    //@dev: Copy the temp array back to the original array.
    for(let i = low; i <= high; i++){
        arr[i] = temp[i - low];
    }
}
