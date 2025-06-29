def fibonacci_sequence(n: int) -> int:
  if n == 0:
    return 0
  
  a = 0
  b = 1
  
  for i in range(2, n + 1):
    tmp = a + b
    a = b
    b = tmp
    
  return b

print(fibonacci_sequence(10))