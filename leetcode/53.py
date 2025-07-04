from typing import List

def maxSubArray(nums: List[int]) -> int:
  n = len(nums)
  dp = [0] * n
  dp[0] = nums[0]
  
  for i in range(1, n):
    dp[i] = max(nums[i], nums[i] + dp[i - 1])
  
  return max(dp)

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6 (subarray [4,-1,2,1] has the largest sum = 6)
print(maxSubArray([1]))  # Output: The subarray [1] has the largest sum 1.
print(maxSubArray([5, 4, -1, 7, 8]))  # Output: 23 (subarray [5,4,-1,7,8] has the largest sum = 23)