//Q: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

//Input: arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
//Output: {1,2,3,4,5}

//Approach: Using Map T: O(n) | S: O(n)
//Step1: Add the two arrays
//Step2: Iterate through the added array and create a map.
//Step3: Convert the keys of the map to an array.


function ArrayUnion(arr1, arr2){
    let Unique = new Map();
    let count = 0
    let temp = arr1.concat(arr2);
    
    for( let i = 0; i < temp.length; i++){
        if(!Unique.has(temp[i])){
            Unique.set(temp[i], count+1);
        }else{
            Unique.set(temp[i], Unique.get(temp[i]) + 1); 
        }
    }

    return Array.from(Unique.keys());
}

ArrayUnion([1,2,3,4,5], [2,3,4,4,5]);