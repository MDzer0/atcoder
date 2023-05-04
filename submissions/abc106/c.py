S = input()
N = int(input())

index = -1
r = -1
for i in range(len(S)):
    if index == -1:
        if S[i] == '1':
            index = i
            r = 1
            continue

    if index != -1 and r != 0:
        if S[i] == '1':
            r += 1
        else:
            break
if index == -1:
    print(S[0])
elif index != 0:
    print(S[0])
elif r >= N:
    print(1)
else:
    print(S[r])
