N,L=map(int,input().split())
S=input()
ans=0
t=1
for c in S:
  if c == '+':
    t += 1
    if t > L:
      t = 1
      ans += 1
  else:
    t -= 1
print(ans)
