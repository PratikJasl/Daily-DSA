//Leetcode: 58: Length of Last Word

//Input: s
//Output: Return length of last word.

//Approach: O(n)
//Step1: Trim the white-space
//Step2: split the string into an array.
//Step3: Return the length of last element in the array.

var lengthOfLastWord = function(s) {
    let str = s.trim();
    let arr = str.split(" ");
    return (arr[arr.length-1]).length;
};