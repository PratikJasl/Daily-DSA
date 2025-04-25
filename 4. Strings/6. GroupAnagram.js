//Leetcode: 49: Group Anagrams
//https://leetcode.com/problems/group-anagrams/

//Approach1: 
 //Step1: Loop through the strings.
 //Step2: Create a sorted string variable.
 //Step3: if soreted string is not in map, add it to the map with an empty array.
 //Step4: Get the empty array using sorted string and push the original string inside.
 //Step5: Create an array of the map values and return it.

function groupAnagrams(strs){
    let map = new Map();
    
    for (let str of strs) {
        // Sort the string to use as the key
        let sortedStr = str.split('').sort().join('');
        
        // If the key doesn't exist, create a new array for it
        if (!map.has(sortedStr)) {
            map.set(sortedStr, []);
        }
        
        // Push the original string into the array of its sorted counterpart
        map.get(sortedStr).push(str);
    }
    
    // Convert map values to an array and return
    return Array.from(map.values());
}