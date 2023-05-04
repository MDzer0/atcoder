N, A, B, C, D = map(int, input().split())
S = list(input())
S[A - 1] = 'A'
S[B - 1] = 'B'
a1 = 0
a2 = 0
ans = ''
if C > D:
    a1 = 'A'
    a2 = 'B'
    tmp1 = C - 1
    tmp2 = D - 1
    now1 = A - 1
    now2 = B - 1
else:
    a1 = 'B'
    a2 = 'A'
    tmp1 = D - 1
    tmp2 = C - 1
    now1 = B - 1
    now2 = A - 1

while True:
    if now1 != tmp1:
        if now1 + 1 <= len(S) - 1 and S[now1 + 1] == '.' and now1 + 1 <= tmp1:
            S[now1] = '.'
            S[now1 + 1] = a1
            now1 += 1
        elif now1 + 2 <= len(S) - 1 and S[now1 + 2] == '.' and now1 + 2 <= tmp1:
            S[now1] = '.'
            S[now1 + 2] = a1
            now1 += 2
        elif now2 + 1 <= len(S) - 1 and S[now2 + 1] == '.' and now2 + 1 <= tmp2:
            S[now2] = '.'
            S[now2 + 1] = a2
            now2 += 1
        elif now2 + 2 <= len(S) - 1 and S[now2 + 2] == '.' and now2 + 2 <= tmp2:
            S[now2] = '.'
            S[now2 + 2] = a2
            now2 += 2
        else:
            ans = 'No'
            break
    elif now2 != tmp2:
        if now2 + 1 <= len(S) - 1 and S[now2 + 1] == '.' and now2 + 1 <= tmp2:
            S[now2] = '.'
            S[now2 + 1] = a2
            now2 += 1
        elif now2 + 2 <= len(S) - 1 and S[now2 + 2] == '.' and now2 + 2 <= tmp2:
            S[now2] = '.'
            S[now2 + 2] = a2
            now2 += 2
        else:
            ans = 'No'
            break
    else:
        ans = 'Yes'
        break

print(ans)
