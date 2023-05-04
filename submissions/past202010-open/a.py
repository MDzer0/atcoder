A, B, C = map(int, input().split())
abc = [A, B, C]
abc.sort()

if abc[1] == A:
  print('A')
elif abc[1] == B:
  print('B')
else:
  print('C')
