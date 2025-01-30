//LeetCode: 14. Longest Common Prefix:  https://leetcode.com/problems/longest-common-prefix/
//Problem: Write a function to find the longest common prefix string amongst an array of strings.

//Example 1:
//Input: strs = ["flower","flow","flight"]
//Output: "fl"

 //Approach1: O(n^2)
 //step1: Loop thourgh the first string.
 //Step2: comapre the first letter of the first string with all other strings.
 //Step3: if all the first letters are equal add it to prefix.
 //step4: else check the next letter.
 //Step5 return the prefix at end.

 var longestCommonPrefix = function(strs) {
    let prefix = '';
    if (strs.length < 1) return prefix;

    for(let i = 0; i < strs[0].length; i++){
        const character = strs[0][i];
        for (let j = 0; j < strs.length; j++){
            if(strs[j][i] !== character) return prefix
        }
        prefix += character;
    }

    return prefix
}