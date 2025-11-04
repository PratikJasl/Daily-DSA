//Leetcode: 461: Hamming Distance: https://leetcode.com/problems/hamming-distance/description/

// The Hamming distance between two integers is the number of positions at which 
// the corresponding bits are different.
// Given two integers x and y, return the Hamming distance between them.

 
// Example 1:
// Input: x = 1, y = 4
// Output: 2
// Explanation:
// 1   (0 0 0 1)
// 4   (0 1 0 0)
//        ↑   ↑
// The above arrows point to positions where the corresponding bits are different.

//Approach: O(n)
//Step1: convert the given number to a binary format using "toString()"
//Step2: If the length of the two is not equal add zero to front and make them of equal lenght.
//Step3: iterate through the bits and count how many bits are not equal.

function hammingDistance(x,y){
    x = x.toString(2);
    y = y.toString(2);
    let count = 0;

    //make sure both bits are of equal length.
    if(x.length != y.length){
        if(x.length < y.length){
            while(x.length != y.length) x = "0" + x;
        }else{
            while(x.length != y.length) y = "0" + y;
        }
    }
    //Check for difference count.
    for(let i = 0; i < x.length; i ++){
        if(x[i] != y[i]){
            count++;
        }
    }
    return count;
}