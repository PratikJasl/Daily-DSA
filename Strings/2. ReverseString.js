//Leetcode: 344: Reverse String: https://leetcode.com/problems/reverse-string/description/

// Write a function that reverses a string. The input string is given as an array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory.


// Example 1:

// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]

//Approach1: O(n)
//Use build in function.
var reverseString = function(s) {
    s.reverse();
};

//Approach2: O(n)
// reverse using for loop.
function reverseString(s){
    let reversed = []
    for(let i = s.length-1; i >=0; i--){
        reversed.push(s[i]);
    }
    return reversed;
}

console.log(reverseString(["h","e","l","l","o"]));
 