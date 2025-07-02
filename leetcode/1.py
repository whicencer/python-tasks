from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  hash = {}
  
  for i in range(len(nums)):
    currentNum = nums[i]
    if currentNum in hash:
      return [hash[currentNum], i]
    
    hash[target - currentNum] = i
  
  return []

print(twoSum([2, 7, 11, 15], 9)) # Output: [0, 1]
print(twoSum([3, 2, 4], 6)) # Output: [1, 2]
print(twoSum([3, 3], 6)) # Output: [0, 1]
print(twoSum([1, 2, 3, 4, 5], 9)) # Output: [3, 4]