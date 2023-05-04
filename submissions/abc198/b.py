N = input()
cnt = 0
for i in reversed(N):
    if i == '0':
        cnt += 1
    else:
        break
        
N = '0' * cnt + N
tmp = len(N) // 2

for i in range(tmp):
    if N[i] != N[-i - 1]:
        print('No')
        exit()

print('Yes')
