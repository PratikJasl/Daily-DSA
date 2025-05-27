//Q: Given an array of integers nums, return the value of the largest element in the array
//Input: array of integers
//Output: largest integer in the array

//Approach: T: O(n) | S: O(1)
//Step1: Create a variable to store the largest element, initialized to the first element of the array.
//Step2: Iterate through the array starting from the second element.
//Step3: Compare each element with the largest element.
//Step4: If the current element is larger than the largest element, update the largest element.


function largestElement(nums) {
    let largest = nums[0];
    let n = nums.length;

    if(n <= 0) return "Empty Array";
    if(n <= 1) return nums[0];

    for (let i = 1; i < n; i++){
        if(nums[i] > largest){
            largest = nums[i];
        }
    }

    console.log("Largest element is:", largest);
    return largest;
}

console.log(largestElement([1]));