//LeetCode: 189 : https://leetcode.com/problems/rotate-array/description/
//Question: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3 n = 7
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

//Approach:1
//Step1: splice the last 3 characters of the array and store it in a variable.
//Step2: Add it to the front.

function rotateArray(nums, k){
    k = k % nums.length; //this is added to prevent the cases where nums.length is greater than K
    let res = nums.splice(nums.length - k);
    nums.unshift(...res);
}

console.log(rotateArray([-1,-100,3,99],2));


