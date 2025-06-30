from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
  n = len(nums)
  tmp, res = [0] * (n + 1), []
  
  for num in nums: tmp[num] = 1
  
  for i in range(1, n + 1):
    if tmp[i] == 0: res.append(i)
  
  return res

print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [5, 6]
print(findDisappearedNumbers([1, 1]))  # Output: [2]