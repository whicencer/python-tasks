from typing import List

def containsDuplicate(nums: List[int]) -> bool:
  hash_set = set()
  
  for num in nums:
    if num in hash_set:
      return True
    hash_set.add(num)
  return False
  
print(containsDuplicate([1, 2, 3, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4]))  # Output: False