class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1           # Left = Buy, Right = Sell
        maxP = 0              # Track max profit

        while r < len(prices):
            if prices[l] < prices[r]:
                # Valid profit window
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # Not profitable → move l to r (new buy day)
                l = r
            r += 1            # Always move r forward
        return maxP
