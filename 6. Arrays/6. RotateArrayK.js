//LeetCode: 189 : https://leetcode.com/problems/rotate-array/description/
//Q: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

// Input: [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

//Approach: T: O(n) | S: O(1)
//Step1: Calculate the K value of shifting. by moduling it with arr.length. to avaoid cases where K is greater than arr.length.
//Step2: Splice from 

function rotateArray(nums, k){

    k = k % nums.length;
    let res = nums.splice(nums.length - k);
    nums.unshift(...res);
    
}

console.log(rotateArray([-1,-100,3,99],2));


