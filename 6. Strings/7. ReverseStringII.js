//LeetCode: 541. Reverse String II: https://leetcode.com/problems/reverse-string-ii/

//Problem: Given a string s and an integer k, reverse the first k characters for every 2k 
// characters counting from the start of the string.

//Example:
//Input: s = "abcdefg", k = 2
//Output: "bacdfeg"

//Approach: Sliding window O(n^2)
//Step1: create a fixed size window uing left and right.
//Step2: swap the first 2 elements then skip to 2*K index.
//Step3: Add i+k-1 to get the correct right pointer.
//Step4: Repeat the steps

var reverseStr = function(s, k) {
    output = s.split('');
    let count = 0;
    function swap(left, right, s, k){
        while(left < right){
            let temp = s[right];
            output[right] = s[left];
            output[left] = temp;
            right--;
            left++;
        }
    }

    for(let i = 0; i < s.length; i += 2*k){
        let left = i;
        let right = Math.min( i+k-1, s.length-1);
        swap(left, right, s, k);
    }
    console.log('output:', output);
    return output.join('')
};