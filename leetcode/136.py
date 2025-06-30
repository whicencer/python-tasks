from typing import List

def singleNumber(nums: List[int]) -> int:
  hash = set()
  
  for num in nums:
    if num in hash:
      hash.remove(num)
    else:
      hash.add(num)
  
  return hash.pop()

print(singleNumber([2, 2, 1]))  # Output: 1
print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(singleNumber([1]))  # Output: 1

# [1, 2, 2]
# [1, 1, 2, 2, 4]