//Q: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

//Input: [1, 1, 0, 1, 1, 1]
//Output: 3

//Approach: T: O(n) | S: O(1)
//Step1: Maintain a count and max-count variable.
//Step2: Iterate through the array, whenever you find 1 increment count else update max and reset count.
//Step3: Return max count after the loop.

function ConsecutiveOnes(arr){
    let count = 0;
    let maxCount = 0;

    for(let i = 0; i < arr.length; i++){
        if(arr[i] == 1){
            count ++;
        }else{
            count = 0;
        }

        maxCount = Math.max(maxCount, count);
    }

    return maxCount;
}

console.log(ConsecutiveOnes([1, 1, 1, 1, 1, 1]));