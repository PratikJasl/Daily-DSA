//Leetcode: 27: Remove Elements: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

//Approach: O(nlogn)
//Step1: Loop through the array.
//Step2: When ever we encounter val, replace it with '_'.
//Step3: when we do-not encounter val, increment count.

var removeElement = function(nums, val) {
    let count = 0;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] === val){
            nums[i] = Infinity
        }else{
            count++;
        }
    }
    nums.sort((a,b) => a-b);
    return count;
};