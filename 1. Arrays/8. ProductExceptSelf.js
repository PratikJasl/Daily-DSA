//Leetcode: 238: Product of Array Except Self: https://leetcode.com/problems/product-of-array-except-self/description/

//Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// Example 1:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]

// Example 2:
// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

//Brute Force: O(N^2)
//Write two for-loops, start at zero and get a product of everything expect when i == j;

// Approach 2: Sliding window : O(n)/O(n^2)
//Step1: Create a function which will expand outwards from center.
//Step2: While expanding outwards calculate the product.
//Step3: push the product inside an array.


function productExceptSelf(nums){
    let answer = [];
    let arrLen = nums.length;

    function expandOutwards(left, right){
        let product = 1;
        while(left >= 0 && right <= arrLen-1){
            if(left === 0){
                right ++;
                if(right <= arrLen - 1){
                    product = product * nums[right];
                    console.log('line 28:', left, right, product);
                }
            }else if(right === arrLen-1){
                left--;
                product = product * nums[left];
                console.log('line 33:', left, right, product);
            }
            else{
                left--;
                right++;
                product = product * nums[left] * nums[right];
                console.log('line 39:', left, right, product);
            }
        }
        return product;
    }

    for(let i = 0; i < arrLen; i++){
        let res = expandOutwards(i,i);
        answer.push(res);
    }

    return answer;
}
console.log(productExceptSelf([-1,1,0,-3,3]));
//[1,2,3,4] l=2,r=2 arrlen = 3
//answer = [24,]