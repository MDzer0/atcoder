a, b, x, y = map(int, input().split())

y = min(2*x, y)
if a<=b:
  print(x+(b-a)*y)
else:
  print(x+(a-b-1)*y)
