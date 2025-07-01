from typing import List

def maxProfit(prices: List[int]) -> int:
  min_price = prices[0]
  max_profit = 0
  
  for i in range(0, len(prices)):
    current_price = prices[i]
    profit = current_price - min_price
    
    if current_price < min_price:
      min_price = current_price
      
    if profit > max_profit:
      max_profit = profit
  
  return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4])) # Output: 5
print(maxProfit([7,6,4,3,1])) # Output: 0