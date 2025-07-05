from typing import List
from collections import Counter

def findLucky(arr: List[int]) -> int:
  res = []
  frequency = Counter(arr)
  
  for i in frequency.items():
    if i[0] == i[1]:
      res.append(i[0])
  
  return max(res) if res else -1

print(findLucky([2, 2, 3, 4]))  # Output: 2
print(findLucky([1,2,2,3,3,3]))  # Output: 3
print(findLucky([2,2,2,3,3]))  # Output: -1