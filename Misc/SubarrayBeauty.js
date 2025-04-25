//Leetcode: 2653: https://leetcode.com/problems/sliding-subarray-beauty/

//Approach: O(nlogn)
//Step1: you iterate through the loop.
//step2: you add the elements to a temp array.
//Step3: when window size is meet, you sort the window and figure out the xth element.
//Step4: delete the left element and move left pointer.

var getSubarrayBeauty = function(nums, k, x) {
    let output = [];
    let temp = [];
    let left = 0;
    let smallest = 100;
    let secondSmallest = 0;
    let arrLen = nums.length;

    for(let right = 0 ; right < arrLen; right++){
        temp.push(nums[right]);
        if (temp.length === k) {
            let sortedTemp = [...temp].sort((a, b) => a - b);  // Sort a copy of the current window
            let beauty = sortedTemp[x - 1];  
            if(beauty >= 0){
                output.push(0);
            }else{
                output.push(beauty);
            }
            temp.shift();  
        }
    }
    return output;
};