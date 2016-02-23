from math import factorial, pow


def combination(N, n):
  num = factorial(N)
  den = factorial(n) * factorial(N - n)
  print str(N) + '/ ' + str(n)
  return num / den

p = 0.1
N = 35

ans = 0

for i in range(0, 5):
  ans += combination(N, i) * pow(p, i) * pow(1 - p, N - i)

print str(ans) 
