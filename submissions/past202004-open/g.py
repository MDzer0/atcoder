from collections import deque, defaultdict

que = deque()
Q = int(input())

for i in range(Q):
    inp = list(input().split())
    if int(inp[0]) == 1:
        que.append([inp[1], int(inp[2])])
    else:
        d = defaultdict(int)
        cnt = int(inp[1])
        ans = 0
        while cnt > 0:
            if len(que) == 0:
                break

            if que[0][1] > cnt:
                que[0][1] -= cnt
                d[que[0][0]] += cnt
                cnt = 0
                break
            else:
                tmp = que.popleft()
                d[tmp[0]] += tmp[1]
                cnt -= tmp[1]
        for v, c in d.items():
            ans += c ** 2
        print(ans)
