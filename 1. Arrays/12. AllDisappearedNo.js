//Leetcode: 448: Find all numbers disappeared in an Array: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

// Given an array nums of n integers where nums[i] is in the range [1, n], 
// return an array of all the integers in the range [1, n] that do not appear in nums.

// Example 1:

// Input: nums = [4,3,2,7,8,2,3,1]
// Output: [5,6]

//Approach1: O(n)
//step1: Create a set to hold all unique elements.
//Step2: check if range [1-n] exists in the set or not.
//Step3: if it does not exist push it to result/


var findDisappearedNumbers = function(nums) {
    let temp = new Set(nums);
    let result = [];

    for(let i = 1; i < nums.length+1; i++){
          if(!temp.has(i)){
              result.push(i);
          }
    }
    
    return result
  };