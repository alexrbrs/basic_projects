from math import *
import random
characters=('[]{}_,→";:%#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ')
out = ''
f = ""
long = int(input())
while long!=0:
  out = random.choice(characters)
  long=long-1
  f+=str(out)
print(f)