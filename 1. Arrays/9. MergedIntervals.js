//Leetcode: 56: Merge Intervals : https://leetcode.com/problems/merge-intervals/

// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of 
// the non-overlapping intervals that cover all the intervals in the input.

// Example 1:

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

/*
Approach1: O(nlogn)
Step1: sort the array based on 1st indexes.
Step2: compare the last index of an interval with the first index of the next interval.
Step3: If the last index of the first interval is greater, than update the last index.
Step4: Loop thourgh the whole loop.
*/



var merge = function(intervals) {
    if (intervals.length == 0) return [];
    //sort array in ascending order.
    intervals.sort((a,b)=> a[0]-b[0]);

    let output = [intervals[0]];

    for(let i = 1; i < intervals.length; i++){
        let lastinterval = output[output.length-1];
        if(lastinterval[1] >= intervals[i][0]){
            lastinterval[1] = Math.max(lastinterval[1], intervals[i][1]);
        }
        else{
            output.push(intervals[i]);
        }
    }
    return output;
};