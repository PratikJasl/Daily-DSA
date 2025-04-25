//Approach: O(n)
 //Step1: Create a Set, a maxCount and a left and right pointer variable.
 //Step2: Iterate through the string till right is less than length.
 //Step3: If element does not exist in set add it to set and increment right and count.
 //Step4: If element does not exist delete the first element, and increment left.

 var lengthOfLongestSubstring = function(s) {
    if(s.length < 1) return 0;
    let set = new Set();
    let maxCount = 0;
    let left = 0;
    let right = 0;

    while (right < s.length){
        let letter = s[right]
        if (!set.has(letter)){
            set.add(letter);
            maxCount = Math.max(maxCount, set.size);
            right++;
        }else{
            set.delete(s[left]);
            left++;
        }
    }
    return maxCount;
};