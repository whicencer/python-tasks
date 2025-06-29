from typing import List

def missingNumber(nums: List[int]) -> int: # O(n^2)
  total_sum = len(nums) * (len(nums) + 1) / 2
  
  for num in nums:
    total_sum -= num
  
  return int(total_sum)

print(missingNumber([3, 0, 1]))              # Output: 2
print(missingNumber([0, 1]))                 # Output: 2
print(missingNumber([9,6,4,2,3,5,7,0,1]))    # Output: 8
print(missingNumber([0,1,2,3,4,5,6,7,8,9]))  # Output: 10