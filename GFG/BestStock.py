#Best Time to Buy and Sell Stock
# Input: prices[] = {7, 1, 5, 3, 6, 4}
# Output: 5
# Explanation:
# The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
# Therefore, maximum possible profit = 6 – 1 = 5. 
class BestStock():
    def __init__(self):
        self.prices = []
    def MaxProfit(self,prices):
        l,r=0,1
        maxP = 0
        while(r<len(prices)):
            if(prices[l]<prices[r]):
                profit = prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    two_sum_instance = BestStock()
    print(two_sum_instance.MaxProfit(prices))
