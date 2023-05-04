a,b,c = map(int,input().split())
t = 0
for i in range(61):
    if t%60 < (t+a)%60:
        if t%60 <= c <= (t+a)%60:
            t += c - t%60
            print(t)
            exit()
    else:
        if t%60 <= c or c <= (t+a)%60:
            t += (c - t%60) % 60
            print(t)
            exit()
    t += a+b
print(-1)
