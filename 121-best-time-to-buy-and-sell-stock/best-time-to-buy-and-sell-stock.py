class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pos = 0
        l = len(prices)
        max_pos = 1
        diff = 0
        
        for i in range(0,len(prices) - 1):
            if(prices[min_pos] >= prices[max_pos]):
                min_pos = max_pos 
                max_pos += 1
            elif(prices[min_pos] < prices[max_pos]):
                if diff < (prices[max_pos] - prices[min_pos]):
                    diff = (prices[max_pos] - prices[min_pos])

                max_pos +=1
                
        return diff
