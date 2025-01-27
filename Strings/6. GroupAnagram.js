

//Approach1: 

var groupAnagrams = function(strs) {
    // let output = [];
    // let valid = new Set();
    // //Determines the valid anagrams.
    // function validAnagram(left, right, strs){
    //     let temp = []
    //     while(left >= 0 && right < strs.length){
    //         if(strs[left].split('').sort().join() === strs[right].split('').sort().join()){
    //             temp.push(strs[right]);
    //             valid.add(strs[right]);
    //             right++;
    //         }else{
    //             right++;
    //         }
    //     }
    //     return temp;
    // }
    // //Checks if the anagram already exists in the output
    // function validateExist(longestVal){
    //     if(output.length < 1) return true
    //     for(let i = 0; i < longestVal.length; i++){
    //         if(valid.has(longestVal[i])){
    //             return false;
    //         }else{
    //             return true;
    //         }
    //     }
    // }

    // for(let i = 0; i < strs.length; i++){
    //     let longestVal = validAnagram(i, i , strs);
    //     console.log("longestVal:", longestVal);
    //     console.log("Valid:", valid)
    //     if(validateExist(longestVal)){
    //         output.push(longestVal);
    //         console.log('Output', output);
    //     }
    // }

    // return output;
};  


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