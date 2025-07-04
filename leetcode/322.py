from typing import List

def coinChange(coins: List[int], amount: int) -> int:
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0
  
  for coin in coins:
    for i in range(coin, amount + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)
  
  return int(dp[amount]) if dp[amount] != float('inf') else -1

print(coinChange([1, 2, 5], 11))  # Output: 3
print(coinChange([2], 3))  # Output: -1