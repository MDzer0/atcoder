n = int(input())

if n < 3:
    print(0)
    exit()

ans = [2]

for i in range(3,n,2):
    flag = 1
    for j in ans:
        if i%j == 0:
            flag = 0
    if flag == 1:
        ans.append(i)

print(len(ans))
