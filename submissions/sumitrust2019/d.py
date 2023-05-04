N = int(input())
S = input()
ans = 0
for i in range(1000):
    index = 0
    for j in range(3):
        if (str(i).zfill(3)[j] in S[index:]) and index < N:
            index += S[index:].index(str(i).zfill(3)[j]) + 1
        else:
            index = -1
            break
    if index != -1:
        ans += 1

print(ans)
