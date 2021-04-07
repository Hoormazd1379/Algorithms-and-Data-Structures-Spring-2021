import sys

A = []
for line in sys.stdin:
 A.append(line)

for a in A:
 i = len(a)
 while i > 0:
  i = i - 1
  print(a[i], end='')

print()


