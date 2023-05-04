N = input()
ans = 0
harf = len(N) // 2
for i in range(harf):
    if N[i] == '(':
        if N[-i - 1] == ')':
            continue
        else:
            ans += 1

    elif N[i] == ')':
        if N[-i - 1] == '(':
            continue
        else:
            ans += 1

    elif N[i] != N[-i - 1]:
        ans += 1

if len(N) % 2 == 1:
    if N[harf] == '(' or N[harf] == ')':
        ans += 1

print(ans)
