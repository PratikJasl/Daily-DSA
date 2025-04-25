//Leetcode: 242: Valid Anagram: https://leetcode.com/problems/valid-anagram/description/

// Given two strings s and t, return true if t is an 
// anagram of s, and false otherwise.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true

 //Approach: O(nlogn)
 //Step1: split the string into an array and sort them.
 //Step2: compare each element and check if they are equal.
 //Step3: return  true or false based on that.

 var isAnagram = function(s, t) {
    if(s.length != t.length) return false;

    if(s.split('').sort().join() === t.split('').sort().join()){
        return true
    }else{
        return false
    }
};