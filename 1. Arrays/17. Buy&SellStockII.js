//Leetcode: 122: Best Time to Buy and Sell Stock II

//input: prices
 //output: maxprofit you can buy and sell multiple times.

 //Appraoch: O(n)
 //Step1: loop thourgh the array from with left and right pointer.
 //Step2: check if left is less than right.
 //Step3: calculate the profit.
 //Step4: increment left and right.

 var maxProfit = function(prices) {
    if(prices.length < 2) return 0;
    let left = 0;
    let right = 1;
    let profit = 0
    while(left < right && right < prices.length){
        if(prices[left] < prices[right]){
            profit = profit + prices[right] - prices[left];
            left++;
            right++
        }else{
            left++;
            right++
        }
    }
    return profit;
};