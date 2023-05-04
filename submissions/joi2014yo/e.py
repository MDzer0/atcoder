from collections import defaultdict, deque
from heapq import heappop, heappush

if __name__ == '__main__':
    N, K = map(int, input().split())
    cars = [list(map(int, input().split())) for _ in range(N)]
    path = defaultdict(list)
    for _ in range(K):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        path[a].append(b)
        path[b].append(a)

    ans = [float('inf')] * N
    ans[0] = 0
    que = [(0, 0)]
    while que:
        cost, current = heappop(que)
        if current == N - 1:
            break
        seen = [False] * N
        seen[current] = True
        tmp = deque([[current, 0]])
        c, r = cars[current]
        while tmp:
            n, path_num = tmp.popleft()
            for _next in path[n]:
                if seen[_next] or path_num + 1 > r:
                    continue
                seen[_next] = True
                tmp.append([_next, path_num + 1])
                if c + cost < ans[_next] and path_num + 1 <= r:
                    ans[_next] = c + cost
                    heappush(que, (c + cost, _next))

    print(ans[N - 1])
