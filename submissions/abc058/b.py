O = input()
E = input()
tmp = max(len(O), len(E))
ans = ''
for i in range(tmp):
    if len(O) - 1 >= i and len(E) - 1 >= i:
        ans += O[i] + E[i]
    elif len(O) - 1 < i and len(E) - 1 >= i:
        ans += E[i]
    elif len(O) -1 >= i and len(E) - 1 < i:
        ans += O[i]

print(ans)
