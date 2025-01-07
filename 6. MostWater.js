//Leet Code: 11 : Container with Most Water: https://leetcode.com/problems/container-with-most-water/description/

//Approach1: O(n)
//Step1: create variables for start and end.
//Step2: calculate volume between the start and end index.
//Step3: Volume = smaller-height * abs(i-j)
//Step4: Compare volume with max volume.
//Step5: Return the max volume.

function containerWithMostWater(height){
    let left = 0;
    let right = height.length -1;
    let volume = 0;
    let maxVolume = 0;
    while (left < right){
        volume = Math.min(height[left], height[right])*Math.abs(left-right);
        if(volume > maxVolume){
            maxVolume = volume;
        }

        if(height[left] > height[right]){
            right --;
        }
        else{
            left ++;
        }
    }
    return maxVolume;
}

console.log(containerWithMostWater([1,1]));
