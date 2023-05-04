S = input()
index = 'FESTIVAL'
f = S[::-1].find(index[::-1])
ans = S[::-1]
ans = ans[f+8:]
print(ans[::-1])
