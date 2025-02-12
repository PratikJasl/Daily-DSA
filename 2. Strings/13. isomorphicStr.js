 //Leetcode: 205: Isomorphic String
 
 //Approach: O(N)
 //Step1: create a map.
 //Step2: Loop through the string
 //Step3: if the value and key is not already present add it to the map.
 //Step4: if the key is not present but value is already in map return fasle.
 //Step5: if key is already present but a new value is getting added return false
 
 var isIsomorphic = function(s, t) {
    if (s.length !== t.length) return false;

    let map = new Map();

    for(let i = 0; i < s.length; i++){
        let key = s[i];
        let value = t[i];

        if(!map.has(key)){ //Checks if key is not present already.
            if(! Array.from(map.values()).includes(value)){ //Checks if value is not already present.
                map.set(key, value);
            }else{
                return false;
            }
        }else{
            let existingVal = map.get(key); //if an existing key is found it should have the same value.
            if(existingVal != value){
                return false;
            }
        }
    }
    return true;
};