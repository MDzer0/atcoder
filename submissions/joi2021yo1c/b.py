N = int(input())
S = input()
chklist = ['I', 'O']
cnt = 0
for i in range(N):
    if i % 2 == 0:
        if S[i] != chklist[0]:
            cnt += 1
    else:
        if S[i] != chklist[1]:
            cnt += 1
print(cnt)
