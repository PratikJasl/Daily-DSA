//Missing Number Leetcode: 268 : https://leetcode.com/problems/missing-number/


// Approach 1: O(nlogn)
//Step1: Sort the array.
//Step2: take the first element and check if it's the increment of next element.
//Step3: If yes move to next element.
//Step4: if no send it to output.

var missingNumber = function(nums) {
 if(nums.length < 2){
   if(nums[0] === 0){
       return nums[0]+1;
   }else{
       return nums[0]-1;
   }
 }

 nums.sort((a,b) => a-b);
 console.log('Sorted Nums:', nums);
 let miss = nums[0]
 let i = 1;
 let output = 0;
 while(i < nums.length){
   if(miss+1 === nums[i]){
       miss = nums[i];
       i++;
       if(i === nums.length && output === 0 && nums[0] === 0){
           output = miss+1;
       }else if(i === nums.length && output === 0){
           output = 0;
       }
   }else{
       output = miss+1;
       miss = nums[i];
       i++;
   }
 }
 console.log(output);
 return output;  
};