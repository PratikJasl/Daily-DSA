//Leetcode: 55: Jump Game

//Input: nums, initialy at first index.
//Output: if you can reach the end or not.

//approach: O(n)
//Step1: Target is to reach last index.
//Step2: Loop through the array from end.
//Step3: Check if the last element can reach target.
//Step4: if it can update the target to i.
//Step5: if we are able to reach till first element, return true else false.

var canJump = function(nums) {
    let target = nums.length-1;
    for(let i = nums.length-1; i >= 0; i--){
        if(i + nums[i] >= target){
            target = i;
        }
    }
    return target === 0;
};