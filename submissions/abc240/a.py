a, b = map(int, input().split())
if abs((a % 10) - abs(b % 10)) == 1 or b - a == 1:
  print('Yes')
else:
  print('No')
