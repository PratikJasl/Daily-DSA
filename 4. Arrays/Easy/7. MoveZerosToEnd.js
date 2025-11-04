//Q: You are given an array of integers, your task is to move all the zeros in the array to the end of the array
// and move non-negative integers to the front by maintaining their order.


//Input: [1,0,2,3,0,4,0,1]
//Output: [1,2,3,4,1,0,0,0]


//Approach:Brute Force T:O(n) | S:O(n)
//Step1: Iterate through the array and move all non-zeros to a new array.
//Step2: Keep a count of the zeros.
//Step3: add zeros to the new array.

// function MoveZerosToEnd(arr){
//     let temp = [];
//     let count = 0;
//     for(let i = 0; i < arr.length; i++){
//         if(arr[i] !== 0){
//             temp.push(arr[i]);
//         }else{
//             count++;
//         }
//     }

//     while(count >=0 ){
//         temp.push(0);
//         count--;
//     }

//     return temp;
// }



//Approach: Optimal: Two Pointer
//Step1: Point "j" to the first zero and "i" to "j+1"
//Step2: Whenever you find i != 0 swap i and j and increment them.
//Step3: Whenever i==0 only increment i.

function MoveZerosToEnd(arr){
    let j = -1;
    
    //@Dev: Point "j" to first zero.
    for(i = 0; i < arr.length; i++){
        if(arr[i] == 0){
            j = i;
            break;
        }
    }

    //@dev: No non-zero elements
    if (j === -1) return arr;

    //@dev: swap when we find a zero at i
    for(let i = j + 1; i < n; i++) {
        if (a[i] !== 0) {
            [a[i], a[j]] = [a[j], a[i]];
            j++;
        }
    }
    
    return a;
}

console.log(MoveZerosToEnd([1,0,2,3,0,4,0,1]));