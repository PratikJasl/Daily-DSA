

//Approach1: 

var groupAnagrams = function(strs) {
    let output = [];
    function validAnagram(left,right, strs){
        let temp = []
        while(left >= 0 && right < strs.length){
            if(strs[left].split('').sort().join() === strs[right].split('').sort().join()){
                temp.push(strs[right]);
                right++;
            }else{
                right++;
            }
        }
        return temp;
    }

    function validateExist(longestVal){
        if(output.length < 1) return true
        let j = 0;
        for(let i = 0; i < output.length; i++){
            if(longestVal[i] === output[j][i]){
                return false;
            }
            j++;
        }
    }

    for(let i = 0; i < strs.length; i++){
        let longestVal = validAnagram(i, i , strs);
        console.log("longestVal:", longestVal);
        if(validateExist(longestVal)){
            output.push([longestVal])
        }
    }
};  