N = int(input())
a = [int(input()) for _ in range(N)]
for i in a:
    if i % 2 != 0:
        print('first')
        exit()
print('second')
