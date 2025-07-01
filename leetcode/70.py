def climbStairs(N: int) -> int:
  cache = {}
  def climb(n) -> int:
    if n == 0: return 1
    if n < 0: return 0
    
    if n in cache:
      return cache[n]
    else:
      cache[n] = climb(n - 1) + climb(n - 2)
      
      return cache[n]
  
  return climb(N)

print(climbStairs(2))  # Output: 2 (1 + 1; 2)
print(climbStairs(3))  # Output: 3 (1 + 1 + 1; 1 + 2; 2 + 1)
print(climbStairs(5))  # Output: 8 (1 + 1 + 1 + 1 + 1; 1 + 1 + 1 + 2; ...)