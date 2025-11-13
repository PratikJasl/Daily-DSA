//Leetcode: 383: Ransom Note

//Approach: O(N)
//Step1: Create a map of magazine with element count.
//Step2: Loop through ransomNote string.
//Step3: Every time an element of ransom is found in map, reduce its count.
//Step4: Return false if an element is not found or its count became < 0.

var canConstruct = function(ransomNote, magazine) {
    let map = new Map();
    
    for(let i = 0; i < magazine.length; i++){
        let count = 1;
        if(!map.has(magazine[i])){
            map.set(magazine[i], count);
        }else{
            map.set(magazine[i], map.get(magazine[i])+1);
        }
    }
    console.log(map)
    for(let i = 0; i < ransomNote.length; i++){
        if(map.has(ransomNote[i]) && map.get(ransomNote[i]) > 0){
            map.set(ransomNote[i], map.get(ransomNote[i])-1);
        }
        else{
            return false;
        }
    }
    return true;
};