# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#


## 直接A过
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell = 0
        profit = 0
        for  i in range(len(prices)):
            if prices[buy] > prices[i]:  
                buy = i                  #  找最小的买价
                sell = i                 # 买入之后就可以开始卖了
            if prices[sell] < prices[i] : #  找最大的卖价
                sell = i
            if sell > buy:
                profit = max(profit,prices[sell] - prices[buy])
            #print(profit,buy,sell)
        return profit       
        