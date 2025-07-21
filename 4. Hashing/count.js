//Count the frequency of occurance of elements of an array.
let arr = [1,2,1,3,3,4,4,5,2,2,2]

function countFrequency(arr){
    let count = 0;
    let map = new Map();
    for(let i = 0; i < arr.length; i++){
        if(!map.has(arr[i])){
            map.set(arr[i], count+1);
        }else{
            map.set(arr[i], map.get(arr[i])+1);
        }
    }
    console.log(map);
    return map;
}

countFrequency(arr)

