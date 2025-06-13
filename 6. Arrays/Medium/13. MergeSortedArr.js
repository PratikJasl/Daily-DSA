//Leetcode: 88: Merge Sorted Array: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


//inputs: nums1/nums2, m/n
//objective: merge nums1 and nums2;

//Approach: O(nlogn)
//Step1: loop through nums1 from 'm'.
//Step2: Whenever we encounter a '0'.
//Step3: Replace it with element of nums2.
//Step4: sort the array.

var merge = function(nums1, m, nums2, n) {
    let j = 0;

    for( let i = m; i < nums1.length; i++){
        if(nums1[i] === 0){
            nums1[i] = nums2[j];
            j++;
        }
    }
    
    nums1.sort((a,b)=> a-b);
};