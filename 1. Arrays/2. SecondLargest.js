//Find the second largest element in an array. Else return -1.

// Example:
// Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

// Output:  6


//Approach: O(n)
//Step1: Iterate through the array.
//Step2: if the element is greater than max update max. 
//Step3: if it is greater than 2nd max update that.

function findSecondLargest(nums){

    if(nums.length < 2) return -1;
    let largest = -Infinity;
    let secondLargest = -Infinity;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] > largest){
            secondLargest = largest;
            largest = nums[i];
        }else if(nums[i] > secondLargest){
            secondLargest = nums[i];
        }
    }
    
    return secondLargest;
}

console.log(findSecondLargest([2, 10, 5, 6, 8]));


//Approach2: O(nlogn)
//Step1: Sort the array.
//Step2: Return length -2 element.