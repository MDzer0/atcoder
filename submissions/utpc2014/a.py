S=input().split()
flag=0

for i in range(len(S)-1,-1,-1):
    if S[i]!="not":
        flag=1
    elif flag==1 and S[i]==S[i+1]=="not":
        S.pop(i)
        S.pop(i)

print(*S)
