# 121. Best time to Buy and Sell Stocks

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Brute Force:
# Step1: Use nested loop and check all the profit combination.
# Step2: return max profit .

# Optimal Solution: Kadane's Algorith variation
# Step1: Create a min_price and max_profit variable.
# Step2: Iterate through the array.
# Step3: Compute profit,
# Step4: Update min_price and max_profit
def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    min_price = prices[0]
    max_profit = 0

    for i in range(1, n):
        profit = prices[i] - min_price

        max_profit = max(profit, max_profit)

        min_price = min(prices[i], min_price)
    
    return max_profit

# Optimal Solution: Using Two Pointers
# Step 1: Create left and right pointers.
# Step 2: If price of left is less than right, then calculate profit and move only right
# Step 3: If price of left is more than right, move both left and right.

