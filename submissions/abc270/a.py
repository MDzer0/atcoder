AB = list(map(int, input().split()))
ansList = [0] * 5

for i in AB:
    if i == 1 or i == 3 or i == 5 or i  == 7:
        ansList[1] = 1
    if i == 2 or i == 3 or i == 6 or i == 7:
        ansList[2] = 1
    if i == 4 or i == 5 or i == 6 or i == 7:
        ansList[4] = 1
ans = 0
for i in range(len(ansList)):
    if ansList[i] == 1:
        ans += i
print(ans)
