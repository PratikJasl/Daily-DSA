//Missing Number Leetcode: 268 : https://leetcode.com/problems/missing-number/


// Approach 1: O(nlogn)
//Step1: Sort the array.
//Step2: take the first element and check if it's the increment of next element.
//Step3: If yes move to next element.
//Step4: if no send it to output.

// var missingNumber = function(nums) {
//  if(nums.length < 2){
//    if(nums[0] === 0){
//        return nums[0]+1;
//    }else{
//        return nums[0]-1;
//    }
//  }

//  nums.sort((a,b) => a-b);
//  console.log('Sorted Nums:', nums);
//  let miss = nums[0]
//  let i = 1;
//  let output = 0;
//  while(i < nums.length){
//    if(miss+1 === nums[i]){
//        miss = nums[i];
//        i++;
//        if(i === nums.length && output === 0 && nums[0] === 0){
//            output = miss+1;
//        }else if(i === nums.length && output === 0){
//            output = 0;
//        }
//    }else{
//        output = miss+1;
//        miss = nums[i];
//        i++;
//    }
//  }
//  console.log(output);
//  return output;  
// };

//Approach 2: O(logn)
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