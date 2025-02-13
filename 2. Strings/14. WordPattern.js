//Leetcode: 290: Word Pattern
 
 
 //Approach: O(n)
 //Step1: Create a hash map.
 //Step2: If an element and key is not present inside add it to the map.
 //Step3: If a value is already inside with other key return false.
 //Step4: If a key is already inside check if it has same value or not.

 var wordPattern = function(pattern, s) {
    let map = new Map();
    let arr = s.split(' ');

    if(arr.length !== pattern.length) return false;

    for(let i = 0; i < pattern.length; i++){
        if(!map.has(pattern[i])){
            if(!Array.from(map.values()).includes(arr[i])){
                map.set(pattern[i], arr[i]);
            }else{
                return false;
            }
        }else{
            if(map.get(pattern[i]) !== arr[i]){
                return false;
            }
        }
    }
    return true;
};