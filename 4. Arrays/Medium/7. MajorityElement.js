//Leetcode: 168: Majority Element

//Input: nums, n, 
//output: return majority element more than [n/2]

//Approach: O(n)
//Step1: Loop through the array.
//Step2: count the elements in a map.
//Step3: Loop through the array.
//Step4: Check if the element count is more than [n/2], return element.

var majorityElement = function(nums) {
    let map = new Map();
    
    for(let i = 0; i < nums.length; i++){
        if(!map.has(nums[i])){
            map.set(nums[i], 1);
        }else{
            map.set(nums[i], map.get(nums[i]) + 1);
        }
    }

    // console.log(map);
    for(let i = 0; i < nums.length; i++){
        if(map.get(nums[i]) > (nums.length/2)){
            return nums[i]
        }
    }
    return 0;
};