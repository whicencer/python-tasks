def isPowerOfTwo(n: int, step: int = 0) -> bool:
  if 2 ** step > n:
    return False
  elif 2 ** step == n:
    return True
  
  return isPowerOfTwo(n, step + 1)

print(isPowerOfTwo(1)) # True
print(isPowerOfTwo(16)) # True
print(isPowerOfTwo(3)) # False