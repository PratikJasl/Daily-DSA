//Leetcode: 26 : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

//remove duplicates from a sorted array, and return number of unique elements. Make changes to the original array.

// Input: nums = [1,1,2]
// Output: 2, nums = [1,2,_]

//Approach: T: O(n) | S: O(1)
//Step1: Maintain a varible, starting at zero.
//Step2: Iterate through the array from zero.
//Step3: Compare if index of an element is equal to i.
//Step4: When ever index of element and I are equal it means its a unique, replace k with unique and increment k.

function removeDuplicate(nums){
    let k = 0;

    for(i = 0; i < nums.length; i++){
        if(nums.indexOf(nums[i]) === i){
            nums[k] = nums[i];
            k++;
        }
    }
    
    return k;
}

//Approach2: T: O(N) | S: O(1)  BEST SOLUTION
//Step1: Maintain 2 pointers i=0/j=1
//Step2: Iterate through the loop and whenever arr[i] and arr[j] are different, replace arr[i] and increment i.
//Step3: At the end return i+1

function removeDuplicates(arr) {
  let i = 0;

  for (let j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j];
    }
  }

  return i + 1;
}
