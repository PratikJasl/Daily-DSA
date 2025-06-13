//Q: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

//Input: arr = [2,3,5] , sum = 5
//Output: 2

//Approach:  T:O(2n) | S: O(1)
//Step1: Point the left and right pointer at arr[0], and make sum as arr[0]
//Step2: Check if Sum is equal to K, if yes update MaxLen
//Step3: If Sum is greater than K, substract left from sum and increment it till sum is less than K.
//Step4: if Sum is less than k, increment Right and add right to sum.

function LongestSubArray(arr, k){
    let maxLen = 0;
    let left = 0;
    let right = 0;
    let sum = arr[0];

    while(right < arr.length){
        while(left <= right && sum > k){
            sum -= arr[left];
            left++;
        }

        if(sum == k){
            maxLen = Math.max(maxLen, right-left+1);
        }

        right++
        if(right < arr.length) sum += arr[right];
    }

    console.log(maxLen);
    return maxLen;
}

LongestSubArray([1,5,2,3], 7);