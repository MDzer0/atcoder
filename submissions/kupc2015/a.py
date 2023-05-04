T = int(input())
d = {'tokyo', 'kyoto'}

for i in range(T):
    S = input()
    index = 0
    cnt = 0
    while len(S) - 4 > index:
        if S[index: index + 5] in d:
            cnt += 1
            index += 5
        else:
            index += 1
    print(cnt)
