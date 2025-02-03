//leetcode: 28: Find the Index of the First Occurence in a String.


//Input: needle, haystack
//Ouput: index of first occurace of needle.

//Approach1: O(n)
//Step1: check if haystack includes needle.
//Step2: If it does return index using in-built method.

var strStr = function(haystack, needle) {
    let match = haystack.includes(needle);
    
    if(match == true){
        return haystack.indexOf(needle);
    }else{
        return -1;
    }
};