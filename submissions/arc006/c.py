N = int(input())
w = int(input())
ans = [[]]
ans[0].append(w)
for i in range(1, N):
    add = True
    w = int(input())
    for j in range(len(ans)):
        if ans[j][-1] >= w:
            ans[j].append(w)
            add = False
            break
    if add:
        ans.append([w])

print(len(ans))
