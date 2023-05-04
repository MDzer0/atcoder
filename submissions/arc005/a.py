N = int(input())
tlst = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
w = list(input().split())
cnt = 0
for i in range(len(w)):
    for j in tlst:
        tmp = w[i].split('.')
        if tmp[0] == j:
            cnt += 1

print(cnt)
