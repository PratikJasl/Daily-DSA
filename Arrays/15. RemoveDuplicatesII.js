//Leetcode: 80: Remove Duplicates from Sorted Array II

//Input: nums
//Output: 1. modify nums, it should hold uniques appearing only twice. 2. return count.

//Approach: O(nlogn)
//Step1: Loop through the array.
//Step2: create a map to count the occurace of elements.
//Step3: Loop through the array.
//Step4: When ever an element with count more than 2 is encountered make it infinity, reduce the count.
//Step5: Sort the array at the end.

var removeDuplicates = function(nums) {
    let map = new Map();
    let count = 0;
    for(let i = 0; i < nums.length; i++){
        if(!map.has(nums[i])){
            map.set(nums[i], 1);
        }else{
            map.set(nums[i], map.get(nums[i]) + 1);
        }
    }

    for(let i = 0; i < nums.length; i++){
        console.log(map.get(nums[i]));
        if(map.get(nums[i]) > 2){
            map.set(nums[i], map.get(nums[i]) - 1);
            nums[i] = Infinity;
        }else{
            count++;
        }
    }
    nums.sort((a,b)=> a-b);
    return count;
};
