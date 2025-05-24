//@dev: Quick Sort can sort elements in both ascending and descending order with little modifications.

//Step1: Pick a pivot place it in the correct place.

//Step2: place all the elements smaller to pivot to left and all the elements greater than pivot to right.

//Step3: repeat step 1 & 2

function quickSort(arr, low = 0, high = arr.length - 1) {
    if (low < high) {
        const pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
    return arr;
}