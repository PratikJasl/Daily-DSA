//Q: Given an array of N integrers, left rotate the array by one place.

//Input: [1,2,3,4,5]
//Output: [2,3,4,5,1]

//Approach: T: O(N) | S: O(1)
//Step1: Use the splice operator from 1 to end.
//Step2: We add the spliced part to the front of the array.

function LeftRotateBy1(arr){

    let newArr = arr.splice(1);
    arr.unshift(...newArr);

}

LeftRotateBy1([1,2,3,4,5]);