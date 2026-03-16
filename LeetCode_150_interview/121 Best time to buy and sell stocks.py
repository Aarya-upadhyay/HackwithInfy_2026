class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # To track the minimum price so far
        max_profit = 0  # To track the maximum profit
        
        # Traverse the price list
        for price in prices:
            # Update the minimum price
            if price < min_price:
                min_price = price
            # Calculate profit if selling at current price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit       
