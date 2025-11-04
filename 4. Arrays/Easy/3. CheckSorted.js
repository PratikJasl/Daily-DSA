//Q: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not.
// If the array is sorted then return True, Else return False.

//Input: array of integers
//Ouput: boolean

//Approach: T: O(n) | S: O(1)
//Step1: Create a boolean to determine array is sorted or not.
//Step2: Ierate through the array and check if the elements are in asec.
//Step3: If all are in ascending return true.
//Step4: Repeat the same for descending.



function checkSorted(arr){
    let asc = true;
    let desc = true;
    let n = arr.length;

    for(let i = 0; i < n-1; i++){
        if(!(arr[i] <= arr[i+1])){
            asc = false;
        }
    }

    if (asc == true) return true;

    for(let i = 0; i < n-1; i++){
        if(!(arr[i] >= arr[i+1])){
            desc = false;
        }
    }

    if (desc == true ) return true;
    return false;
}

console.log(checkSorted([7,6,5,4,3,2,1]));