//Q: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

//Input: {2,2,1}
//Output: 1

//Approach: T:O(N) | S:O(N)
//Step1: Create a map and count frequency
//Step2: Return element with frequence 1.

function AppearingOnce(arr){
    let map = new Map();
    let result = 0;

    for(let i = 0; i < arr.length; i++){
        if(!map.has(arr[i])){
            map.set(arr[i], 1);
        }else{
            map.set(arr[i], map.get(arr[i]) + 1);
        }
    }

    map.forEach((value, key) => {
        if(map.get(key) === 1){
            result = key;
        }
    })

    return result;
}

console.log(AppearingOnce([2,2,1,5,1,1,3,3]));