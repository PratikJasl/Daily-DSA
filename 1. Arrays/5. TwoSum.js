//Leet code: 1 : Two Sum : https://leetcode.com/problems/two-sum/

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

//Approach 1: O(n) - This approach fails for negative no's
//Step1: iterate through the loop and compare right and left pointer.
//Step2: if they add up to the target return left and right.
//Step3: Else if sum of left and right is less than target move left forward else move right backward.

function TwoSum(nums, target){
    let right = nums.length - 1;
    let left = 0;

    while(left < right){
        console.log(nums[left] + nums[right]);
        if( nums[left] + nums[right] === target){
            return [left, right];
        }
        else if(nums[left] + nums[right] < target){
            left ++;
        }
        else{
            right --;
        }
    }
}

//Approach 2: O(n)
//Step1: Create a Map and iterate through the array.
//Step2: if target - nums[i] exist inside the map return index.
//Step3: Else add it inside the map.

//Two values adds up to get target, this approach works by finding the difference between a value and target resulting in the second value.

function twoSum(nums, target){
    let map = new Map();
    
    for (let i = 0; i < nums.length; i++){
        const compliment = target - nums[i];

        if(map.has(compliment)){
            return(i, map.get(compliment));
        }
        else{
            map.set(nums[i], i);
        }
    }
}