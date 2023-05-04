N = int(input())
A = list(map(int, input().split()))

kingaku = [0] * 4
for i in A:
    if i == 100: kingaku[0] += 1
    elif i == 200: kingaku[1] += 1
    elif i == 300: kingaku[2] += 1
    else: kingaku[3] += 1

print(kingaku[0] * kingaku[3] + kingaku[1] * kingaku[2])
