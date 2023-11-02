
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    lowPosition = 0

    for i in range(len(prices)):
        if prices[i] < prices[lowPosition]:
            lowPosition = i
        if profit < prices[i] - prices[lowPosition]:
            profit = prices[i] - prices[lowPosition]
    return profit

