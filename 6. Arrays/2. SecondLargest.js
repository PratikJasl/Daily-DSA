//Q: Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

//Input: array of integers
//Output: Second Largest element, or -1.

//Approach:  T: O(n) | S: O(1)
//Step1: Create a variable largest and second largest variable and initialize it -1.
//Step2: Iterate through the array from 0.
//Step3: Compare element with largest, if element is larger than largest, we update the largest and second largest.
//Step4: Else we check if the element is less than largest and greater than second largest, if ues update second largest.

function findSecondLargest(nums){
    let largest = -1;
    let secondLargest = -1;
    let n = nums.length;

    for( let i = 0; i < n;  i++){
        if(nums[i] > largest){
            secondLargest = largest;
            largest = nums[i];
        }else if(nums[i] < largest && nums[i] > secondLargest){
            secondLargest = nums[i];
        }
    }
    
    return secondLargest;
}

console.log(findSecondLargest([2, 10, 5, 6, 8]));