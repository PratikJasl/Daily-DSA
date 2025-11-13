//Missing Number Leetcode: 268 : https://leetcode.com/problems/missing-number/

//Approach 1: O(logn)
//Step1: create an array of size n+1 and fill it with -1.
//step2: iterate over ther new array and fill it with elements where index matches value.
//Step3: iterate over the array and return -1 index.

var missingNumber = function(nums) {
    let n = nums.length;
    let temp = new Array(n+1).fill(-1);

    for(let i = 0; i < nums.length; i ++){
        temp[nums[i]] = nums[i];
    }
    
    for(let i = 0; i < temp.length; i++){
        if(temp[i] === -1) return i;
    }
    return 0;
};