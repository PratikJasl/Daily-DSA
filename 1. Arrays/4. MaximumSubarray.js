//Leetcode: 53: Maximum Subarray : https://leetcode.com/problems/maximum-subarray/description/

// Given an integer array nums, find the 
// subarray with the largest sum, and return its sum.


// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.


//Approach: O(n);
//Step1: iterate through the array.
//Step2: calculate sum and compare with max and update max.
//Step3: If sum is less than zero, make it zero.

function maximumSubarray(nums){
    let sum = 0;
    let max = nums[0];

    for(let i = 0; i < nums.length; i++){
        sum += nums[i];
        if(sum > max){
            max = sum;
        }
        if(sum < 0){
            sum = 0;
        }
    }
    return max;
}