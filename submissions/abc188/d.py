N, C = map(int, input().split())
abc = []
for i in range(N):
    a, b, c = map(int, input().split())
    abc.append((a, c))
    abc.append((b + 1, -c))
abc.sort()
ans = 0
ryokin = 0
hiduke = 0
for i in range(len(abc)):
    ans += min(C, ryokin) * (abc[i][0] - hiduke)
    ryokin += abc[i][1]
    hiduke = abc[i][0]
print(ans)
