N = int(input())
S = list(input() for _ in range(N))
ans = []

for i in S:
    ans.append((int(i), len(i)))

ans.sort(key=lambda x: x[1], reverse=True)
ans.sort(key=lambda x: x[0])

for i in ans:
    print(str(i[0]).zfill(i[1]))
