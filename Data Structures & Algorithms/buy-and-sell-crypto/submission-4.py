class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #Left is buy and right is sell
        maxP=0

        while r< len(prices):
            #isprofitable?
            if prices[l]<prices[r]:
                profit =prices[r]-prices[l]
                maxP=max(profit,maxP)
            else:
                l=r
            r+=1
        return maxP

        