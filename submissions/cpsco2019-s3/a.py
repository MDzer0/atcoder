S = input()
ans = ''
for i in S:
    if i == 'O':
        ans += 'A'
    elif i == 'A':
        ans += 'O'
    else:
        ans += i

print(ans)
