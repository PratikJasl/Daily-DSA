//To find the maximum sum of all subarrays of size K:
//Using Sliding Window with constant size.

//Explanation: https://www.geeksforgeeks.org/window-sliding-technique/

//Approach: O(n) Sliding Window
 //Step1: create a set to hold the unique elements.
 //Step2: Iterate through the array and add a element to the set when a unique is encountered, and update the sum.
 //Step3: If the window size is equal to k, update the result, and remove the last element from the window update sum, and left.
 //Step4: If an element already exist, remove all the duplicates it has by moving the left pointer.
 
 var maximumSubarraySum = function(nums, k) {
    const n = nums.length;
    const elements = new Set();
    let sum = 0, answer = 0, left = 0;

    for (let right = 0; right < n; right++) {
        const current = nums[right];

        if (!elements.has(current)) {
            sum += current;
            elements.add(current);

            if (right - left + 1 === k) {
                answer = Math.max(answer, sum);
                sum -= nums[left];
                elements.delete(nums[left]);
                left++;
            }
        } else {
            //Loop removes duplicate elements from the set.
            while (nums[left] !== nums[right]) {
                sum -= nums[left];
                elements.delete(nums[left]);
                left++;
            }
            left++;
        }
    }

    return answer;
};;