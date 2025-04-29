//Count the frequency of occurance of elements of an array.
let arr = [1,2,1,3,3,4,4,5,2, 2]

function countFrequency(arr){
    let map = new Map();
    let count = 0;
    let maxFrequency = 0;
    let leastFrequency = 1;
    let mostFrequentElements = [];
    let leastFrequentElements = [];
    //Create frequency map.
    for (let i = 0; i < arr.length; i++){
        if(!map.has(arr[i])){
            map.set(arr[i], count+1);
        }else{
           map.set(arr[i], map.get(arr[i]) + 1) 
        }
    }
    console.log(map);

    //Return highest occuring.
    map.forEach((count, element ) => {
        if(count > maxFrequency){
            maxFrequency = count;
            mostFrequentElements = [element]; 
        }else if(count === maxFrequency){
            mostFrequentElements.push(element);
        }
    })
    console.log(mostFrequentElements);

    //Return lowest occuring.
    map.forEach((count, element ) => {
        if(count <= leastFrequency){
            leastFrequency = count;
            leastFrequentElements = [element]; 
        }else if(count === leastFrequency){
            leastFrequentElements.push(element);
        }
    })
    console.log(leastFrequentElements);
}
countFrequency(arr)

//Find Highest and lowest frequency element.