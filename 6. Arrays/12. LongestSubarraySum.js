//Q: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

//Input: arr = [2,3,5] , sum = 5
//Output: 2

//Approach:  




function LongestSubArray(arr, k){
    let max = 0;
    let left = 0;
    let right = arr.length-1;
    arr.sort((a,b) => a-b);

    while(left <= right){
        let sum = 0;
        if(arr[left] == k) max = Math.max(max, 1);
        
        if(arr[right] == k) max = Math.max(max, 1);
        
        for(let i = left; i <= right; i++){
            sum = sum + arr[i];
        }

        if(sum == k) max = Math.max(max, left+right+1);

        if(sum > k){
            right--;
        }else{
            left++;
        }
    }

    console.log(max);
    return max;
}

LongestSubArray([1,5,2,3], 7);