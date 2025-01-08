//LeetCode: 121: Best Time To Buy And Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


//Approach: O(n)
//Step1: iterate through the loop.
//Step2: compare the minprice with i to determine the min price.
//Step3: Sell the stock and check the profit.

var maxProfit = function(prices) {
    let minPrice = prices[0];
    let maxProfit = 0;
    if(prices.length < 2) return 0;

    for(let i = 1; i < prices.length; i++){
        minPrice = Math.min(minPrice, prices[i]);

        let max = prices[i] - minPrice;

        if( max > maxProfit){
            maxProfit = max;
        }
    }
    return maxProfit;
};