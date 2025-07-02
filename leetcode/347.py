from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
  counter = dict(Counter(nums))
  
  sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)
  sorted_dict = dict(sorted_list[:k])
  
  return list(sorted_dict.keys())

print(topKFrequent([3,0,1,0,3], 2)) # {1: 3, 2: 2, 3: 1}