//Q: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

//Input: arr = [-1,1,1] k = 1
//Output: 3

//Approach:
// Step1:
// Step2:
// Step3:



function getLongestSubarray(a, k) {
    let n = a.length;

    let preSumMap = new Map();
    let sum = 0;
    let maxLen = 0;
    for (let i = 0; i < n; i++) {
        // calculate the prefix sum till index i
        sum += a[i];

        // if the sum = k, update the maxLen
        if (sum === k) {
            maxLen = Math.max(maxLen, i + 1);
        }

        // calculate the sum of remaining part i.e. x-k
        let rem = sum - k;

        // calculate the length and update maxLen
        if (preSumMap.has(rem)) {
            let len = i - preSumMap.get(rem);
            maxLen = Math.max(maxLen, len);
        }

        // finally, update the map checking the conditions
        if (!preSumMap.has(sum)) {
            preSumMap.set(sum, i);
        }
    }

    return maxLen;
}

let a = [-1, 1, 1];
let k = 1;
let len = getLongestSubarray(a, k);
console.log("The length of the longest subarray is:", len);


