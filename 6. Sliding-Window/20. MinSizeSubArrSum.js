//LeetCode: 209: Minimum Size Subarray Sum

//Approach: O(n^2)
//Step1: Loop through the array and call the expand right pointer.
//Step2: Calculate the sum.
//Step3: If Sum is >= Target, decrease the window size and update sum.
//Step4: keep updating the minLen variable.
var minSubArrayLen = function(target, nums) { 
    let minLen = Infinity;
    let left = 0;
    let sum = 0;

    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        
        // When the current sum >= target, move the left pointer to minimize the window
        while (sum >= target) {
            minLen = Math.min(minLen, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }
    
    return minLen === Infinity ? 0 : minLen;
};