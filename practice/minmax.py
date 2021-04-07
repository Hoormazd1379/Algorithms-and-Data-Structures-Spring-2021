import sys

A = []
for line in sys.stdin:
 for a in line.split( ):
   A.append(int(a))

min = None
max = None

for a in A:
 if min == None or a < min:
  min = a
 if max == None or a  > max:
  max = a 

print ('min = ', min)
print ('max = ', max)

