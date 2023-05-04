S = list(input())
key = 'keyence'
ans = 'NO'
if len(S) == 7:
    if ''.join(S) == key:
        print('YES')
        exit()
    else:
        print('NO')
        exit()
for i in range(len(S)):
    tmp = S[0: i] + S[i + len(S) - 7:]
    if key == ''.join(tmp):
        ans = 'YES'
        break
print(ans)
