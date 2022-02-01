prices = [7,1,5,3,6,4]


#----------------------------------------------#
maxvalue = 0
for buy in prices:
    for sell in prices:
        if (sell - buy) > maxvalue:
            maxvalue = (sell - buy)
            #print(maxvalue, sell, buy)
        
#----------------------------------------------#

buy = 0
sell = buy + 1
maxvalue = 0

for buy in range(len(prices)):
    for sell in range(len(prices)):
        #print(sell)
        if prices[sell] - prices[buy] > maxvalue:
            maxvalue = prices[sell] - prices[buy]
            #print(maxvalue, sell, buy)

#----------------------------------------------#


#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735550/Python-Javascript-Easy-solution-with-very-clear-Explanation

buy = 0
sell = 1
maxvalue = 0

while sell < len(prices):
    profit = prices[sell] - prices[buy]
    
    if prices[buy] < prices[sell]:
        maxvalue = max(profit, maxvalue)
    else:
        buy = sell
    sell += 1
    
print(maxvalue)