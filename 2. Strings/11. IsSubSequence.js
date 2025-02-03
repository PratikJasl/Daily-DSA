 //Leetcode: 392: Is Subsequence. 
 
 //input: s, t
 //output: true/false

 //Approach1: O(n)
 //Step1: loop thorugh the string 't'
 //Step2: when ever we find element in t, increment the pointer.
 //Step3: if we have found all elements before ending the loop it means elements are in sequence.

 var isSubsequence = function(s, t) {
    let index = 0;
    
    for (let i = 0; i < t.length; i++) {
        if (t[i] === s[index]) {
            index++;
        }
        
        if (index === s.length) {
            return true;
        }
    }

    return index === s.length;
};