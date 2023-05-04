N = int(input())
S = input()
tmp = S[0]
cnt = 1
sum_list = []
ans = (N * (N + 1)) // 2

for i in S[1:]:
    if tmp == i:
        cnt += 1
    else:
        sum_list.append(cnt)
        cnt = 1
        tmp = i

sum_list.append(cnt)

minus = 0
for i in sum_list:
    minus += (i * (i + 1)) // 2

print(ans - minus)
