from math import *
u=0
d=0
c=0
m=0
z=10
#for i in range(10):
while z==10:
  u=u+1
  if u==9:
    u=0
    d=d+1
    if d==9:
      d=0
      c=c+1
      if c==9:
        c=0
        m=m+1

  print(str(m)+str(c)+str(d)+str(u))

   