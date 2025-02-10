//Leetcode: 167: Two Sum II


//Approach1: Brute Force
 //Step1: uses nested loops to check each combination.

// var twoSum = function(numbers, target) {
//     for(let i = 0; i < numbers.length; i++){
//         for(let j = i+1; j < numbers.length; j++){
//             let output = numbers[i] + numbers[j];
//             if(output === target){
//                 return [i+1, j+1];
//             }
//         }
//     }
// };


//Approach2: 
//Step1: Create a map with all the elements.
//Step2: Sub a value with the traget and check if the result exist. 
//If two elements adds up to be target then target minus one element will give the another.

var twoSum = function(numbers, target) {
    let map = new Map();
    for(let i = 0; i < numbers.length; i++){
        map.set(numbers[i], i);
    }
    console.log(map);

    for(let i = 0; i < numbers.length; i++){
        let compliment = target - numbers[i];
        if(map.has(compliment)){
            return [i+1, map.get(compliment)+1]
        }
    }
};