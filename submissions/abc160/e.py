X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)

for i in p[:X]:
    r.append(i)
for j in q[:Y]:
    r.append(j)
r.sort(reverse=True)
print(sum(r[:X + Y]))
