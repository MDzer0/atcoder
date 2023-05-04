N = int(input())
x = list(map(int, input().split()))
mans = 0
for i in x:
    mans += abs(i)
print(mans)

yans = 0
for i in x:
    yans += i ** 2
print(pow(yans, 0.5))

tans = 0
for i in x:
    tans = max(tans, abs(i))
print(tans)
