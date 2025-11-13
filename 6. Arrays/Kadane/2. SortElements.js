// Given an array consisting of only 0s, 1s, and 2s. 
// Write a program to in-place sort the array without using inbuilt sort functions.

// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

function sortElements(nums){
    let low = 0;
    let mid = 0;
    let high = nums.length-1;

    while(mid <= high){
        if(nums[mid] == 0){
            let temp = nums[low];
            nums[low] = nums[mid];
            nums[low] = temp;
            low++;
            mid++; 
        }
        else if(nums[mid] == 1){
            mid++;
        }else{
            let temp = nums[high];
            nums[high] = nums[low];
            nums[low] = temp;
            high--;
        }
    }

    return nums;
}

console.log(sortElements([2,0,2,1,1,0]));
