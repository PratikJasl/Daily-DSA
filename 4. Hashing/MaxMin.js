//Write a function to find the highest occuring element in an array.

//Approach: Using Hash
//Step1: Create a frequency map.
//Step2: iterate over the map.
//Step3: compare value with maxFrequency
//Step3: if more push value inside array.

let arr = [1,2,1,3,3,4,4,5,2,2,2];
let map = new Map();
let count = 1;
let maxFrequency = 0;
let leastFrequecy = 1;
let mostFrequent = [];
let leastFrequent = [];

function countFrequency(arr){
    for(let i = 0; i < arr.length; i++){
        if(!map.has(arr[i])){
            map.set(arr[i], count);
        }else{
            map.set(arr[i], map.get(arr[i])+1)
        }
    }
    console.log(map);

    map.forEach((value, key) => {
        if(value > maxFrequency){
            maxFrequency = value
            mostFrequent = [key];
        }else if(value == maxFrequency){
            mostFrequent.push(key);
        }
    })

    map.forEach((value, key) => {
        if(value <= leastFrequecy){
            leastFrequecy = value
            leastFrequent = [key];
        }else if(value == maxFrequency){
            leastFrequent.push(key);
        }
    })
    console.log(mostFrequent, leastFrequent)
}

countFrequency(arr)