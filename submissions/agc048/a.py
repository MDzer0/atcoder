N = int(input())
hikaku = 'atcoder'
for i in range(N):
    S = input()
    if len(S) == S.count('a'):
        print(-1)
        continue
    if S > hikaku:
        print(0)
        continue
    cnt = 1
    for j in S:
        if 'a' != j:
            if j > 't':
                cnt -= 2
            else:
                cnt -= 1
            break
        else:
            cnt += 1
    print(cnt)
