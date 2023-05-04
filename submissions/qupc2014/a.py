a, b, c, d = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(c)]

for i in range(100, -1, -1):
  cnt = 0
  for e in E:
    if sum(x >= i for x in e) >= b:
      cnt += 1
  if cnt >= d:
    print(i)
    exit()
