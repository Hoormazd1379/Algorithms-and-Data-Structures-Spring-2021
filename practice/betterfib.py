def F(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  pp = 0
  p = 1
  while n > 1:
   x = p + pp
   pp = p
   p = x
   n = n - 1
  return x
