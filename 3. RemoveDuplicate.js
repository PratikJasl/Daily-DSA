//Leetcode: 26 : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

//remove duplicates from a sorted array, and return number of unique elements. Make changes to the original array.

// Input: nums = [1,1,2]
// Output: 2, nums = [1,2,_]

//Approach: O(n)
//Step1: Maintain a varible to hold unique elements.
//Step2: Whenever you encounter a dublicate replace it with unique.

function removeDuplicate(nums){
    let j = 0;
    for(i = 0; i < nums.length; i++){
        if(nums.indexOf(nums[i] === i)){
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}